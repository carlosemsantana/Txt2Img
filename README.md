<!-- #region -->
# Criando Microsserviços: Projetando componete com Python e API OpenAI


**Introdução: O que são microsserviços?**

>***Newman (2022, p. 24) define microsserviços da seguinte forma:***
>
>(…) microsserviços são serviços que podem ser lançados de forma independente e são modelados com base em um domínio de negócios. Um serviço encapsula uma funcionalidade e a torna acessível a outros serviços através de redes – podemos criar um sistema mais complexo a partir destes blocos de construção. 
Um microsserviço pode representar um estoque, outro pode representar o gerenciamento de pedidos, enquanto outro ainda representa a expedição de mercadorias; juntos, porém, eles podem compor um sistema completo de comércio eletrônico.

**Contexto**

O desenvolvimento de microsserviços, tem sido uma área em rápido crescimento nos últimos anos, pois muitas empresas estão buscando construir sistemas de grande escala de maneira escalonável. Neste artigo, vamos descrever um exemplo de prova de conceito com microsserviço. O exemplo consiste, em desenvolver e implantar um microsserviço sem servidor. Microsserviços sem servidor, são um novo paradigma de desenvolvimento de aplicações baseadas na arquitetura de microsserviços. Ao contrário dos microsserviços tradicionais, os microsserviços sem servidor são executados em um ambiente de nuvem, que permite que as aplicações sejam executadas em qualquer lugar. Essa abordagem permite que as aplicações sejam acessíveis a partir de qualquer lugar, a qualquer hora, desde que exista uma conexão à internet.

**Objetivo**

O objetivo principal é verificar se microsserviços sem servidor são viáveis, e se atendem às necessidades de um projeto. Esta prova de conceito implementará uma solução de um problema hipotético de forma limitada.

**Definição do problema**

***Exemplo hipotético:***

Um sistema monolítico modular, que comercializa imagens e recebe centenas de requisições de pedidos na internet, está gerando muito "tikets" de suporte no setor de atendimento da empresa. A principal reclamação é lentidão na geração das imagens.

Sistema monolítico modular, é um sistema de software cujas principais características são: código é mantido em módulos, todas as partes do sistema são dependentes e todos os módulos precisam ser atualizados ao mesmo tempo.

Estudo preliminar do problema, recomendou à gestão de produtos atualização urgente do sistema de imagens.
<!-- #endregion -->

**Quais foram os principais desafios?**

- Tráfego do site muito alto;
- Código do sistema extenso e sem documentação;
- Complexidade para escalar e testar;
- Forte dependência dos componentes: o sistema inteiro pode ser afetado se o novo componente falhar.


**Solução**

> Não há uma solução única para este problema, estamos propondo um exercício para estudos.

A proposição foi refatorar o módulo de geração de imagens do sistema monolítico, transformando-o em um microsserviço.


**Proposição: Refatoração do sistema monolítico**

**Riscos**

a) O ambiente de produção suporta microsserviços?<br>
b) O custo da mudança será suportado pela empresa?<br>
c) Existe algum "gap" na equipe desenvolvimento para trabalhar com microsserviços?<br>
d) Temos visão clara do módulo que vamos extrair?<br>

**Design Parttners**

a) Refatore gradualmente;<br>
b) Estude padrões de migração e adote uma técnica; (exemplos: strangler fig, composição de UI, branch por abstração, execução em paralelo, colaborador decorado, captura de dados modificados e outros.)<p>


**Cenário atual: AS-IS**


Elabore esboço que represente o cenário atual e considere: o negócio, os dados, a aplicação e as tecnologias.
Consulte as documentações disponíveis do sistema, arquitetura, infra-estrutura, tecnologia, explore o código fonte (quando possível) e converse com os mantenedores do sistema. 
No diagrama AS-IS, identifique o módulo a ser movido, as depedências, os fluxos dos processos, as chamadas que serão redirecionadas e todas as dependências externas. A figura 1. representa exemplo simplificado.


![](img/fig1.png)


**Cenário futuro: TO-BE**



No diagrama TO-BE, considere processo gradual de refatoração do sistema monolítico. O ideal ao extrair a funcionalidade para implementação na nova arquitetura, não tenhamos alteração no sistema atual, porém, em alguns casos, não é possível. Precisamos examinar, qual é a melhor solução. Existem muitas soluções que poderão ser adotadas, tais como: Interceptação de mensagens, roteamento, espelhamento, implementação de API interna; que redirecione o fluxo de requisições do módulo que foi extraído para o novo serviço. O importante é que tenhamos a disposição, ambiente seguro e isolado, onde provas de conceito poderão ser avaliadas. E lembre-se: agilidade não tem nada a ver com "Go Horse", planejamento é fundamental.

Figura 2. representa exemplo simplificado da extração do módulo a ser refatorado para microsserviços.


![](img/fig2.png)


**Modelar o microsserviço: Gerador de Imagens**


**Requisitos:**


