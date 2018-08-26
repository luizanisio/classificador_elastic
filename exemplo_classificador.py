# coding=utf-8
from requests.auth import HTTPBasicAuth
import requests
import json

class Elastic:
    def __init__(self, host='http://elasticsearch:9200', indice='', tipo='', usuario=None, senha=None):
        self.host = host
        self.indice = indice
        self.tipo = tipo
        self.usr = usuario
        self.psd = senha

    def url_elastic(self, indice=True, tipo=True, funcionalidade=None):
        result = self.host
        if indice: result = result + '/' + self.indice
        if tipo: result = result + '/' + self.tipo
        if funcionalidade: result = result + '/' + funcionalidade
        return result

    def url_search(self):
        return self.url_elastic(True, True, '_search')

    def url_analyze(self):
        return self.url_elastic(True, False, '_analyze')

    def url_term_vectors(self):
        return self.url_elastic(True, True, '_termvectors')

    def url_indice(self):
        return self.url_elastic(True, False)

    def url_tipo(self):
        return self.url_elastic(True, True)

    def requisicao(self, url, json_data, metodo):
        if metodo == 'GET':
            r = requests.get(url, json=json_data, auth=HTTPBasicAuth(self.usr, self.psd))
        elif metodo == 'POST':
            r = requests.post(url, json=json_data, auth=HTTPBasicAuth(self.usr, self.psd))
        elif metodo == 'PUT':
            r = requests.put(url, json=json_data, auth=HTTPBasicAuth(self.usr, self.psd))
        elif metodo == 'DELETE':
            r = requests.delete(url, auth=HTTPBasicAuth(self.usr, self.psd))
        return json.loads(r.content.decode())

    def get(self, url, json_data=None):
        resultado = self.requisicao(url, json_data, 'GET')
        return resultado

    def post(self, url, json_data):
        resultado = self.requisicao(url, json_data, 'POST')
        return resultado

    def put(self, url, json_data):
        resultado = self.requisicao(url, json_data, 'PUT')
        return resultado

    def delete(self, url, json_data):
        resultado = self.requisicao(url, json_data, 'DELETE')
        return resultado

    def search(self, json_data=None):
        if json_data:
            return self.post(self.url_search(), json_data)
        else:
            return self.get(self.url_search())

    def analyze(self, analyzer, campo, texto):
        if campo and (campo != ''):
            dados = {"field": campo, "text": texto}
        else:
            dados = {"analyzer": analyzer, "text": texto}
        resultado = self.post(self.url_analyze(), dados)
        if resultado.get('status') == 404:
            raise ValueError(''.join(['Não foi possível identificar o analyzer especificado [', analyzer,
                                      '] no índice [', self.indice, '] - erro 404']))
        if resultado:
            return resultado['tokens']
        else:
            return {}

    def classificar(self, query, campo_classe):
        assert query and campo_classe and len(query)>0 and len(campo_classe)>0, "Elastic.classificar: É necessário informar a query e o campo_classe usados na classificação"
        res = self.search(query)
        if not res:
            return []
        res = res.get('hits', {}).get('hits', [])
        scores = {}
        for r in res:
            classe = r.get('_source', {}).get(campo_classe, '')
            score = r.get('_score', 0)
            scores[classe] = score + scores.get(classe, 0)
        return scores

if __name__ == "__main__":
    elastic = Elastic('http://localhost:9200', 'meustextos', 'textos', '', '')
    '''print("## Dados do elastic ###############################")

    res = elastic.search({"size" : 1000})
    res = res.get('hits',{}).get('hits',[])
    res = [ r.get('_source',{}) for r in res]
    [ print ("POST meustextos/textos/{}\n".format(r.get('Id')),r,"\n") for r in res]
    '''

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

