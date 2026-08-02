# HER-ADR-0001 — Estrategia de Persistencia para MVP

## Estado
Aprobado

## Contexto
HER-STD-0001 requiere persistencia auditable. ISSUE-005 analizo SQLite vs PostgreSQL.

## Decisión
Adoptar SQLite con SQLAlchemy 2.0 async para el MVP.

## Consecuencias positivas
- Zero-config en Termux
- SQLAlchemy 2.0 permite migrar a PostgreSQL sin cambiar ORM
- WAL mode mejora concurrencia de lectura
- Alembic para migraciones desde el inicio

## Consecuencias negativas
- 1 writer a la vez
- Limite practico: ~1GB, ~10K expedientes
- Backup manual requerido

## Reevaluacion

| Trigger | Accion |
|---------|--------|
| Escritura concurrente > 1 | Evaluar PostgreSQL |
| DB > 500MB | Particionar o PostgreSQL |
| Replicacion/remoto | PostgreSQL + cloud |

## Implementacion

Engine async: sqlite+aiosqlite:///data/hereditaria.db
WAL mode: PRAGMA journal_mode=WAL;
Migraciones: alembic en packages/her_core/alembic/

## Referencias
- ISSUE-005
- HER-STD-0001
- HER-RFC-001
