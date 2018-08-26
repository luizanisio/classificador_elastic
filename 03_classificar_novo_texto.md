# Algoritmos de score para as classes
Aqui será mostrado um algoritmo em python e um em angular que faz a consulta no elasticsearch e contabiliza os scores para prever a classe no novo texto.
Pode-se criar um campo "Ativo", ou "Descartado" para não usar determinados textos na classificação, melhorando a predição para textos mal escritos ou com classificações iprecisas.
Pode-se também criar um campo "Validado" para inserir um fluxo de validação dos textos utilizados pelo algoritmo.

Os algoritmos são simples e estão baseados no artigo de Saskia Vola em https://www.elastic.co/blog/text-classification-made-easy-with-elasticsearch

### Python

O arquivo <b>exemplo_classificador.py</b> demonstra uma classe base para uso do elasticsearch (<b>Elastic</b>) em python, incluindo o método <b>classificar</b>
- os parâmetros são a query do elastic e o campo usado para classificação.
- o exemplo é a implementação direta da proposta de Saskia Vola e demonstrou um ótimo resultado em alguns contextos.
- um size muito grande pode atrapalhar, já que pode retornar vários resultados com scores baixos de uma classe que somados resultarão em um score maior para a pior classe.

```py
    elastic = Elastic('http://localhost:9200', 'meustextos', 'textos', '', '')
    print('### Retorno da classificação do texto')
    textoNovo="isso é muito legal, adoro esse texto"
    campo='Classificacao'
    campoTexto='Texto_Shingle'
    query= { "size" : 7,
      "_source": [campo],
        "query": {
            "function_score": {
              "query": {
                "more_like_this": {
                "fields": [campoTexto],
                "like": textoNovo,
                "min_term_freq": 1,
                "min_doc_freq": 1,
                "max_query_terms": 3
              }
              },
              "functions": [
                  {   "field_value_factor": {
                        "field": "Votos",
                        "factor": 2,
                        "modifier": "sqrt",
                        "missing": 1
                    }
                  }
              ],
              "max_boost": 2,
              "boost_mode": "multiply",
              "min_score" : 0.7
        }  }  }

    scores = elastic.classificar(query=query,campo_classe='Classificacao')
    print('Classes e scores',scores)
```

Abaixo segue o resultado usando as frases de exemplo, sem pretensão de acertar, pois não há exemplos suficientes para uma boa classificação. Com isso a frase <b>"isso é muito legal, adoro esse texto"</b> receberia a classificação de <b>Alegria</b>. Caso o usuário alterasse a classificação, e esse texto fosse inserido no elastic, o algoritmo iria <b>"aprender"</b> essa nova classificação.
```
### Retorno da classificação do texto
Classes e scores [('Alegria', 6.864011959999999), ('Amor', 2.0344672), ('Tristeza', 1.6214796), ('Raiva', 1.2806222), ('Amizade', 1.0230638)]
```

Em breve será incluído um exemplo usando flask para responder requisições do angular na classificação contínua em um fluxo simples de trabalho.
1. Pesquisar textos
2. inserir um novo texto e receber a sugestão da classe
3. possibilidade de ajustar a classe, aperfeiçoando as próximas classificações

### Angular

...em breve
