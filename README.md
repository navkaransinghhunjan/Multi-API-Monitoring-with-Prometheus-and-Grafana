# Multi-API Monitoring with Prometheus and Grafana
This project demonstrates a setup for monitoring multiple APIs using Prometheus and Grafana. It includes simple Flask-based APIs to expose metrics and Docker Compose for easy orchestration. This configuration allows you to monitor API availability and response times with customizable alerts sent via email.

Project Structure
```
    .
    ├── api1/
    │   ├── Dockerfile             # Dockerfile for the first API
    │   └── app.py                 # Sample Flask app for API 1
    ├── api2/
    │   ├── Dockerfile             # Dockerfile for the second API
    │   └── app.py                 # Sample Flask app for API 2
    ├── prometheus.yml             # Prometheus configuration file with API targets
    ├── docker-compose.yml         # Docker Compose configuration to launch services
    └── grafana/
        └── provisioning/
            ├── dashboards/
            │   └── dashboard.json # Grafana dashboard configuration for API monitoring
            └── datasources/
                └── prometheus.yml # Grafana datasource configuration for Prometheus
```
Key Components
api1 and api2: Simple APIs for example purpose that expose health and metrics endpoints for monitoring.
Prometheus: Configured to scrape metrics from the APIs and send alert notifications.
Grafana: Provides a dashboard for visualizing API availability and response time metrics.
Prerequisites
Docker
Docker Compose

# Getting Started
## 1. Clone the repository:

```bash

git clone https://github.com/yourusername/multi-api-monitoring.git
cd multi-api-monitoring
```
## 2. Set up Gmail SMTP for Grafana Alerts:

 * Edit docker-compose.yml and replace the following environment variables in the Grafana service with your Gmail credentials:

```
- GF_SMTP_USER=your_email@gmail.com        # Your Gmail address
- GF_SMTP_PASSWORD=your_app_password       # App-specific password
- GF_SMTP_FROM=your_email@gmail.com        # Sender email address
- GF_SMTP_TO=recipient_email@gmail.com      # Recipient email address
```
## 3. Build and Start Services:

Use Docker Compose to build and start the services:

```
docker-compose up --build
```
## 4. Access Services:

 * API1: http://localhost:5000/status
 * API2: http://localhost:5001/status
 * Prometheus: http://localhost:9090
 * Grafana: http://localhost:3000 (Login with admin/admin, or change the password in docker-compose.yml)
   
## 5. Load the Dashboard in Grafana:

* Grafana should automatically load the dashboard from
  ```
   grafana/provisioning/dashboards/dashboard.json.
  ```
* Navigate to the dashboard to view real-time metrics for each API.
# API Endpoints
* GET /status: Returns a JSON object indicating the API status and timestamp.
* GET /metrics: Exposes Prometheus-compatible metrics.
  
# Alerts Setup
Prometheus sends alerts when an API is down based on the up{job="api_monitoring"} metric. Grafana uses SMTP settings to send alert emails.

* Alert Query:
  up{job="api_monitoring"}
* Condition:
  Alert triggers when any API’s up value is below 1.
* Evaluation Behavior:
  Set the evaluation interval and alert state durations as required in Grafana's alert configuration.

# Sample Grafana Dashboard
The dashboard provides:

* API Availability: Displays up/down status of each API.
* API Response Time: Shows average response times per API.
  
For more details, check grafana/provisioning/dashboards/dashboard.json.

