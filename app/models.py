from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

class TipoUsuarioEnum(enum.Enum):
    cliente = "cliente"
    profesional = "profesional"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String(100), nullable=False)
    dni = Column(String(20), nullable=True)
    edad = Column(Integer, nullable=True)
    telefono = Column(String(20), nullable=True)
    tipo_usuario = Column(Enum(TipoUsuarioEnum), nullable=False)
    especialidad = Column(String(100), nullable=True)  # solo profesionales
