# HEREDITARIA-OS — Context Snapshot

Generado: 2026-08-01T14:49:09Z
Rama: main
Último commit: f569318 Resolve ISSUE-003 by direct confirmation: Curador/Generador belong to unrelated prior project (2026-07-31)

> Este archivo se genera automáticamente desde el estado real
> del repositorio. No es una fuente de verdad por sí mismo —
> es un resumen para arrancar una sesión nueva. Ante cualquier
> duda, el repositorio (no este archivo, no el chat) manda.

---

## Instrucción para la nueva sesión

1. Usar el Bootstrap Prompt v1.0 como contrato operativo (sin
   volver a pegarlo completo salvo que cambie; referenciarlo).
2. Este snapshot reemplaza cualquier resumen de conversación.
3. No aceptar como hecho ningún documento de gobierno (informe
   de auditoría, resolución, ADR) que no esté aquí abajo o en
   el repositorio real — no reconstruir de memoria.

---

## PROJECT_STATE.md

# PROJECT_STATE

Última actualización: 2026-07-31
Sprint activo: SPRINT 001
Estado general: Execution Mode

## Fase

- Architecture & Governance: **Cerrada** (Resolución AR-2026-07-31-001)
- Execution: **En curso** (SPRINT 001)

## Sprint 001 — Infraestructura mínima reproducible

### Objetivo
Inicializar HEREDITARIA-OS con la infraestructura mínima reproducible
y versionable, compatible con Android 14/15 + Termux.

### Artefactos entregados
- [x] README.md
- [x] PROJECT_STATE.md
- [x] CHANGELOG.md
- [x] VERSION
- [x] LICENSE
- [x] .gitignore
- [x] install.sh
- [x] termux_setup.sh
- [x] requirements.txt
- [x] knowledge/README.md
- [x] scripts/update.sh

### Criterios de éxito
- [x] Archivos base existen
- [x] Estructura de directorios creada
- [ ] Proyecto clonado y verificado desde GitHub (validado por `unzip` local; pendiente `git clone` real desde remoto tras `git push`)
- [x] Inicializado desde Android + Termux — validado en dispositivo real, 2026-08-01 (ver `logs/SPRINT-001-validation.log`)
- [x] Estado registrado en este archivo
- [x] Validación del sprint sin inconsistencias — `git init`, `git add .`, `git commit` (53e141e, 21 archivos), `termux_setup.sh` e `install.sh` ejecutados sin errores

### Evidencia de validación (2026-08-01, Termux real)
- Commit inicial: `53e141e`, 21 archivos, rama `master`.
- `termux_setup.sh`: git 2.54.0, python 3.13.13 — sin instalaciones nuevas (paquetes ya presentes).
- `install.sh`: entorno virtual creado en `.venv`, pip actualizado, `requirements.txt` procesado sin dependencias.
- Log completo: `logs/SPRINT-001-validation.log`.

### Pendiente para cerrar el criterio de GitHub
- Crear repositorio remoto.
- `git remote add origin <URL>`
- `git push -u origin master` (o renombrar a `main` antes del push, ver aviso de Git más abajo).
- Validar `git clone` desde el remoto en un directorio limpio.

## Documentos de gobierno vigentes

| Documento | Estado |
|---|---|
| HER-001 — Manifiesto | Aprobado |
| HER-RFC-001 — WhatsApp First Architecture | Aprobado (Draft v0.1) |
| HER-ADR-0000 — Repository as Product | Aprobado (v1.1) |
| HER-STD-0001 — Repository Contract | Aprobado (v1.0, 10 criterios) |
| HER-STD-0002 — Sprint Freeze Rule | Aprobado |
| HER-000 — Constitución del Proyecto | Pendiente (reevaluar tras Sprint 003) |
| Bootstrap Prompt | v1.0 |

## Supuestos no verificados

