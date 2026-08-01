# ISSUE-005 — Análisis de Riesgo: SQLite → PostgreSQL

## Estado
Análisis preliminar. Decisión aplazada a Sprint 006+.

## Contexto
HER-STD-0001 requiere persistencia auditable. SQLite es la elección
actual (ADR-001). Se desconoce si escalará.

## Escenarios evaluados

| Escenario | Volumen | SQLite | PostgreSQL |
|-----------|---------|--------|------------|
| MVP | < 1K expedientes | ✅ Adecuado | ❌ Overkill |
| Crecimiento | 1K-10K | ⚠️ Límite concurrencia | ✅ Recomendado |
| Escala | > 10K | ❌ No recomendado | ✅ Necesario |

## Criterios de decisión (para Sprint 006)

Decidir cuando:
- Concurrencia de escritura > 1 simultánea sostenida
- Tamaño de DB > 500MB
- Necesidad de replicación o backup remoto

## Mitigación inmediata (sin cambiar DB)

- WAL mode en SQLite
- Backup periódico a Git
- Archivado de expedientes cerrados

## Conclusión
SQLite es correcto para Sprints 004-005. Reevaluar tras her-core.
