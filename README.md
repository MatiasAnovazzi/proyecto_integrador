# Proyecto Integrador

Este repositorio contiene el desarrollo de un proyecto integrador que busca consolidar conocimientos en diversas áreas del desarrollo de software, incluyendo Python, JavaScript, Docker y Shell scripting.

## Estructura del Proyecto

- **app/**: Carpeta principal que contiene el código fuente de la aplicación.
- **docker-compose.yml**: Archivo de configuración para Docker Compose, facilitando la orquestación de contenedores necesarios para la aplicación.
- **ejercicio.js**: Archivo JavaScript que posiblemente contiene scripts o ejercicios relacionados con el proyecto.
- **estadistica.txt**: Archivo de texto que puede contener datos estadísticos o información relevante para el análisis del proyecto.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para el desarrollo del backend de la aplicación.
- **JavaScript**: Utilizado para funcionalidades del frontend o scripts adicionales.
- **Docker**: Herramienta de contenedorización para facilitar el despliegue y la gestión de entornos.
- **Shell Script**: Para automatización de tareas y configuración del entorno.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes componentes en tu sistema:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

## Instrucciones de Uso

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/MatiasAnovazzi/proyecto_integrador.git
   cd proyecto_integrador

2. **Construir y levantar los contenedores:**

   ```bash
   docker-compose up --build

Este comando descargará las imágenes necesarias y levantará los servicios definidos en `docker-compose.yml`.

3. **Acceder a la aplicación:**

   Una vez que los contenedores estén en funcionamiento, puedes acceder a la aplicación a través del navegador en la dirección especificada (por ejemplo, `http://localhost:8000`), dependiendo de la configuración establecida en el archivo `docker-compose.yml`.
