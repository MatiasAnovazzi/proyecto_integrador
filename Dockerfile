FROM python:3.11-slim

WORKDIR /app

# Copiá los archivos necesarios
COPY app/ ./app/
COPY ejercicio.js .
COPY estadistica.txt .
COPY wait-for-mysql.sh .

# Instalá dependencias (ajustá según tu entorno)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Si necesitás JS, también podés instalar node/npm

CMD ["bash", "wait-for-mysql.sh", "&&", "python", "app/main.py"]
