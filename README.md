# Criando Microsserviços com Python, Flask e OpenAI: Construindo APIs para Retornar Imagens

**Resumo**

Neste artigo, vamos explorar como criar microsserviços usando Python, Flask e a API do OpenAI para retornar imagens. Começaremos com uma visão geral dos microsserviços e como eles se relacionam à API OpenAI. Depois, usaremos o Python e o Flask para criar um microsserviço que retornará uma imagem a partir da API OpenAI. Por último, discutiremos algumas considerações e lógicas que devem ser consideradas ao construir APIs para retornar imagens.

**Introdução: O que são microsserviços?**

>***Newman (2022, p. 24) define microsserviços d
a seguinte forma:***
>
>(…) microsserviços são serviços que podem ser lançados de forma independente e são modelados com base em um domínio de negócios. Um serviço encapsula uma funcionalidade e a torna acessível a outros serviços através de redes – podemos criar um sistema mais complexo a partir destes blocos de construção. 
Um microsserviço pode representar um estoque, outro pode representar o gerenciamento de pedidos, enquanto outro ainda representa a expedição de mercadorias; juntos, porém, eles podem compor um sistema completo de comércio eletrônico.

**Contexto**

O desenvolvimento de microsserviços tem sido uma área em rápido crescimento nos últimos anos, pois muitas empresas estão buscando construir sistemas de grande escala de maneira escalonável. Neste artigo, vamos descrever um exemplo de prova de conceito com microsserviço. O exemplo consiste em desenvolver e implantar um microsserviço sem servidor. Microsserviços sem servidor são um novo paradigma de desenvolvimento de aplicações baseadas na arquitetura de microsserviços. Ao contrário dos microsserviços tradicionais, os microsserviços sem servidor são executados em um ambiente de nuvem, que permite que as aplicações sejam executadas em qualquer lugar. Essa abordagem permite que as aplicações sejam acessíveis a partir de qualquer lugar, a qualquer hora, desde que exista uma conexão à internet.

**Objetivo**

O objetivo principal de realizar o estudo deste tema é verificar se microsserviço sem servidor é viável e se atende às necessidades de um projeto. Esta prova de conceito implementará uma solução de forma limitada.

**Definição do problema**

***Exemplo hipotético:***

Um sistema monolítico modular de e-commerce de imagens que recebe centenas de requisições de pedidos na internet, está gerando muito "tikets" de suporte no setor de atendimento da empresa. A principal reclamação é lentidão na geração das imagens.


**Implementação: Case**


O estudo da causa raiz do problema recomenda a necessidade do sistema monolítico modular de e-commerce de imagens ser atualizado, porém, como é um sistema crítico será preciso realizar planejamento para a migração do sistema monolítico modular para outra solução.

Um sistema monolítico modular é um sistema de software cujas principais características são o fato de que o código é mantido em módulos, porém, todas as partes do sistema são construídas e mantidas como uma unidade.


**Quais foram os principais desafios?**

- As boas práticas não haviam sido implementadas no sistema;
- Complexidade de escalar, pois todos os módulos precisavam ser modificados e atualizados ao mesmo tempo;
- A complexidade do sistema torna-o difícil de entender e não havia documentação;
- Para reescrever o módulo de imagens, não seria tarefa fácil sem documentação;
- Seria difícil testar, pois todas as partes do sistema devem ser testadas simultaneamente;
- A dependência dos componentes: o sistema inteiro pode ser afetado se o novo componente falhar.


**Solução**

> Não há uma solução única para este problema, estamos propondo um exercício para estudos.

Separar o módulo de geração de imagens do sistema monolítico, transformando-o em um microsserviço. Ao final da migração, teremos um sistema híbrido, parte monolítico e parte microsserviços.


**Implementação: Refatoração do sistema monolítico**

**Riscos**

a) O ambiente de produção suporta microsserviços?
b) O custo da mudança será suportado pela empresa?
c) Existe algum "gap" na equipe desenvolvimento para trabalhar com microsserviços?
d) Temos visão clara do módulo que vamos extrair?
e) Código não está organizado em torno de conceito de domínios de negócios.

**Design Parttners**

a) Refatore gradualmente;<br>
b) Estude padrões de migração e adote uma técnica; (exemplos: strangler fig, composição de UI, branch por abstração, execução em paralelo, colaborador decorador e/ou captura de dados modificados, ...)

**Cenário atual: AS-IS**

<img src="img/fig1.png" alt="Cenário Atual" style="float:left;width:320px">


**Cenário futuro: TO-BE**



Arquitetura

Tecnologias: Python | Fask | OAuth | OpenAI API | Docker | AWS

Modelar

Comunicação

Monitoração

Segurança

Testes

Conclusão

```python

```

```python

```
