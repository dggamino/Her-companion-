#!/usr/bin/env python3
"""
HER-STD-0007 — Validador de entradas del Observatorio.

Verifica:
1. Frontmatter con campos obligatorios presentes.
2. Ninguna secuencia de más de 15 palabras se repite tal cual desde
   afuera es imposible de verificar sin el original, así que esta
   heurística solo detecta bloques de texto sospechosamente largos
   dentro del propio archivo (posible copia-pega accidental de un
   párrafo entero) y advierte para revisión humana.

Uso:
    python3 scripts/validate_observatorio.py
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OBS_DIR = REPO_ROOT / "knowledge" / "observatorio"

REQUIRED_FIELDS = [
    "fuente_tipo", "medio", "fecha_publicacion", "url",
    "fuente_conocimiento_tier", "keywords_rfc001",
]

REQUIRED_SECTIONS = ["## Resumen", "## Datos clave", "## Relevancia patrimonial"]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw = parts[1]
    body = parts[2]
    fields = {}
    for line in fm_raw.strip().splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fields[k.strip()] = v.strip()
    return fields, body


def check_long_verbatim_blocks(body, max_words=15):
    warnings = []
    for para in body.split("\n\n"):
        words = re.findall(r"\S+", para)
        # crude heuristic: a very long unbroken sentence-like block
        # inside quotes is suspicious
        quoted = re.findall(r'"([^"]{0,500})"', para)
        for q in quoted:
            qwords = re.findall(r"\S+", q)
            if len(qwords) > max_words:
                warnings.append(
                    f"Cita entre comillas con {len(qwords)} palabras "
                    f"(límite {max_words}): \"{q[:60]}...\""
                )
    return warnings


def validate_file(path):
    text = path.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    errors = []
    warnings = []

    for f in REQUIRED_FIELDS:
        if f not in fields or not fields[f].strip("[]' \""):
            if f == "keywords_rfc001" and f in fields:
                continue  # empty list is fine, just must exist
            errors.append(f"Falta campo obligatorio: {f}")

    for sec in REQUIRED_SECTIONS:
        if sec not in body:
            errors.append(f"Falta sección obligatoria: {sec}")

    warnings.extend(check_long_verbatim_blocks(body))

    return errors, warnings


def main():
    if not OBS_DIR.exists():
        print(f"No existe {OBS_DIR}")
        sys.exit(1)

    files = sorted(OBS_DIR.rglob("*.md"))
    files = [f for f in files if f.name not in ("README.md", "INDEX.md")]

    if not files:
        print("Sin entradas en observatorio/ todavía.")
        sys.exit(0)

    total_errors = 0
    for f in files:
        errors, warnings = validate_file(f)
        rel = f.relative_to(REPO_ROOT)
        if errors:
            print(f"❌ {rel}")
            for e in errors:
                print(f"   ERROR: {e}")
            total_errors += len(errors)
        elif warnings:
            print(f"⚠️  {rel}")
        else:
            print(f"✅ {rel}")
        for w in warnings:
            print(f"   AVISO: {w}")

    print(f"\n{len(files)} archivos revisados, {total_errors} errores.")
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
