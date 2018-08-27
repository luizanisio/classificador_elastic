## Algumas dicas que consolidei para resolver problemas no dia-a-dia

### Retirar do read only quando ocorrem erros no elasticsearch
- <i>ERRO: FORBIDDEN/12/index read-only / allow delete (api)</i>

Pode ocorrer por falta de espaço, ou problemas diversos, deixando o índice em readonly.
```json
PUT /meustextos/_settings
    {     "index": {
    "blocks": {
    "read_only_allow_delete": "false"
    }   }     }
```

### Copiando dados de um índice para outro:
- <b>/_reindex?wait_for_completion=true</b>   (para não dar timeout)
<b>Copiando todos os dados:</b>

```json
POST /_reindex
{   "source": {
    "index": "twitter"  },
  "dest": { "index": "new_twitter"} }
```

<b>Copiando dados filtrados:</b>
```json
POST /_reindex
{   "source": {
    "index": "twitter",
    "query": {     "term": {      "user": "kimchy"      }     }   
},   "dest": {
    "index": "new_twitter"
  } }
```

<b>Copiando dados randômicos:</b>
```json
POST _reindex
{ "size": 10,
  "source": {
    "index": "meustextos",
    "query": {
      "function_score" : {
        "query" : { "match_all": {} },
        "random_score" : {}
      }    },
    "sort": "_score"    
  },
  "dest": {
    "index": "teste"
  }}
```

### Update by query:
```json
POST teste/_update_by_query?conflicts=proceed
{ "query": { 
    "term": {
      "Tipo_produto": 1
    }
  },
  "script": {
    "source": "ctx._source['Atualizacao'] = '' "
  }
}
```

### Update all
```json
POST meusdocumentos/_update_by_query?conflicts=proceed&wait_for_completion=true
{  "query": { "match_all": {} }
  ,"script": {
    "source": "ctx._source['Atualizacao'] = '2000-01-01 00:00:00.000' "
  }
}
```
### Delete by query:
```json
POST teste/_delete_by_query
{ "query": { 
    "term": {
      "Tipo_produto": 1
    }
  }
}
```
