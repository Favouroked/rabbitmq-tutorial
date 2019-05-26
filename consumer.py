import json

from libraries.Rabbit import Rabbit
from libraries.Crawler import Crawler
from libraries.Utilities import convert_to_pdf, send_email

rabbit = Rabbit()


def callback(ch, method, properties, body):
    body = json.loads(body.decode('utf-8'))
    print("[x] {}".format(body))
    print('[x] Consuming this request')
    crawler = Crawler(body['start_chapter'], body['end_chapter'])
    book_name, txt_path = crawler.start()
    pdf_path = convert_to_pdf(txt_path, book_name)
    send_email(pdf_path, book_name, body['email'])
    ch.basic_ack(delivery_tag=method.delivery_tag)


rabbit.consume_queue(callback)
