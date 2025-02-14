import requests
import os
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
        link = call.find("a")["href"] if call.find("a") else "Sem link"
        extracted_calls.append(f"{title}: http://finep.gov.br/{link}")

    return "\n".join(extracted_calls) if extracted_calls else "Nenhuma chamada pública encontrada."

# def fetch_finep_pdf():


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

if __name__ == "__main__":
    scraped_data = fetch_finep_calls()
    chat_response = ask_chatgpt(scraped_data)
    print("ChatGPT Resumo:", chat_response)
