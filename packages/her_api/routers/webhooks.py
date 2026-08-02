"""Router para webhooks de integraciones externas (WAHA)."""

from fastapi import APIRouter, HTTPException, Request

from her_api.services.whatsapp import procesar_mensaje_entrante
from her_core.database import async_session

router = APIRouter(prefix="/api/v1/webhooks", tags=["webhooks"])


@router.post("/waha")
async def webhook_waha(request: Request) -> dict[str, str]:
    """Recibe mensajes entrantes de WhatsApp via WAHA.

    Payload esperado (WAHA):
    {
      "event": "message",
      "session": "default",
      "payload": {
        "from": "1234567890@c.us",
        "body": "texto del mensaje",
        "type": "chat"
      }
    }
    """
    try:
        data = await request.json()
        payload = data.get("payload", {})

        # Extraer número de teléfono (formato: 1234567890@c.us)
        from_field = payload.get("from", "")
        telefono = from_field.split("@")[0] if "@" in from_field else from_field

        # Extraer mensaje
        mensaje = payload.get("body", "")

        if not telefono or not mensaje:
            raise HTTPException(status_code=400, detail="Datos incompletos")

        # Procesar mensaje
        async with async_session() as db:
            exp = await procesar_mensaje_entrante(db, telefono, mensaje)

        return {
            "status": "ok",
            "expediente_id": exp.id,
            "accion": "creado" if exp.created_at == exp.created_at else "actualizado",
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
