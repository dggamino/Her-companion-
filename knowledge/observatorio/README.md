# knowledge/observatorio/ — Fuentes externas

Tier 4 de 5 en el orden de fuentes de HER-RFC-001 §10 (por debajo de
Knowledge Base, RFC y Legislación; por encima de Biblioteca propia
para efectos de actualidad, aunque Biblioteca es la obra fundacional).

## Diferencia con knowledge/biblioteca/

| | `biblioteca/` | `observatorio/` |
|---|---|---|
| Autoría | Propia (Daniel Gómez Gamiño) | Terceros |
| Reproducción | Texto completo permitido | Solo paráfrasis + cita ≤15 palabras |
| Estándar | — | HER-STD-0007 |
| Actualización | Estática (obra publicada) | Continua (noticias, estudios) |

## Regla de gobierno

Toda entrada nueva debe cumplir HER-STD-0007. Antes de commitear:

```bash
python3 scripts/validate_observatorio.py
```

## Entradas actuales

- `2026-08-as-com-abel-marin-plantilla-testamento.md` — error común en
  testamentos (España), relevante para Cuadrante Congelado/Planeador.
- `2026-07-euronews-patrimonio-jovenes-europeos.md` — datos BCE/HFCS
  sobre patrimonio neto juvenil, contexto comparativo europeo.

## Cómo se genera una entrada nueva

1. Buscar/leer la fuente (web_search + web_fetch si el sitio lo
   permite).
2. Completar el frontmatter de HER-STD-0007.
3. Escribir Resumen (paráfrasis), Datos clave (cifras con atribución),
   Relevancia patrimonial (conexión con el resto del conocimiento
   HEREDITARIA™) — nunca copiar párrafos completos del original.
4. Ejecutar `validate_observatorio.py` antes de commitear.

Este proceso requiere criterio editorial humano o de IA en cada
entrada — no es automatizable con un script de scraping, precisamente
porque la paráfrasis y la selección de relevancia son lo que evita
infringir derechos de autor.
