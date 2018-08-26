# Algoritmos de score para as classes
Aqui será mostrado um algoritmo em python e um em angular que faz a consulta no elasticsearch e contabiliza os scores para prever a classe no novo texto.
Pode-se criar um campo "Ativo", ou "Descartado" para não usar determinados textos na classificação, melhorando a predição para textos mal escritos ou com classificações iprecisas.
Pode-se também criar um campo "Validado" para inserir um fluxo de validação dos textos utilizados pelo algoritmo.

Os algoritmos são simples e estão baseados no artigo de Saskia Vola em https://www.elastic.co/blog/text-classification-made-easy-with-elasticsearch

### Python

O arquivo <b>exemplo_classificador.py</b> demonstra uma classe base para uso do elasticsearch em python, incluindo o método <b>classificar</b>
- os parâmetros são a query do elastic e o campo usado para classificação.
- o exemplo é a implementação direta da proposta de Saskia Vola e demonstrou um ótimo resultado em alguns contextos.

Em breve será incluído um exemplo usando flask para responder requisições do angular na classificação contínua em um fluxo simples de trabalho.
1. Pesquisar textos
2. inserir um novo texto e receber a sugestão da classe
3. possibilidade de ajustar a classe, aperfeiçoando as próximas classificações

### Angular

...em breve
