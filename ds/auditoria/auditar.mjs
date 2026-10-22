// Auditoria da Fase 1 do Jeff DS no site.
//
// Abre cada página em 390, 768 e 1440px, confere quais peças de
// pecas.json existem nela, fotografa cada peça e a página inteira,
// mede o contraste do texto e lista as classes que nenhuma peça
// cobre. O resultado vai para resultado.json, e os documentos em
// ds/ são escritos a partir dele (ver montar.py).
//
// Uso, com o site servido em http://localhost:4173:
//   npm i playwright-core
//   node ds/auditoria/auditar.mjs <caminho do Chrome>
import { chromium } from "playwright-core";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const raiz = path.resolve(aqui, "../..");
const BASE = process.env.BASE || "http://localhost:4173";
const LARGURAS = [1440, 390, 768]; // a 1440 vai primeiro: é ela que fixa a matriz
const PAGINAS = [
  { id: "home", url: "/index.html", nome: "Home" },
  { id: "processo", url: "/case-processo.html", nome: "Processo com IA" },
  { id: "omnichat", url: "/case-omnichat.html", nome: "Omnichat" },
  { id: "inpulse", url: "/case-inpulse.html", nome: "Inpulse" },
  { id: "mapa", url: "/case-mapa-experiencia.html", nome: "Mapa de experiência" },
  { id: "manifesto", url: "/manifesto/index.html", nome: "Manifesto", foraDaVersao: true },
];
const pecas = JSON.parse(fs.readFileSync(path.join(aqui, "pecas.json"), "utf8"));
const slug = (s) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

const saida = path.join(raiz, "ds/capturas");
for (const l of LARGURAS) fs.mkdirSync(path.join(saida, String(l)), { recursive: true });
fs.mkdirSync(path.join(saida, "paginas"), { recursive: true });

const navegador = await chromium.launch({ executablePath: process.argv[2] });
const resultado = { geradoEm: new Date().toISOString(), larguras: LARGURAS, paginas: PAGINAS.map(({ id, nome, foraDaVersao }) => ({ id, nome, foraDaVersao: !!foraDaVersao })), matriz: {}, capturas: {}, semPeca: {}, ocultas: {}, contraste: {}, verde: {}, falhas: [] };
for (const p of pecas) resultado.matriz[p.nome] = {};

/* Mostra tudo: o site esconde o que ainda não entrou na tela, e uma
   fotografia de elemento escondido sai em branco. Rola a página
   inteira devagar para os observadores dispararem e volta ao topo. */
async function acordar(page) {
  await page.addStyleTag({ content: "html{scroll-behavior:auto!important}" });
  const h = await page.evaluate(() => document.documentElement.scrollHeight);
  const passo = await page.evaluate(() => Math.round(innerHeight * 0.6));
  for (let y = 0; y < h; y += passo) {
    await page.evaluate((v) => scrollTo(0, v), y);
    await page.waitForTimeout(70);
  }
  await page.evaluate(() => {
    document.querySelectorAll("[data-revelar]").forEach((e) => e.classList.add("revelado"));
    scrollTo(0, 0);
  });
  await page.waitForTimeout(900);
}

