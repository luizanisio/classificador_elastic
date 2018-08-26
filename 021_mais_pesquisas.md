## Alguns exemplos complementares de tipos de pesquisas que podem ser feitas com o More Like This (MLT) do Elasticsearch

<b>Documentação do More Like This (MLT)</b>
- https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-mlt-query.html 

<b>Parâmetros:</b>
- <b>min_term_freq</b>: frequência mínima de termos para aceitar o documento (padrão 2)
- <b>min_doc_freq</b>: frequência mínima de documentos encontrados para usar o termo (padrão 5)
- <b>max_query_terms</b>: máximo número de query terms usados, quanto maior, mais acurado e mais pesado (padrão 25 - diz-se que o valore mágico é 12). 

<b>More like this simples:</b>
```json
{   "query": {
       "more_like_this" : {
           "fields" : ["titulo"],
           "like" : ["testando outro documento","testando elastic documento"],
           "min_term_freq" : 1,
           "min_doc_freq":1
       }  } }
```

<b>More like this simples retornando alguns campos apenas:</b>
```json
{  "_source": ["Unidade_Tecnico_SG","Descricao", "Solucao"],
"query": {
       "more_like_this" : {
           "fields" : ["titulo"],
           "like" : ["testando outro documento","testando elastic documento"],
           "min_term_freq" : 1,
           "min_doc_freq":1
       }  } }
```

<b>More like this com like e unlike:</b>
```json
{  "query": {
       "more_like_this" : {
           "fields" : ["titulo"],
           "like" : ["testando documento","testando elastic documento"],
           "unlike" : "outro documento",
           "min_term_freq" : 1,
           "min_doc_freq":1
       }    }  }
```

<b>More like this com filtro:</b>
```json
{  "query": {
   "bool": { "filter": [ 
      	{ "range" : { "ABERTURA" : {"gte" : "2017-01-01", "lt" :  "2018-05-01" } } }
      ,
        { "more_like_this" : {
           "fields" : ["DESCRICAO","SOLUCAO"],
           "like" : ["Clienta informou que não está conseguindo abrir o word"],
           "min_term_freq" : 1,
           "min_doc_freq":1  }
        } 
        ]
} } }
```

<b>More like this com booster em dois MLT:</b>
- https://stackoverflow.com/questions/26863350/boosting-in-more-like-this-elasticsearch 
- https://www.elastic.co/guide/en/elasticsearch/reference/6.2/compound-queries.html 

Para testar, basta criar dois critérios diferentes e alterar o boost para ver o resultado mudar.

Pode-se alterar a frequência dos termos entre os MLT para alterar o score de resultados sem descartar nenhum
```json
{   "_source": ["Unidade_Tecnico_SG","Descricao", "Solucao"],
    "query": { 
        "dis_max": {
           "queries": [
       {  "more_like_this": {
            "fields": ["Descricao","Solucao"],
            "like": ["usuario diz que visualizador de processos está com página em branco"],
            "min_term_freq": 1,
            "min_doc_freq": 1,
            "max_query_terms": 12,
            "boost":1
          }
               },
       {  "more_like_this": {
            "fields": ["Descricao","Solucao"],
            "like": ["gestão de peças eletrônicas página em branco"],
            "unlike" : ["visualizador","externo","SEI","iSTJ","agilis"],
            "min_term_freq": 1,
            "min_doc_freq": 1,
            "max_query_terms": 12,
            "boost": 0.8
          }
       }
            ]
        }
    }
}
```


<b>More Like This com booster dependendo de resultados de filtros:</b>
https://www.elastic.co/guide/en/elasticsearch/reference/6.2/query-dsl-function-score-query.html#function-weight 
- min_score retira do resultado valores abaixo
- score_mode - max - vai usar o máximo score das funções
- boost_mode - multiply - multiplica o valor das functions pelo score do documento
- max_boost - é o valor máximo do boost para ser aplicado ao score
```json
{   "_source": ["Unidade_Tecnico_SG","Descricao", "Solucao","Tipo_Estrutura"],
    "query": { 
        "function_score": {
          "query": { 
            "more_like_this": {
            "fields": ["Descricao","Solucao"],
            "like": ["usuario diz que visualizador de processos está com página em branco"],
            "min_term_freq": 1,
            "min_doc_freq": 1,
            "max_query_terms": 12
          }            
          },
          "functions": [
              {   "filter": { "term" : { "Tipo_Estrutura": "Subchamado" } },
                  "weight": 1.1
              },
              {
                  "filter": { "term" : { "Tipo_Estrutura": "Chamado" } },
                  "weight": 0.8
              }
          ],
          "max_boost": 42,
          "score_mode": "max",
          "boost_mode": "multiply",
          "min_score" : 0
    }
}}
```

<b>Filtros por script:</b>
Alguns atributos/métodos não funcionam em campos text. Se criar o keyword do text, alguns atributos/métodos funcionam, outros não (rsr). 

<b>Filtro verificando o tamanho de um campo texto:</b>
```json
{"query": {"script" : {"script": "doc['Texto'].value.length() >= 4 " } } 
```

<b>Filtro verificando se um campo existe e se um campo texto é maior que outro:</b>
```json
{ "_source" : ["Texto","Descricao","Unidade"],
  "query": { "bool" : { "must_not" : {"term": {"Fold": 1 }},
                          "must" :  [
                        {"exists" : { "field" : "Texto" }},
                        {"exists" : { "field" : "Descricao" }},
                        {"range" :  { "Unidades" : {"gte" : 5 }}},
                        {"script":  { "script": "return doc['Descricao'].value>=doc['Texto'].value;"}} ]
    }}  }
```

<b>Filtros semelhantes ao in do SQL:</b> <i>Tipo in ('Artigo','Tese')</i>
```json
{ "size": 2000,
       "_source": ["CodigoProduto" ],
       "query": {
           "bool": {
               "must": [
                   {"match": {"Validado": "S"}},
                   {"match": {"Concluido": "N"}},
                   {"script": 
                      { "script": "return doc['Texto'].length>=3;"}},
                   {"range" : { "Num_Palavras" : {"gte": 15 } }},
                   {"bool": {"should": 
                      [{"match": { "Tipo":"Artigo"}},
                       {"match": { "Tipo":"Tese"}}
                      ], "minimum_should_match" : 1  }}
               ]
           }
       }
   }
```
