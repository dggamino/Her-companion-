"""Core domain models for HEREDITARIA™ OS."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Expediente:
    """Representa un expediente inmobiliario en el sistema."""

    id: str
    direccion: str
    created_at: datetime
    observaciones: Optional[str] = None

    def resumen(self) -> str:
        """Devuelve un resumen legible del expediente."""
        obs = f" | Obs: {self.observaciones}" if self.observaciones else ""
        return f"[{self.id}] {self.direccion}{obs}"


def crear_expediente(
    expediente_id: str,
    direccion: str,
    observaciones: Optional[str] = None,
) -> Expediente:
    """Factory para crear un nuevo expediente."""
    return Expediente(
        id=expediente_id,
        direccion=direccion,
        created_at=datetime.now(),
        observaciones=observaciones,
    )
