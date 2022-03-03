#pip install requests_html bs4

from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs

channel = input("Url youtube video...")
word = input("Word to check is...")

response = HTMLSession().get(channel)
soup = bs(response.html.html, "html.parser")
description = soup.find("meta", itemprop="description")["content"]

if word in description:
    print("Found word")
else:
    print("Not found word")
