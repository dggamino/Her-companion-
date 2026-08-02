# HER-RFC-002 — Framework de API para HEREDITARIA OS

## Version
1.0.0

## Estado
Aprobado

## Contexto
ISSUE-006 evaluo frameworks de API. Decision aplazada hasta tener her-core.

## Propuesta
Adoptar FastAPI como framework de API.

## Justificacion

| Criterio | FastAPI | Flask | Django |
|----------|---------|-------|--------|
| Async nativo | Si | Extensiones | Channels |
| Pydantic v2 | Integrado | Manual | DRF |
| OpenAPI auto | Si | Manual | DRF-yasg |
| Memoria base | ~40MB | ~30MB | ~80MB |
| WAHA webhooks | Async handlers | Sync default | Overkill |

## Decisiones derivadas
- Pydantic v2: reutiliza modelos her_models
- Uvicorn: ASGI server con --workers 1 en Termux
- Endpoints: /api/v1/expedientes, /api/v1/webhooks/waha, /health

## Riesgos y mitigaciones
- Memoria Termux < 100MB: monitorear con ps; fallback a Flask documentado
- Startup lento: lazy loading de modulos

## Implementacion
Archivo: packages/her_api/main.py
FastAPI app con health check y routers CRUD

## Referencias
- ISSUE-006
- HER-RFC-001
- HER-ADR-0001
