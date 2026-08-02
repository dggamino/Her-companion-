# Issues Sprint 010

## ISSUE-017 — RESUELTO

**Tipo:** INF
**Descripción:** Implementar API FastAPI con endpoints CRUD para Expediente.
**Resolución:**
- Creado `packages/her_api/` con capa de API
- `her_api/main.py`: FastAPI app con lifespan (init_db en startup)
- `her_api/schemas.py`: Pydantic schemas para validación
- `her_api/routers/expedientes.py`: Endpoints CRUD (POST, GET, GET list)
- `tests/test_her_api.py`: 5 tests de integración con AsyncClient
- Health check: `GET /health`
- Dependency injection para sesiones de DB

## ISSUE-015 — ABIERTO

**Tipo:** INF
**Descripción:** Desalineación DRY entre CI y validador local.
**Prioridad:** Baja
**Resolver en:** Sprint 011+
