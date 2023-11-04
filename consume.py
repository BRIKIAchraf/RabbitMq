from connection import connection

my_queue = "csharp"
#create channel 
channel = connection.channel()
channel.queue_declare(my_queue)
def callback_func(ch, method, properties, body):
    print(f"received -> {body}")
try :
    channel.basic_consume(queue=my_queue, on_message_callback=callback_func, auto_ack=True)
    channel.start_consuming()
except KeyboardInterrupt:
    pass
    connection.close()
    