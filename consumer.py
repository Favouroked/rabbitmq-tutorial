import json

from libraries.Rabbit import Rabbit
from libraries.Crawler import Crawler

rabbit = Rabbit()


def callback(ch, method, properties, body):
    body = json.loads(body.decode('utf-8'))
    print(body)
    print('Consuming this request')
    crawler = Crawler(body['start_chapter'], body['end_chapter'])
    crawler.start()
    ch.basic_ack(delivery_tag=method.delivery_tag)


rabbit.consume_queue(callback)
