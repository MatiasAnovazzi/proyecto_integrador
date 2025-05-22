from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from database import SessionLocal

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clientes", response_model=schemas.UsuarioOut)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    nuevo = models.Usuario(
        nombre_completo=cliente.nombre_completo,
        dni=cliente.dni,
        edad=cliente.edad,
        telefono=cliente.telefono,
        tipo_usuario=models.TipoUsuarioEnum.cliente
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.post("/profesionales", response_model=schemas.UsuarioOut)
def crear_profesional(pro: schemas.ProfesionalCreate, db: Session = Depends(get_db)):
    nuevo = models.Usuario(
        nombre_completo=pro.nombre_completo,
        telefono=pro.telefono,
        tipo_usuario=models.TipoUsuarioEnum.profesional,
        especialidad=pro.especialidad
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
