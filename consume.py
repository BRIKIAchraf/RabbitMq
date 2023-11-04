from connection import connection
queue1 = 'queue1'
channel = connection.channel()
channel.queue_declare(queue='queue1')

def callback_func(ch, method, properties, body):
    print (f"received -> {body}")
    #logic goes here 
    channel.basic_ack(delivery_tag=method.delivery_tag)
    
channel.basic_consume(queue='queue1', on_message_callback=callback_func, auto_ack=True)
channel.start_consuming()