const CONTRASTE = () => {
  const num = (s) => s.match(/[\d.]+/g).map(Number);
  const parse = (s) => { const [r, g, b, a = 1] = num(s); return { r, g, b, a }; };
  const sobre = (f, b) => ({ r: f.r * f.a + b.r * (1 - f.a), g: f.g * f.a + b.g * (1 - f.a), b: f.b * f.a + b.b * (1 - f.a), a: 1 });
  const lum = ({ r, g, b }) => { const c = [r, g, b].map((v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }); return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]; };
  const razao = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  const hex = ({ r, g, b }) => "#" + [r, g, b].map((v) => Math.round(v).toString(16).padStart(2, "0")).join("");
  const fundo = (el) => {
    const camadas = [];
    let imagem = false;
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.backgroundImage !== "none") imagem = true;
      const c = parse(cs.backgroundColor);
      if (c.a > 0) { camadas.push(c); if (c.a === 1) break; }
    }
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = camadas.length - 1; i >= 0; i--) base = sobre(camadas[i], base);
    return { cor: base, imagem };
  };
  const opac = (el) => { let o = 1; for (let e = el; e; e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; };
  const sig = (el) => { const c = [...el.classList][0]; return (el.tagName.toLowerCase() + (c ? "." + c : "")); };
  const visivel = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== "hidden" && cs.display !== "none"; };
  const grupos = new Map();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const vistos = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode;
    if (!t.textContent.trim()) continue;
    const el = t.parentElement;
    if (!el || vistos.has(el) || el.closest("script,style,svg,noscript") || !visivel(el)) continue;
    vistos.add(el);
    const cs = getComputedStyle(el);
    const o = opac(el);
    // Escondido (opacidade zero) não é lido por ninguém, e o que está
    // na barra do topo troca de fundo conforme a seção que passa
    // por trás, então não tem um par de cores fixo para medir.
    if (o < 0.05 || el.closest(".nav")) continue;
    const f = fundo(el);
    const texto = sobre({ ...parse(cs.color), a: parse(cs.color).a * o }, f.cor);
    const r = razao(texto, f.cor);
    const px = parseFloat(cs.fontSize);
    const grande = px >= 24 || (px >= 18.66 && parseInt(cs.fontWeight) >= 700);
    const meta = grande ? 3 : 4.5;
    if (r >= meta) continue;
    const k = [hex(texto), hex(f.cor), grande ? "G" : "P"].join("|");
    const g = grupos.get(k) || { texto: hex(texto), fundo: hex(f.cor), sobreImagem: f.imagem, grande, razao: Math.round(r * 100) / 100, meta, n: 0, exemplos: [] };
    g.n++;
    if (g.exemplos.length < 4) g.exemplos.push({ el: sig(el), px, texto: el.textContent.trim().slice(0, 40) });
    grupos.set(k, g);
  }
  return [...grupos.values()].sort((a, b) => b.n - a.n);
};

const VERDE = () => {
  const alvo = [[43, 238, 75], [196, 228, 201]];
  const perto = (s) => { const m = s.match(/[\d.]+/g); if (!m) return false; const [r, g, b, a = 1] = m.map(Number); return a > 0 && alvo.some(([x, y, z]) => Math.abs(x - r) + Math.abs(y - g) + Math.abs(z - b) < 12); };
  const sig = (el) => { const c = [...el.classList].slice(0, 2).join("."); return el.tagName.toLowerCase() + (c ? "." + c : ""); };
  const achados = new Map();
  const marca = (el, uso) => { const k = uso + "|" + sig(el); achados.set(k, { uso, el: sig(el), n: (achados.get(k)?.n || 0) + 1 }); };
  for (const el of document.body.querySelectorAll("*")) {
    const cs = getComputedStyle(el);
    if (cs.display === "none") continue;
    const tem = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    if (tem && perto(cs.color)) marca(el, "texto");
    if (parseFloat(cs.borderTopWidth) > 0 && perto(cs.borderTopColor)) marca(el, "borda");
    if (parseFloat(cs.borderBottomWidth) > 0 && perto(cs.borderBottomColor)) marca(el, "borda");
    if (cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) > 0 && perto(cs.outlineColor)) marca(el, "anel de foco ou contorno");
    if (perto(cs.backgroundColor)) marca(el, "preenchimento");
  }
  return [...achados.values()];
};

/* Uma classe está coberta quando todo elemento que a tem mora
   dentro de alguma peça (ou é a própria peça). O que sobra é o que
   o inventário ainda não nomeou. */
