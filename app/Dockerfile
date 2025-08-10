# app/Dockerfile
FROM python:3.10.12-slim

WORKDIR /app # El directorio de trabajo dentro del contenedor es /app


COPY requirements.txt .
RUN apt-get update && apt-get install -y default-mysql-client

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]