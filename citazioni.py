#!/usr/bin/env python3
"""
citazioni.py — Estrae le citazioni rilevanti da articoli e altre fonti.

Funziona in locale, senza API e solo con la libreria standard di Python.
Per i PDF usa `pypdf` se è installato, altrimenti `pdftotext` (poppler).

Formati accettati: .pdf, .txt, .md, .html/.htm, URL http(s) e cartelle
(vengono letti tutti i file supportati che contengono).

Esempi:
    python3 citazioni.py articolo.pdf altro.html -t "Etiopia Tigray TPLF Eritrea"
    python3 citazioni.py fonti/ -t "Groenlandia Trump" -o citazioni.md --csv citazioni.csv
    python3 citazioni.py https://esempio.com/notizia -t "Suiza neutralidad" --min 3

Cosa estrae:
  * citazioni dirette tra «», “”, "" e ‘’ (in qualsiasi lingua);
  * frasi attribuite senza virgolette («según The Economist…», «secondo Reuters…»).
Per ciascuna prova a individuare chi parla, le assegna un punteggio di
rilevanza rispetto al tema e suggerisce dove può servire nell'articolo
(tesi, dato, contrasto, voce locale, chiusura).
"""

import argparse
import csv
import html
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.request
from dataclasses import dataclass, field

# ---------------------------------------------------------------------------
# Lessico (spagnolo, italiano, inglese, francese, tedesco)
# ---------------------------------------------------------------------------

VERBI_ATTRIBUZIONE = """
dijo dice afirma afirmó asegura aseguró explica explicó subraya subrayó apunta apuntó
señala señaló recuerda recordó juzga juzgó advierte advirtió sostiene sostuvo resume resumió
añade añadió reconoce reconocía reconoció declaró declara ironizó ironiza zanjó expresó
admite admitió destaca destacó recalcó critica criticó calificó concluye concluyó recoge
informó informa considera consideró predice predijo estima estimó opina opinó
disse dice afferma affermato spiega spiegato sottolinea sottolineato ricorda ricordato
avverte avvertito sostiene sostenuto aggiunge aggiunto riconosce dichiara dichiarato
conclude osserva osservato commenta commentato denuncia denunciato
said says say told tells argues argued explains explained notes noted warns warned
adds added claims claimed reckons reckoned insists insisted admits admitted predicts
predicted recalls recalled concludes concluded declared declares according
dit déclare déclaré affirme affirmé explique expliqué souligne souligné estime ajoute
sagte sagt erklärt erklärte betont betonte warnt warnte meint meinte
""".split()

INTRO_FONTE = [
    r"según", r"segun", r"de acuerdo con", r"en palabras de", r"a juicio de",
    r"secondo", r"a detta di", r"according to", r"selon", r"laut", r"zufolge",
]

PAROLE_VUOTE = set("""
el la los las un una unos unas de del al a en y o que por para con sin sobre como
más mas pero su sus se lo le les es son fue ha han este esta estos estas ese esa
il lo gli i le uno una di da in con su per tra fra e o che non è sono come più
the a an of to in on for and or that is are was were be by with as at from it its this
le la les un une des de du et ou que qui est sont dans pour par sur avec
der die das ein eine und oder ist sind mit von zu im den dem
""".split())

# Indizi per suggerire il ruolo nel pezzo (vedi schema Página Internacional)
INDIZI_CONTRASTO = r"\b(pero|sin embargo|en realidad|ma|tuttavia|in realtà|but|yet|however|in fact|mais|aber)\b"
INDIZI_FUTURO = r"\b(podría|podrá|amenaza|riesgo|si no|tarde o temprano|potrebbe|rischio|could|may|might|threat|risk|pourrait|könnte)\b"
INDIZI_IRONIA = r"(\?|¡|!|enhorabuena|ironiz|teatro|absurdo|simplemente)"
INDIZI_UFFICIALE = r"\b(gobierno|ministr|president|portavoz|secretari|governo|portavoce|government|minister|spokes|official|gouvernement|regierung)\w*"
INDIZI_ANALISI = r"\b(economist|times|journal|post|guardian|monde|stampa|reuters|analista|experto|profesor|historiador|esperto|analyst|expert|professor|crisis group|think tank)\w*"

