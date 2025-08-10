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

    turnos_cliente = relationship("Turno", foreign_keys="[Turno.id_cliente]", back_populates="cliente")
    turnos_profesional = relationship("Turno", foreign_keys="[Turno.id_profesional]", back_populates="profesional")


class Turno(Base):
    __tablename__ = "turnos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)  # <- acá poner tamaño
    hora_inicio = Column(DateTime, nullable=False)
    hora_fin = Column(DateTime, nullable=False)
    id_profesional = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descripcion = Column(String(255))  # o Text
    id_cliente = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    profesional = relationship("Usuario", foreign_keys=[id_profesional], back_populates="turnos_profesional")
    cliente = relationship("Usuario", foreign_keys=[id_cliente], back_populates="turnos_cliente")
