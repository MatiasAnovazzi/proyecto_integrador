from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4, UUID
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.types import TypeDecorator
from sqlalchemy import create_engine

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://fastapi_user:clave123@localhost:3306/turnos_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Definir tipo UUID para MySQL (char 36)
class GUID(TypeDecorator):
    impl = CHAR(36)

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if not isinstance(value, UUID):
            return str(UUID(value))
        return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return UUID(value)

# Modelo ORM (tabla turnos)
class Turno(Base):
    __tablename__ = "turnos"

    id = Column(GUID(), primary_key=True, default=uuid4, unique=True, nullable=False)
    nombrecompleto = Column(String(100), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Esquemas Pydantic para validación y respuesta
class TurnoBase(BaseModel):
    nombrecompleto: str
    fecha_hora: datetime

class TurnoCreate(TurnoBase):
    pass

class TurnoUpdate(BaseModel):
    nombrecompleto: Optional[str] = None
    fecha_hora: Optional[datetime] = None

class TurnoSchema(TurnoBase):
    id: UUID

    class Config:
        orm_mode = True

# Crear FastAPI
app = FastAPI()

# Dependencia para obtener sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints usando la base de datos

@app.post("/turnos/", response_model=TurnoSchema)
def crear_turno(turno: TurnoCreate, db: Session = Depends(get_db)):
    if turno.fecha_hora < datetime.now():
        raise HTTPException(status_code=400, detail="La fecha y hora deben ser futuras")
    nuevo_turno = Turno(**turno.dict())
    db.add(nuevo_turno)
    db.commit()
    db.refresh(nuevo_turno)
    return nuevo_turno

@app.get("/turnos/", response_model=List[TurnoSchema])
def listar_turnos(db: Session = Depends(get_db)):
    turnos = db.query(Turno).all()
    return turnos

@app.get("/turnos/{turno_id}", response_model=TurnoSchema)
def obtener_turno(turno_id: UUID, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno

@app.put("/turnos/{turno_id}", response_model=TurnoSchema)
def actualizar_turno(turno_id: UUID, turno_actualizado: TurnoCreate, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    turno.nombrecompleto = turno_actualizado.nombrecompleto
    turno.fecha_hora = turno_actualizado.fecha_hora
    db.commit()
    db.refresh(turno)
    return turno

@app.delete("/turnos/{turno_id}")
def eliminar_turno(turno_id: UUID, db: Session = Depends(get_db)):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    db.delete(turno)
    db.commit()
    return {"detail": "Turno eliminado"}
