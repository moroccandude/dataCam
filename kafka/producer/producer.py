from confluent_kafka import Producer
import json
import os

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def validate_connection(host: str, port: int = 9092):
    """
    Validate the connection to the Kafka server.
    """
    try:
        config = {'bootstrap.servers': f"{host}:{port}",
                  # 'queue.buffering.max.messages': 100000,
                  #  'message.max.bytes': 1000000
                   }

        producer = Producer(config)
        print("Connection to Kafka server is valid.")
        return producer
    except Exception as e:
        print(f"Error connecting to Kafka server: {e}")
        return None

def send_messages(path: str, producer: Producer):
    try:
        with open(path, 'r') as f:
            data = json.load(f)

        topic = "logs"
        for i, ele in enumerate(data[:10]):
            try:
                producer.produce(topic, key=str(i), value=json.dumps(ele), callback=delivery_report)
                producer.poll(0)
                print(f"message {ele}:{i}  ")

            except BufferError:
                print("Local queue is full, flushing...")
                producer.flush()
                producer.produce(topic, key=str(i), value=json.dumps(ele), callback=delivery_report)
        producer.flush()
    except Exception as e:
        print(f"Error sending messages: {e}")

if __name__ == '__main__':
    producer = validate_connection(host='localhost', port=9092)

    if producer:
        parent_path = "./data"
        file_path = os.path.join(parent_path, "data_test.json")
        send_messages(file_path, producer)
