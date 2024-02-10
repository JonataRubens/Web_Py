import requests 
from bs4 import BeautifulSoup

# Requisição para o site
link = "https://www.google.com/search?q=dolar+hoje"
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'}
requisicao = requests.get(link, headers=headers)

#print(requisicao)
#print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())      

titulo = site.find("title")
#print(titulo)

pesquisa = site.find_all("textarea")
#print(pesquisa)

pesquisa2 = site.find("textarea", class_="gLFyf")
print(pesquisa2["value"])
print("é")

cotacao = site.find("span", class_= "SwHCTb")
print(cotacao["data-value"])


