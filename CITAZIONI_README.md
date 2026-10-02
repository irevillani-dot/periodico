# citazioni.py: estrattore di citazioni

Programma locale (Python 3, nessuna API, nessuna dipendenza obbligatoria) che legge articoli e altre fonti ed estrae le citazioni utili per costruire un pezzo nello stile di *Página Internacional*.

## Uso

```bash
python3 citazioni.py FONTI... -t "parole chiave della storia" [opzioni]
```

Le fonti possono essere file `.pdf`, `.txt`, `.md`, `.html`, intere cartelle o URL.

| Opzione | Effetto |
|---|---|
| `-t "Etiopía Tigray Eritrea"` | Tema: le citazioni pertinenti salgono in classifica |
| `-n 15` | Mostra solo le 15 più rilevanti |
| `-o citazioni.md` | Salva il report in Markdown |
| `--csv citazioni.csv` | Salva anche un foglio apribile con Excel |
| `--solo-dirette` | Solo frasi tra virgolette |
| `--min 3` | Lunghezza minima (in parole) di una citazione diretta |
| `--senza-contesto` | Non riporta la frase completa in cui compare la citazione |

Esempio:

```bash
python3 citazioni.py fonti_groenlandia/ https://www.esempio.com/articolo \
    -t "Groenlandia Trump acuerdo soberanía" -n 20 -o citazioni.md --csv citazioni.csv
```

## Cosa produce

Per ogni citazione:
- **testo**: virgolettato diretto («», “”, "") oppure frase attribuita («según Reuters…», «secondo il NYT…», «according to…»);
- **chi parla**: individuato dai verbi di attribuzione (*dice, subraya, juzga, ironizó, said, warns…*). Se l'autore è stato dedotto dalla frase precedente compare l'avviso *(prob., frase precedente)*; se non è stato trovato, *da verificare*;
- **uso suggerito** secondo lo schema dell'articolo: `tesi/analisi`, `dato`, `versione ufficiale`, `contrasto`, `rischio/futuro`, `possibile chiusura`;
- **punteggio**: pertinenza al tema, centralità nella fonte, presenza dell'autore, lunghezza adatta, presenza di cifre.

In testa al report c'è l'elenco delle **voci presenti**, utile per verificare la varietà delle fonti (stampa locale, esperti, versione ufficiale).

## PDF

Usa `pypdf` se è installato (`pip install pypdf`), altrimenti `pdftotext` (poppler: `brew install poppler` / `apt install poppler-utils`).

## Limiti

L'attribuzione è euristica: **verifica sempre chi parla sulla fonte originale** prima di pubblicare, soprattutto per le voci segnate *prob.* o *da verificare*.
