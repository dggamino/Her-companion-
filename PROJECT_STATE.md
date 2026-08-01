# PROJECT_STATE

Última actualización: 2026-08-01
Sprint activo: SPRINT 007
Estado general: Execution Mode

## Fase
- Architecture & Governance: ✅ Cerrada
- Execution: 🔄 En curso

## Sprint 006 — CI GitHub Actions

### Objetivo
Establecer validación continua del repositorio.

### Alcance
- [x] ISSUE-012: Crear pipeline CI (`.github/workflows/ci.yml`)
- [x] ISSUE-014: Materializar HER-STD-0006 — Definition of Done
- [x] Hotfix: corregir scope de link-check en CI

### Artefactos
- `.github/workflows/ci.yml`
- `scripts/validate_governance.sh`
- `governance/std/HER-STD-0006.md`
- `governance/issues/SPRINT-006.md`

### Criterios de éxito
- [x] Commit y push a main
- [x] CI verde en GitHub Actions

## Sprint 007 — a definir por el responsable

### Recomendado
- Primer sprint de código Python (`packages/her-models/`, `her-core/`)
- Resolver ISSUE-013: activar `python-placeholder` con tests reales
- Avanzar ISSUE-005 (ADR DB) o ISSUE-006 (RFC API) si hay contexto

## Documentos vigentes (15)

| Documento | Estado | Versión |
|---|---|---|
| HER-001 — Manifiesto | Aprobado | v1.0.0 |
| HER-ADR-0000 — Repository as Product | Aprobado | v1.1 |
| HER-RFC-001 — WhatsApp First Architecture | Aprobado | v1.0.0 |
| HER-STD-0001 — Repository Contract | Aprobado | v1.0 |
| HER-STD-0002 — Sprint Freeze Rule | Aprobado | v1.0 |
| HER-STD-0003 — Convenciones Git | Aprobado | v1.0.0 |
| HER-STD-0004 — Context Snapshot Standard | Aprobado | v1.0.0 |
| HER-STD-0005 — Definition of Ready | Aprobado | v1.0.0 |
| HER-STD-0006 — Definition of Done | Aprobado | v1.0.0 |
| HER-000 — Constitución | Aprobado | v1.0.1 |
| AR-2026-07-31-001 | Aprobada | — |

## Issues abiertos

- ISSUE-005: Decisión migración DB (Sprint 006+)
- ISSUE-006: Decisión API framework (Sprint 008+)
- ISSUE-013: Activar python-placeholder con tests reales (Sprint 007+)
- ISSUE-015: Desalineación DRY CI/local (Sprint 008+)

## Próximo sprint

SPRINT 007 — primer sprint de código o continuación de infraestructura.
Requiere HER-STD-0005 (Ready) y HER-STD-0006 (Done) vigentes.
