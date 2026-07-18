---
id: HER-KB-001
title: Learning Path
version: 1.0.0
status: Active
owner: HER Companion™
type: Knowledge
created: 2026-07-18
updated: 2026-07-18
related:
  - HER-KB-000
  - HER-KB-011
  - HER-KB-012
---

# HER-KB-001 — Learning Path

## Propósito

Este documento define el recorrido de aprendizaje para administrar y desarrollar HER Companion™.

Está diseñado para personas sin experiencia técnica ("no-tech"), permitiendo avanzar mediante pequeños ejercicios repetibles hasta adquirir autonomía.

El objetivo no es aprender programación, sino desarrollar una metodología de trabajo basada en conocimiento, trazabilidad y control de versiones.

---

# Principios

- Aprender haciendo.
- Un cambio pequeño es mejor que un cambio grande sin comprender.
- La repetición genera confianza.
- Git registra la historia; la Base de Conocimiento conserva el conocimiento.
- Ninguna conversación sustituye la documentación.

---

# Ruta de Aprendizaje

## Nivel 0 — Orientación

### Objetivo

Comprender qué es HER Companion™ y cómo está organizado el laboratorio.

### Debes conocer

- Qué es Git.
- Qué es GitHub.
- Qué es una Base de Conocimiento.
- Qué es Markdown.
- Qué es un repositorio.

### Ejercicio

- Abrir el repositorio.
- Explorar las carpetas.
- Leer:

  - PROJECT_STATE.md
  - knowledge/00_Foundation.md

### Criterio de finalización

Puedes explicar con tus propias palabras cómo está organizado el proyecto.

---

## Nivel 1 — Flujo Operativo

### Objetivo

Aprender el ciclo básico de trabajo.

### Flujo

```text
Abrir Termux
      ↓
Entrar al repositorio
      ↓
git status
      ↓
Leer PROJECT_STATE
      ↓
Editar un documento
      ↓
git diff
      ↓
git add
      ↓
git commit
      ↓
git push
```

### Ejercicio

Realizar este flujo completo cinco veces.

No importa el contenido.

Importa comprender el proceso.

### Criterio de finalización

Puedes realizar un commit sin consultar una guía.

---

## Nivel 2 — Administración del Conocimiento

### Objetivo

Aprender dónde registrar cada tipo de información.

### Debes distinguir

Pregunta

↓

knowledge/12_Preguntas_Abiertas.md

Hipótesis

↓

knowledge/02_Hipotesis.md

Decisión

↓

knowledge/11_Decisiones.md

Investigación

↓

research/

Conocimiento estable

↓

knowledge/

### Ejercicio

Clasificar correctamente diez ideas distintas.

### Criterio de finalización

No confundes preguntas con decisiones o hipótesis.

---

## Nivel 3 — Trazabilidad

### Objetivo

Comprender cómo evoluciona el conocimiento.

### Aprenderás

- identificadores HER
- referencias cruzadas
- historial de decisiones
- relación entre documentos

### Ejercicio

Registrar una decisión que responda a una pregunta existente.

### Criterio de finalización

Puedes seguir la trazabilidad entre una pregunta y una decisión.

---

## Nivel 4 — Gestión del Laboratorio

### Objetivo

Administrar el laboratorio sin depender de una IA específica.

### Debes ser capaz de

- iniciar una sesión;
- cerrar una sesión;
- actualizar PROJECT_STATE;
- mantener Working_On;
- revisar cambios;
- realizar commits consistentes.

### Ejercicio

Completar una sesión de trabajo sin asistencia.

### Criterio de finalización

El laboratorio permanece organizado y actualizado.

---

## Nivel 5 — Arquitectura

### Objetivo

Mejorar el sistema.

### Aprenderás

- diseñar nuevos documentos;
- modificar el flujo;
- proponer mejoras;
- mantener consistencia.

### Criterio de finalización

Puedes ampliar HER Companion™ sin romper la estructura existente.

---

# Rutina Diaria

Cada sesión comienza leyendo únicamente:

1. PROJECT_STATE.md
2. knowledge/00_Foundation.md
3. knowledge/08_Working_On.md
4. knowledge/11_Decisiones.md
5. knowledge/12_Preguntas_Abiertas.md

---

Cada sesión termina:

1. Actualizar PROJECT_STATE.md.
2. Actualizar Working_On.md.
3. Revisar cambios con git diff.
4. Ejecutar git status.
5. Crear un commit.
6. Ejecutar git push.

---

# Reglas de Oro

1. Nunca trabajar directamente desde la memoria.
2. Registrar las decisiones importantes.
3. Mantener los commits pequeños.
4. No mezclar diferentes tipos de conocimiento.
5. La Base de Conocimiento siempre tiene prioridad sobre la conversación.
6. Antes de crear un documento nuevo, comprobar si ya existe uno adecuado.
7. La simplicidad es preferible a la complejidad.

---

# Indicadores de Progreso

| Nivel | Estado | Fecha |
|--------|--------|-------|
| Nivel 0 | ☐ | |
| Nivel 1 | ☐ | |
| Nivel 2 | ☐ | |
| Nivel 3 | ☐ | |
| Nivel 4 | ☐ | |
| Nivel 5 | ☐ | |

---

# Definición de Éxito

El Learning Path se considera completado cuando el operador puede:

- mantener la Base de Conocimiento;
- preservar la continuidad del proyecto entre sesiones;
- utilizar Git con confianza;
- documentar decisiones con trazabilidad;
- continuar el desarrollo sin depender del contexto de una conversación específica.

---

# Evolución

Este documento evolucionará junto con HER Companion™.

Cada mejora del laboratorio deberá reflejarse aquí para que futuros operadores dispongan de un recorrido de aprendizaje claro, progresivo y reproducible.

