"""Router CRUD para agentes."""

from collections.abc import AsyncGenerator
from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from her_api.schemas import AgenteCreate, AgenteResponse
from her_core.database import async_session
from her_core.models import Agente

router = APIRouter(prefix="/api/v1/agentes", tags=["agentes"])


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency para obtener sesión de base de datos."""
    async with async_session() as session:
        yield session


@router.post("", response_model=AgenteResponse, status_code=201)
async def crear_agente(
    data: AgenteCreate,
    db: AsyncSession = Depends(get_db),
) -> Agente:
    """Crea un nuevo agente."""
    result = await db.get(Agente, data.id)
    if result is not None:
        raise HTTPException(status_code=409, detail="Agente ya existe")

    agente = Agente(
        id=data.id,
        nombre=data.nombre,
        telefono=data.telefono,
        email=data.email,
        created_at=datetime.now(UTC),
    )
    db.add(agente)
    await db.commit()
    await db.refresh(agente)
    return agente


@router.get("/{agente_id}", response_model=AgenteResponse)
async def obtener_agente(
    agente_id: str,
    db: AsyncSession = Depends(get_db),
) -> Agente:
    """Obtiene un agente por ID."""
    result = await db.get(Agente, agente_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Agente no encontrado")
    return result


@router.get("", response_model=list[AgenteResponse])
async def listar_agentes(
    db: AsyncSession = Depends(get_db),
) -> list[Agente]:
    """Lista todos los agentes."""
    result = await db.execute(select(Agente))
    return list(result.scalars().all())
