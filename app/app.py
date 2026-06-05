from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import time
import random

app = Flask(__name__)

REQUEST_COUNT = Counter('app_request_count', 'Total request count', ['endpoint'])
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Request latency', ['endpoint'])

@app.route('/')
def home():
    REQUEST_COUNT.labels(endpoint='/').inc()
    with REQUEST_LATENCY.labels(endpoint='/').time():
        time.sleep(random.uniform(0.1, 0.5))
    return 'App is running!'

@app.route('/metrics')
def metrics():
    from flask import Response
    return Response(generate_latest(), mimetype='text/plain; version=0.0.4')

@app.route('/error')
def error():
    REQUEST_COUNT.labels(endpoint='/error').inc()
    return 'Simulated error!', 500

@app.route('/home')
def homepage():
    REQUEST_COUNT.labels(endpoint='/home').inc()
    with REQUEST_LATENCY.labels(endpoint='/home').time():
        time.sleep(random.uniform(0.1, 0.5))
    return 'This is the home page'

@app.errorhandler(404)
def not_found(e):
    REQUEST_COUNT.labels(endpoint='404').inc()
    return 'Page not found!', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)