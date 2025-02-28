# app/producer.py

from kafka import KafkaProducer
import json

def get_producer(kafka_server: str = "kafka:9092"):
    """
    Returns a KafkaProducer connected to the specified kafka_server.
    By default: "kafka:9092", which is the correct hostname:port inside Docker.
    """
    return KafkaProducer(
        bootstrap_servers=[kafka_server],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def send_message(topic: str, message: dict, kafka_server: str = "kafka:9092"):
    """
    Send a dictionary message to the given Kafka topic.
    """
    producer = get_producer(kafka_server)
    producer.send(topic, message)
    producer.flush()  # ensure delivery
    return True
