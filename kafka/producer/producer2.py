from confluent_kafka import Producer
import json
import time
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

if __name__=="__main__":
    with open("./data/DataCoSupplyChainDataset.json", 'r') as f:
        data = json.load(f)
        conf={
            'bootstrap.servers': 'localhost:9092',

        }
        Producer=Producer(conf)
        for i in data[:10]:
            try:
                time.sleep(4)
                Producer.produce('logs', key=str(i), value=json.dumps(i), callback=delivery_report)
                Producer.poll(0)
                print(f"message {i}  ")
            except BufferError:
                print("Local queue is full, flushing...")
                Producer.flush()
                Producer.produce('logs', key=str(i), value=json.dumps(i), callback=delivery_report)
        Producer.produce('logs', key='key', value='value', callback=delivery_report)
# Producer.produce('logs', key='key', value='value')