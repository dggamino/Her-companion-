# PROJECT_STATE

Ultima actualizacion: 2026-08-01
Sprint activo: SPRINT 008
Estado general: Execution Mode

## Fase
- Architecture & Governance: ✅ Cerrada
- Execution: 🔄 En curso

## Sprint 006 — CI GitHub Actions

### Objetivo
Establecer validacion continua.

### Alcance
- [x] ISSUE-012: Pipeline CI
- [x] ISSUE-014: HER-STD-0006 Definition of Done

### Criterios de exito
- [x] CI verde

## Sprint 007 — Activacion de Python

### Objetivo
Bootstrap primer codigo Python.

### Alcance
- [x] ISSUE-013: Activar python-placeholder con tests reales

### Criterios de exito
- [x] CI verde con job python
- [x] Tests pasan localmente

## Sprint 008 — Arquitectura de Persistencia y API

### Objetivo
Materializar decisiones arquitectonicas pendientes.

### Alcance
- [x] ISSUE-005: ADR DB — SQLite + SQLAlchemy 2.0
- [x] ISSUE-006: RFC API — FastAPI
- [ ] ISSUE-015: Desalineacion DRY CI/local

### Artefactos
- governance/adr/HER-ADR-0001.md
- governance/rfc/HER-RFC-002.md
- governance/issues/SPRINT-008.md

### Criterios de exito
- [ ] CI verde con nuevos documentos en validacion
- [ ] Commit y push a main

## Documentos vigentes (17)

| Documento | Estado | Version |
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
| HER-000 — Constitucion | Aprobado | v1.0.1 |
| AR-2026-07-31-001 | Aprobada | — |

## Issues abiertos

- ISSUE-015: Desalineacion DRY CI/local (Sprint 009+)

## Proximo sprint

SPRINT 009 — Implementacion de capa de persistencia.
Recomendado: SQLAlchemy 2.0 + Alembic, modelo Expediente como SQLAlchemy model.
Prerrequisitos cumplidos: ADR-0001 (DB), RFC-002 (API), STD-0005/0006 (Ready/Done).
