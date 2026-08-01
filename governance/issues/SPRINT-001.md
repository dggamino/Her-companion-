# Issues detectados durante SPRINT 001

## ISSUE-001

**Tipo:** KB (gobernanza / trazabilidad)

**Detectado en:** Sprint 001

**Descripción:**
La Resolución AR-2026-07-31-001 (cierre de la fase Architecture &
Governance) fue aprobada en conversación pero no forma parte de los
11 artefactos explícitamente definidos para el Sprint 001. Aún no
está materializada en `governance/resolutions/`,
`governance/architecture.md` ni `governance/decisions.md`.

**Impacto:**
Mientras no se materialice, la Resolución no cumple HER-STD-0001,
Criterio 10 (Auditabilidad): no puede reconstruirse desde el
repositorio, solo desde el historial de conversación.

**Prioridad:** Media — no bloquea el criterio de éxito del Sprint 001
(infraestructura mínima reproducible), pero debe resolverse antes de
que se abran nuevos Sprints de contenido de gobierno.

**Resolver en:** Sprint 002

---

## ISSUE-002

**Tipo:** STD

**Detectado en:** Sprint 001 (validación real en Termux)

**Descripción:**
`git init` en el dispositivo usó `master` como rama por defecto (Git
no tenía `init.defaultBranch` configurado). No existe una decisión
constitucional sobre el nombre de la rama principal del repositorio
(`main` vs `master`).

**Impacto:**
Bajo, pero afecta consistencia si se automatizan workflows de GitHub
Actions o scripts que asuman un nombre de rama específico.

**Prioridad:** Baja

**Resolver en:** Sprint 002 (definir como parte de un HER-STD de
convenciones de Git, o adoptar `main` explícitamente antes del primer
`git push`).
