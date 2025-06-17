from pydantic import BaseModel
from enum import Enum
from typing import Optional
import datetime

class TipoUsuarioEnum(str, Enum):
    cliente = "cliente"
    profesional = "profesional"

class UsuarioBase(BaseModel):
    nombre_completo: str
    telefono: Optional[str]

class ClienteCreate(UsuarioBase):
    dni: str
    edad: int

class ProfesionalCreate(UsuarioBase):
    especialidad: str

class UsuarioOut(UsuarioBase):
    id: int
    tipo_usuario: TipoUsuarioEnum
    dni: Optional[str]
    edad: Optional[int]
    especialidad: Optional[str]

    class Config:
        orm_mode = True

class TurnoBase(BaseModel):
    cliente_id: int
    profesional_id: int
    horario: datetime.datetime

class TurnoCreate(TurnoBase):
    pass

class TurnoOut(TurnoBase):
    id: int

    class Config:
        orm_mode = True
