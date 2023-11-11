from bs4 import BeautifulSoup
import requests

URL = "https://www.parlamento.pt/ArquivoDocumentacao/Paginas/Arquivodevotacoes.aspx"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

votes_list = soup.find_all("div", class_="row home_calendar hc-detail") # row home_calendar hc-detail

print(votes_list)

#print(soup.prettify())