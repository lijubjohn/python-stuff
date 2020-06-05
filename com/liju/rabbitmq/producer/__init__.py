#!/usr/bin/env python

import pika
credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World22!')
print(" [x] Sent 'Hello World!!!'")

connection.close()