Registrados por restricción de HER-STD-0001 y el Bootstrap Prompt v1.0.
Ninguno de estos supuestos debe tratarse como hecho de arquitectura
hasta ser validado en entorno real.

- WAHA puede operar de forma continua sobre Termux en un dispositivo
  Android sin verse afectado por Doze mode / gestión de batería.
- GitHub Actions en repositorio privado se mantiene dentro de límites
  de minutos gratuitos del Free Tier para el volumen esperado.
- Netlify Functions (Free Tier) es suficiente para necesidades futuras
  de lógica server-side (ej. webhook WAHA), aún no confirmado.
- Termux permite instalar todas las dependencias de `requirements.txt`
  sin requerir compilación nativa adicional (a validar según crezca
  la lista de dependencias).

## Pendientes registrados como Issue

- ISSUE-001 (`governance/issues/SPRINT-001.md`): materializar la
  Resolución AR-2026-07-31-001 en `governance/resolutions/` y
  `governance/architecture.md` / `governance/decisions.md`. No estaba
  en el alcance explícito de los 11 archivos del Sprint 001; se
  registra en lugar de expandir el alcance del sprint en curso.

## Próximo sprint

SPRINT 002 — a definir. No debe iniciarse hasta cerrar validación de
SPRINT 001 (clonado real + Termux real).

---

## Issues abiertos (governance/issues/)

### Archivo: `governance/issues/SPRINT-001.md`

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

### Archivo: `governance/issues/SPRINT-002.md`

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

---

## Auditorías (audits/)

### Archivo: `audits/AUDIT-001-Ontology.md`

---
id: HER-AUDIT-0001
title: Auditoría Ontológica — Blueprint vs ONTOLOGIA.md
version: 1.0
status: Draft
owner: HEREDITARIA
created: 2026-08-01
---

# AUDIT-001 — Comparación de Ontología Oficial

Resolución: **WARNING**

## Nota de integridad

Un informe previo con esta misma referencia (`AUDIT-001-Ontology.md`,
`status: Approved`, resolución PASS) fue recibido en conversación sin
haber sido producido mediante comparación real de los documentos
fuente. Ese informe se descarta en su totalidad. Este documento es la
primera auditoría real, basada en el contenido íntegro de
`ONTOLOGIA.md` compartido el 2026-08-01.

---

# Resumen ejecutivo

`ONTOLOGIA.md` y `01_Ontology_Blueprint_v1.0.md` no son versiones del
mismo documento ni capas del mismo modelo: pertenecen a dominios
distintos. El Blueprint define el modelo de entidades y relaciones
del patrimonio familiar. `ONTOLOGIA.md` es un corpus de gobernanza de
marca y contenido para un nodo "Curador" que valida material
publicable. No se detecta contradicción directa con la arquitectura
aprobada.

**Actualización 2026-08-01:** el Hallazgo 3 (arquitectura de runtime)
queda resuelto por confirmación directa: Curador/Generador pertenecen
a un proyecto anterior no relacionado. Esto descarta el riesgo de
"deuda de coherencia por sistemas paralelos no reconciliados", pero
introduce una pregunta distinta y más concreta: ¿la sección 7 de
`ONTOLOGIA.md` (protocolo del Curador) debe corregirse, eliminarse o
reimplementarse sobre el Motor HEREDITARIA™ OS? Ver Hallazgo 3 y
ISSUE-003 actualizados.

Se mantiene **WARNING**, no PASS, hasta que esa pregunta se
resuelva — ya no por riesgo de arquitectura paralela, sino porque un
documento de gobierno vigente contiene una sección operativa que
depende de infraestructura ajena al proyecto.

---

# 1. Alcance

Auditar la consistencia entre `01_Ontology_Blueprint_v1.0.md` y
`ONTOLOGIA.md`, y su impacto sobre HER-001, HER-RFC-001,
HER-ADR-0000 y HER-STD-0001.

# 2. Documentos auditados

