# classificador_elastic
Criando um classificador simples com ElasticSearch

Dicas de como criar um classificador para sugerir preenchimento de campos, classes de documentos ou identificar fluxos de trabalho baseado em textos inseridos no ElasticSearch.

O primeiro passo é criar um índice definindo os campos de forma a potencializar a pesquisa do elastic e aumentar a eficácia do classificador.
- pode-se criar um arquivo de sinônimo para cada contexto (sinônimo de somes, termos de informática, termos de áreas específicas, etc)
- não é sugerida a criação de listas muito grandes de sinônimos, apenas o que realmente for útil no contexto
- o arquivo de exemplo de sinônimo de nomes foi encontrado em um fórum (vou resgatar e incluir o endereço aqui) e alguns nomes foram acrescidos apenas como exemplo.

O segundo passo é criar uma pesquisa com More Like This que reflita corretamente a relação entre o campo de pesquisa e o campo da classe, acrescentando pesos com filtros em relação a outros campos relacionados.

O terceiro passo é criar o algoritmo de score da melhor classe. Deve-se escolher um size na pesquisa (de 5 a 10 parece um número adequado). Após o retorno da pesquisa, basta somar o score de cada classe e utilizar a classe com maior score.
Pode-se verificar a diferença entre a primeira classe e a segunda para avaliar se existe uma "dúvida" muito grande entre as classes. Valores muito próximos podem sugerir uma dúvida maior. A ordem das classes retornadas pode facilitar o preenchimento de um combo de seleção facilitando o trabalho de preenchimento do campo.
- O segredo desse passo está na estrutura robusta de pesquisa do elasticsearch que constrói índices com pesos para os termos (ou conjunto de termos) baseados na ocorrência deles no conjunto de textos da base (com TFIDF ou BM25).

O último passo, e contínuo, é a avaliação dos dados da base, remoção ou desativação de textos com pouca qualidade, etc.
Pode-se melhorar a pesquisa usando diversos recursos do elasticsearch como relacionar campos e pesos, incluir pesos em termos e aumentar ou diminuir scores. 

É importante verificar se o classificador está fazendo uma boa classificação. Uma forma simples é incluir uma rotina que simule a classificação de textos já classificados, removendo o próprio texto da pesquisa (pelo seu ID) e depois retornar um percentual de acertos. Existem diversas técnicas de validação na ciência de dados, esse é só um começo de forma simples e com bons resultados.

O exemplo aqui apresentado é muito simples, apenas para ilustrar a solução. 

Baseado na publicação de Saskia Vola: https://www.elastic.co/blog/text-classification-made-easy-with-elasticsearch