1° Defina as Fronteiras do microsserviço: Fronteira é uma delimitação de responsabilidade entre dois microsserviços. Ela define quais ações cada microsserviço deve executar, e quais regras devem ser seguidas para que os serviços se comuniquem. As fronteiras permitem que microsserviços sejam desenvolvidos, implantados e gerenciados de forma independente, melhorando a escalabilidade e flexibilidade da arquitetura;


2° Defina sempre que possível; design orientado a Domínio (linguagem ubíqua, agregado, contexto delimitado), o que permite ao microsserviço, baixo acoplamento: capacidade de ser implantado, executado e mantido de forma independente e isolada dos outros módulos do sistemas; 


3° Defina a Comunicação que será implementada no Microsserviço: Neste exemplo adotamos o REST (requisição-resposta);


4° Defina se haverá persistência dos Dados: Adotaremos padrão de dados não estruturados (NoSQL);


5° Prova de conceito com as seguintes tecnologias: Python, JSON, Flask, OpenAI API, Docker, Função como serviço (FaaS): AWS Lambda, API Gateway, AWS DinamoDB e Github;


6° Monitoração: Os logs centralizados são uma parte importante do desenvolvimento de microsserviços, pois permitem que os desenvolvedores tenham uma visão abrangente sobre o que está acontecendo com sistema. As ferramentas de log centralizadas permitem que os desenvolvedores rastreiem erros, monitorar as principais métricas de performance e verificar o comportamento dos serviços. Isso ajuda a garantir que os serviços estejam operando corretamente e permitem que os desenvolvedores identifiquem rapidamente e corrijam erros ou problemas que possam surgir;


7° Defina o fluxo de trabalho: O sistema monolítico tem o seu fluxo de transações ACID, e quando ocorre erro é preciso executar rollback. Considere que quando houver um erro o microsserviço precisará executar algum processo que realize o rollback;


8° Segurança: Defina os aspéctos da segurança de acordo com o complice;


**Implementação**


Exemplo de diagrama da arquitetura (freestyle); PoC - prova de conceito, para a implantação da solução de forma hibrida e gradual, onde foi extraído do sistema monolítico somente a funcionalidade que estava apresentando o problema, em destaque: Figura 3. Visão geral da estrutura e componentes-chave. 


![](img/fig3.png)


Vamos escrever um microsserviço com base no diagrama de entradas e saídas, Figura 5. Não implementaremos a monitoração, Figura 6.  A depuração de problemas em ambiente microsserviços é extremamente complexa. Recomendamos que considere implemetar, uma forma automatizada ou não de centralizar e examinar os logs.


![](img/fig4.png)


**Requitos Técnicos**


1° Cadastro e cheve de acesso aos recursos da AWS;<br>
2° Cadastro e chave de acesso - API OpenAI API;<br>
3° Python 3.9;<br>
4° AWS Command Line Interface; ([Installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))<br>
5° Docker (latest);<br>
6° Github (latest); 


**Exemplo ilustrando o processo da criação de Função como serviço (FaaS) na AWS**

<!-- #region -->
1° Crie o ambiente desenvolvimento:
```python
$ mkdir geradorImagens
$ cd geradorImagens
$ mkdir imagemCriada
$ python3 -m venv venv
$ . venv/bin/activate
```
2° Instale todas as dependências no ambiente:
```python
$ pip install requests
$ pip install openai
$ pip install wget
$ pip install json
$ pip install os
$ pip install boto3
```

3° Exemplo ilustrativo de código de serviço em Python 3.9, escrito no formato suportado pelo AWS Lambda. Este serviço acessa uma API externa, (OpenAI API) envia requisição para que a IA crie uma imagem, e recebe a requisição de resposta e grava a imagem no Bucket S3. (Não foi implementado gravação dos dados no AWS DinamoDB)

Arquivo: app.py

```python
# Instale os pacotes requeridos.
import requests
import json
import os
import openai
import boto3
import wget

def handler(event, context):
    # Este serviço recebe uma requisição formato JSON, com os requisitos da imagem,
    # envia a requisição para a IA via API OpenAI API, que elabora a imagem e retona um URL com a imagem.
    # O serviço recebe a requisição, baixa a imagem em diretório temporário e envia o aquivo para o S3.
    # Retorna ao cliente mensagem informando o resultado do processamento. 
    # A integração com DinamoDB, está agendada para a próxima refatoração.

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

    # Configurações internas
    FILE_NAME = resposta['data'][0]['url']
    BUCKET_NAME = "2mstech" # Repositório S3
    OBJECT_NAME = os.path.basename(FILE_NAME)
    PATH = "/tmp"
    IMAGEM = OBJECT_NAME + str(".png")
    PATH_IMAGEM = PATH +"/"+ IMAGEM
    
    # Faz o download da imagem que foi gerada, em diretório temporário.
    wget.download(FILE_NAME,PATH_IMAGEM)

    # Envia a imagem criada para o Bucket Amazon S3:  Upload a new file
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
```
4° Gerar o arquivo requeriments.txt com as dependências deste exemplo.