- Documento A: `01_Ontology_Blueprint_v1.0.md` (Estado: ACTIVO)
- Documento B: `ONTOLOGIA.md` — "Corpus de gobernanza para el nodo
  Curador", v1.0, Daniel Gómez Gamiño, 2026

# 3. Fuente de verdad utilizada hasta ahora

Toda la fase Architecture & Governance (HER-001, HER-RFC-001,
HER-ADR-0000, HER-STD-0001) se construyó usando exclusivamente
`01_Ontology_Blueprint_v1.0.md` y `02_Glosario_Taxonomia_v1.0.md`
como referencia terminológica. `ONTOLOGIA.md` no fue consultado
durante esa fase porque no se compartió hasta este punto.

# 4. Metodología

Comparación directa del texto íntegro de ambos documentos, sección
por sección, contra: identidad de marca, modelo de entidades,
terminología, gobernanza, arquitectura de runtime y restricciones
legales/operativas ya aprobadas.

# 5. Hallazgos

## Hallazgo 1 — Naturaleza del documento
`ONTOLOGIA.md` no define entidades ni relaciones (Persona, Familia,
Inmueble, Evento, Ruta, Kit, Expediente, Programa, Beneficio, Alerta,
Regla). Define una clasificación editorial de contenido
(HARD_CANON / SOFT_CANON / PROVISIONAL / DEPRECATED / COUNTERFACTUAL
/ SIMULATION_BRANCH) para un pipeline de publicación.
**No es una ontología en el sentido del Blueprint.**

## Hallazgo 2 — Identidad de marca
HEREDITARIA™ se mantiene como marca madre en ambos documentos. Sin
contradicción directa. `ONTOLOGIA.md` introduce dos elementos nuevos
no presentes en ningún documento aprobado: el programa "Patrimonio
Vivo" y la voz narrativa/personaje "Don Severo Villanueva". Ninguno
de los dos está registrado en `02_Glosario_Taxonomia_v1.0.md`.

## Hallazgo 3 — Arquitectura de runtime no reconciliada (RESUELTO 2026-08-01)
`ONTOLOGIA.md` referencia `RUNTIME_MASTER_PROMPT_v2` y nodos
"Curador" y "Generador". HER-RFC-001 define un orquestador distinto
("Motor HEREDITARIA™ OS") con módulos Observatorio / Biblioteca /
Boutique / Expediente, sin mencionar Curador ni Generador.

**Confirmación directa (2026-08-01):** el responsable del proyecto
confirma que `RUNTIME_MASTER_PROMPT` (solo existe v1 en disco, ver
Addendum de Hallazgo 3.1) y los nodos Curador/Generador pertenecen a
**un proyecto anterior y no relacionado con HEREDITARIA™**. No son
arquitectura paralela de HEREDITARIA™ ni una versión previa del
Motor HEREDITARIA™ OS — son de otro proyecto.

