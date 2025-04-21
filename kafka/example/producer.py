from confluent_kafka import Producer

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092'  # or your Kafka broker
}

# Create Producer instance
producer = Producer(conf)

# Delivery callback
def delivery_report(err, msg):
    if err is not None:
        print(f'Delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Produce some messages
for i in range(5):
    producer.produce('my_topic', key=str(i), value=f'hello {i}', callback=delivery_report)

# Wait for any outstanding messages to be delivered
producer.flush()