```python
# Gerar lista de pacotes requeridos do projeto.
$ pip freeze > requirements.txt

Dependências:

aiohttp==3.8.3
aiosignal==1.3.1
async-timeout==4.0.2
attrs==22.2.0
boto3==1.26.54
botocore==1.29.54
certifi==2022.12.7
charset-normalizer==2.1.1
click==8.1.3
frozenlist==1.3.3
idna==3.4
importlib-metadata==6.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
jmespath==1.0.1
MarkupSafe==2.1.2
multidict==6.0.4
openai==0.26.1
python-dateutil==2.8.2
requests==2.28.2
s3transfer==0.6.0
six==1.16.0
tqdm==4.64.1
urllib3==1.26.14
Werkzeug==2.2.2
wget==3.2
yarl==1.8.2
zipp==3.11.0
```
<!-- #endregion -->

**Gerar imagem e enviar para AWS**

<!-- #region -->
Estamos trabalhando com containers Dockers; usaremos o Docker compose para o gerenciar as imagens. Os próximos passos são:

1° criar arquivo docker-compose.yml

```python
version: '3.8'
services:
    microsservicos:
      container_name: geradorimagens
      build: .     
```

2° criar arquivo Dockerfile

```python

FROM public.ecr.aws/lambda/python:3.9

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# Install the function's dependencies using file requirements.txt
# from your project folder.

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]

```

3° Gerar a imagem docker e testar

```python

$ docker compose up -d 
```
<!-- #endregion -->

Build da imagem do container do microsserviço gerado com sucesso.

![](img/fig5.png)


4° Preparar a imagem para envio ao ECR (Amazon Elastic Container Registry).

**Rquesito: repositório ECR criado.**

Referência: [Amazon Elastic Container Registry Documentation](https://docs.aws.amazon.com/ecr/)

<!-- #region -->
Renomeie a imagem de acordo requerido pelo ECR e envie o microsserviço.
```python
$ docker tag txt2img-microsservicos:latest 65********48.dkr.ecr.us-east-1.amazonaws.com/2ms:latest
$ docker push 65********48.dkr.ecr.us-east-1.amazonaws.com/2ms:latest
```
<!-- #endregion -->

Imagem enviada para o repositório com sucesso.
![](img/fig6.png)


**Última etapa (AWS): Criar a Função, API Gateway, Bucket S3, Endpoint e Testar.**


**Rquisitos:**

1° Crie usuário no Identity and Access Management (IAM), configure permissões e gere a chave de acesso;<br>
2° Configure a chave de acesso no seu ambiente desenvolvimento; <br>
3° Crie a Função e use a imagem que foi enviada para o ECR;<br>
4° Crie e configure um Bucket S3 para receber as imagens (fotos) geradas pelo serviço;<br>
5° Configure as permissões e rotas de acesso ao S3;<br>
4° Ajuste e Teste o Lambda;<br>
6° Crie API Gateway;<br>
7° Crie o Endpoint público;<br>

Referência: [Implante funções do Lambda em Python com imagens de contêiner](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/python-image.html)


**Repositório ECR (Amazon Elastic Container Registry)**

A figura 8. ilustra imagem docker com instância do microsserviço implementado.


![](img/fig7.png)


**Função como serviço (FaaS): AWS Lambda**


Figuras 9 e 13. ilustram a função Lambda, o API Gateway e endpoint do microserviço **Gerador-Imagens**.


![](img/fig8.png)


![](img/fig12.png)


**Crie uma role com permissões para gravação do serviço Lambda no Buckect S3**


![](img/fig13.png)


**Testes e Ajustes da Função Lambda**

A figura 10. ilustra mensagem de resposta do teste inicial aplicado Lambda.


![](img/fig9.png)


**Bucket S3: Repositório onde as imagens geradas são armazenadas**

No exemplo abaixo, figura 14. lista o conteúdo do Bucket S3: Imagens (fotos) geradas pelo serviço.


![](img/fig10.png)


**Endpoint acesso ao serviço**

Nos exemplos figuras 12 e 16. ilustram, acesso direto ao endpoint do Gerador de Imagens. A resposta da requisição é o nome da imagem (foto) que foi criada.


![](img/fig11.png)


**Postman**


![](img/fig14.png)


**Imagens**
A figura 17. ilustra todas as imagens que foram geradas pelo microserviço. 

O microsserviço recebeu um JSON com a quantidade, tamanho e característica da imagem a ser gerada. 

Para as ilustrações que seguem abaixo as características foram:
>**Crie uma cópia idêntica da obra: Relógios Encontrando Relógios - Salvador Dalí**


![](img/fig15.png)


**Conclusão**


Concluímos que a implantação de um microsserviço na AWS é um processo altamente complexo, que requer um planejamento cuidadoso e uma compreensão profunda das ferramentas e serviços da AWS. Embora este artigo tenha fornecido uma visão geral dessa jornada, são necessários mais testes para garantir que todos os aspectos sejam considerados de forma apropriada. Portanto, recomendamos a realização de testes adicionais para validar os detalhes do processo de implantação. Além disso, recomendamos que os usuários também realizem testes de carga para garantir o desempenho adequado do microsserviço.


Gratidão

[Carlos Eugênio](https://github.com/carlosemsantana )

Referências:<BR>
[1] https://beta.openai.com/<BR>
[2] https://docs.aws.amazon.com/
