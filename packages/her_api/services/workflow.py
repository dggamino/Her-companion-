"""Servicio de workflow y lógica de negocio para expedientes."""

from sqlalchemy.ext.asyncio import AsyncSession

from her_core.models import EstadoExpediente, Expediente

TRANSICIONES_VALIDAS: dict[str, set[str]] = {
    EstadoExpediente.NUEVO.value: {
        EstadoExpediente.EN_PROCESO.value,
        EstadoExpediente.ARCHIVADO.value,
    },
    EstadoExpediente.EN_PROCESO.value: {
        EstadoExpediente.PENDIENTE.value,
        EstadoExpediente.CERRADO.value,
        EstadoExpediente.ARCHIVADO.value,
    },
    EstadoExpediente.PENDIENTE.value: {
        EstadoExpediente.EN_PROCESO.value,
        EstadoExpediente.CERRADO.value,
        EstadoExpediente.ARCHIVADO.value,
    },
    EstadoExpediente.CERRADO.value: {
        EstadoExpediente.ARCHIVADO.value,
    },
    EstadoExpediente.ARCHIVADO.value: set(),
}


class TransicionInvalidaError(ValueError):
    """Error cuando se intenta una transición de estado inválida."""


async def cambiar_estado(
    db: AsyncSession,
    expediente: Expediente,
    nuevo_estado: str,
) -> Expediente:
    """Cambia el estado de un expediente si la transición es válida."""
    estado_actual = expediente.estado

    if nuevo_estado not in TRANSICIONES_VALIDAS.get(estado_actual, set()):
        raise TransicionInvalidaError(
            f"Transición inválida: {estado_actual} -> {nuevo_estado}"
        )

    expediente.estado = nuevo_estado
    await db.commit()
    await db.refresh(expediente)
    return expediente


async def asignar_agente(
    db: AsyncSession,
    expediente: Expediente,
    agente_id: str,
) -> Expediente:
    """Asigna un agente a un expediente."""
    expediente.agente_id = agente_id
    await db.commit()
    await db.refresh(expediente)
    return expediente
