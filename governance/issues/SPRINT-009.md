# Issues Sprint 009

## ISSUE-016 — RESUELTO

**Tipo:** INF
**Descripción:** Implementar capa de persistencia con SQLAlchemy 2.0 async.
**Resolución:**
- Creado `packages/her_core/` con configuración de base de datos
- `her_core/database.py`: engine async, session factory, `init_db()`
- `her_core/models.py`: modelo ORM `Expediente` (SQLAlchemy 2.0 declarative)
- Configurado Alembic en `her_core/alembic/` para migraciones
- Tests ORM en `tests/test_her_core.py` con SQLite en memoria
- Actualizadas dependencias: `sqlalchemy[asyncio]`, `aiosqlite`, `alembic`, `pytest-asyncio`

## ISSUE-015 — ABIERTO

**Tipo:** INF
**Descripción:** Desalineación DRY entre CI y validador local.
**Prioridad:** Baja
**Resolver en:** Sprint 010+
