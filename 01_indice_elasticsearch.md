# Criando o índice
Segue um exemplo simples de criação do índice no Elastic Search.
O maior segredo está na criação correta dos campos para permitir um score mais preciso e consequentemente uma associação correta com a classe que se desejada prever. O uso de <b>shingle</b> auxilia na criação de índices com termos compostos. No exemplo do filter <b>filtro_shingle</b> são criados shingles com 2 ou 3 termos.

PUT /meustextos/
{    "analysis": {
     "filter": {
       "stemmer_br": {"type": "stemmer", "language":   "brazilian" },
       "sinonimo_nomes" : { "type" : "synonym", "synonyms_path" : "sin_nomes.txt"},
       "filtro_shingle":{ "type":"shingle", "max_shingle_size":3,
                          "min_shingle_size":2, "output_unigrams":"true"}
     },
     "analyzer": {
       "texto_br": {
         "tokenizer":  "standard",
         "filter": ["lowercase","asciifolding","stemmer_br"]
       },
       "nome_br": {
         "tokenizer":  "whitespace",
         "filter": ["lowercase","asciifolding","sinonimo_nomes"]
       },
         "shingle_br":{
         "tokenizer":"standard",
         "filter":["standard","asciifolding", "lowercase", "stemmer_br","filtro_shingle"]
       },
         "shingle_raw":{
         "tokenizer":"standard",
         "filter":["standard","asciifolding", "lowercase", "filtro_shingle"]
       }
      }
   }
}

PUT /meustextos/_mapping/textos/
{ "properties": {
       "Id": { "type": "keyword"},
       "Autor": { "type": "text", "analyzer" : "nome_br"},
       "Texto": { "type": "text", "analyzer" : "texto_br",
                                "term_vector": "with_positions_offsets"  },
       "Texto_Shingle": { "analyzer": "shingle_br", "type":"text" },
       "Texto_Shingle_RAW": { "analyzer": "shingle_raw", "type":"text" },
       "Atualizacao": { "type": "date", 
          "format": "yyyy-MM-dd HH:mm:ss||yyyy-MM-dd HH:mm:ss.SSS||yyyy-MM-dd" }
     }
}



