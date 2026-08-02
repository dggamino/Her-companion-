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


class ExpedienteUpdate(BaseModel):
    """Schema para actualizar un expediente."""

    direccion: str | None = None
    observaciones: str | None = None
    estado: str | None = None
    agente_id: str | None = None


class ExpedienteResponse(ExpedienteBase):
    """Schema para respuestas de expediente."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime
    estado: str
    agente_id: str | None = None


class AgenteBase(BaseModel):
    """Schema base para Agente."""

    nombre: str
    telefono: str | None = None
    email: str | None = None


class AgenteCreate(AgenteBase):
    """Schema para crear un nuevo agente."""

    id: str


class AgenteResponse(AgenteBase):
    """Schema para respuestas de agente."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime


class HealthResponse(BaseModel):
    """Schema para health check."""

    status: str
    version: str
