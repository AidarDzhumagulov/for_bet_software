FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

# Устанавливаем необходимые пакеты и зависимости, включая PostgreSQL
RUN apk update && \
    apk add --no-cache postgresql-dev gcc musl-dev libffi-dev openssl-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

COPY .. /app
# Копируем остальные файлы

EXPOSE 80

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
