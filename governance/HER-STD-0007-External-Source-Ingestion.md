---
id: HER-STD-0007
title: External Source Ingestion Standard
version: "1.0.0"
status: Approved
created: 2026-08-02
---

# HER-STD-0007 — Estándar de Ingesta de Fuentes Externas (Observatorio)

## Alcance

Aplica a todo contenido de terceros (noticias, estudios, artículos,
entrevistas) incorporado a `knowledge/observatorio/`. No aplica a
`knowledge/biblioteca/` (obra propia del autor del proyecto, otro
tier — ver HER-RFC-001 §10).

## Regla de oro

Ningún archivo de `observatorio/` puede contener el texto original
reproducido más allá de una cita textual de máximo 15 palabras, una
sola por fuente. Todo lo demás debe ser paráfrasis propia. Las cifras,
fechas y datos duros no están sujetos a esta restricción (los hechos
no son propiedad intelectual, la redacción sí).

## Esquema obligatorio (frontmatter)

```yaml
fuente_tipo: noticia | estudio | entrevista | reporte
medio: "Nombre del medio"
autor_original: "Nombre, si se identifica"
fecha_publicacion: "YYYY-MM-DD"
url: "https://..."
fuente_conocimiento_tier: "Observatorio"  # HER-RFC-001 §10, orden 4/5
keywords_rfc001: []
relevancia_cuadrante: []  # Congelado | Calculador | Validador | Planeador
cita_textual_max15: ""    # opcional, <=15 palabras, UNA sola
```

## Secciones obligatorias del cuerpo

1. **Resumen** — 2-4 frases, paráfrasis propia, sin mirroring de
   estructura del original.
2. **Datos clave** — lista de cifras/hechos verificables, con fuente
   atribuida inline.
3. **Relevancia patrimonial** — cómo conecta con el Cuadrante, con
   RFC-001, o con la Biblioteca propia. Esta sección es la que da
   valor real al Observatorio; sin ella, la entrada es solo un
   resumen de noticias sin propósito dentro de HEREDITARIA™.

## Validación automática

`scripts/validate_observatorio.py` — verifica que ningún campo de
texto libre exceda ~15 palabras consecutivas idénticas a un patrón de
cita (heurística simple, no sustituye revisión humana), y que los
campos obligatorios existan.

## Relación con otros documentos

- HER-RFC-001 §10 (orden de fuentes de conocimiento) — el Observatorio
  nunca es fuente de mayor prioridad que Knowledge Base, RFC o
  Legislación.
- `governance/HER-STD-0001-Repository-Contract.md` Criterio 9 — el
  Observatorio no debe contener datos personales de terceros
  identificables (personas mencionadas en noticias públicas están
  exceptuadas si la mención ya es pública, pero no se agregan datos
  no publicados).
