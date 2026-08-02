"""ORM models for HEREDITARIA™ OS."""

import enum
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from her_core.database import Base


class EstadoExpediente(str, enum.Enum):
    """Estados posibles de un expediente inmobiliario."""

    NUEVO = "nuevo"
    EN_PROCESO = "en_proceso"
    PENDIENTE = "pendiente"
    CERRADO = "cerrado"
    ARCHIVADO = "archivado"


class Agente(Base):
    """Modelo ORM para agentes inmobiliarios."""

    __tablename__ = "agentes"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    nombre: Mapped[str] = mapped_column(Text)
    telefono: Mapped[str | None] = mapped_column(Text, nullable=True)
    email: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime)

    # Relación
    expedientes: Mapped[list["Expediente"]] = relationship("Expediente", back_populates="agente")


class Expediente(Base):
    """Modelo ORM para expedientes inmobiliarios."""

    __tablename__ = "expedientes"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    direccion: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    observaciones: Mapped[str | None] = mapped_column(Text, nullable=True)
    estado: Mapped[str] = mapped_column(String(20), default=EstadoExpediente.NUEVO.value)
    agente_id: Mapped[str | None] = mapped_column(ForeignKey("agentes.id"), nullable=True)

    # Relación
    agente: Mapped[Agente | None] = relationship("Agente", back_populates="expedientes")

    def resumen(self) -> str:
        """Devuelve un resumen legible del expediente."""
        obs = f" | Obs: {self.observaciones}" if self.observaciones else ""
        agente_str = f" | Agente: {self.agente_id}" if self.agente_id else ""
        return f"[{self.id}] {self.direccion} ({self.estado}){agente_str}{obs}"
