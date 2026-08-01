# ISSUE-006 — Análisis de Riesgo: FastAPI vs Alternativas Ligeras

## Estado
Análisis preliminar. Decisión aplazada a Sprint 008+.

## Contexto
HER-RFC-001 asume FastAPI para API REST. Termux tiene recursos limitados.

## Alternativas evaluadas

| Framework | Memoria base | Startup | Async | Termux |
|-----------|-------------|---------|-------|--------|
| FastAPI | ~50MB | Medio | ✅ | ✅ |
| Flask | ~20MB | Rápido | ❌ (sin ext) | ✅ |
| Starlette | ~30MB | Rápido | ✅ | ✅ |
| Sanic | ~40MB | Rápido | ✅ | ⚠️ |

## Criterios de decisión (para Sprint 008)

Decidir cuando:
- her-router esté implementado (Sprint 007)
- Se conozca el volumen de requests WAHA
- Se haya medido memoria en Termux real

## Conclusión
FastAPI sigue siendo la opción por defecto. Reevaluar si memoria
en Termux < 100MB disponible para el proceso API.

## Nota
No bloquea Sprints 004-007. La API es el último componente.
