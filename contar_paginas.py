#!/usr/bin/env python3
"""
contar_paginas.py
------------------
Script único para Termux que analiza uno o varios archivos PDF y/o ePub
y reporta:
  - PDF: número real de páginas (metadato del archivo)
  - ePub: conteo de palabras y páginas ESTIMADAS (no existe página fija
    en ePub; se estima con 250 y 300 palabras/página, estándar editorial)

USO:
    python3 contar_paginas.py archivo1.pdf archivo2.epub ...
"""

import sys
import os


def analizar_pdf(ruta):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("  [ERROR] Falta pypdf. Instala con: pip install pypdf")
        return

    try:
        r = PdfReader(ruta)
        n = len(r.pages)
        print(f"  Tipo: PDF")
        print(f"  Páginas reales: {n}")
    except Exception as e:
        print(f"  [ERROR] No se pudo leer el PDF: {e}")


def analizar_epub(ruta):
    try:
        from ebooklib import epub
        import ebooklib
        from bs4 import BeautifulSoup
    except ImportError:
        print("  [ERROR] Falta ebooklib/beautifulsoup4.")
        print("  Instala con: pip install ebooklib beautifulsoup4")
        return

    try:
        book = epub.read_epub(ruta, options={"ignore_ncx": True})
        total_words = 0
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_content(), "html.parser")
                total_words += len(soup.get_text().split())

        paginas_250 = round(total_words / 250)
        paginas_300 = round(total_words / 300)

        print(f"  Tipo: ePub")
        print(f"  Palabras totales: {total_words:,}")
        print(f"  Páginas estimadas (250 palabras/pág): {paginas_250}")
        print(f"  Páginas estimadas (300 palabras/pág): {paginas_300}")
        print(f"  Nota: ePub no tiene páginas fijas; el conteo real varía")
        print(f"        según tamaño de fuente y pantalla del lector.")
    except Exception as e:
        print(f"  [ERROR] No se pudo leer el ePub: {e}")


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 contar_paginas.py archivo1.pdf archivo2.epub ...")
        sys.exit(1)

    archivos = sys.argv[1:]
    print("=" * 60)
    print("ANÁLISIS DE PÁGINAS — PDF / ePub")
    print("=" * 60)

    for ruta in archivos:
        print(f"\nArchivo: {os.path.basename(ruta)}")
        print("-" * 60)

        if not os.path.isfile(ruta):
            print("  [ERROR] Archivo no encontrado.")
            continue

        ext = os.path.splitext(ruta)[1].lower()

        if ext == ".pdf":
            analizar_pdf(ruta)
        elif ext == ".epub":
            analizar_epub(ruta)
        else:
            print(f"  [OMITIDO] Extensión no soportada: {ext}")

    print("\n" + "=" * 60)
    print("Listo.")
    print("=" * 60)


if __name__ == "__main__":
    main()
