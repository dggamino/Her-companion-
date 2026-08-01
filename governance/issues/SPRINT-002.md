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

**Estado (2026-08-01): RESUELTO por confirmación directa.** El
responsable del proyecto confirma que `RUNTIME_MASTER_PROMPT` (solo
existe v1 en disco; sin v2 localizable en el dispositivo) y los
nodos Curador/Generador pertenecen a un proyecto anterior, no
relacionado con HEREDITARIA™. No hay arquitectura paralela ni
sistema no reconciliado dentro de HEREDITARIA™ — Motor HEREDITARIA™
OS (RFC-001) sigue siendo el único orquestador vigente.

**Nuevo seguimiento (no es continuación de ISSUE-003, es hallazgo
derivado):** `ONTOLOGIA.md` §7 ("Protocolo de validación del
Curador") depende operativamente de esa infraestructura ajena.
Pendiente de decisión del responsable: (a) el concepto de Curador se
reimplementa sobre Motor HEREDITARIA™ OS, (b) la sección se marca
como DEPRECATED/vestigial y se elimina, o (c) se deja documentado
como trabajo futuro sin fecha. Registrar como ISSUE-005 cuando se
tome la decisión.

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

**Estado (2026-08-01):** Verificación legal completada. Se confirmó
contra el documento oficial (Gaceta del Gobierno del Estado de
México, Decreto 87, 7 de mayo de 2013) que la cita de `ONTOLOGIA.md`
§1.6 es exacta: artículos 7.1144 Bis a 7.1144 Undecies del Código
Civil del Estado de México, vigencia julio 2013, y la autorización a
instituciones privadas/sociales/personas físicas/públicas del Art.
7.1144 Quater coincide casi textualmente con el decreto. No hay error
ni invención en la fuente legal.

**Pendiente:** la pregunta de alcance de producto sigue abierta —
¿es la hipoteca inversa EdoMex el producto real vigente, o uno de
varios casos de uso dentro de un alcance nacional? Es una decisión
estratégica, no legal; no se resuelve con la verificación del
documento.

**Resolver en:** Sprint 002, antes de construir contenido o
automatización específica de producto.
