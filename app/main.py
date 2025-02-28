# app/main.py

from flask import Flask, request, jsonify
from kafka_producer import send_message
from kafka_consumer import consume_messages

app = Flask(__name__)

TOPIC_NAME = "test-topic"
KAFKA_SERVER = "kafka:9092"  # Inside Docker

@app.route("/produce", methods=["POST"])
def produce():
    """
    Expects JSON in the request body, for example: { "hello": "world" }
    """
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    send_message(topic=TOPIC_NAME, message=data, kafka_server=KAFKA_SERVER)
    return jsonify({"status": "Message produced", "data": data}), 200


@app.route("/consume/<group_name>", methods=["GET"])
def consume_by_group(group_name):
    """
    Consumes messages from the topic using the specified group_name.
    Example usage:
      GET /consume/my_group_1
      GET /consume/my_group_2
      GET /consume/my_group_3
    """
    messages = consume_messages(
        topic=TOPIC_NAME,
        group_id=group_name,
        kafka_server=KAFKA_SERVER
    )
    return jsonify({"messages": messages}), 200


if __name__ == "__main__":
    # Run Flask on 0.0.0.0:7500 inside the container
    app.run(host="0.0.0.0", port=7500, debug=True)