APERTURE = "«“\"‘"
CHIUSURE = {"«": "»", "“": "”", "\"": "\"", "‘": "’"}


# ---------------------------------------------------------------------------
# Lettura delle fonti
# ---------------------------------------------------------------------------

def leggi_pdf(percorso):
    try:
        import pypdf  # type: ignore
        lettore = pypdf.PdfReader(percorso)
        return "\n".join((p.extract_text() or "") for p in lettore.pages)
    except ImportError:
        pass
    if shutil.which("pdftotext"):
        out = subprocess.run(["pdftotext", percorso, "-"], capture_output=True, text=True)
        return out.stdout
    sys.exit("Per leggere i PDF installa `pypdf` (pip install pypdf) o `pdftotext` (poppler).")


class _EstrattoreHTML:
    """Estrazione minimale del testo da HTML senza dipendenze."""

    @staticmethod
    def testo(sorgente):
        sorgente = re.sub(r"(?is)<(script|style|nav|footer|header|aside|noscript)[^>]*>.*?</\1>", " ", sorgente)
        sorgente = re.sub(r"(?i)<\s*(br|/p|/div|/h\d|/li|/blockquote)\s*/?>", "\n\n", sorgente)
        sorgente = re.sub(r"<[^>]+>", " ", sorgente)
        return html.unescape(sorgente)


def leggi_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (citazioni.py)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        grezzo = r.read().decode(r.headers.get_content_charset() or "utf-8", errors="replace")
    return _EstrattoreHTML.testo(grezzo)


def leggi_fonte(fonte):
    if re.match(r"https?://", fonte):
        return leggi_url(fonte)
    est = os.path.splitext(fonte)[1].lower()
    if est == ".pdf":
        return leggi_pdf(fonte)
    with open(fonte, encoding="utf-8", errors="replace") as f:
        testo = f.read()
    if est in (".html", ".htm"):
        testo = _EstrattoreHTML.testo(testo)
    return testo


def espandi_fonti(voci):
    estensioni = {".pdf", ".txt", ".md", ".html", ".htm"}
    for v in voci:
        if os.path.isdir(v):
            for nome in sorted(os.listdir(v)):
                if os.path.splitext(nome)[1].lower() in estensioni:
                    yield os.path.join(v, nome)
        else:
            yield v


# ---------------------------------------------------------------------------
# Pulizia e segmentazione
# ---------------------------------------------------------------------------

def pulisci(testo):
    testo = unicodedata.normalize("NFC", testo).replace("\r", "")
    righe = []
    for r in testo.split("\n"):
        s = r.strip()
        # intestazioni/piè di pagina tipici dei PDF stampati dal browser
        if re.match(r"^https?://\S+\s+\d+/\d+$", s) or re.match(r"^\d{1,2}/\d{1,2}/\d{2,4},?\s+\d{1,2}:\d{2}", s):
            continue
        if re.fullmatch(r"(Subscribe|Menu|Save|Share|advertisement|Listen to this story|\d+:\d+ / \d+:\d+)", s, re.I):
            continue
        righe.append(s)
    testo = "\n".join(righe)
    testo = re.sub(r"(\w)-\n(\w)", r"\1\2", testo)          # parole spezzate a fine riga
    testo = re.sub(r"\n{2,}", " ", testo)               # segna i paragrafi
    testo = re.sub(r"\s*\n\s*", " ", testo)                  # unisce le righe
    testo = re.sub(r"[ \t]+", " ", testo)
    return [p.strip() for p in testo.split(" ") if p.strip()]


_FINE_FRASE = re.compile(r"(?<=[.!?…»”])\s+(?=[«“\"¿¡A-ZÁÉÍÓÚÀÈÌÒÙÄÖÜÑ])")


def frasi(paragrafo):
    # non spezza dentro le virgolette
    pezzi, buf, profondita = [], "", 0
    for parte in _FINE_FRASE.split(paragrafo):
        buf = f"{buf} {parte}".strip() if buf else parte
        profondita = buf.count("«") - buf.count("»") + buf.count("“") - buf.count("”")
        if profondita <= 0:
            pezzi.append(buf)
            buf = ""
    if buf:
        pezzi.append(buf)
    return pezzi


