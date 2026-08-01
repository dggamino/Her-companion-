# Issues detectados antes/durante SPRINT 002

## ISSUE-003

**Tipo:** RFC / ADR (arquitectura de runtime)

**Detectado en:** PRE-SPRINT AUDIT 001 (AUDIT-001-Ontology.md, Hallazgo 3)

**Descripción:**
`ONTOLOGIA.md` referencia `RUNTIME_MASTER_PROMPT_v2` y nodos
"Curador" y "Generador". HER-RFC-001 define un orquestador distinto
("Motor HEREDITARIA™ OS") con módulos Observatorio/Biblioteca/
Boutique/Expediente. No está confirmado si ambos son el mismo
sistema, sistemas paralelos, o arquitectura no reconciliada.

**Impacto:**
Alto si Sprint 002 construye automatización asumiendo un runtime
incorrecto.

**Prioridad:** Alta — requiere confirmación explícita antes de que
Sprint 002 dependa de esta arquitectura.

**Resolver en:** Antes de cerrar Sprint 002, o al inicio del mismo.

---

## ISSUE-004

**Tipo:** KB / RFC (alcance de producto)

**Detectado en:** PRE-SPRINT AUDIT 001 (AUDIT-001-Ontology.md, Hallazgo 4)

**Descripción:**
`ONTOLOGIA.md` fija el fundamento legal en el Decreto 87 (Estado de
México, hipoteca inversa). HER-001 y HER-RFC-001 describen alcance
nacional y multi-ruta. No está confirmado si la hipoteca inversa
EdoMex es el producto real vigente o uno de varios casos de uso
futuros.

**Impacto:**
Medio — afecta cómo se interpreta el alcance de "patrimonio familiar"
en toda la documentación ya aprobada.

**Prioridad:** Media

**Resolver en:** Sprint 002, antes de construir contenido o
automatización específica de producto.
