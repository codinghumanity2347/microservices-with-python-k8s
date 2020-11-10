FROM python:3.7-slim

WORKDIR .
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .
CMD ["python", "kafka_consumer.py"]