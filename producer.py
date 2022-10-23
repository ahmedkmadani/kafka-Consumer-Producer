from kafka import KafkaProducer
from time import sleep
import requests
import json

url = 'https://api.coinbase.com/v2/prices/btc-usd/spot'

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))

while True:
    sleep(2)
    price = (requests.get(url).json())
    print("Price fetched")
    producer.send('first-topic', price)
    print('Price sent to consumer')
