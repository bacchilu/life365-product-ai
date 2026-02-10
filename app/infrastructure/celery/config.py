import os

RABBITMQ_HOST: str = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_URL: str = f"amqp://guest:guest@{RABBITMQ_HOST}:5672//"
