# Issues Sprint 008

## ISSUE-005 — RESUELTO

Tipo: ADR
Descripcion: Decision arquitectonica — migracion de base de datos.
Resolucion:
- Materializado HER-ADR-0001.md
- Decision: SQLite + SQLAlchemy 2.0 async para MVP
- WAL mode para concurrencia de lectura
- Alembic para migraciones
- Triggers de reevaluacion documentados

## ISSUE-006 — RESUELTO

Tipo: RFC
Descripcion: Decision tecnica — framework de API.
Resolucion:
- Materializado HER-RFC-002.md
- Decision: FastAPI
- Justificacion: async nativo, Pydantic v2, OpenAPI auto, compatible WAHA
- Riesgo memoria Termux mitigado

## ISSUE-015 — ABIERTO

Tipo: INF
Descripcion: Desalineacion DRY entre CI y validador local.
Prioridad: Baja
Resolver en: Sprint 009+
