import pika
import json
import pandas as pd
import openpyxl
import uuid


def GenExcel(message):
    message = json.loads(message)
    df = pd.DataFrame(message)
    df.to_excel(f'output_{uuid.uuid4()}.xlsx', index=False)
   



def callback(ch,method, properties, body):
    message = body.decode()
    GenExcel(message)
    
params = pika.URLParameters('amqps://gesxrrrl:n2Fns-HpIT0oz0U-XMzKld8JlUM6D--n@puffin.rmq2.cloudamqp.com/gesxrrrl')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello' , on_message_callback=callback, auto_ack=True)
print("start consuming")
channel.start_consuming()