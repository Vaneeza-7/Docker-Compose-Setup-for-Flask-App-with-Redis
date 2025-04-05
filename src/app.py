from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Initialize visit counter
def initialize_counter():
    if not redis_client.exists("visits"):
        redis_client.set("visits", 0)

initialize_counter()

@app.route("/")
def home():
    """Tracks visits and returns a welcome message."""
    redis_client.incr("visits")
    visit_count = redis_client.get("visits")
    return f"Hello! This page has been visited {visit_count} times."

@app.route("/api/data", methods=["GET"])
def get_data():
    """Retrieves data from Redis"""
    data = redis_client.get("sample_data")
    return jsonify({"message": "Stored data", "data": data})

@app.route("/api/data/<value>", methods=["POST"])
def set_data(value):
    """Stores data into Redis"""
    redis_client.set("sample_data", value)
    return jsonify({"message": f"Data '{value}' stored in Redis!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
