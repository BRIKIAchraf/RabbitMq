import pika

credentials = pika.PlainCredentials("azcdxhax", "V0pGrjvEr1nGGh-JDBZT2wW56fyy7bZj")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="cow-01.rmq2.cloudamqp.com",
        credentials=credentials,
        port=5672,
        virtual_host="uqqmqcbd",
    )
)