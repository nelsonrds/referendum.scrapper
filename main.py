from bs4 import BeautifulSoup
import requests
import os
import pika

rabbitmq_host = os.environ.get("RABBITMQ_HOST", 'localhost')
rabbitmq_queue = os.environ.get("RABBITMQ_QUEUE", 'laws')

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()
channel.queue_declare(queue=rabbitmq_queue)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")


URL = "https://www.parlamento.pt/ArquivoDocumentacao/Paginas/Arquivodevotacoes.aspx"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

votes_list = soup.find_all("div", class_="row home_calendar hc-detail") # row home_calendar hc-detail

print(votes_list)

#print(soup.prettify())