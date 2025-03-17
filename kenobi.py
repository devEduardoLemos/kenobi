import requests
import os
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from responseDTO import ResponseDTO


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

    return soup 

def parseToResponseDTO(responseText):
    """Parses the JSON response and converts it into DTOs."""
    # Extract JSON part from the response

    print(f"This is the original text: {responseText}")
    jsonStart = responseText.find("{")  # Locate where JSON starts
    jsonEnd = responseText.rfind("```")
    jsonData = responseText[jsonStart:jsonEnd]  # Extract only JSON content
    
    print(f"This is the json after tretment: {jsonData}")
    # Parse JSON
    try:
        parsedJson = json.loads(jsonData)
        calls = parsedJson.get("oportunidades", [])  # Get the 'chamadas' array
    except json.JSONDecodeError as e:
        # print(f"❌ Error parsing JSON: {e}")
        return []

    # Convert JSON into DTOs
    opportunities = [
        ResponseDTO(
            title=call.get("titulo", "N/A"),
            resume = call.get("resume","N/A"),
            publicationDate=call.get("data_publicacao", "N/A"),
            deadline=call.get("prazo_envio", "N/A"),
            fundingSource=call.get("fonte_recurso", "N/A"),
            targetAudience=call.get("publico_alvo", "N/A"),
            theme=call.get("tema", "N/A"),
            link=call.get("link", "N/A"),
            status=call.get("status","N/A")
        )
        for call in calls
    ]

    return opportunities

def ask_chatgpt():
    """Sends scraped data to ChatGPT for analysis."""
    # content = title + "" + link

    content = fetch_finep_calls()
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil que analisa sites de chamadas públicas."},
            {"role": "user", "content": f"Esse é o conteúdo de um site de chamadas públicas extraídas do site FINEP:\n{content}\n\nResuma as oportunidades disponíveis e seus links, o resumo deve conter título do edital, resumo, data de publicação, prazo para envio de propostas, fonte do recurso, publico alvo, tema ou áreas, link, status. Traga a resposta em formato json, o array que contém toda informação deve ter o nome de oportunidades"}
        ],
        "temperature": 0.7
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro na API: {response.status_code}, {response.text}"


if __name__ == "__main__":
    response = ask_chatgpt()
    print(f"This is the response: {response}")
    responseDTO = parseToResponseDTO(response)
    # for dto in infoDTO:
    #     resume = ask_chatgpt(dto.title,dto.link)
    #     response = ResponseDTO(dto.title, resume,'','',dto.pdfLink)
        # print(dto.title)
    
    print(f"This is the json:{responseDTO}")
        

