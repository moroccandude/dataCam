from confluent_kafka import Producer
import sys

def test_kafka_connection(host: str = 'localhost', port: int = 9092):
    """Test connection to Kafka server by listing topics."""
    bootstrap_servers = f"{host}:{port}"
    print(f"Testing connection to {bootstrap_servers}...")

    try:
        producer = Producer({'bootstrap.servers': bootstrap_servers})
        topics = producer.list_topics(timeout=5).topics
        print(f"Connection successful! Available topics: {list(topics.keys())}")
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == '__main__':
    success = test_kafka_connection(host='localhost', port=9092)
    sys.exit(0 if success else 1)