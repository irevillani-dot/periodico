#!/usr/bin/env python3
"""Porcentaje de palabras entre comillas en un artículo (objetivo de la casa: 15-20 %).

Uso: python3 herramientas/porcentaje_citas.py articulo.md [--min 15 --max 20] [--limite 900]

Cuenta las palabras del cuerpo del texto (sin titular «# », subtítulo **…**
ni ladillos «## ») y las que van entre comillas latinas « » o inglesas “ ”
(las citas anidadas cuentan una sola vez, dentro de la exterior).
"""
import argparse
import re
import sys

PALABRA = re.compile(r"[\wÀ-ÿ]+(?:[-'’][\wÀ-ÿ]+)*")


def palabras(texto):
    return PALABRA.findall(texto)


def bloques_cuerpo(lineas):
    for linea in lineas:
        l = linea.strip()
        if not l or l.startswith("#") or l.startswith("<!--"):
            continue
        if l.startswith("**") and l.endswith("**"):
            continue
        yield l


def citas(texto):
    """Devuelve los tramos entre comillas exteriores y avisa de las que no cierran."""
    tramos, pila, inicio = [], [], None
    pares = {"«": "»", "“": "”"}
    for i, c in enumerate(texto):
        if c in pares:
            if not pila:
                inicio = i
            pila.append(pares[c])
        elif pila and c == pila[-1]:
            pila.pop()
            if not pila:
                tramos.append(texto[inicio + 1:i])
    return tramos, bool(pila)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivo")
    ap.add_argument("--min", type=float, default=15)
    ap.add_argument("--max", type=float, default=20)
    ap.add_argument("--limite", type=int, default=900, help="máximo de palabras del cuerpo")
    a = ap.parse_args()

    lineas = open(a.archivo, encoding="utf-8").read().split("\n")
    total = citadas = 0
    todas, sin_cerrar = [], []
    for n, bloque in enumerate(bloques_cuerpo(lineas), 1):
        total += len(palabras(bloque))
        tramos, abierta = citas(bloque)
        if abierta:
            sin_cerrar.append(n)
        for t in tramos:
            k = len(palabras(t))
            citadas += k
            todas.append((k, n, t))

    pct = 100 * citadas / total if total else 0
    completo = sum(len(palabras(l.lstrip("#").strip("*"))) for l in lineas if not l.strip().startswith("<!--"))
    print(f"Cuerpo: {total} palabras (con titular, subtítulo y ladillos: {completo})")
    if total > a.limite:
        print(f"EXTENSIÓN: sobran {total - a.limite} palabras para el límite de {a.limite}")
    else:
        print(f"EXTENSIÓN: dentro del límite de {a.limite}")
    print(f"Entre comillas: {citadas} palabras · {pct:.1f} %")
    lo, hi = a.min * total / 100, a.max * total / 100
    if pct < a.min:
        print(f"POR DEBAJO del {a.min:g}-{a.max:g} %: faltan unas {round(lo - citadas)} palabras citadas")
    elif pct > a.max:
        print(f"POR ENCIMA del {a.min:g}-{a.max:g} %: sobran unas {round(citadas - hi)} palabras citadas")
    else:
        print(f"DENTRO del {a.min:g}-{a.max:g} %")
    if sin_cerrar:
        print(f"AVISO: comillas sin cerrar en los párrafos {sin_cerrar}")
    print(f"\n{len(todas)} citas, de mayor a menor (palabras · párrafo · texto):")
    for k, n, t in sorted(todas, reverse=True):
        print(f"  {k:3d} · §{n:<2d} · «{t[:90]}{'…' if len(t) > 90 else ''}»")


if __name__ == "__main__":
    sys.exit(main())
