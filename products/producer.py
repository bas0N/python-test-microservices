import pika,json
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join('/app/.env')
print("the path is", dotenv_path)
load_dotenv(dotenv_path)
rabbit_mq_url = os.environ.get('RABBITMQ')

if(rabbit_mq_url is None):
    raise Exception("RABBITMQ not found in environment variables")

params = pika.URLParameters(rabbit_mq_url)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)