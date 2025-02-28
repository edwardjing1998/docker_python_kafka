# app/consumer.py

from kafka import KafkaConsumer
import json
import time

def consume_messages(topic: str, group_id: str = "my_group", kafka_server: str = "kafka:9092"):
    """
    Create a KafkaConsumer to consume messages from a topic.
    Return a list of messages (as dictionaries).
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[kafka_server],
        # Change #1: read from earliest offset if no commit exists
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=group_id,
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    messages = []

    # Change #2: poll in a loop for ~5 seconds,
    # so there's enough time to capture messages.
    start_time = time.time()
    while time.time() - start_time < 5:
        raw_msgs = consumer.poll(timeout_ms=1000)
        for tp, msgs in raw_msgs.items():
            for msg in msgs:
                messages.append(msg.value)

    consumer.close()
    return messages
