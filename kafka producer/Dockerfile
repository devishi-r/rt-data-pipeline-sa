from python:3.8-slim

COPY requirements.txt .

RUN set -ex; \
    pip install --no-cache-dir -r requirements.txt

# copy resources
WORKDIR /
COPY wait-for-it.sh wait-for-it.sh

ADD python-producer.py .

CMD ./wait-for-it.sh -s -t 30 $ZOOKEEPER_SERVER -- ./wait-for-it.sh  -s - t 30 $KAFKA_SERVER -- python python-producer.py
# wait for zookeeper server(manages kafka brokers) and kafka server to start for 30 seconds each