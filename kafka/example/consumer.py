from confluent_kafka import Consumer, KafkaException

# Kafka config
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'  # Read messages from beginning if no offset exists
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to topic
consumer.subscribe(['my_topic'])

print("Starting consumer...")

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            print(f"Received message: {msg.value().decode('utf-8')} (key: {msg.key()})")

except KeyboardInterrupt:
    pass
finally:
    # Leave group and commit final offsets
    consumer.close()
