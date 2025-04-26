FROM python:3.8-slim

COPY requirements.txt .

# Install dependencies
RUN set -ex; \
    apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy resources
WORKDIR /
COPY wait-for-it.sh wait-for-it.sh

ADD python-consumer.py .

ENV ZOOKEEPER_SERVER="zookeeper:32181"
ENV KAFKA_SERVER="kafka:9092"

# CMD ["bash", "-c", "./wait-for-it.sh", "-s", "-t", "30", "$ZOOKEEPER_SERVER", "--", "./wait-for-it.sh", "-s", "-t", "30", "$KAFKA_SERVER", "--", "python", "-u", "python-consumer.py"]
CMD ["bash", "-c", "./wait-for-it.sh $ZOOKEEPER_SERVER:32181 -s -t 30 -- ./wait-for-it.sh $KAFKA_SERVER:9092 -s -t 30 -- python -u python-consumer.py"]

# wait for zookeeper server(manages kafka brokers) and kafka server to start for 30 seconds each