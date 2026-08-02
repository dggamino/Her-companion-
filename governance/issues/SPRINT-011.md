# Issues Sprint 011

## ISSUE-018 — RESUELTO

**Tipo:** INF
**Descripción:** Integrar recepción de mensajes WhatsApp via WAHA webhooks.
**Resolución:**
- Creado `packages/her_api/routers/webhooks.py` — webhook receptor WAHA
- Creado `packages/her_api/services/whatsapp.py` — procesador de mensajes
  - Crea expediente nuevo si no existe (ID: `WA-{telefono}`)
  - Actualiza observaciones si el expediente ya existe
- Creado `tests/test_webhooks.py` — 4 tests de integración
- Actualizado `her_api/main.py` — incluye router de webhooks
- Payload WAHA esperado: `{event, session, payload: {from, body, type}}`

## ISSUE-015 — ABIERTO

**Tipo:** INF
**Descripción:** Desalineación DRY entre CI y validador local.
**Prioridad:** Baja
**Resolver en:** Sprint 012+
