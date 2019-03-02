import pika
import sys

conn_params = pika.ConnectionParameters('localhost', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.exchange_declare(exchange='topic_example',
                         exchange_type='topic')

routing_key = 'mocked.key'
if len(sys.argv) >= 2:
    routing_key = sys.argv[1]

message = ' '.join(sys.argv[2:]) or routing_key
channel.basic_publish(exchange='topic_example',
                      routing_key=routing_key,
                      body=message)

print("Sent %r:%r" % (routing_key, message))
connection.close()
