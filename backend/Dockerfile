FROM python:3.11-slim-bullseye AS builder
RUN apt update && \
    apt install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.11-slim-bullseye AS runner
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update && \
    apt install -y libpq5 && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
