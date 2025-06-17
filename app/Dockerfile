# app/Dockerfile
FROM python:3.10.12-slim

WORKDIR /app # El directorio de trabajo dentro del contenedor es /app

# Copia solo los requirements primero para aprovechar el cache de Docker
COPY requirements.txt .
RUN apt-get update && apt-get install -y default-mysql-client

RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la carpeta 'app' del host (que ahora es el build context)
# al WORKDIR /app dentro del contenedor.
COPY . . 
RUN chmod +x ./wait-for-mysql.sh
# Comando para ejecutar la aplicación. Como main.py está directamente en /app,
# el comando es 'main:app'.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]