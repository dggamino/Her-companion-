"""ORM models for HEREDITARIA™ OS."""

from datetime import datetime
from sqlalchemy import DateTime, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from her_core.database import Base


class Expediente(Base):
    """Modelo ORM para expedientes inmobiliarios."""

    __tablename__ = "expedientes"

    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    direccion: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    observaciones: Mapped[str | None] = mapped_column(Text, nullable=True)

    def resumen(self) -> str:
        """Devuelve un resumen legible del expediente."""
        obs = f" | Obs: {self.observaciones}" if self.observaciones else ""
        return f"[{self.id}] {self.direccion}{obs}"
