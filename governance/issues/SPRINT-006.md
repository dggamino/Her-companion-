# Issues Sprint 006

## ISSUE-012 — RESUELTO

**Tipo:** INF
**Descripción:** Crear pipeline CI para validación continua del repositorio.
**Resolución:**
- `.github/workflows/ci.yml` con dos jobs:
  - `governance`: valida estructura de documentos, sintaxis shell, links rotos
  - `python-placeholder`: prepara entorno Python 3.11 para código futuro
- `scripts/validate_governance.sh` para validación local en Termux

## ISSUE-013 — ABIERTO

**Tipo:** INF
**Descripción:** Activar job `python-placeholder` con tests reales cuando
`packages/her-models/` y código Python sean agregados.
**Prioridad:** Media
**Resolver en:** Sprint 007+

## ISSUE-014 — ABIERTO

**Tipo:** STD
**Descripción:** Definir HER-STD-0006 — Definition of Done.
**Prioridad:** Media
**Resolver en:** Sprint 007 (antes de primer sprint de código)
