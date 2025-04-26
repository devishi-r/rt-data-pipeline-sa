import time
import schedule
from json import dumps # serialises Python dictionaries into JSON format

from faker import Faker #helps generate random strings
from kafka import KafkaProducer

kafka_nodes = "kafka:9092"
myTopic = "sentence"

def gen_data():
    fake = Faker()
    producer = KafkaProducer(bootstrap_servers=kafka_nodes, value_serializer=lambda v: dumps(v).encode('utf-8'))
    my_data = {"sentence": fake.sentence()}
    print(my_data)
    producer.send(topic = myTopic, value = my_data)
    producer.flush()

if __name__ == "__main__":
    schedule.every(5).seconds.do(gen_data)

    while(True):
        schedule.run_pending()
        time.sleep(0.5)