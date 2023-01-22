# Instale os pacotes requeridos.
import requests
import json
import os
import openai
import boto3
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

    # FILE_NAME da imagem que foi gerada.
    FILE_NAME = resposta['data'][0]['url']
    BUCKET_NAME = "2mstech"
    OBJECT_NAME = os.path.basename(FILE_NAME)

    # Faz o download da imagem que foi gerada, em diretório temporário
    PATH = "/tmp"
    IMAGEM = OBJECT_NAME + str(".png")
    PATH_IMAGEM = PATH +"/"+ IMAGEM
    # Download
    wget.download(FILE_NAME,PATH_IMAGEM)

    # Let's use Amazon S3:  Upload a new file
    s3 = boto3.client('s3')
    with open(PATH_IMAGEM, "rb") as f:
        s3.upload_fileobj(f, BUCKET_NAME, IMAGEM)

    # Verifica se a imagem foi Baixada
    if os.path.exists(PATH_IMAGEM):
        # retorna código de sucesso e o nome da imagem gerada
        value = {"processamento": 200,"imagem": IMAGEM}
        return json.dumps(value)
    else:
        # retorna código de erro.
        value = {"processamento": 400,"msg": "Erro, imagem não foi criada ou baixada..."}       
        return json.dumps(value)
  
# Quando executado via console
if __name__ == "__main__":
    handler(0,0)