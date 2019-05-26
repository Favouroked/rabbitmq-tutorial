import pika
import json

from .Config import config


class Rabbit:
    def __init__(self):
        queue_name = config['rabbitmq']['queue_name']
        print('About to establish queue {}'.format(queue_name))
        self.queue_name = queue_name
        host = config['rabbitmq']['host']
        port = config['rabbitmq']['port']
        username = config['rabbitmq']['username']
        password = config['rabbitmq']['password']
        credentials = pika.PlainCredentials(username, password)
        parameters = pika.ConnectionParameters(host, port, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)

    def push_to_queue(self, data):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=json.dumps(data))
        return {'status': True, 'message': 'Message sent'}

    def consume_queue(self, callback):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=callback)
        print('[x] Waiting for messages. To exit, press CTRL+C')
        self.channel.start_consuming()
