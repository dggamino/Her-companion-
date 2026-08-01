# PROJECT_STATE

Última actualización: 2026-08-01
Sprint activo: SPRINT 005
Estado general: Execution Mode

## Fase
- Architecture & Governance: ✅ Cerrada
- Execution: 🔄 En curso

## Sprint 005 — Corrección de deuda técnica de gobernanza

### Objetivo
Materializar documentos fundacionales ausentes y corregir defectos
de integridad en documentos aprobados.

### Alcance
- [x] ISSUE-008: Crear HER-001 — Manifiesto
- [x] ISSUE-009: Corregir `constitution.md` (quitar citas a ADR inexistentes)
- [x] ISSUE-010: Materializar HER-ADR-0000, HER-STD-0001, HER-STD-0002
- [x] ISSUE-011: Registrar HER-STD-0006 para Sprint 006

### Artefactos
- `governance/HER-001-Manifiesto.md`
- `governance/adr/HER-ADR-0000.md`
- `governance/std/HER-STD-0001.md`
- `governance/std/HER-STD-0002.md`
- `governance/constitution.md` (v1.0.1)
- `governance/issues/SPRINT-005.md`

### Criterios de éxito
- [ ] Commit y push a main
- [ ] Validación: `find governance/adr/` no vacío
- [ ] Validación: `grep ADR-007 constitution.md` sin resultados

## Documentos vigentes (14)

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
| HER-000 — Constitución | Aprobado | v1.0.1 |
| AR-2026-07-31-001 | Aprobada | — |

## Issues abiertos

- ISSUE-005: Decisión migración DB (Sprint 006+)
- ISSUE-006: Decisión API framework (Sprint 008+)
- ISSUE-007: HER-STD-0006 Definition of Done (Sprint 006)
- ISSUE-011: HER-STD-0006 Definition of Done (duplicado, consolidar)

## Próximo sprint

SPRINT 006 — a definir por el responsable.
Recomendado: HER-STD-0006 (Definition of Done) o primer sprint de código.
