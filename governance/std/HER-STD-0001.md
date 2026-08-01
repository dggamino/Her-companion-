# HER-STD-0001 — Repository Contract

## Versión
1.0

## Estado
Aprobado

## Alcance
Toda interacción con el repositorio HEREDITARIA™ OS.

## Criterios

| # | Criterio | Descripción |
|---|----------|-------------|
| 1 | Existencia | Todo archivo mencionado existe físicamente |
| 2 | Trazabilidad | Todo commit referencia un sprint o issue |
| 3 | Atomicidad | Un commit = un cambio lógico |
| 4 | Mensaje | Formato: `tipo(alcance): descripción (HER-XXX)` |
| 5 | Rama | `main` para producción; `feature/*` para desarrollo |
| 6 | Revisión | Ningún push a `main` sin validación previa |
| 7 | Dependencias | `requirements.txt` o `pyproject.toml` actualizado |
| 8 | Tests | Código nuevo requiere prueba asociada |
| 9 | Documentación | Cambio de interfaz requiere actualización de docs |
| 10 | Auditabilidad | Toda decisión arquitectónica tiene ADR o resolución |

## Referencias
- HER-001 — Manifiesto
- HER-STD-0003 — Convenciones Git
