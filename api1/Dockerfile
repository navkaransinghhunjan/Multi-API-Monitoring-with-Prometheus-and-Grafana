FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
RUN pip install prometheus_flask_exporter
CMD ["python", "app.py"]
