# Issues Sprint 012

## ISSUE-019 — RESUELTO

**Tipo:** INF
**Descripción:** Implementar lógica de negocio — estados de expediente, agentes, workflow.
**Resolución:**
- Añadido `EstadoExpediente` enum (nuevo, en_proceso, pendiente, cerrado, archivado)
- Añadido campo `estado` y `agente_id` a modelo `Expediente`
- Creado modelo `Agente` con relación a expedientes
- Creado `her_api/services/workflow.py` — transiciones de estado validadas
- Creado `her_api/routers/agentes.py` — CRUD agentes
- Actualizado `her_api/routers/expedientes.py` — PUT para actualizar estado y agente
- Creado `tests/test_workflow.py` — 5 tests de transiciones de estado
- Creado `tests/test_agentes.py` — 4 tests de integración CRUD agentes

## ISSUE-015 — ABIERTO

**Tipo:** INF
**Descripción:** Desalineación DRY entre CI y validador local.
**Prioridad:** Baja
**Resolver en:** Sprint 013+
