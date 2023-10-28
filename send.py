from connection import connection

queue1 = 'queue1'
#create a channel
channel = connection.channel()
#declare a queue
channel.queue_declare(queue= queue1 )   
try:
    channel.basic_publish(exchange='', routing_key='queue1', body='Hello World!')
except keyboardInterrupt:
    pass
    connection.close()