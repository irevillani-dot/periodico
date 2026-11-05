// Texto ORIGINAL de la autora con las correcciones como control de cambios y comentarios.
// Marcado: {-borrado-} {+insertado+} {/cursiva añadida/} ⟦n⟧…⟦/n⟧ = comentario n sobre ese tramo.
// *texto* va en cursiva en cualquier tramo (sin cambios, borrado o insertado).
// Uso: node build_tracked.js <original.md> <salida.docx> <salida_limpia.md> <marcado.json>
// Necesita el paquete npm «docx» (npm install docx@9.8.1).
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, InsertedTextRun, DeletedTextRun,
  CommentRangeStart, CommentRangeEnd, CommentReference, HeadingLevel,
  AlignmentType, Header, Footer, PageNumber,
} = require("docx");

const [, , originalPath, outDocx, outMd, specPath] = process.argv;
const AUTHOR = "Corrección";
const DATE = new Date().toISOString().slice(0, 19) + "Z";
const LANG = { value: "es-ES" };

// Bloques y comentarios desde un JSON: {"blocks": [[tipo, texto], ...], "comments": {"1": "..."}}
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
const comments = spec.comments;
const blocks = spec.blocks;

const TOKEN = /(\{-[\s\S]*?-\}|\{\+[\s\S]*?\+\}|\{\/[\s\S]*?\/\}|⟦\/?\d+⟧)/;
const tokens = (s) => s.split(TOKEN).filter(Boolean);
const pieces = (s) => s.split(/(\*[^*]+\*)/).filter(Boolean)
  .map((p) => (/^\*[^*]+\*$/.test(p) ? [p.slice(1, -1), true] : [p, false]));

// Rechazar todo = original; aceptar todo = corregido.
function flatten(s, mode) {
  return tokens(s).map((t) => {
    if (t.startsWith("{-")) return mode === "reject" ? t.slice(2, -2) : "";
    if (t.startsWith("{+")) return mode === "accept" ? t.slice(2, -2) : "";
    if (t.startsWith("{/")) return mode === "accept" ? `*${t.slice(2, -2)}*` : t.slice(2, -2);
    if (t.startsWith("⟦")) return "";
    return t;
  }).join("");
}

let rev = 100;
const change = () => ({ id: rev++, author: AUTHOR, date: DATE });

function runs(s) {
  const out = [];
  for (const t of tokens(s)) {
    let m;
    if (t.startsWith("{-")) {
      for (const [text, italics] of pieces(t.slice(2, -2))) out.push(new DeletedTextRun({ text, italics, ...change() }));
    } else if (t.startsWith("{+")) {
      for (const [text, italics] of pieces(t.slice(2, -2))) out.push(new InsertedTextRun({ text, italics, ...change() }));
    } else if (t.startsWith("{/")) {
      out.push(new TextRun({ text: t.slice(2, -2), italics: true, revision: { ...change(), italics: false } }));
    } else if ((m = t.match(/^⟦(\d+)⟧$/))) {
      out.push(new CommentRangeStart(+m[1]));
    } else if ((m = t.match(/^⟦\/(\d+)⟧$/))) {
      out.push(new CommentRangeEnd(+m[1]));
      out.push(new TextRun({ children: [new CommentReference(+m[1])] }));
    } else {
      for (const [text, italics] of pieces(t)) out.push(new TextRun({ text, italics }));
    }
  }
  return out;
}

const children = blocks.map(([kind, s]) => {
  if (kind === "title") return new Paragraph({ heading: HeadingLevel.TITLE, children: runs(s) });
  if (kind === "h2") return new Paragraph({ heading: HeadingLevel.HEADING_2, children: runs(s) });
  if (kind === "subtitle") return new Paragraph({ style: "Subtitulo", children: runs(s) });
  return new Paragraph({ style: "Cuerpo", children: runs(s) });
});

// Comprobación: rechazando todos los cambios se obtiene exactamente el original.
const norm = (s) => s.split("\n").map((l) => l.trim()).filter(Boolean)
  .map((l) => l.replace(/^#+\s*/, "").replace(/^\*\*(.*)\*\*$/, "$1")).join("\n");
const original = norm(fs.readFileSync(originalPath, "utf8"));
const rejected = blocks.map(([, s]) => flatten(s, "reject")).join("\n");
if (rejected !== original) {
  const a = rejected.split("\n"), b = original.split("\n");
  a.forEach((l, i) => { if (l !== b[i]) console.error(`DIFERENCIA en bloque ${i}:\n  marcado: ${l}\n  original: ${b[i]}`); });
  process.exit(1);
}
console.log("OK: rechazando todos los cambios se obtiene el original exacto");

// Versión con todos los cambios aceptados, en markdown (los bloques vacíos se omiten).
const md = blocks.map(([kind, s]) => {
  const it = flatten(s, "accept").trim();
  if (!it) return null;
  if (kind === "title") return `# ${it}`;
  if (kind === "h2") return `## ${it}`;
  if (kind === "subtitle") return `**${it}**`;
  return it;
}).filter(Boolean).join("\n\n") + "\n";
fs.writeFileSync(outMd, md);

const commentOpts = Object.entries(comments).map(([id, text]) => ({
  id: +id, author: AUTHOR, initials: "C", date: new Date(DATE),
  children: [new Paragraph({ children: [new TextRun(text)] })],
}));

const doc = new Document({
  creator: AUTHOR,
  title: flatten(blocks[0][1], "reject") + " — correcciones",
  features: { trackRevisions: true },
  comments: { children: commentOpts },
  styles: {
    default: { document: { run: { font: "Georgia", size: 23, language: LANG } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: "Georgia", size: 44, bold: true, color: "111111" },
        paragraph: { spacing: { after: 200 } } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: "Arial", size: 26, bold: true, color: "1F3864" },
        paragraph: { spacing: { before: 360, after: 120 }, outlineLevel: 1, keepNext: true } },
      { id: "Subtitulo", name: "Subtítulo", basedOn: "Normal", next: "Normal",
        run: { font: "Georgia", size: 27, bold: true, color: "444444" },
        paragraph: { spacing: { after: 280, line: 300 } } },
      { id: "Cuerpo", name: "Cuerpo", basedOn: "Normal", next: "Cuerpo",
        run: { font: "Georgia", size: 23 },
        paragraph: { spacing: { after: 180, line: 312 } } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 },
      margin: { top: 1418, bottom: 1418, left: 1587, right: 1587 } } },
    headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.RIGHT,
      children: [new TextRun({ text: "Texto original · correcciones con control de cambios", font: "Arial", size: 16, color: "888888" })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ children: ["Página ", PageNumber.CURRENT, " de ", PageNumber.TOTAL_PAGES], font: "Arial", size: 16, color: "888888" })] })] }) },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outDocx, buf);
  console.log(`OK ${outDocx} (${buf.length} bytes), ${Object.keys(comments).length} comentarios, ${rev - 100} cambios`);
});
