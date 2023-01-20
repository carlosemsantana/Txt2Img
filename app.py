# Instale os pacotes requeridos.
import requests
import json
import os
import openai
import wget

def handler(event, context):   

    # Simulação de entrada de dados no formato JSON
    solicitacao_cliente = {
        "prompt": "Crie uma cópia idêntica da obra: Relógios Encontrando Relógios - Salvador Dalí",
        "n": 1,
        "size": "1024x1024"
    }
    payload = json.dumps(solicitacao_cliente)

    # Para gerar o token cadastre-se em (https://beta.openai.com/account/api-keys)
    # Token de acesso
    # Atenção: Não permita que o seu token seja descoberto, neste exemplo esse token
    #          já foi revogado (cancelado)
    token = openai.api_key = "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"

    # Endpoint do OpenAI API a cada requisição enviada uma resposta é retornada.
    # https://beta.openai.com/docs/api-reference/images
    url = "https://api.openai.com/v1/images/generations"

    # Cabeçalho com formato e o token de acesso. O Token é passado via Header no POST
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(token)
    }

    # OpenAI API aceita as requisições com atributos formatados em JSON
    # Atributos: Prompt: Entrada de dados, descreva o que deseja que a IA desenhe".
    #                 n: Quantidade de repetições
    #              size: Tamanho das imagens (1024, 512 ou 256)
    # https://beta.openai.com/docs/models/overview

    response = requests.request("POST", url, headers=headers, data=payload)
    resposta = json.loads(response.text)

    # A resposta da API é uma imagem. 
    # Baixar e gravar a imagem em disco
    # Formato da mensagem de resposta da API - Está mensagem tem tempo de vida .
    # [{'url': 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-7FoyzXPtgPrSoxwHakbEG667/
    #           user-a0FVNqzRRLgdzcyK0uncb4hy/img-l7TBsU3AGVXbM2DAtSc7t7vP.png?st=2023-01-20T14%3A31%3A
    #           54Z&se=2023-01-20T16%3A31%3A54Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoi
    #           d=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2
    #           023-01-20T12%3A26%3A51Z&ske=2023-01-21T12%3A26%3A51Z&sks=b&skv=2021-08-06&sig=raNSN5jZI
    #           6iKUowiFh5hr5rAglaEVUvqwwFBrmJUGRk%3D'}]

    # URI da imagem que foi gerada.
    url = resposta['data'][0]['url']

    # Grava imagem no S3
    file = "imagemCriada/teste.png"
    wget.download(url,file)

    # Verifica se a imagem foi gerada
    if os.path.exists(file):
        # retorna código de sucesso e o nome da imagem gerada
        value = {"processamento": 200,"imagem": file}
        return json.dumps(value)
    else:
        # retorna código de erro.
        value = {"processamento": 400,"msg": "Erro, imagem não foi criada..."}
        return json.dumps(value)
  
# Quando executado via console
if __name__ == "__main__":
    handler(0,0)