const CLASSES = (uniao) => {
  const m = {};
  for (const el of document.body.querySelectorAll("*")) {
    if (el.closest(uniao)) continue;
    for (const c of el.classList) m[c] = (m[c] || 0) + 1;
  }
  return m;
};

for (const pg of PAGINAS) {
  resultado.semPeca[pg.id] = {};
  for (const larg of LARGURAS) {
    const ctx = await navegador.newContext({ viewport: { width: larg, height: larg === 1440 ? 900 : larg === 768 ? 1024 : 844 }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    await page.goto(BASE + pg.url, { waitUntil: "networkidle" });
    await page.waitForTimeout(1200);
    await acordar(page);

    await page.screenshot({ path: path.join(saida, "paginas", `${pg.id}-${larg}.jpg`), type: "jpeg", quality: 55, fullPage: true });

    if (!pg.foraDaVersao) {
      /* Peças: quantas vezes aparece e fotografia da primeira. */
      for (const p of pecas) {
        const loc = page.locator(p.seletor);
        const n = await loc.count();
        if (larg === 1440) resultado.matriz[p.nome][pg.id] = n;
        else if ((resultado.matriz[p.nome][pg.id] || 0) !== n) resultado.falhas.push(`${p.nome} em ${pg.id}: ${n} em ${larg}px contra ${resultado.matriz[p.nome][pg.id]} em 1440px`);
        if (!p.captura || !n) continue;
        const f = path.join(saida, String(larg), `${slug(p.nome)}.jpg`);
        // A primeira página onde a peça aparece é a da fotografia.
        if (larg === 1440) resultado.capturas[p.nome] ||= pg.id;
        if (resultado.capturas[p.nome] !== pg.id) continue;
        try {
          const el = loc.locator("visible=true").first();
          if (p.captura !== "menu" && !(await loc.locator("visible=true").count())) { (resultado.ocultas[p.nome] ||= []).push(larg); continue; }
          if (p.captura === "menu") {
            await page.locator(".menu-btn").first().click();
            await page.waitForTimeout(900);
            await page.screenshot({ path: f, type: "jpeg", quality: 70 });
            await page.locator(".menu-btn").first().click();
            await page.waitForTimeout(600);
          } else if (p.captura === "viewport") {
            await el.scrollIntoViewIfNeeded();
            await page.waitForTimeout(700);
            await page.screenshot({ path: f, type: "jpeg", quality: 70 });
          } else {
            await el.scrollIntoViewIfNeeded();
            await page.waitForTimeout(500);
            const box = await el.boundingBox();
            if (!box || box.height < 2) { resultado.falhas.push(`${p.nome} em ${pg.id} ${larg}px: sem área visível`); continue; }
            const alto = Math.min(box.height, 2400);
            await page.screenshot({ path: f, type: "jpeg", quality: 70, fullPage: true, clip: { x: Math.max(0, box.x), y: box.y + (await page.evaluate(() => scrollY)), width: Math.min(box.width, larg), height: alto } });
          }
        } catch (e) {
          resultado.falhas.push(`${p.nome} em ${pg.id} ${larg}px: ${String(e.message).split("\n")[0]}`);
        }
      }

      /* Classes que nenhuma peça cobre. */
      if (larg === 1440) {
        const uniao = pecas.map((p) => p.seletor).join(", ");
        resultado.semPeca[pg.id] = await page.evaluate(CLASSES, uniao);
      }
    }

    if (larg === 1440 || larg === 390) {
      resultado.contraste[`${pg.id}-${larg}`] = await page.evaluate(CONTRASTE);
      if (!pg.foraDaVersao) resultado.verde[`${pg.id}-${larg}`] = await page.evaluate(VERDE);
    }
    await ctx.close();
  }
}
await navegador.close();
fs.writeFileSync(path.join(aqui, "resultado.json"), JSON.stringify(resultado, null, 1));
console.log("pronto", resultado.falhas.length, "falhas");
for (const f of resultado.falhas) console.log(" -", f);
