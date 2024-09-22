import pika

def callback_message(ch, method, properties, body) :
    print(body)
    print(type(body))

connection_parameters = pika.ConnectionParameters(
    host='rabbit',
    port=5672,
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(
    queue='data_queue',
    durable=True
)

channel.basic_consume(
    queue='data_queue',
    auto_ack=True,
    on_message_callback=callback_message
)

print(f'Listen RabbitMQ on Port 5672')
channel.start_consuming()