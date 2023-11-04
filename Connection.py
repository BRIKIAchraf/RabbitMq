import pika

credentials = pika.PlainCredentials("ofjvtkrg", "L1glukL7Wh8W8V00fbIOTAXjmU-vSlc0")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="cow-01.rmq2.cloudamqp.com",credentials=credentials,port=5672,virtual_host="ofjvtkrg",)
)