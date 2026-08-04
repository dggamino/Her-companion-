"""Servicios de reporting y agregación para dashboard."""

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from her_core.models import Agente, EstadoExpediente, Expediente


async def conteo_por_estado(db: AsyncSession) -> dict[str, int]:
    """Retorna conteo de expedientes agrupados por estado."""
    result = await db.execute(
        select(Expediente.estado, func.count(Expediente.id))
        .group_by(Expediente.estado)
    )
    return {estado.value: count for estado, count in result.all()}


async def conteo_por_agente(db: AsyncSession) -> dict[str, int]:
    """Retorna conteo de expedientes agrupados por agente asignado."""
    result = await db.execute(
        select(Agente.nombre, func.count(Expediente.id))
        .join(Expediente, Agente.id == Expediente.agente_id)
        .group_by(Agente.nombre)
    )
    return dict(result.all())


async def metricas_dashboard(db: AsyncSession) -> dict:
    """Retorna métricas clave del dashboard."""
    from datetime import datetime, timedelta

    hoy = datetime.now().date()
    inicio_mes = hoy.replace(day=1)

    # Total expedientes
    total_result = await db.execute(select(func.count(Expediente.id)))
    total = total_result.scalar()

    # Creados hoy
    hoy_result = await db.execute(
        select(func.count(Expediente.id)).where(
            func.date(Expediente.creado_en) == hoy
        )
    )
    creados_hoy = hoy_result.scalar()

    # Cerrados este mes
    cerrados_result = await db.execute(
        select(func.count(Expediente.id)).where(
            Expediente.estado == EstadoExpediente.cerrado,
            func.date(Expediente.actualizado_en) >= inicio_mes,
        )
    )
    cerrados_mes = cerrados_result.scalar()

    return {
        "total_expedientes": total,
        "creados_hoy": creados_hoy,
        "cerrados_este_mes": cerrados_mes,
    }
