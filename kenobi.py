import fitz
import requests
import os
import io
from bs4 import BeautifulSoup
from dotenv import load_dotenv


# Load OpenAI API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

FINEP_URL = "http://www.finep.gov.br/chamadas-publicas/chamadaspublicas"
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"

def fetch_finep_calls():
    """Scrapes FINEP website for public calls."""
    response = requests.get(FINEP_URL)
    if response.status_code != 200:
        return f"Erro ao acessar o site: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    calls = soup.find_all("div", class_="item")  # Adjust based on site structure    

    extracted_calls = []
    for call in calls:
        title = call.find("h3").text.strip() if call.find("h3") else "Sem título"
        link = call.find("a")["href"] if call.find("a") else "#"
        full_link = f"http://finep.gov.br/{link}"
        extracted_calls.append({"title": title, "link": full_link})

    return extracted_calls if extracted_calls else "Nenhuma chamada pública encontrada."

def fetch_finep_pdf(extracted_calls):

    pdfs = []

    for call in extracted_calls:
        response = requests.get(call["link"])
        if response.status_code !=200:
            return f"Fail to access the page: {response.status_code}"
        
        soup = BeautifulSoup(response.text, "html.parser")
        editals = soup.find_all("td")
        for edital in editals:
            link = edital.find("a")["href"] if edital.find("a") else "#"
            linkComEdital = link if "edital" in link.lower() else ""
            linkComEditalPDF = f"http://finep.gov.br{linkComEdital}" if linkComEdital.endswith("pdf") else ""
            print(f"{call["title"]}: {linkComEditalPDF}") 

            text = ""
            # response = requests.get(linkComEditalPDF)
            # if response.status_code == 200:
            #     pdf_file = io.BytesIO(response.content)
            # else:
            #     text = "Fail to get pdf"

            # with fitz.open(stream=pdf_file,filetype="pdf") as doc:
            #     for page in doc:
            #         text+=page.get_text("text")+"\n"

        pdfs.append({"title": call["title"],"link": call["link"], "pdfLink":linkComEditalPDF, "pdfContent": text}) if linkComEditalPDF != "" else ""
    
    return pdfs
    

def ask_chatgpt(content):
    """Sends scraped data to ChatGPT for analysis."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil que analisa chamadas públicas."},
            {"role": "user", "content": f"Essas são as chamadas públicas extraídas do site FINEP:\n{content}\n\nResuma as oportunidades disponíveis."}
        ],
        "temperature": 0.7
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro na API: {response.status_code}, {response.text}"


def analyze_pdf_chatgpt(content):
    """Sends scraped data to ChatGPT for analysis."""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Você é um assistente especializado em analise de documentos."},
            {"role": "user", "content": f"Esse é o documento\n{content}\n\nDestaque a elegibilidade e cronograma."}
        ],
        "temperature": 0.7
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro na API: {response.status_code}, {response.text}"


if __name__ == "__main__":
    scraped_data = fetch_finep_calls()
    # chat_response = ask_chatgpt(scraped_data)
    # print("ChatGPT Resumo:", chat_response)
    pdfs = fetch_finep_pdf(scraped_data)
    print (pdfs)
    # print("Resposta do chat:",analyze_pdf_chatgpt(pdfs))
