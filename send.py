from connection import connection

queue1 = 'queue1'
#create a channel
channel = connection.channel()
#declare a queue
channel.queue_declare(queue= queue1 )   
try:
    while True:
        message = input("Enter message: ")
        channel.basic_publish(exchange='', routing_key='queue1', body=message)
        print("message sent ..")
except keyboardInterrupt:
    pass
    connection.close()