**Consecuencia no trivial:** `ONTOLOGIA.md` §7 ("Protocolo de
validación del Curador"), documento de gobierno vigente para
HEREDITARIA™, depende operativamente de infraestructura de ese
proyecto ajeno. Esto no es solo una referencia obsoleta — es una
sección completa de un documento de gobierno actualmente activo que
apunta a un runtime que no pertenece a HEREDITARIA™. Queda abierta
la pregunta de si el *concepto* de Curador (validación de contenido
contra HARD_CANON/SOFT_CANON/etc.) se conserva y se reimplementa
sobre el Motor HEREDITARIA™ OS, o si toda la sección 7 es también
vestigial. Ver ISSUE-003 actualizado.

### Addendum — Hallazgo 3.1
Búsqueda exhaustiva en el dispositivo (`find ~ -iname
"*runtime_master_prompt*"`) confirma que **no existe ningún archivo
v2** — solo dos copias de `RUNTIME_MASTER_PROMPT_v1.md` idénticas en
nombre, ambas en el repositorio ya existente
`~/runtime-master-prompt` (git, remoto
`https://github.com/dggamino/runtime-master-prompt`, rama `main`).
La referencia a "v2" en `ONTOLOGIA.md` no corresponde a ningún
artefacto real localizable.

## Hallazgo 4 — Alcance legal más específico de lo declarado (ACTUALIZADO 2026-08-01)
La sección 1.6 fija como fundamento legal el Decreto 87 (Estado de
México), específico para hipoteca inversa. **Verificado contra el
texto íntegro de la Gaceta del Gobierno del Estado de México (7 de
mayo de 2013):** la cita es exacta — número de decreto, fecha de
publicación, vigencia (60 días después, Art. Tercero Transitorio) y
artículos 7.1144 Bis a Undecies del Código Civil del Estado de
México, incluyendo la redacción literal del Art. 7.1144 Quater sobre
quién puede otorgar la hipoteca inversa. **No es una cita inventada
ni mal transcrita.**

Lo que permanece sin resolver es distinto: si la hipoteca inversa en
Estado de México es el producto comercial real y vigente de
HEREDITARIA™, o uno de varios casos de uso previstos dentro del
alcance nacional multi-ruta que describen HER-001 y HER-RFC-001. Esa
es una pregunta de alcance de negocio, no de exactitud legal, y
ningún documento fuente disponible la responde — requiere
confirmación directa del responsable del proyecto.

## Hallazgo 5 — Vocabulario de marca sin integrar al Glosario
Los términos de la sección 1.3 (Activo dormido/muerto/vivo,
Cleptonomía familiar, Heredero anticipado, Arquitectura patrimonial,
Default del cuidador) no aparecen en
`02_Glosario_Taxonomia_v1.0.md`. No entran en conflicto léxico con
los términos ya definidos ahí (EPA, Evento Patrimonial, Ruta
Patrimonial, etc.), pero constituyen un sistema terminológico
paralelo no registrado, en tensión con la instrucción de proyecto de
mantener coherencia con el Glosario.

## Hallazgo 6 — Material ficticio y de simulación
Las secciones COUNTERFACTUAL y SIMULATION_BRANCH son consistentes
con las restricciones ya aprobadas en HER-RFC-001 §11 (HEREDITARIA
no sustituye asesoría, no toma decisiones por el usuario). Sin
impacto negativo.

# 6. Diferencias identificadas

| Aspecto | Blueprint | ONTOLOGIA.md |
|---|---|---|
| Función | Modelo de entidades del dominio patrimonial | Gobernanza editorial de contenido publicable |
| Público | Arquitectos de producto / conocimiento | Nodo Curador (validación automatizada) |
| Runtime referenciado | Motor HEREDITARIA™ OS (RFC-001) | RUNTIME_MASTER_PROMPT_v2 (no reconciliado) |
| Alcance legal | General, sin instrumento específico | Decreto 87, EdoMex, hipoteca inversa |
| Vocabulario | EPA, Evento/Ruta/Expediente Patrimonial | Activo dormido/muerto/vivo, etc. |

Conclusión: **no conflictivos en el modelo de entidades**, pero
**no reconciliados en arquitectura de runtime, alcance legal
declarado y vocabulario**.

# 7. Impacto sobre documentos aprobados

| Documento | Impacto |
|---|---|
| HER-001 (Manifiesto) | Sin contradicción directa; alcance nacional declarado no confirmado ni refutado |
| HER-RFC-001 | Arquitectura de runtime (Curador/Generador) no reconciliada con Motor HEREDITARIA™ OS |
| HER-ADR-0000 | Sin impacto |
| HER-STD-0001 | Sin impacto; vocabulario nuevo no viola Criterio 9 (no contiene datos reales) |

# 8. Riesgo

**Nivel: Medio** (no Bajo, no Alto).

No hay riesgo de invalidar la arquitectura aprobada, pero sí riesgo
de que Sprint 002 construya sobre una arquitectura de runtime
(Curador/Generador vs. Motor HEREDITARIA™ OS) sin que ambas piezas
estén reconciliadas, generando deuda de coherencia difícil de
revertir después.

# 9. Recomendación

1. No declarar `ONTOLOGIA.md` como "Ontología Operativa" — el nombre
   induce a error. Es un corpus de gobernanza de marca/contenido;
   renombrar o reclasificar (ej. `HER-STD` de Brand & Content
   Governance) evitaría confundirlo con el modelo de entidades.
2. Aclarar directamente con el responsable del proyecto (no inferir):
   ¿`RUNTIME_MASTER_PROMPT_v2` y los nodos Curador/Generador son el
   mismo sistema que el Motor HEREDITARIA™ OS de RFC-001, un sistema
   paralelo, o una versión previa a reemplazar?
3. Confirmar si la hipoteca inversa en Estado de México es el
   producto real vigente o un caso de uso entre varios previstos.
4. Registrar el vocabulario de marca (sección 1.3) en
   `02_Glosario_Taxonomia_v1.0.md` o documentar explícitamente por
   qué permanece como vocabulario separado.

# 10. Resolución

**WARNING.** No se identifican contradicciones que invaliden la
arquitectura aprobada; no se abre HER-ISSUE-0003 con carácter de
FAIL. Se registran las preguntas abiertas del Hallazgo 3 y 4 como
seguimiento obligatorio antes de que Sprint 002 dependa de ellas.

# 11. Evidencia

Comparación basada en el texto completo de `ONTOLOGIA.md` (11
secciones, compartido 2026-08-01) contra `01_Ontology_Blueprint_v1.0.md`
(Estado: ACTIVO, documento de proyecto). Sin inferencias sobre
contenido no visto.

# 12. Próximas acciones

- Cerrar PRE-SPRINT AUDIT 001 con resolución WARNING (no PASS).
- Registrar seguimiento en `governance/issues/SPRINT-002.md`:
  reconciliación de runtime (Curador/Generador vs. Motor HEREDITARIA™
  OS) y confirmación de alcance de negocio (hipoteca inversa EdoMex
  como producto único vigente vs. uno de varios casos de uso).
- SPRINT 002 puede iniciar, pero no debe asumir que ambos runtimes
  son el mismo sistema hasta confirmación explícita.
- No fusionar `ONTOLOGIA.md` con el Blueprint; mantener separados por
  dominio (entidades vs. gobernanza de contenido).

## Addendum — 2026-08-01

Se verificó el texto íntegro de la Gaceta del Gobierno del Estado de
México (Decreto 87, 7 de mayo de 2013) contra la cita de
`ONTOLOGIA.md` §1.6. **Resultado: cita legal exacta y verificable.**
Esto no cambia la resolución general (WARNING se mantiene, por el
Hallazgo 3 sin resolver), pero cierra la dimensión de "exactitud de
la cita legal" dentro del Hallazgo 4. La dimensión de "alcance de
negocio" (¿es este el producto único vigente?) permanece abierta y
no se resuelve con este documento.

---

## Resoluciones (governance/resolutions/)

_(ninguna materializada todavía — ver ISSUE-001)_
---

## Últimos commits (últimos 10)

```
f569318 Resolve ISSUE-003 by direct confirmation: Curador/Generador belong to unrelated prior project
c69a962 Add session context snapshot mechanism (HER-ADR-0000 compliance)
2854b68 AUDIT-001: verify Decreto 87 citation against Gaceta del Gobierno PDF
daf8de1 SPRINT 001 Fix stray .gitkeep files from packaging bug
1d8a7fb PRE-SPRINT AUDIT 001: WARNING resolution, register ISSUE-003 and ISSUE-004
28e8766 SPRINT 001 Apply gitignore and changelog fix
82cb8a8 SPRINT 001 Fix gitignore excluding validation log
c44a3c2 SPRINT 001 Validate on Termux, log evidence
53e141e SPRINT 001 Bootstrap repository
```
