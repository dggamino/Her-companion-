"""Servicio de procesamiento de mensajes WhatsApp (WAHA)."""

from datetime import UTC, datetime

from sqlalchemy.ext.asyncio import AsyncSession

from her_core.models import Expediente


async def procesar_mensaje_entrante(
    db: AsyncSession,
    telefono: str,
    mensaje: str,
) -> Expediente:
    """Procesa un mensaje entrante de WhatsApp.

    Si existe un expediente para el teléfono, añade el mensaje
    como observación. Si no existe, crea uno nuevo.
    """
    expediente_id = f"WA-{telefono}"
    exp = await db.get(Expediente, expediente_id)

    if exp is None:
        # Crear nuevo expediente
        exp = Expediente(
            id=expediente_id,
            direccion=f"Contacto WhatsApp: {telefono}",
            observaciones=mensaje,
            created_at=datetime.now(UTC),
        )
        db.add(exp)
    else:
        # Actualizar observaciones
        exp.observaciones = (
            f"{exp.observaciones or ''}\n[{datetime.now(UTC).isoformat()}] {mensaje}"
        ).strip()

    await db.commit()
    await db.refresh(exp)
    return exp
