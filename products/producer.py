import pika

params = pika.URLParameters('amqp://guest:guest@localhost:5672/%2F')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')