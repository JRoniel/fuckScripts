# FUNCIONALIDADE:
# CHECAR SE EXISTE UMA 'PALAVRA-CHAVE' INCLUSA NA DESCRIÇÃO DE UM VÍDEO DE YOUTUBE
# PODE SER REPLICADO PARA PROCURAR PALAVRAS CHAVES EM OUTROS SITES

# REQUERIMENTOS:
#pip install requests_html bs4

from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs

#Capturando informações nescessárias, Url do vídeo do youtube a ser checado.
channel = input("Url do vídeo a ser checado...")
word = input("Palavra a ser checada")

#Pescando e checando valores no video
response = HTMLSession().get(channel)
soup = bs(response.html.html, "html.parser")
description = soup.find("meta", itemprop="description")["content"]

#Verificar funcionamento
if word in description:
    print("Palavra encontrada!")
else:
    print("Essa palavra não existe aqui...")
