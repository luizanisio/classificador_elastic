# Exemplos 
- Copie e cole os dados abaixo no kibana, selecione tudo e tecle ctrl+enter para inserir todos os exemplos no índice
- A inserção deve ser feita depois do índice criado e os campos definidos

### Script para inserir os exemplos no kibana

```json
POST meustextos/textos/1
{ "Id" : 1,
  "Autor" : "Maria da Quitanda",
  "Classificacao" : "Desgosto", "Votos" : 2,
  "Texto" : "Detesto frutas, são muito doces e cheias de líquido.",
  "Texto_Shingle" : "Detesto frutas, são muito doces e cheias de líquido.",
  "Texto_Shingle_Raw" : "Detesto frutas, são muito doces e cheias de líquido.",
  "Atualizacao" : "2018-01-01 10:22:33"
}


POST meustextos/textos/2
{ "Id" : 2,
  "Autor" : "Marcel Proust",
  "Classificacao" : "Filosofico", "Votos" : 1,
  "Texto" : "O amor causa verdadeiros levantamentos geológicos do pensamento.",
  "Texto_Shingle" : "O amor causa verdadeiros levantamentos geológicos do pensamento.",
  "Texto_Shingle_Raw" : "O amor causa verdadeiros levantamentos geológicos do pensamento.",
  "Atualizacao" : "2018-01-01 10:22:33"
}

POST meustextos/textos/3
{ "Id" : 3,
  "Autor" : "Felícius",
  "Classificacao" : "Feliz", "Votos" : 3,
  "Texto" : "Gosto muito de coisas boas, a felicidade é o segredo do sucesso.",
  "Texto_Shingle" : "Gosto muito de coisas boas, a felicidade é o segredo do sucesso.",
  "Texto_Shingle_Raw" : "Gosto muito de coisas boas, a felicidade é o segredo do sucesso.",
  "Atualizacao" : "2018-01-01 10:22:33"
}

POST meustextos/textos/4
{ "Id" : 4,
  "Autor" : "Indecísius",
  "Classificacao" : "Neutro", "Votos" : 1,
  "Texto" : "É interessante, nem bom, nem ruim.",
  "Texto_Shingle" : "É interessante, nem bom, nem ruim.",
  "Texto_Shingle_Raw" : "É interessante, nem bom, nem ruim.",
  "Atualizacao" : "2018-01-01 10:22:33"
}

POST meustextos/textos/1
	{	"Id": "1",
		"Classificacao": "Alegria",
		"Autor": "Ippolito",
		"Texto": "A alegria é a juventude eterna do ânimo.",
		"Texto_Shingle": "A alegria é a juventude eterna do ânimo.",
		"Texto_Shingle_Raw": "A alegria é a juventude eterna do ânimo.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/2
	{	"Id": "2",
		"Classificacao": "Alegria",
		"Autor": "Rubem Alves",
		"Texto": "O prazer é único, não se repete. A alegria repete-se sempre. Basta lembrar.",
		"Texto_Shingle": "O prazer é único, não se repete. A alegria repete-se sempre. Basta lembrar.",
		"Texto_Shingle_Raw": "O prazer é único, não se repete. A alegria repete-se sempre. Basta lembrar.",
		"Atualizacao": "2018-08-22 13:14:15"
	}
	
POST meustextos/textos/3
	{	"Id": "3",
		"Classificacao": "Alegria",
		"Autor": "Kliksberg",
		"Texto": "A alegria de contemplar e de conhecer é a mais bela dádiva da natureza. ",
		"Texto_Shingle": "A alegria de contemplar e de conhecer é a mais bela dádiva da natureza. ",
		"Texto_Shingle_Raw": "A alegria de contemplar e de conhecer é a mais bela dádiva da natureza. ",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/4
	{	"Id": "4",
		"Classificacao": "Alegria",
		"Autor": "Barthélemy",
		"Texto": "A alegria é a saúde da alma. ",
		"Texto_Shingle": "A alegria é a saúde da alma. ",
		"Texto_Shingle_Raw": "A alegria é a saúde da alma. ",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/5
	{	"Id": "5",
		"Classificacao": "Alegria",
		"Autor": "Charles Chaplin",
		"Texto": "Estou sempre alegre. Essa é a maneira de resolver os problemas da vida. ",
		"Texto_Shingle": "Estou sempre alegre. Essa é a maneira de resolver os problemas da vida. ",
		"Texto_Shingle_Raw": "Estou sempre alegre. Essa é a maneira de resolver os problemas da vida. ",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/6
	{	"Id": "6",
		"Classificacao": "Amizade",
		"Autor": "Lincoln",
		"Texto": "A melhor parte da vida são as amizades.",
		"Texto_Shingle": "A melhor parte da vida são as amizades.",
		"Texto_Shingle_Raw": "A melhor parte da vida são as amizades.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/7
	{	"Id": "7",
		"Classificacao": "Amizade",
		"Autor": "Caleb Colton",
		"Texto": "A verdadeira amizade é como a saúde perfeita, seu valor raramente é reconhecido até que seja perdida.",
		"Texto_Shingle": "A verdadeira amizade é como a saúde perfeita, seu valor raramente é reconhecido até que seja perdida.",
		"Texto_Shingle_Raw": "A verdadeira amizade é como a saúde perfeita, seu valor raramente é reconhecido até que seja perdida.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/8
	{	"Id": "8",
		"Classificacao": "Amizade",
		"Autor": "Vinícius de Moraes",
		"Texto": "A gente não faz amigos, reconhece-os.",
		"Texto_Shingle": "A gente não faz amigos, reconhece-os.",
		"Texto_Shingle_Raw": "A gente não faz amigos, reconhece-os.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/9
	{	"Id": "9",
		"Classificacao": "Amizade",
		"Autor": "Caminhão",
		"Texto": "Os amigos escutam o que você fala. Os melhores amigos prestam atenção ao que você não diz.",
		"Texto_Shingle": "Os amigos escutam o que você fala. Os melhores amigos prestam atenção ao que você não diz.",
		"Texto_Shingle_Raw": "Os amigos escutam o que você fala. Os melhores amigos prestam atenção ao que você não diz.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/10
	{	"Id": "10",
		"Classificacao": "Amor",
		"Autor": "Hubbard",
		"Texto": "O amor que damos é o único que preservamos.",
		"Texto_Shingle": "O amor que damos é o único que preservamos.",
		"Texto_Shingle_Raw": "O amor que damos é o único que preservamos.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/11
	{	"Id": "11",
		"Classificacao": "Amor",
		"Autor": "Pascal",
		"Texto": "Amar é preservar a sua singularidade.",
		"Texto_Shingle": "Amar é preservar a sua singularidade.",
		"Texto_Shingle_Raw": "Amar é preservar a sua singularidade.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/12
	{	"Id": "12",
		"Classificacao": "Amor",
		"Autor": "Desmond Tutu",
		"Texto": "Não somos amados por sermos bons. Somos bons porque somos amados.",
		"Texto_Shingle": "Não somos amados por sermos bons. Somos bons porque somos amados.",
		"Texto_Shingle_Raw": "Não somos amados por sermos bons. Somos bons porque somos amados.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/13
	{	"Id": "13",
		"Classificacao": "Amore",
		"Autor": "anônimo",
		"Texto": "Comprimidos aliviam a dor, mas só o amor alivia o sofrimento.",
		"Texto_Shingle": "Comprimidos aliviam a dor, mas só o amor alivia o sofrimento.",
		"Texto_Shingle_Raw": "Comprimidos aliviam a dor, mas só o amor alivia o sofrimento.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/14
	{	"Id": "14",
		"Classificacao": "Raiva",
		"Autor": "Mário Quintana",
		"Texto": "Se eu pudesse eu pegava a dor. Colocava dentro de um envelope e devolvia ao remetente!",
		"Texto_Shingle": "Se eu pudesse eu pegava a dor. Colocava dentro de um envelope e devolvia ao remetente!",
		"Texto_Shingle_Raw": "Se eu pudesse eu pegava a dor. Colocava dentro de um envelope e devolvia ao remetente!",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/15
	{	"Id": "15",
		"Classificacao": "Raiva",
		"Autor": "Selena Gomez",
		"Texto": "A ironia da dor é que você quer ser consolado por quem te machucou.",
		"Texto_Shingle": "A ironia da dor é que você quer ser consolado por quem te machucou.",
		"Texto_Shingle_Raw": "A ironia da dor é que você quer ser consolado por quem te machucou.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/16
	{	"Id": "16",
		"Classificacao": "Raiva",
		"Autor": "Jeannie Tenney",
		"Texto": "A raiva pode ser breve, mas pode causar danos que vão durar para sempre.",
		"Texto_Shingle": "A raiva pode ser breve, mas pode causar danos que vão durar para sempre.",
		"Texto_Shingle_Raw": "A raiva pode ser breve, mas pode causar danos que vão durar para sempre.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/17
	{	"Id": "17",
		"Classificacao": "Raiva",
		"Autor": "Sheldon",
		"Texto": "Odeio quem fala tô chegando, quando ainda nem saiu de casa.",
		"Texto_Shingle": "Odeio quem fala tô chegando, quando ainda nem saiu de casa.",
		"Texto_Shingle_Raw": "Odeio quem fala tô chegando, quando ainda nem saiu de casa.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/18
	{	"Id": "18",
		"Classificacao": "Tristeza",
		"Autor": "Filme",
		"Texto": "Estou cansado. Cansado de pessoas sendo ruins umas com as outras. Cansado de toda a dor que eu sinto e ouço no mundo todos os dias.",
		"Texto_Shingle": "Estou cansado. Cansado de pessoas sendo ruins umas com as outras. Cansado de toda a dor que eu sinto e ouço no mundo todos os dias.",
		"Texto_Shingle_Raw": "Estou cansado. Cansado de pessoas sendo ruins umas com as outras. Cansado de toda a dor que eu sinto e ouço no mundo todos os dias.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/19
	{	"Id": "19",
		"Classificacao": "Tristeza",
		"Autor": "anônimo",
		"Texto": "O veneno da dor causada a outros, retornará a você.",
		"Texto_Shingle": "O veneno da dor causada a outros, retornará a você.",
		"Texto_Shingle_Raw": "O veneno da dor causada a outros, retornará a você.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/20
	{	"Id": "20",
		"Classificacao": "Tristeza",
		"Autor": "Nathália Theylor",
		"Texto": "Magoar quem a gente gosta dói na gente mesmo.",
		"Texto_Shingle": "Magoar quem a gente gosta dói na gente mesmo.",
		"Texto_Shingle_Raw": "Magoar quem a gente gosta dói na gente mesmo.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/21
	{	"Id": "21",
		"Classificacao": "Tristeza",
		"Autor": "Querido John",
		"Texto": "Sinto tanto a sua falta que até dói.",
		"Texto_Shingle": "Sinto tanto a sua falta que até dói.",
		"Texto_Shingle_Raw": "Sinto tanto a sua falta que até dói.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/22
	{	"Id": "22",
		"Classificacao": "Raiva",
		"Autor": "Nietzsche",
		"Texto": "Detesto quem me rouba a solidão sem em troca me oferecer verdadeira companhia.",
		"Texto_Shingle": "Detesto quem me rouba a solidão sem em troca me oferecer verdadeira companhia.",
		"Texto_Shingle_Raw": "Detesto quem me rouba a solidão sem em troca me oferecer verdadeira companhia.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/23
	{	"Id": "23",
		"Classificacao": "Raiva",
		"Autor": "Caio Abreu",
		"Texto": "Odeio circo. Aliás, odeio tudo que me encanta e depois vai embora.",
		"Texto_Shingle": "Odeio circo. Aliás, odeio tudo que me encanta e depois vai embora.",
		"Texto_Shingle_Raw": "Odeio circo. Aliás, odeio tudo que me encanta e depois vai embora.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/24
	{	"Id": "24",
		"Classificacao": "Tristeza",
		"Autor": "Caio Abreu",
		"Texto": "Sofrer dói. Dói e não é pouco. Mas faz um bem danado depois que passa.",
		"Texto_Shingle": "Sofrer dói. Dói e não é pouco. Mas faz um bem danado depois que passa.",
		"Texto_Shingle_Raw": "Sofrer dói. Dói e não é pouco. Mas faz um bem danado depois que passa.",
		"Atualizacao": "2018-08-22 13:14:15"
	}

POST meustextos/textos/_search