# ---------------------------------------------------------------------------
# Estrazione
# ---------------------------------------------------------------------------

@dataclass
class Citazione:
    fonte: str
    testo: str
    contesto: str
    tipo: str               # "diretta" | "attribuita"
    autore: str = ""
    punteggio: float = 0.0
    ruoli: list = field(default_factory=list)


_NOME = r"(?:[A-ZÁÉÍÓÚÀÈÌÒÙÄÖÜÑ][\w’'\.-]+(?:\s+(?:de|del|la|von|van|di|da|al|bin)?\s*[A-ZÁÉÍÓÚÀÈÌÒÙÄÖÜÑ][\w’'\.-]+){0,4})"
_RE_VERBI = re.compile(r"\b(" + "|".join(map(re.escape, sorted(VERBI_ATTRIBUZIONE, key=len, reverse=True))) + r")\b", re.I)
_RE_INTRO = re.compile(r"\b(?i:(" + "|".join(INTRO_FONTE) + r"))\s+(?:el |la |los |las |il |lo |le |der |die )?(" + _NOME + ")")
_NON_NOMI = {"En", "In", "Pero", "Ma", "But", "Y", "E", "Según", "Secondo", "Si", "No", "Para", "Por", "Sin", "Embargo"}
_ARTICOLI = {"El", "La", "Los", "Las", "Il", "Lo", "The", "Le", "Der", "Die", "Das"}
_DESCRITTORE = r"[\s,]*((?:a|an|un|una|uno|une|ein|eine)\s+(?:[\w’'-]+\s+){0,3}[\w’'-]+)"


def trova_virgolettati(frase):
    risultati, i = [], 0
    while i < len(frase):
        c = frase[i]
        if c in APERTURE:
            chiusura = CHIUSURE[c]
            j, livello = i + 1, 1
            while j < len(frase):
                if c != chiusura and frase[j] == c:
                    livello += 1
                elif frase[j] == chiusura:
                    livello -= 1
                    if livello == 0:
                        break
                j += 1
            if j < len(frase):
                risultati.append((i, j, frase[i + 1:j].strip()))
                i = j
        i += 1
    return risultati


def trova_autore(frase, fuori=None):
    """Cerca chi parla: nome vicino a un verbo di attribuzione o a 'según/secondo…'."""
    testo = fuori if fuori is not None else frase
    m = _RE_INTRO.search(testo)
    if m:
        return pulisci_nome(m.group(2))
    candidati = []
    for v in _RE_VERBI.finditer(testo):
        # nome subito dopo il verbo, anche preceduto da una qualifica: "ironizó el profesor … Peter Jakobsen"
        segmento = re.split(r"[,;:…]", testo[v.end():v.end() + 120])[0]
        nomi = list(re.finditer(_NOME, segmento))
        dopo = nomi[-1] if nomi and re.match(r"[\s]*(?:[a-záéíóúàèìòùäöüñ’'-]+\s+|" + _NOME + r"\s+){0,12}$", segmento[:nomi[-1].start()]) else None
        # nome prima del verbo, ammettendo pronomi atoni in mezzo: "McFaul lo resumió"
        prima = re.search("(" + _NOME + r")[\s,]*(?:–[^–]*–\s*)?(?:(?:lo|la|le|se|l’|ha|had|has|lo ha|si è)\s+){0,2}$", testo[:v.start()])
        for mm, dist in ((dopo, 0), (prima, 1)):
            if mm:
                nome = pulisci_nome(mm.group(1) if mm.re.groups else mm.group(0))
                if nome:
                    candidati.append((dist, nome))
    if not candidati:
        # descrizione anonima dopo il verbo: "says a well-connected observer", "dice un diplomático"
        for v in _RE_VERBI.finditer(testo):
            d = re.match(_DESCRITTORE + r"\s*[.,;]?\s*$", testo[v.end():].replace("…", "").strip() and " " + testo[v.end():].split("…")[0])
            if d:
                candidati.append((2, d.group(1).strip()))
            p = re.search(r"\b((?:an?|un|una|une|ein|eine)\s+(?:[\w’'-]+\s+){0,2}[\w’'-]+)\s*$", testo[:v.start()])
            if p:
                candidati.append((3, p.group(1).strip()))
    if candidati:
        candidati.sort(key=lambda x: (x[0], -len(x[1])))
        return candidati[0][1]
    # testate giornalistiche in corsivo/maiuscolo citate nella frase
    m = re.search(r"\b(The [A-Z]\w+(?: [A-Z]\w+)*|Le Temps|Le Monde|El País|Il Post|La Stampa|Reuters|Al Jazeera|NZZ|Neue Zürcher Zeitung)\b", testo)
    return m.group(1) if m else ""


