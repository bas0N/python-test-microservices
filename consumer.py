import pika
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
print("the path is", dotenv_path)
load_dotenv(dotenv_path)
rabbit_mq_url = os.environ.get('RABBITMQ')

if(rabbit_mq_url is None):
    raise Exception("RABBITMQ not found in environment variables")

params = pika.URLParameters(rabbit_mq_url)

connection = pika.BlockingConnection(params)

if(connection.is_open):
    print('Connection opened')
else:
    print('Connection error')

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback,auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

