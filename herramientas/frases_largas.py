#!/usr/bin/env python3
"""Señala las frases del cuerpo que pasan de un número de palabras (30 por defecto).

Uso: python3 herramientas/frases_largas.py nombre.md [--max 30]
Excluye titular (# ), subtítulo (**…**), ladillos (## ) y comentarios (<!--).
"""
import argparse
import re
import sys

PALABRA = re.compile(r"[\wÀ-ÿ]+(?:[-'’][\wÀ-ÿ]+)*")
# Fin de frase: . ? ! seguidos de espacio, opcionalmente tras cierre de comillas.
FIN = re.compile(r"(?<=[.?!])[»”]?\s+(?=[«“¿¡(A-ZÁÉÍÓÚÑ])")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo")
    ap.add_argument("--max", type=int, default=30)
    a = ap.parse_args()

    largas = 0
    n = 0
    for linea in open(a.archivo, encoding="utf-8"):
        linea = linea.strip()
        if not linea or linea.startswith(("#", "<!--")) or re.fullmatch(r"\*\*.*\*\*", linea):
            continue
        n += 1
        for frase in FIN.split(linea):
            k = len(PALABRA.findall(frase))
            if k > a.max:
                largas += 1
                print(f"§{n:<2d} · {k} palabras · {frase[:120]}{'…' if len(frase) > 120 else ''}")
    print(f"\n{largas} frases de más de {a.max} palabras")
    return 0


if __name__ == "__main__":
    sys.exit(main())
