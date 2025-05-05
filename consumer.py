import pika

def callback(ch,method, properties, body):
    message = body.decode()
    print(message)
    
params = pika.URLParameters('amqps://gesxrrrl:n2Fns-HpIT0oz0U-XMzKld8JlUM6D--n@puffin.rmq2.cloudamqp.com/gesxrrrl')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(queue='hello' , on_message_callback=callback, auto_ack=True)
print("start consuming")
channel.start_consuming()