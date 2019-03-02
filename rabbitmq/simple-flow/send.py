#!/usr/bin/env python
import pika
import time

conn_params = pika.ConnectionParameters('localhost', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

for i in range(100):
    channel.basic_publish(exchange='',
			  routing_key='first-queue',
			  body='Hi, consumer!')
    print("Greeting sent")
    time.sleep(2)

connection.close()
