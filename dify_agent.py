pip install --upgrade pip
import requests

def chamar_agente_dify(texto):
    url = "https://api.dify.ai/v1/agent"
    headers = {"Authorization": api_key}
    payload = {"input": texto}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
