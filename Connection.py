import pika

credentials = pika.PlainCredentials("qnmbfmzr", "kggkrhGqamt6J5PR16bNsci1-nFWvAn1")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="cow-01.rmq2.cloudamqp.com",credentials=credentials,port=5672,virtual_host="qnmbfmzr",)
)