import requests

def chamar_agente_dify(texto):
    url = "https://api.dify.ai/v1/agent"
    headers = {"Authorization": "app-B6XKSIIIEJv3u382S8AnWRQ2"}
    payload = {"input": texto}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
