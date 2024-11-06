from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Exposes /metrics endpoint automatically

@app.route("/")
def home():
    return "Welcome to API 1"

@app.route("/status")
def status():
    return jsonify(status="up", timestamp=time.time())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
