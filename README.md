<!-- #region -->
# Criando Microsserviços: Projetando componete com Python, Flask e API OpenAI


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

```python

```

```python

```



```python

```

```python

```
