# PROJECT_STATE

Última actualización: 2026-08-01
Sprint activo: SPRINT 010
Estado general: Execution Mode

## Fase
- Architecture & Governance: ✅ Cerrada
- Execution: 🔄 En curso

## Sprint 006 — CI GitHub Actions

### Objetivo
Establecer validación continua.

### Alcance
- [x] ISSUE-012: Pipeline CI
- [x] ISSUE-014: HER-STD-0006 Definition of Done

### Criterios de éxito
- [x] CI verde

## Sprint 007 — Activación de Python

### Objetivo
Bootstrap primer código Python.

### Alcance
- [x] ISSUE-013: Activar python-placeholder con tests reales

### Criterios de éxito
- [x] CI verde con job python
- [x] Tests pasan localmente

## Sprint 008 — Arquitectura de Persistencia y API

### Objetivo
Materializar decisiones arquitectónicas pendientes.

### Alcance
- [x] ISSUE-005: ADR DB — SQLite + SQLAlchemy 2.0
- [x] ISSUE-006: RFC API — FastAPI

### Criterios de éxito
- [x] CI verde con nuevos documentos

## Sprint 009 — Capa de Persistencia

### Objetivo
Implementar persistencia real con SQLAlchemy 2.0 async.

### Alcance
- [x] ISSUE-016: SQLAlchemy 2.0 + Alembic + tests ORM

### Criterios de éxito
- [x] CI verde con tests ORM
- [x] Tests pasan localmente

## Sprint 010 — API FastAPI

### Objetivo
Implementar API REST con endpoints CRUD.

### Alcance
- [x] ISSUE-017: FastAPI + endpoints CRUD Expediente + tests integración

### Artefactos
- `packages/her_api/`
- `tests/test_her_api.py`
- `GET /health`, `POST /api/v1/expedientes`, `GET /api/v1/expedientes/{id}`, `GET /api/v1/expedientes`

### Criterios de éxito
- [ ] CI verde con tests de API
- [ ] Tests pasan localmente

## Documentos vigentes (17)

| Documento | Estado | Versión |
|---|---|---|
| HER-001 — Manifiesto | Aprobado | v1.0.0 |
| HER-ADR-0000 — Repository as Product | Aprobado | v1.1 |
| HER-ADR-0001 — Estrategia de Persistencia | Aprobado | v1.0.0 |
| HER-RFC-001 — WhatsApp First Architecture | Aprobado | v1.0.0 |
| HER-RFC-002 — Framework de API | Aprobado | v1.0.0 |
| HER-STD-0001 — Repository Contract | Aprobado | v1.0 |
| HER-STD-0002 — Sprint Freeze Rule | Aprobado | v1.0 |
| HER-STD-0003 — Convenciones Git | Aprobado | v1.0.0 |
| HER-STD-0004 — Context Snapshot Standard | Aprobado | v1.0.0 |
| HER-STD-0005 — Definition of Ready | Aprobado | v1.0.0 |
| HER-STD-0006 — Definition of Done | Aprobado | v1.0.0 |
| HER-000 — Constitución | Aprobado | v1.0.1 |
| AR-2026-07-31-001 | Aprobada | — |

## Issues abiertos

- ISSUE-015: Desalineación DRY CI/local (Sprint 011+)

## Próximo sprint

SPRINT 011 — Integración con WhatsApp (WAHA).
Recomendado: Webhook receptor para mensajes entrantes, mapeo a expedientes.