def pulisci_nome(nome):
    parole = nome.strip(" ,.;:").split()
    while parole and (parole[0] in _NON_NOMI or (parole[0] in _ARTICOLI and len(parole) == 1)):
        parole.pop(0)
    nome = " ".join(parole)
    if len(nome) < 3 or nome.lower() in VERBI_ATTRIBUZIONE:
        return ""
    return nome


def estrai(fonte, paragrafi, min_parole):
    trovate = []
    for par in paragrafi:
        ultimo_autore = ""
        for frase in frasi(par):
            virg = [v for v in trova_virgolettati(frase) if len(v[2].split()) >= min_parole]
            if virg:
                fuori = frase
                for a, b, _ in reversed(virg):
                    fuori = fuori[:a] + " … " + fuori[b + 1:]
                autore = trova_autore(frase, fuori)
                if not autore and ultimo_autore:
                    autore = f"{ultimo_autore} (prob., frase precedente)"
                ultimo_autore = autore.split(" (prob.")[0] or ultimo_autore
                for _, _, testo in virg:
                    trovate.append(Citazione(fonte, testo, frase, "diretta", autore))
            elif _RE_INTRO.search(frase) or (_RE_VERBI.search(frase) and len(frase.split()) >= 8):
                autore = trova_autore(frase)
                if autore:
                    ultimo_autore = autore
                    trovate.append(Citazione(fonte, frase, frase, "attribuita", autore))
    return trovate


# ---------------------------------------------------------------------------
# Punteggio e ruoli
# ---------------------------------------------------------------------------

def normalizza(parola):
    parola = unicodedata.normalize("NFD", parola.lower())
    return "".join(c for c in parola if unicodedata.category(c) != "Mn")


def parole_chiave(testo):
    return [normalizza(p) for p in re.findall(r"\w+", testo) if normalizza(p) not in PAROLE_VUOTE and len(p) > 2]


def valuta(c, tema, freq_doc):
    parole = parole_chiave(c.contesto)
    punteggio = 0.0
    # 1. pertinenza al tema (radice di 5 lettere per tollerare plurali/flessioni)
    if tema:
        radici = {t[:5] for t in tema}
        punteggio += 3.0 * sum(1 for p in set(parole) if p[:5] in radici)
    # 2. centralità nel documento: parole frequenti nella fonte
    punteggio += sum(min(freq_doc.get(p, 0), 6) for p in set(parole)) / max(len(set(parole)), 1)
    # 3. qualità della citazione
    n = len(c.testo.split())
    punteggio += 2.0 if c.tipo == "diretta" else 0.5
    punteggio += 2.0 if c.autore else -1.0
    punteggio += 1.5 if 6 <= n <= 40 else (0 if n < 6 else -1.0)
    if re.search(r"\d", c.contesto):
        punteggio += 1.0
    c.punteggio = round(punteggio, 1)

    # ruoli suggeriti
    ruoli, ctx, aut = [], c.contesto.lower(), c.autore.lower()
    if re.search(INDIZI_ANALISI, ctx + " " + aut):
        ruoli.append("tesi/analisi")
    if re.search(r"\d+[\d.,]*\s*(%|por ciento|per cento|percent|millones|milioni|million|mil |muertos|morti|dead)", ctx):
        ruoli.append("dato")
    if re.search(INDIZI_UFFICIALE, ctx):
        ruoli.append("versione ufficiale")
    if re.search(INDIZI_CONTRASTO, ctx):
        ruoli.append("contrasto")
    if re.search(INDIZI_FUTURO, ctx):
        ruoli.append("rischio/futuro")
    if c.tipo == "diretta" and (re.search(INDIZI_IRONIA, c.testo.lower()) or n <= 12):
        ruoli.append("possibile chiusura")
    c.ruoli = ruoli or ["contesto"]


