from dify_agent import chamar_agente_dify

def processar_requisicao_usuario(texto_usuario):
    resposta_agente = chamar_agente_dify(texto_usuario)
    return resposta_agente
