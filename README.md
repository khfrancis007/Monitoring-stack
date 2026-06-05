# Flask App Monitoring Stack

A local observability stack built from scratch using Docker, Flask, Prometheus, and Grafana.

## Overview

This project simulates a production monitoring environment — the open source equivalent of enterprise APM tools like Dynatrace. It demonstrates end-to-end observability: metric collection, real-time visualization, incident simulation, and alerting.

## Stack

- **Locust** - Simulate User traffic and stress testing
- **Flask** - Python web application (the monitored service)
- **Prometheus** - Metrics collection and storage (scrape interval: 3s)
- **Grafana** - Real-time dashboards and alerting
- **Docker** - Containerized deployment via Docker Compose

## Features

- Real-time request count and error rate dashboards
- Simulated production incident (500 error spike)
- Alert rule configured to fire when error count exceeds threshold
- Persistent Grafana dashboards across container restarts

## How to Run

1. Install Docker Desktop
2. Clone this repo
3. Run `docker-compose up --build`
4. Open Grafana at `http://localhost:3000` (admin/admin)
5. Open the Flask app at `http://localhost:5001`

## Simulate an Incident

Hit the error endpoint to trigger the alert:

http://localhost:5001/error

Watch the error rate spike on the Grafana dashboard in real time.

## Author

Khalid Francis — Application Support Engineer  
[LinkedIn](https://linkedin.com/in/khfrancis)