def deduplica(citazioni):
    viste, uniche = set(), []
    for c in citazioni:
        chiave = normalizza(c.testo)[:80]
        if chiave not in viste:
            viste.add(chiave)
            uniche.append(c)
    return uniche


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def scrivi_markdown(citazioni, tema_testo, contesto):
    righe = ["# Citazioni estratte", ""]
    if tema_testo:
        righe += [f"**Tema:** {tema_testo}", ""]
    righe += [f"Totale: {len(citazioni)} citazioni, ordinate per rilevanza.", ""]
    autori = {}
    for c in citazioni:
        if c.autore:
            autori.setdefault(c.autore, 0)
            autori[c.autore] += 1
    if autori:
        righe += ["## Voci presenti", ""]
        righe += [f"- {a} ({n})" for a, n in sorted(autori.items(), key=lambda x: -x[1])]
        righe.append("")
    righe += ["## Citazioni", ""]
    for i, c in enumerate(citazioni, 1):
        apice = f"«{c.testo}»" if c.tipo == "diretta" else c.testo
        righe.append(f"### {i}. {apice}")
        righe.append("")
        righe.append(f"- **Chi parla:** {c.autore or '— (da verificare)'}")
        righe.append(f"- **Fonte:** {os.path.basename(c.fonte)} · {c.tipo} · punteggio {c.punteggio}")
        righe.append(f"- **Uso suggerito:** {', '.join(c.ruoli)}")
        if contesto and c.tipo == "diretta" and c.contesto != f"«{c.testo}»":
            righe.append(f"- **Contesto:** {c.contesto}")
        righe.append("")
    return "\n".join(righe)


def scrivi_csv(citazioni, percorso):
    with open(percorso, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["punteggio", "citazione", "autore", "tipo", "uso_suggerito", "fonte", "contesto"])
        for c in citazioni:
            w.writerow([c.punteggio, c.testo, c.autore, c.tipo, "; ".join(c.ruoli), c.fonte, c.contesto])


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Estrae citazioni rilevanti da articoli e altre fonti.")
    ap.add_argument("fonti", nargs="+", help="file (.pdf .txt .md .html), cartelle o URL")
    ap.add_argument("-t", "--tema", default="", help="parole chiave della storia, es. \"Etiopia Tigray Eritrea\"")
    ap.add_argument("-n", "--max", type=int, default=0, help="numero massimo di citazioni (0 = tutte)")
    ap.add_argument("--min", type=int, default=4, help="parole minime di una citazione diretta (default 4)")
    ap.add_argument("--solo-dirette", action="store_true", help="esclude le frasi attribuite senza virgolette")
    ap.add_argument("--senza-contesto", action="store_true", help="non mostra la frase completa")
    ap.add_argument("-o", "--output", help="salva il report Markdown in questo file")
    ap.add_argument("--csv", help="salva anche un CSV (apribile con Excel)")
    args = ap.parse_args()

    tema = parole_chiave(args.tema)
    tutte = []
    for fonte in espandi_fonti(args.fonti):
        try:
            paragrafi = pulisci(leggi_fonte(fonte))
        except Exception as e:  # noqa: BLE001
            print(f"[!] Impossibile leggere {fonte}: {e}", file=sys.stderr)
            continue
        freq = {}
        for p in parole_chiave(" ".join(paragrafi)):
            freq[p] = freq.get(p, 0) + 1
        citazioni = estrai(fonte, paragrafi, args.min)
        for c in citazioni:
            valuta(c, tema, freq)
        print(f"[+] {os.path.basename(fonte)}: {len(citazioni)} citazioni", file=sys.stderr)
        tutte.extend(citazioni)

    if args.solo_dirette:
        tutte = [c for c in tutte if c.tipo == "diretta"]
    tutte = deduplica(sorted(tutte, key=lambda c: -c.punteggio))
    if args.max:
        tutte = tutte[: args.max]

    report = scrivi_markdown(tutte, args.tema, not args.senza_contesto)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"[✓] Report salvato in {args.output}", file=sys.stderr)
    else:
        print(report)
    if args.csv:
        scrivi_csv(tutte, args.csv)
        print(f"[✓] CSV salvato in {args.csv}", file=sys.stderr)


if __name__ == "__main__":
    main()
