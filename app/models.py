from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import enum
import datetime

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

    turnos_cliente = relationship("Turno", foreign_keys="[Turno.cliente_id]", back_populates="cliente")
    turnos_profesional = relationship("Turno", foreign_keys="[Turno.profesional_id]", back_populates="profesional")

class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("usuarios.id"))
    profesional_id = Column(Integer, ForeignKey("usuarios.id"))
    horario = Column(DateTime, nullable=False)

    cliente = relationship("Usuario", foreign_keys=[cliente_id], back_populates="turnos_cliente")
    profesional = relationship("Usuario", foreign_keys=[profesional_id], back_populates="turnos_profesional")