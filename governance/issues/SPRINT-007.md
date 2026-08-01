# Issues Sprint 007

## ISSUE-013 — RESUELTO

**Tipo:** INF
**Descripción:** Activar job `python-placeholder` con tests reales.
**Resolución:**
- Creado `pyproject.toml` con metadatos del proyecto y configuración de herramientas
- Creado `packages/her_models/` con modelo `Expediente` (dataclass frozen)
- Creado `tests/test_her_models.py` con 5 tests unitarios
- Reemplazado job `python-placeholder` por `python` en CI:
  - `ruff check` + `ruff format --check`
  - `mypy packages/`
  - `pytest -v`
- Añadido `HER-STD-0006.md` a lista de validación de gobernanza
- Creado `requirements-dev.txt` para compatibilidad Termux

## ISSUE-005 — ABIERTO

**Tipo:** ADR
**Descripción:** Decisión arquitectónica — migración de base de datos.
**Estado:** Análisis completo, decisión aplazada.
**Prioridad:** Alta
**Resolver en:** Sprint 006+ (cuando haya contexto de implementación)

## ISSUE-006 — ABIERTO

**Tipo:** RFC
**Descripción:** Decisión técnica — framework de API.
**Estado:** Análisis completo, decisión aplazada.
**Prioridad:** Alta
**Resolver en:** Sprint 008+

## ISSUE-015 — ABIERTO (registro técnico)

**Tipo:** INF
**Descripción:** Desalineación DRY entre CI y validador local.
**Contexto:** Detectado en Sprint 006. Listas de archivos en `.github/workflows/ci.yml`
y `scripts/validate_governance.sh` deben mantenerse sincronizadas manualmente.
**Prioridad:** Baja
**Resolver en:** Sprint 008+ (reemplazar por fuente única o parser robusto)
