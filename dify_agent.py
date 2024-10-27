import requests

def chamar_agente_dify(texto):
    url = "https://api.dify.ai/v1/agent"
    headers = {"Authorization": "Bearer sua-chave-de-api"}
    payload = {"input": texto}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
