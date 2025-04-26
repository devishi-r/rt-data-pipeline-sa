FROM python:3.8-slim

COPY requirements.txt .

RUN set -ex; \
  	pip install --no-cache-dir -r requirements.txt

# Copy resources
WORKDIR /
COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh

COPY python-producer.py .

ENV ZOOKEEPER_SERVER="zookeeper:32181"
ENV KAFKA_SERVER="kafka:9092"

# CMD ["bash", "-c", "./wait-for-it.sh", "-s", "-t", "30", "$ZOOKEEPER_SERVER", "--", "./wait-for-it.sh", "-s", "-t", "30", "$KAFKA_SERVER", "--", "python", "-u", "python-producer.py"]
CMD ["bash", "-c", "./wait-for-it.sh $ZOOKEEPER_SERVER:32181 -s -t 30 -- ./wait-for-it.sh $KAFKA_SERVER:9092 -s -t 30 -- python -u python-producer.py"]
