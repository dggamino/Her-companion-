"""Pydantic schemas for API requests/responses."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ExpedienteBase(BaseModel):
    """Schema base para Expediente."""

    direccion: str
    observaciones: str | None = None


class ExpedienteCreate(ExpedienteBase):
    """Schema para crear un nuevo expediente."""

    id: str


class ExpedienteResponse(ExpedienteBase):
    """Schema para respuestas de expediente."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime


class HealthResponse(BaseModel):
    """Schema para health check."""

    status: str
    version: str
