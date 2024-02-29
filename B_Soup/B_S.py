import requests 
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

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

###########################################################
conn = sqlite3.connect('dados_cotacao.bd')

conn.execute('''CREATE TABLE IF NOT EXISTS cotacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data_pesquisa TEXT,
                valor_cotacao REAL)'''
            )

conn = sqlite3.connect('dados_cotacao.bd')

data_pesquisa = datetime.now() .strftime("%Y-%m-%d %H:%M:%S")

valor_cotacao = cotacao["data-value"]

conn.execute('''
             INSERT INTO cotacao (data_pesquisa, valor_cotacao)
             VALUES (?, ?)
             ''', (data_pesquisa, valor_cotacao))

conn.commit()

conn.close()