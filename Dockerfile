FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY .env .env

RUN uv pip install -r requirements.txt

COPY . .

CMD ["python", "app/main.py"]
