from fastapi import FastAPI
from routers import usuarios, turnos
from database import Base, engine

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(turnos.router)
