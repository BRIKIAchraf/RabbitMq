from connexion import connection
queue_name = ["achraf", "achraf2"]
channel = connection.channel()
channel.exchange_declare