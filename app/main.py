from fastapi import FastAPI
from routers import usuarios
from database import Base, engine

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuarios.router)
