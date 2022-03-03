#Instalando dependencias com o PIP
#pip install requests_html bs4

from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs

#Capturando informações nescessárias, Url do vídeo do youtube a ser checado.
channel = input("Url youtube video...")
word = input("Word to check is...")

#Pescando e checando valores no video
response = HTMLSession().get(channel)
soup = bs(response.html.html, "html.parser")
description = soup.find("meta", itemprop="description")["content"]

#Verificar funcionamento
if word in description:
    print("Found word")
else:
    print("Not found word")
