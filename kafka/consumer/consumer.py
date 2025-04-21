from confluent_kafka import Consumer, KafkaError
import json
import sys

def create_consumer(host: str, port: int = 9092, group_id: str = "log_consumer_group"):
        """
        Create and configure a Kafka consumer.
        """
        try:
                config = {
                        'bootstrap.servers': f"{host}:{port}",
                        'group.id': group_id,
                        'auto.offset.reset': 'earliest',  # Start reading at the earliest message
                        'enable.auto.commit': True,       # Automatically commit offsets
                        'max.poll.records': 100          # Limit records per poll for controlled processing
                }
                consumer = Consumer(config)
                consumer.subscribe(['logs'])  # Subscribe to the 'logs' topic
                print("Consumer connected to Kafka server and subscribed to 'logs' topic.")
                return consumer
        except Exception as e:
                print(f"Error connecting to Kafka server: {e}")
                return None

def process_message(message):
        """
        Process a single Kafka message.
        """
        try:
                key = message.key().decode('utf-8') if message.key() else None
                value = json.loads(message.value().decode('utf-8'))  # Deserialize JSON message
                print(f"Received message: key={key}, value={value}")
                # Add your message processing logic here (e.g., save to database, analyze data)
        except Exception as e:
                print(f"Error processing message: {e}")

def consume_messages(consumer: Consumer):
        """
        Continuously consume messages from the Kafka topic.
        """
        try:
                while True:
                        msg = consumer.poll(1.0)  # Poll for messages every second
                        if msg is None:
                                continue
                        if msg.error():
                                if msg.error().code() == KafkaError._PARTITION_EOF:
                                        print(f"Reached end of partition: {msg.partition()}")
                                else:
                                        print(f"Consumer error: {msg.error()}")
                        else:
                                process_message(msg)
        except KeyboardInterrupt:
                print("Consumer interrupted, shutting down...")
        except Exception as e:
                print(f"Error in consumer loop: {e}")
        finally:
                consumer.close()
                print("Consumer closed.")

if __name__ == '__main__':
        consumer = create_consumer(host='localhost', port=9092)
        if consumer:
                consume_messages(consumer)