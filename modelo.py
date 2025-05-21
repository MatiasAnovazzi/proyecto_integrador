from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID

app = FastAPI()

# Modelos
class Turno(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nombrecompleto: str
    fecha_hora: datetime

class TurnoCreate(BaseModel):
    nombrecompleto: str
    fecha_hora: datetime

class TurnoUpdate(BaseModel):
    nombrecompleto: Optional[str] = None
    fecha_hora: Optional[datetime] = None

# Base de datos en memoria
turnos_db: List[Turno] = []

# Crear turno
@app.post("/turnos/", response_model=Turno)
def crear_turno(turno: TurnoCreate):
    if turno.fecha_hora < datetime.now():
        raise HTTPException(status_code=400, detail="La fecha y hora deben ser futuras")
    nuevo_turno = Turno(**turno.dict())
    turnos_db.append(nuevo_turno)
    return nuevo_turno

# Listar todos los turnos
@app.get("/turnos/", response_model=List[Turno])
def listar_turnos():
    return turnos_db

# Obtener turno por ID
@app.get("/turnos/{turno_id}", response_model=Turno)
def obtener_turno(turno_id: UUID):
    for turno in turnos_db:
        if turno.id == turno_id:
            return turno
    raise HTTPException(status_code=404, detail="Turno no encontrado")

# Actualización completa (PUT)
@app.put("/turnos/{turno_id}", response_model=Turno)
def actualizar_turno(turno_id: UUID, turno_actualizado: TurnoCreate):
    for idx, turno in enumerate(turnos_db):
        if turno.id == turno_id:
            actualizado = Turno(id=turno_id, **turno_actualizado.dict())
            turnos_db[idx] = actualizado
            return actualizado
    raise HTTPException(status_code=404, detail="Turno no encontrado")

# Eliminar turno
@app.delete("/turnos/{turno_id}")
def eliminar_turno(turno_id: UUID):
    for idx, turno in enumerate(turnos_db):
        if turno.id == turno_id:
            del turnos_db[idx]
            return {"detail": "Turno eliminado"}
    raise HTTPException(status_code=404, detail="Turno no encontrado")
