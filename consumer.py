from libraries.Rabbit import Rabbit

rabbit = Rabbit()


def callback(ch, method, properties, body):
    body = body.decode('utf-8')
    print(body)
    print('Consuming this request')
    ch.basic_ack(delivery_tag=method.delivery_tag)


rabbit.consume_queue(callback)
