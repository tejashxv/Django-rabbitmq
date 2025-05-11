import pika
import random 
import json


def publish_message(message):
    params = pika.URLParameters('amqps://gesxrrrl:n2Fns-HpIT0oz0U-XMzKld8JlUM6D--n@puffin.rmq2.cloudamqp.com/gesxrrrl')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    # message = f"Hello World! {random.randint(1, 100)}"
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    # print(f" [x] Sent {message}")
    connection.close()



















