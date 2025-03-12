from kafka import KafkaConsumer
import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import psycopg2
import nltk

nltk.download('vader_lexicon')
analyzer =  SentimentIntensityAnalyzer()

conn = psycopg2.connect(
    dbname="postgres"   ,
    user="postgres",
    password="passw0rd",
    host="postgres",
    port="5432  "
) #ideally, these values are not hardcoded, but come directly from the environment values

curr = conn.cursor()

# Connect to Kafka
kafka_nodes = "kafka:9092"
my_topic = "sentence"

consumer = KafkaConsumer(my_topic, bootstrap_servers=kafka_nodes, value_deserializer = lambda m: json.loads(m.decode('utf-8')))

# Consuming messages from the topic
