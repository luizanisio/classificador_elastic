# classificador_elastic

## Criando um classificador simples com ElasticSearch

Dicas de como criar um classificador para sugerir preenchimento de campos, classes/tipos de documentos ou identificar fluxos de trabalho baseado em textos inseridos no ElasticSearch. Por exemplo uma solicitação de suporte poderia ser aberta e o classificador identificaria uma área de suporte adequada à solicitação de acordo com o texto informado.
Sugiro o uso do <b>Dev Tools</b> do <b>kibana</b> para seguir os exemplos, facilita bastante.

O <b>primeiro passo</b> é criar um índice definindo os campos de forma a potencializar a pesquisa do elastic e aumentar a eficácia do classificador.
- pode-se criar um arquivo de sinônimo para cada contexto (sinônimo de somes, termos de informática, termos de áreas específicas, etc)
- não é sugerida a criação de listas muito grandes de sinônimos, apenas o que realmente for útil no contexto
- o arquivo de exemplo de sinônimo de nomes foi encontrado em um fórum (vou resgatar e incluir o endereço aqui) e alguns nomes foram acrescidos apenas como exemplo.

O <b>segundo passo</b> é criar uma pesquisa com More Like This que reflita corretamente a relação entre o campo de pesquisa e o campo da classe, acrescentando pesos com filtros em relação a outros campos relacionados.
- Outros exemplos de pesquisas com MLT: https://github.com/luizanisio/classificador_elastic/blob/master/021_mais_pesquisas.md

O <b>terceiro passo</b> é criar o algoritmo de score da melhor classe. Deve-se escolher um size na pesquisa (de 5 a 10 parece um número adequado). Após o retorno da pesquisa, basta somar o score de cada classe e utilizar a classe com maior score.
Pode-se verificar a diferença entre a primeira classe e a segunda para avaliar se existe uma "dúvida" muito grande entre as classes. Valores muito próximos podem sugerir uma dúvida maior. A ordem das classes retornadas pode facilitar o preenchimento de um combo de seleção facilitando o trabalho de preenchimento do campo.
- O segredo desse passo está na estrutura robusta de pesquisa do elasticsearch que constrói índices com pesos para os termos (ou conjunto de termos) baseados na ocorrência deles no conjunto de textos da base (com TFIDF ou BM25).

O <b>último passo</b>, e contínuo, é a avaliação dos dados da base, remoção ou desativação de textos com pouca qualidade, etc.
Pode-se melhorar a pesquisa usando diversos recursos do elasticsearch como relacionar campos e pesos, incluir pesos em termos e aumentar ou diminuir scores. 

## Testando o classificador
É importante verificar se o classificador está fazendo uma boa classificação. Uma forma simples é incluir uma rotina que simule a classificação de textos já classificados, removendo o próprio texto da pesquisa (pelo seu ID) e depois retornar um percentual de acertos. Existem diversas técnicas de validação na ciência de dados, esse é só um começo de forma simples e com bons resultados.

## O que fazer se não está dando certo?
- Cada problema exige uma solução específica. Essa proposta visa facilitar o fluxo do processo de classificação, ou adivinhação de um valor de campo baseado em um texto dentro de um contexto. Caso a relação do campo textual com o campo de classificação seja fraca ou ambígua, é muito provável que o algoritmo reflita isso. Sendo assim, várias classificações podem aparecer com valores muito próximos. Isso também pode sugerir que duas classes devam ser unidas. Por exemplo textos parecidos indicarem  alegria em alguns casos e felicidade em outros. 
- O primeiro passo é verificar se os textos da base estão bem classificados
- Deve-se verificar também se o campo com o texto está bem mapeado. O uso de shingles e word_vectors como no exemplo deve melhorar a acurácia pois termos compostos começam a ganhar peso nas pesquisas, diminuindo o problema de termos ambiguos.
- Deve haver um conjunto de textos representativos de cada classe. O próprio uso e realimentação do elastic com novos textos pode melhorar o classificador.

## Concluindo ...
O exemplo aqui apresentado é muito simples, apenas para ilustrar a solução. 

O uso do elasticsearch facilita o processo de realimentação de dados onde o próprio fluxo de trabalho valida as novas entradas que farão parte do corpo de documentos do classificador. E a sua velocidade de indexação e simplicidade de manutenção trazem uma característica de sustentabilidade e aperfeiçeamento do modelo.

Essa proposta não tem a pretenção de substituir soluções baseadas em bibliotecas de <b>NLP</b> e <b>redes neurais</b> como outros exemplos que serão apresentados com o uso do <b>Spacy</b>. Tudo vai depender do problema que precisa ser resolvido, dos dados que estão disponíveis e com a disponibilidade de uma equipe para criação, validação e atualização de modelos. 

Baseado na publicação de <b>Saskia Vola</b>: https://www.elastic.co/blog/text-classification-made-easy-with-elasticsearch
