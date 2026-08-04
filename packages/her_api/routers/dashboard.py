"""Router de dashboard y reporting."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from her_api.dependencies import get_db
from her_api.services.reporting import (
    conteo_por_agente,
    conteo_por_estado,
    metricas_dashboard,
)

router = APIRouter(prefix="/api/v1/dashboard", tags=["dashboard"])


@router.get("/estados")
async def dashboard_estados(db: AsyncSession = Depends(get_db)):
    """Conteo de expedientes por estado."""
    return await conteo_por_estado(db)


@router.get("/agentes")
async def dashboard_agentes(db: AsyncSession = Depends(get_db)):
    """Conteo de expedientes por agente asignado."""
    return await conteo_por_agente(db)


@router.get("/metricas")
async def dashboard_metricas(db: AsyncSession = Depends(get_db)):
    """Métricas clave del dashboard."""
    return await metricas_dashboard(db)
