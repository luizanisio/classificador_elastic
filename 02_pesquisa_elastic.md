# Pesquisa para classificação
Segue o exemplo de uma pesquisa no elasticsearch comparando o texto apresentado com os textos da base.
A escolha dos campos e critérios de pesquisa (shingle, shingle_raw, autor, peso dos votos) afeta o resultado, positicamente ou negativamente. 

```json
POST meustextos/textos/_search
{ "size" : 7,
  "_source": ["Classificacao","Texto"],
    "query": { 
        "function_score": {
          "query": { 
            "more_like_this": {
            "fields": ["Texto","Texto_Shingle"],
            "like": ["isso é muito legal"],
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
          "min_score" : 0
    }
}}
