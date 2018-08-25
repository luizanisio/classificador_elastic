FROM python:3.6.5-alpine3.7

#exemplo base para criar uma imagem com spacy 
#para servir modelos em python ou treinamentos de modelos
#para gerar a imagem base: docker build -t spacybase .

RUN apk add --no-cache tzdata
ENV TZ=America/Sao_Paulo
	 
WORKDIR /usr/src/app

RUN apk update && \
    apk upgrade && \
    apk add --no-cache libstdc++ && \
    apk add --no-cache --virtual=build_deps g++ gfortran && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
	pip3 install --upgrade pip setuptools && \
    pip3 install --no-cache-dir spacy && \
	pip3 install --no-cache-dir flask && \
	python -m spacy download pt &&\
    rm /usr/include/xlocale.h && \
    apk del build_deps
