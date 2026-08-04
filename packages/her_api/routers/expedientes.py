"""Router CRUD para expedientes."""

from collections.abc import AsyncGenerator
from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from her_api.schemas import ExpedienteCreate, ExpedienteResponse, ExpedienteUpdate
from her_api.services.workflow import TransicionInvalidaError, asignar_agente, cambiar_estado
from her_core.database import async_session
from her_core.models import Expediente

from typing import Optional
from fastapi import Query
from sqlalchemy import select, and_

@router.get("/api/v1/expedientes")
async def listar_expedientes(
    estado: Optional[str] = Query(None, description="Filtrar por estado"),
    agente_id: Optional[str] = Query(None, description="Filtrar por agente"),
    direccion_contiene: Optional[str] = Query(None, description="Buscar en dirección"),
    desde: Optional[str] = Query(None, description="Fecha inicio YYYY-MM-DD"),
    hasta: Optional[str] = Query(None, description="Fecha fin YYYY-MM-DD"),
    db: AsyncSession = Depends(get_db),
):
    """Listar expedientes con filtros opcionales."""
    query = select(Expediente)

    if estado:
        query = query.where(Expediente.estado == estado)
    if agente_id:
        query = query.where(Expediente.agente_id == agente_id)
    if direccion_contiene:
        query = query.where(Expediente.direccion.ilike(f"%{direccion_contiene}%"))
    if desde:
        query = query.where(func.date(Expediente.creado_en) >= desde)
    if hasta:
        query = query.where(func.date(Expediente.creado_en) <= hasta)

    result = await db.execute(query)
    return result.scalars().all()

router = APIRouter(prefix="/api/v1/expedientes", tags=["expedientes"])


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency para obtener sesión de base de datos."""
    async with async_session() as session:
        yield session


@router.post("", response_model=ExpedienteResponse, status_code=201)
async def crear_expediente(
    data: ExpedienteCreate,
    db: AsyncSession = Depends(get_db),
) -> Expediente:
    """Crea un nuevo expediente."""
    result = await db.get(Expediente, data.id)
    if result is not None:
        raise HTTPException(status_code=409, detail="Expediente ya existe")

    exp = Expediente(
        id=data.id,
        direccion=data.direccion,
        observaciones=data.observaciones,
        created_at=datetime.now(UTC),
    )
    db.add(exp)
    await db.commit()
    await db.refresh(exp)
    return exp


@router.get("/{expediente_id}", response_model=ExpedienteResponse)
async def obtener_expediente(
    expediente_id: str,
    db: AsyncSession = Depends(get_db),
) -> Expediente:
    """Obtiene un expediente por ID."""
    result = await db.get(Expediente, expediente_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return result


@router.get("", response_model=list[ExpedienteResponse])
async def listar_expedientes(
    db: AsyncSession = Depends(get_db),
) -> list[Expediente]:
    """Lista todos los expedientes."""
    result = await db.execute(select(Expediente))
    return list(result.scalars().all())


@router.put("/{expediente_id}", response_model=ExpedienteResponse)
async def actualizar_expediente(
    expediente_id: str,
    data: ExpedienteUpdate,
    db: AsyncSession = Depends(get_db),
) -> Expediente:
    """Actualiza un expediente (estado, agente, observaciones)."""
    exp = await db.get(Expediente, expediente_id)
    if exp is None:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")

    if data.estado is not None:
        try:
            await cambiar_estado(db, exp, data.estado)
        except TransicionInvalidaError as e:
            raise HTTPException(status_code=400, detail=str(e)) from e

    if data.agente_id is not None:
        await asignar_agente(db, exp, data.agente_id)

    if data.direccion is not None:
        exp.direccion = data.direccion

    if data.observaciones is not None:
        exp.observaciones = data.observaciones

    await db.commit()
    await db.refresh(exp)
    return exp
