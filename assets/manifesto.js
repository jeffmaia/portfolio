/* Manifesto "Antes, Hoje, Futuro".
   Importado do Claude Design (Antes Hoje Futuro - Site.dc.html), que roda em
   React sobre o runtime support.js. O site inteiro é HTML e JS puros, sem
   build nem framework, então a cena foi portada para DOM direto: o mesmo
   roteiro, as mesmas curvas de animação e a mesma geometria, só que
   escrevendo estilo em elementos em vez de devolver árvore de React. */

(() => {
  const scroller = document.getElementById("om-scroller");
  const track    = document.getElementById("om-track");
  const stage    = document.getElementById("om-stage");
  const shotsEl  = document.getElementById("om-shots");
  if (!scroller || !stage || !shotsEl) return;

  const labelEl     = document.getElementById("om-label");
  const counterEl   = document.getElementById("om-counter");
  const railEl      = document.getElementById("om-rail");
  const railFillEl  = document.getElementById("om-rail-fill");
  const hintEl      = document.getElementById("om-hint");
  const hintMouseEl = document.getElementById("om-hint-mouse");
  const hintDotEl   = document.getElementById("om-hint-dot");
  const hintLabelEl = document.getElementById("om-hint-label");
  const signEl      = document.getElementById("om-sign");
  const signRuleEl  = document.getElementById("om-sign-rule");
  const signTextEl  = document.getElementById("om-sign-text");
  const fallbackEl  = document.getElementById("om-fallback");

  /* A versão em texto corrido existe para quem chega sem JS e para os
     robôs de busca; com a cena rodando ela só duplicaria o conteúdo. */
  if (fallbackEl) fallbackEl.hidden = true;

  const INK   = "#0B0B0C";
  const PAPER = "#F2EFE8";
  const SANS  = "'Libre Franklin', system-ui, sans-serif";
  const SERIF = "'Instrument Serif', Georgia, serif";

  const ACCENT    = "#D9481F";
  const SHOW_META = true;
  /* Pixels de rolagem por segundo de roteiro: define o comprimento total da
     página. É o valor padrão do arquivo de design. */
  const PACE      = 220;

  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const eo4  = t => 1 - Math.pow(1 - t, 4);
  const eo3  = t => 1 - Math.pow(1 - t, 3);
  const eio3 = t => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const eiq  = t => (t < 0.5 ? 8 * t * t * t * t : 1 - Math.pow(-2 * t + 2, 4) / 2);

  const tw = (T, start, dur, from, to, ease) => {
    const p = clamp((T - start) / dur, 0, 1);
    return from + (to - from) * (ease ? ease(p) : p);
  };
  const trackVal = (T, kf, vals) => {
    if (T <= kf[0]) return vals[0];
    for (let i = 1; i < kf.length; i++) {
      if (T <= kf[i]) {
        const p = eio3((T - kf[i - 1]) / (kf[i] - kf[i - 1] || 1));
        return vals[i - 1] + (vals[i] - vals[i - 1]) * p;
      }
    }
    return vals[vals.length - 1];
  };

  const B = (at, dur, text, key, layout, fx, bg, art) =>
    ({ at, dur, text, key, layout, fx, bg: bg || "ink", art: art || null });

  const SCRIPT = {
    Antes: [
      B(0.0,  1.7, "Antes,",                          "Antes,",     "hero",   "letters", "ink",    { k: "quarter", pos: "tl",   size: 820 }),
      B(1.7,  2.1, "o designer desenhava",            null,         "left",   "mask",    "ink",    { k: "bars",    pos: "r",    size: 460 }),
      B(3.8,  1.9, "para a tela.",                    "tela.",      "right",  "slide",   "paper",  { k: "sq",      pos: "l",    size: 380 }),
      B(5.7,  2.0, "Cada pixel era",                  null,         "center", "slam",    "ink",    { k: "pix",     pos: "br",   size: 520 }),
      B(7.7,  2.0, "uma decisão manual,",             "manual,",    "center", "mask",    "ink",    { k: "cursor",  pos: "tr",   size: 260 }),
      B(9.7,  2.2, "cada grade um exercício",         null,         "left",   "mask",    "ink",    { k: "grid",    pos: "full", size: 0 }),
      B(11.9, 1.8, "de paciência.",                   "paciência.", "right",  "echo",    "ink",    { k: "clock",   pos: "l",    size: 380 }),
      B(13.7, 2.1, "O trabalho nascia da mão,",       "mão,",       "stack",  "mask",    "ink",    { k: "arcs",    pos: "r",    size: 720 }),
      B(15.8, 1.9, "do olho treinado,",               "olho",       "left",   "slam",    "ink",    { k: "eye",     pos: "r",    size: 440 }),
      B(17.7, 2.2, "do tempo gasto ajustando",        null,         "center", "mask",    "ink",    { k: "stripes", pos: "b",    size: 0 }),
      B(19.9, 2.5, "o que só o humano sabia sentir.", "humano",     "stack",  "mask",    "orange", { k: "dot",     pos: "r",    size: 560 }),
    ],
    Hoje: [
      B(0.0,  1.6, "Hoje,",                           "Hoje,",      "hero",   "letters", "orange", { k: "rays",   pos: "c", size: 1000 }),
      B(1.6,  1.5, "a IA",                            "IA",         "hero",   "slam",    "ink",    { k: "node",   pos: "r", size: 520 }),
      B(3.1,  2.3, "entrou na mesa de trabalho.",     null,         "center", "mask",    "ink",    { k: "bars",   pos: "b", size: 560 }),
      B(5.4,  2.2, "O designer não desenha sozinho,", "sozinho,",   "left",   "slide",   "ink",    { k: "duo",    pos: "r", size: 600 }),
      B(7.6,  2.1, "ele conversa com sistemas",       null,         "right",  "mask",    "ink",    { k: "bubble", pos: "l", size: 440 }),
      B(9.7,  2.4, "que sugerem, geram e testam",     null,         "stack",  "echo",    "ink",    { k: "x",      pos: "r", size: 460 }),
      B(12.1, 1.8, "em segundos",                     "segundos",   "hero",   "slam",    "paper",  { k: "wave",   pos: "b", size: 640 }),
      B(13.9, 2.1, "o que antes levava dias.",        "dias.",      "center", "mask",    "ink",    { k: "grid",   pos: "tr", size: 420 }),
      B(16.0, 2.2, "A criação virou diálogo",         "diálogo",    "left",   "mask",    "ink",    { k: "ring",   pos: "r", size: 560 }),
      B(18.2, 2.2, "entre intenção humana",           null,         "right",  "roll",    "ink",    { k: "eye",    pos: "l", size: 320 }),
      B(20.4, 2.2, "e velocidade artificial.",        "artificial.","center", "slam",    "orange", { k: "rays",   pos: "r", size: 760 }),
    ],
    Futuro: [
      B(0.0,  1.8, "No futuro,",                      "futuro,",     "hero",   "letters", "ink",    { k: "arcs",    pos: "c",    size: 1200 }),
      B(1.8,  2.2, "essa fronteira desaparece.",      "desaparece.", "center", "mask",    "ink",    { k: "stripes", pos: "full", size: 0 }),
      B(4.0,  2.3, "O design deixa de ser",           null,          "left",   "mask",    "ink",    { k: "quarter", pos: "br",   size: 700 }),
      B(6.3,  2.1, "sobre produzir imagens",          null,          "right",  "slide",   "ink",    { k: "frame",   pos: "l",    size: 460 }),
      B(8.4,  2.3, "e passa a ser sobre",             null,          "center", "mask",    "ink",    { k: "chev",    pos: "r",    size: 400 }),
      B(10.7, 2.2, "curar significado,",              "curar",       "hero",   "slam",    "paper",  { k: "ast",     pos: "r",    size: 560 }),
      B(12.9, 2.4, "direcionar sistemas inteligentes",null,          "stack",  "mask",    "ink",    { k: "node",    pos: "r",    size: 660 }),
      B(15.3, 2.2, "e garantir que,",                 null,          "left",   "echo",    "ink",    { k: "ring",    pos: "r",    size: 420 }),
      B(17.5, 2.4, "em meio a tanta automação,",      "automação,",  "right",  "mask",    "ink",    { k: "grid",    pos: "full", size: 0 }),
      B(19.9, 2.3, "ainda exista uma voz humana",     "humana",      "stack",  "mask",    "orange", { k: "wave",    pos: "r",    size: 560 }),
      B(22.2, 2.2, "guiando o que é criado.",         null,          "center", "mask",    "ink",    { k: "dot",     pos: "l",    size: 400 }),
    ],
    Fecho: [
      B(0.0, 2.2, "O ofício muda de forma,",          null,         "left",   "mask",    "ink", { k: "duo",  pos: "r",  size: 540 }),
      B(2.2, 2.4, "mas a essência permanece.",        "essência",   "right",  "mask",    "ink", { k: "ring", pos: "l",  size: 540 }),
      B(4.6, 2.0, "Design sempre foi,",               null,         "center", "slam",    "ink", null),
      B(6.6, 2.2, "e continuará sendo,",              null,         "center", "mask",    "ink", null),
      B(8.8, 6.2, "a arte de decidir o que importa.", "importa.",   "card",   "letters", "ink", { k: "ast",  pos: "bl", size: 400 }),
    ],
  };

  const DUR    = { Antes: 22.4, Hoje: 22.6, Futuro: 24.4, Fecho: 15.0 };
  const ORDER  = ["Antes", "Hoje", "Futuro", "Fecho"];
  const LABELS = { Antes: "ANTES", Hoje: "HOJE", Futuro: "NO FUTURO", Fecho: "" };

  const CUES = (() => {
    let t = 0; const c = {};
    ORDER.forEach(n => { c[n] = t; t += DUR[n]; });
    c.__total = t;
    return c;
  })();
  const TOTAL = CUES.__total;
  const INTRO = 1.15;

  const BEATS = (() => {
    const out = [];
    ORDER.forEach(name =>
      SCRIPT[name].forEach(beat =>
        out.push({ beat, base: CUES[name], section: name, idx: out.length + 1 })));
    return out;
  })();

  /* Motivos que ocupam uma faixa inteira da tela em vez de um quadrado. */
  const BAND = { grid: 1, stripes: 1, bars: 1, wave: 1, pix: 1 };

  const sh  = o => Object.assign({ position: "absolute" }, o);
  const kid = (style, children) => ({ style, children: children || null });

  function motifChildren(art, p, color) {
    const k = art.k;
    const grow = eo4(clamp(p / 0.32, 0, 1));
    const life = clamp(p, 0, 1);
    const spin = life * 24;

    if (k === "dot") return [kid(sh({ inset: 0, borderRadius: "50%", background: color, transform: "scale(" + grow + ")" }))];

    if (k === "ring") return [kid(sh({ inset: 0, borderRadius: "50%", border: "0.06em solid " + color, fontSize: "100%", transform: "scale(" + (0.7 + grow * 0.3) + ") rotate(" + spin + "deg)", clipPath: "inset(0 " + (100 - grow * 100) + "% 0 0)", boxSizing: "border-box" }))];

    if (k === "duo") return [
      kid(sh({ left: 0, top: "12%", width: "62%", height: "62%", borderRadius: "50%", background: color, transform: "translateX(" + (-40 + grow * 40) + "px) scale(" + grow + ")" })),
      kid(sh({ right: 0, bottom: "10%", width: "68%", height: "68%", borderRadius: "50%", background: color, transform: "translateX(" + (46 - grow * 46) + "px) scale(" + grow + ")" })),
    ];

    if (k === "quarter") return [kid(sh({ inset: 0, background: color, borderRadius: "0 0 100% 0", transform: "scale(" + grow + ") rotate(" + (spin * 0.4) + "deg)", transformOrigin: "0% 0%" }))];

    if (k === "arcs") return [0, 1, 2].map(i => {
      const g = eo4(clamp((p - i * 0.08) / 0.4, 0, 1));
      return kid(sh({
        inset: (i * 13) + "%", borderRadius: "50%", boxSizing: "border-box",
        border: "0.07em solid " + color, borderRightColor: "transparent", borderTopColor: "transparent",
        transform: "rotate(" + (-20 + g * 32 + i * 6) + "deg) scale(" + (0.6 + g * 0.4) + ")", opacity: g,
      }));
    });

    if (k === "rays") {
      const rays = Array.from({ length: 14 }).map((_, i) => kid(sh({
        left: "48.5%", top: 0, width: "3%", height: "30%", background: color, transformOrigin: "50% 166%",
        transform: "rotate(" + (i * (360 / 14)) + "deg) scaleY(" + eo4(clamp((p - i * 0.012) / 0.3, 0, 1)) + ")",
      })));
      const core = kid(sh({ left: "30%", top: "30%", width: "40%", height: "40%", borderRadius: "50%", background: color, opacity: 0.9, transform: "scale(" + grow + ")" }));
      return [kid(sh({ inset: 0, transform: "rotate(" + (spin * 1.6) + "deg) scale(" + (0.5 + grow * 0.5) + ")" }), rays.concat([core]))];
    }

    if (k === "ast") return [kid(sh({ inset: 0, transform: "rotate(" + (spin * 2) + "deg) scale(" + grow + ")" }),
      [0, 60, 120].map(a => kid(sh({ left: "38%", top: 0, width: "24%", height: "100%", borderRadius: "50%", background: color, transform: "rotate(" + a + "deg)" }))))];

    if (k === "x") return [kid(sh({ inset: 0, transform: "rotate(" + (45 + spin) + "deg) scale(" + grow + ")" }),
      [[0, 0, "0 0 100% 0"], [1, 0, "0 0 0 100%"], [0, 1, "0 100% 0 0"], [1, 1, "100% 0 0 0"]].map(c =>
        kid(sh({ left: c[0] ? "50%" : 0, top: c[1] ? "50%" : 0, width: "50%", height: "50%", background: color, borderRadius: c[2] }))))];

    if (k === "sq") return [kid(sh({ inset: 0, background: color, transform: "rotate(" + (-6 + grow * 6) + "deg)", clipPath: "inset(" + (100 - grow * 100) + "% 0 0 0)" }))];

    if (k === "frame") return [kid(sh({ inset: 0, border: "0.055em solid " + color, boxSizing: "border-box", transform: "rotate(" + (-6 + grow * 6) + "deg)", clipPath: "inset(" + (100 - grow * 100) + "% 0 0 0)" }),
      [kid(sh({ left: "18%", bottom: "16%", width: "30%", height: "30%", borderRadius: "50%", background: color, transform: "scale(" + grow + ")" }))])];

    if (k === "pix") return [kid(sh({ inset: 0, display: "grid", gridTemplateColumns: "repeat(6,1fr)", gridTemplateRows: "repeat(6,1fr)", gap: "2%" }),
      Array.from({ length: 36 }).map((_, i) => {
        const g = clamp((p - (i % 6) * 0.02 - Math.floor(i / 6) * 0.02) / 0.28, 0, 1);
        return kid({ background: color, opacity: g * (i % 5 === 0 ? 1 : 0.35), transform: "scale(" + eo4(g) + ")" });
      }))];

    if (k === "grid") {
      const cell = 78 + (1 - grow) * 40;
      return [kid(sh({
        inset: "-10%",
        backgroundImage: "linear-gradient(to right, " + color + " 2px, transparent 2px),linear-gradient(to bottom, " + color + " 2px, transparent 2px)",
        backgroundSize: cell + "px " + cell + "px",
        clipPath: "inset(0 " + (100 - grow * 100) + "% 0 0)",
      }))];
    }

    if (k === "stripes") return [kid(sh({
      inset: 0,
      backgroundImage: "repeating-linear-gradient(78deg, " + color + " 0 6px, transparent 6px " + (26 + life * 26) + "px)",
      clipPath: "inset(" + (100 - grow * 100) + "% 0 0 0)",
    }))];

    if (k === "bars") return [kid(sh({ inset: 0, display: "flex", flexDirection: "column", justifyContent: "center", gap: "6%" }),
      [1, 0.72, 0.9, 0.5, 0.66].map((w, i) => {
        const g = eo4(clamp((p - i * 0.05) / 0.32, 0, 1));
        return kid({ height: "9%", width: (w * 100 * g) + "%", background: color, borderRadius: 999 });
      }))];

    if (k === "wave") return [kid(sh({ inset: 0, display: "flex", alignItems: "flex-end", gap: "2.5%" }),
      Array.from({ length: 16 }).map((_, i) => {
        const hh = 24 + 62 * Math.abs(Math.sin(i * 0.7 + life * 5.4));
        const g = clamp((p - i * 0.014) / 0.26, 0, 1);
        return kid({ flex: 1, height: (hh * g) + "%", background: color, borderRadius: 999 });
      }))];

    if (k === "node") {
      const dots  = [[16, 12], [72, 26], [40, 56], [82, 74], [22, 82]];
      const edges = [[16, 12, 72, 26], [72, 26, 40, 56], [40, 56, 82, 74], [40, 56, 22, 82]];
      const dotEls = dots.map((n, i) => kid(sh({
        left: n[0] + "%", top: n[1] + "%", width: "13%", height: "13%", borderRadius: "50%", background: color,
        transform: "translate(-50%,-50%) scale(" + eo4(clamp((p - i * 0.06) / 0.34, 0, 1)) + ")",
      })));
      const edgeEls = edges.map((e, i) => {
        const dx = e[2] - e[0], dy = e[3] - e[1];
        const len = Math.sqrt(dx * dx + dy * dy);
        const g = eo4(clamp((p - 0.1 - i * 0.06) / 0.36, 0, 1));
        return kid(sh({
          left: e[0] + "%", top: e[1] + "%", height: 3, width: (len * g) + "%", background: color, opacity: 0.75,
          transformOrigin: "0 50%", transform: "rotate(" + (Math.atan2(dy, dx) * 180 / Math.PI) + "deg)",
        }));
      });
      return [kid(sh({ inset: 0, transform: "scale(" + (0.75 + grow * 0.25) + ")" }), dotEls.concat(edgeEls))];
    }

    if (k === "bubble") return [
      kid(sh({ left: 0, top: "8%", width: "76%", height: "38%", borderRadius: "999px 999px 999px 12px", background: color, transform: "scale(" + grow + ")", transformOrigin: "0 100%" })),
      kid(sh({ right: 0, bottom: "10%", width: "64%", height: "34%", borderRadius: "999px 999px 12px 999px", border: "0.05em solid " + color, boxSizing: "border-box", transform: "scale(" + eo4(clamp((p - 0.12) / 0.34, 0, 1)) + ")", transformOrigin: "100% 0" })),
    ];

    if (k === "eye") return [kid(sh({ inset: 0, transform: "scale(" + grow + ")" }), [
      kid(sh({ left: 0, top: "22%", width: "100%", height: "56%", borderRadius: "50%", border: "0.06em solid " + color, boxSizing: "border-box" })),
      kid(sh({ left: "34%", top: "34%", width: "32%", height: "32%", borderRadius: "50%", background: color, transform: "translateX(" + (Math.sin(life * 6) * 26) + "px)" })),
    ])];

    if (k === "clock") return [kid(sh({ inset: 0, transform: "scale(" + grow + ")" }), [
      kid(sh({ inset: 0, borderRadius: "50%", border: "0.055em solid " + color, boxSizing: "border-box" })),
      kid(sh({ left: "49%", top: "14%", width: "2.5%", height: "38%", background: color, transformOrigin: "50% 100%", transform: "rotate(" + (life * 320) + "deg)" })),
      kid(sh({ left: "49%", top: "26%", width: "3.5%", height: "26%", background: color, transformOrigin: "50% 100%", transform: "rotate(" + (life * 68) + "deg)" })),
    ])];

    if (k === "cursor") return [kid(sh({
      inset: 0, background: color,
      clipPath: "polygon(6% 0, 6% 84%, 30% 62%, 47% 100%, 62% 92%, 45% 55%, 78% 52%)",
      transform: "scale(" + grow + ") rotate(" + (-8 + Math.sin(life * 5) * 6) + "deg)",
    }))];

    if (k === "chev") return [kid(sh({ inset: 0, display: "flex", flexDirection: "column", gap: "8%", justifyContent: "center" }),
      [0, 1, 2].map(i => {
        const g = eo4(clamp((p - i * 0.07) / 0.32, 0, 1));
        return kid({ height: "16%", background: color, clipPath: "polygon(0 0, 62% 0, 100% 50%, 62% 100%, 0 100%, 38% 50%)", transform: "translateX(" + (-70 + g * 70) + "px)", opacity: g });
      }))];

    return [];
  }

  /* ---- ponte entre descrição de estilo e DOM ---- */

  /* React devolve número puro como px, menos nestas propriedades. */
  const UNITLESS = { opacity: 1, fontWeight: 1, lineHeight: 1, flex: 1, flexGrow: 1, flexShrink: 1, zIndex: 1, order: 1 };

  function applyStyle(node, style) {
    const prev = node.__st;
    const css = node.style;
    if (prev) for (const k in prev) if (!(k in style)) css[k] = "";
    for (const k in style) {
      if (prev && prev[k] === style[k]) continue;
      const v = style[k];
      css[k] = (typeof v === "number" && !UNITLESS[k]) ? v + "px" : v;
    }
    node.__st = style;
  }

  /* Só recria elemento quando a forma da árvore muda (troca de beat, de
     formato de tela). Nos outros quadros mexe apenas em estilo. */
  function syncList(parent, nodes) {
    const kids = parent.children;
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      const tag = n.tag || "div";
      let node = kids[i];
      if (!node || node.tagName.toLowerCase() !== tag) {
        const fresh = document.createElement(tag);
        if (node) parent.replaceChild(fresh, node);
        else parent.appendChild(fresh);
        node = fresh;
      }
      applyStyle(node, n.style);
      if (n.children) {
        if (node.__text) { node.textContent = ""; node.__text = ""; }
        syncList(node, n.children);
      } else {
        const t = n.text == null ? "" : n.text;
        if (node.__text !== t) { node.textContent = t; node.__text = t; }
      }
    }
    while (parent.children.length > nodes.length) parent.removeChild(parent.lastElementChild);
  }

  /* ---- cena ---- */

  const state = { T: INTRO, W: 1280, H: 720, wall: 0, prog: 0 };
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)");

  const fmtOf = W => (W < 640 ? "sm" : W < 1080 ? "md" : "lg");

  function layoutFor(beat, fmt) {
    if (fmt === "lg") return beat.layout;
    if (fmt === "md") return beat.layout === "card" ? "center" : beat.layout;
    if (beat.layout === "hero" || beat.layout === "card") return beat.layout;
    return "stack";
  }

  function buildShot(entry, T, W, H, fmt, accent) {
    const beat = entry.beat;
    const t0 = entry.base + beat.at;
    const t1 = t0 + beat.dur;
    if (T < t0 - 0.55 || T > t1 + 0.45) return null;

    const isLast = entry.idx === BEATS.length;
    const outStart = t1 - 0.34;
    const p = clamp((T - t0) / beat.dur, 0, 1);
    const op = isLast
      ? trackVal(T, [t0 - 0.02, t0 + 0.1], [0, 1])
      : trackVal(T, [t0 - 0.02, t0 + 0.1, outStart, t1], [0, 1, 1, 0]);
    const dy = isLast ? 0 : tw(T, outStart, 0.34, 0, -H * 0.03, eo3);
    const light = beat.bg !== "ink";
    const body = light ? INK : PAPER;
    const keyColor = beat.bg === "orange" ? PAPER : accent;
    const motifColor = light ? INK : PAPER;

    const layout = layoutFor(beat, fmt);
    const pad = fmt === "sm" ? W * 0.075 : fmt === "md" ? W * 0.07 : Math.min(W * 0.08, 160);
    const inW = W - pad * 2;

    const strip = s => s.replace(/[.,;:]+$/, "");
    const bKey = beat.key ? strip(beat.key) : null;
    let words = strip(beat.text).split(" ");
    const stack = layout === "stack";
    if (stack) {
      const merged = [];
      for (let i = 0; i < words.length; i++) {
        if (words[i].length <= 2 && i < words.length - 1 && words[i + 1] !== bKey) { merged.push(words[i] + " " + words[i + 1]); i++; }
        else merged.push(words[i]);
      }
      words = merged;
    }
    const chars = strip(beat.text).length;
    const maxWord = words.reduce((m, w) => Math.max(m, w.length), 1);

    let size;
    if (layout === "hero") {
      size = Math.min(inW * 1.35 / Math.max(chars, 4), fmt === "sm" ? W * 0.3 : fmt === "md" ? W * 0.21 : W * 0.16);
    } else if (stack) {
      size = Math.min(inW / (maxWord * 0.52), (H * (fmt === "sm" ? 0.52 : 0.74)) / (words.length * 1.2), fmt === "sm" ? W * 0.15 : fmt === "md" ? W * 0.085 : W * 0.062);
    } else if (layout === "card") {
      size = Math.min(inW * 2.1 / chars, fmt === "sm" ? W * 0.14 : W * 0.062);
    } else {
      size = Math.min(inW * 2.35 / chars, fmt === "md" ? W * 0.1 : W * 0.086);
    }
    size = Math.max(size, 15);

    /* --- geometria do motivo, reorganizada por formato --- */
    let motifBox = { position: "absolute", opacity: 0 };
    let motif = [];
    if (beat.art) {
      const band = !!BAND[beat.art.k];
      const full = beat.art.pos === "full";
      let box;
      if (fmt === "sm") {
        if (full) box = { left: 0, right: 0, top: 0, height: H * 0.34 };
        else if (band) box = { left: pad, top: H * 0.1, width: inW, height: H * 0.2 };
        else { const S = Math.min(inW * 0.78, H * 0.26); box = { left: (W - S) / 2, top: H * 0.08, width: S, height: S }; }
      } else if (fmt === "md") {
        if (full) box = { inset: 0 };
        else if (band) box = { left: pad, right: pad, bottom: H * 0.12, height: H * 0.24 };
        else { const S = W * 0.5; box = entry.idx % 2 ? { right: -S * 0.14, top: H * 0.5 - S / 2, width: S, height: S } : { left: -S * 0.16, top: H * 0.5 - S / 2, width: S, height: S }; }
      } else {
        if (full) box = { inset: 0 };
        else {
          const S = beat.art.size * (W / 1920);
          const P = {
            tl: { left: -S * 0.15, top: -S * 0.2 },      tr: { right: -S * 0.12, top: -S * 0.18 },
            bl: { left: -S * 0.15, bottom: -S * 0.2 },   br: { right: -S * 0.14, bottom: -S * 0.2 },
            l:  { left: -S * 0.2,  top: H / 2 - S / 2 }, r:  { right: -S * 0.16, top: H / 2 - S / 2 },
            c:  { left: W / 2 - S / 2, top: H / 2 - S / 2 }, b: { left: W / 2 - S / 2, bottom: -S * 0.08 },
          }[beat.art.pos];
          box = Object.assign({ width: S, height: S }, P);
        }
      }
      motifBox = Object.assign({ position: "absolute", opacity: op * (light ? 0.16 : 0.2), pointerEvents: "none", fontSize: (box.width || W) + "px" }, box);
      motif = motifChildren(beat.art, p, motifColor);
    }

    /* --- cortina do fundo claro --- */
    const wIn = eiq(clamp((T - t0 + 0.12) / 0.46, 0, 1));
    const wOut = eiq(clamp((T - outStart) / 0.34, 0, 1));
    const fromLeft = entry.idx % 2 === 1;
    const panel = light ? {
      position: "absolute", inset: 0, background: beat.bg === "orange" ? accent : PAPER,
      clipPath: fromLeft
        ? "inset(0 " + (100 - wIn * 100) + "% 0 " + (wOut * 100) + "%)"
        : "inset(0 " + (wOut * 100) + "% 0 " + (100 - wIn * 100) + "%)",
    } : { display: "none" };

    /* --- posição do bloco de texto --- */
    const align = layout === "right" ? "flex-end" : (layout === "center" || layout === "hero" || layout === "card") ? "center" : "flex-start";
    const block = {
      position: "absolute", inset: 0, display: "flex", opacity: op,
      transform: "translateY(" + dy + "px)",
      justifyContent: fmt === "sm" ? (layout === "hero" || layout === "card" ? "center" : "flex-start") : align,
      alignItems: fmt === "sm" && beat.art ? "flex-end" : "center",
      padding: fmt === "sm"
        ? (beat.art ? H * 0.1 + "px " + pad + "px " + H * 0.19 + "px" : "0 " + pad + "px")
        : "0 " + pad + "px",
      boxSizing: "border-box",
    };
    const inner = {
      fontSize: size + "px", display: "flex", maxWidth: "100%",
      flexWrap: "wrap", flexDirection: stack ? "column" : "row",
      gap: stack ? "0.05em 0.3em" : "0.1em 0.26em",
      alignItems: stack ? "flex-start" : "baseline",
      justifyContent: align,
      textAlign: layout === "right" ? "right" : "left",
    };

    /* --- palavras --- */
    const stepBase = beat.fx === "letters" ? 0.09 : 0.06;
    const vwords = words.map((w, i) => {
      const isKey = !!bKey && w === bKey;
      const s = t0 + i * stepBase;
      const base = {
        fontFamily: isKey ? SERIF : SANS,
        fontStyle: isKey ? "italic" : "normal",
        fontWeight: isKey ? 400 : 800,
        fontSize: (isKey ? 1.12 : 1) + "em",
        lineHeight: 1.0,
        letterSpacing: isKey ? "-0.005em" : "-0.035em",
        color: isKey ? keyColor : body,
        display: "inline-block",
        whiteSpace: "pre",
      };
      const box = { display: "inline-flex", position: beat.fx === "echo" ? "relative" : "static" };
      let units = [];
      let ghosts = [];

      if (beat.fx === "mask" || beat.fx === "letters") {
        const chs = beat.fx === "letters" ? w.split("") : [w];
        const step = beat.fx === "letters" ? 0.045 : 0;
        units = chs.map((c, j) => ({
          c: c,
          wrap: { display: "inline-block", overflow: "hidden", verticalAlign: "bottom", paddingBottom: "0.07em" },
          st: Object.assign({}, base, { transform: "translateY(" + tw(T, s + j * step, 0.62, 112, 0, eo4) + "%)" }),
        }));
      } else if (beat.fx === "slam") {
        units = [{ c: w, wrap: { display: "inline-block" }, st: Object.assign({}, base, { opacity: tw(T, s, 0.22, 0, 1), transform: "scale(" + tw(T, s, 0.5, 1.55, 1, eo4) + ")" }) }];
      } else if (beat.fx === "slide") {
        units = [{ c: w, wrap: { display: "inline-block", overflow: "hidden", paddingBottom: "0.07em" }, st: Object.assign({}, base, { opacity: tw(T, s, 0.3, 0, 1), transform: "translateX(" + tw(T, s, 0.58, -size * 0.6, 0, eo4) + "px)" }) }];
      } else if (beat.fx === "roll") {
        units = [{ c: w, wrap: { display: "inline-block" }, st: Object.assign({}, base, { opacity: tw(T, s, 0.25, 0, 1), transformOrigin: "50% 100%", transform: "perspective(900px) rotateX(" + tw(T, s, 0.6, -88, 0, eo4) + "deg)" }) }];
      } else {
        const x = tw(T, s, 0.6, -size * 0.45, 0, eo4);
        const o = tw(T, s, 0.3, 0, 1);
        ghosts = [2, 1].map(g => ({ t: w, st: Object.assign({}, base, { position: "absolute", left: 0, top: 0, opacity: o * (g === 2 ? 0.16 : 0.3), transform: "translateX(" + (x * (1 + g * 0.55)) + "px)" }) }));
        units = [{ c: w, wrap: { display: "inline-block" }, st: Object.assign({}, base, { opacity: o, transform: "translateX(" + x + "px)" }) }];
      }

      const children = ghosts.map(g => ({ tag: "span", style: g.st, text: g.t }))
        .concat(units.map(u => ({ tag: "span", style: u.wrap, children: [{ tag: "span", style: u.st, text: u.c }] })));
      return { tag: "span", style: box, children: children };
    });

    return {
      nodes: [
        { style: panel },
        { style: motifBox, children: motif },
        { style: block, children: [{ style: inner, children: vwords }] },
      ],
      light: light, section: entry.section, idx: entry.idx, op: op,
    };
  }

  function render() {
    const accent = ACCENT;
    const T = state.T, W = state.W, H = state.H;
    const fmt = fmtOf(W);
    const scrollLen = Math.round((TOTAL - INTRO) * (fmt === "sm" ? PACE * 0.85 : PACE));

    const shots = [];
    BEATS.forEach(entry => {
      const s = buildShot(entry, T, W, H, fmt, accent);
      if (s) shots.push(s);
    });

    let active = null;
    shots.forEach(s => { if (!active || s.op > active.op) active = s; });
    const onLight = active ? active.light : false;
    const chrome = onLight ? INK : PAPER;
    const section = active ? active.section : "Antes";
    const small = fmt === "sm";
    const metaSize = small ? 10 : fmt === "md" ? 13 : 17;
    const edge = small ? W * 0.075 : fmt === "md" ? W * 0.07 : Math.min(W * 0.08, 160);

    applyStyle(track, { position: "relative", width: "100%", height: (H + scrollLen) + "px" });
    applyStyle(stage, { position: "sticky", top: 0, height: H + "px", width: "100%", overflow: "hidden", background: INK });

    /* Cada tomada vive numa camada própria para que a ordem de pilha não
       dependa de quantas estão no ar. */
    syncList(shotsEl, shots.map(s => ({ style: { position: "absolute", inset: 0, pointerEvents: "none" }, children: s.nodes })));

    applyStyle(labelEl, {
      position: "absolute", top: small ? 18 : 40, left: edge,
      fontFamily: SANS, fontWeight: 700, fontSize: metaSize + "px", letterSpacing: "0.32em",
      color: onLight ? INK : accent, opacity: SHOW_META && LABELS[section] ? 1 : 0,
      transition: "color .25s", pointerEvents: "none",
    });
    labelEl.textContent = LABELS[section] || "";

    applyStyle(counterEl, {
      position: "absolute", top: small ? 18 : 40, right: edge,
      fontFamily: SANS, fontWeight: 600, fontSize: (metaSize - 1) + "px", letterSpacing: "0.2em",
      color: chrome, opacity: SHOW_META ? 0.42 : 0, pointerEvents: "none",
    });
    counterEl.textContent = String(active ? active.idx : 1).padStart(2, "0") + " / " + BEATS.length;

    applyStyle(railEl, small
      ? { position: "absolute", right: 8, top: H * 0.3, width: 2, height: H * 0.4, background: onLight ? "rgba(11,11,12,0.18)" : "rgba(242,239,232,0.14)", opacity: SHOW_META ? 1 : 0 }
      : { position: "absolute", left: edge, right: edge, bottom: fmt === "md" ? 30 : 44, height: 2, background: onLight ? "rgba(11,11,12,0.16)" : "rgba(242,239,232,0.12)", opacity: SHOW_META ? 1 : 0 });
    const pct = clamp(T / TOTAL, 0, 1) * 100;
    applyStyle(railFillEl, small
      ? { width: "100%", height: pct + "%", background: onLight ? INK : accent }
      : { width: pct + "%", height: "100%", background: onLight ? INK : accent });

    /* A dica de rolagem entra quando "Antes" assenta e some no primeiro giro. */
    const hintVis = clamp((T - (INTRO - 0.45)) / 0.45, 0, 1) * (1 - clamp(state.prog / 0.012, 0, 1));
    const bob = Math.sin(state.wall * 2.4);
    applyStyle(hintEl, {
      position: "absolute", left: 0, right: 0, bottom: small ? H * 0.11 : H * 0.13,
      display: "flex", flexDirection: "column", alignItems: "center", gap: small ? 10 : 14,
      opacity: hintVis, pointerEvents: "none",
    });
    const mw = small ? 22 : 26;
    applyStyle(hintMouseEl, {
      width: mw, height: mw * 1.62, borderRadius: mw, border: "2px solid " + PAPER,
      opacity: 0.75, display: "flex", justifyContent: "center", paddingTop: mw * 0.24, boxSizing: "border-box",
      transform: "translateY(" + (bob * 3) + "px)",
    });
    applyStyle(hintDotEl, { width: 3, height: mw * 0.34, borderRadius: 3, background: accent, transform: "translateY(" + (2.5 + bob * 3.5) + "px)" });
    applyStyle(hintLabelEl, {
      fontFamily: SANS, fontWeight: 600, fontSize: (small ? 9 : 11) + "px", letterSpacing: "0.34em",
      textTransform: "uppercase", color: PAPER, opacity: 0.5,
    });

    const sigT = CUES.Fecho + 8.8;
    const sigOp = trackVal(T, [sigT + 1.6, sigT + 2.3, TOTAL - 0.2, TOTAL], [0, 1, 1, 1]);
    const signOpacity = T > sigT ? sigOp : 0;
    applyStyle(signEl, {
      position: "absolute", left: 0, right: 0, bottom: small ? H * 0.16 : H * 0.14,
      display: "flex", flexDirection: "column", alignItems: "center", gap: small ? 14 : 22,
      opacity: signOpacity, padding: "0 " + edge + "px", boxSizing: "border-box",
      /* Enquanto a assinatura está invisível o link não pode receber clique
         nem foco de teclado. */
      pointerEvents: signOpacity > 0.6 ? "auto" : "none",
      visibility: signOpacity > 0.02 ? "visible" : "hidden",
    });
    applyStyle(signRuleEl, { width: (small ? 120 : 200) * tw(T, sigT + 1.4, 1, 0, 1, eo4) + "px", height: 1, background: accent, opacity: 0.85 });
    applyStyle(signTextEl, {
      fontFamily: SANS, fontWeight: 600, fontSize: (small ? 11 : fmt === "md" ? 15 : 20) + "px",
      letterSpacing: small ? "0.16em" : "0.2em", textTransform: "uppercase", color: PAPER, opacity: 0.72, textAlign: "center",
    });
  }

  /* ---- laço ---- */

  let target = INTRO;
  let introDone = false;
  let prog = 0;
  let raf = 0;

  function measure() {
    const W = scroller.clientWidth || 1280;
    const H = scroller.clientHeight || 720;
    if (W !== state.W || H !== state.H) { state.W = W; state.H = H; return true; }
    return false;
  }

  function onScroll() {
    const max = Math.max(1, scroller.scrollHeight - scroller.clientHeight);
    const p = clamp(scroller.scrollTop / max, 0, 1);
    prog = p;
    if (p > 0.0004) introDone = true;
    target = INTRO + p * (TOTAL - INTRO);
  }

  measure();
  window.addEventListener("resize", () => { if (measure()) render(); });
  if (window.ResizeObserver) {
    const ro = new ResizeObserver(() => { if (measure()) render(); });
    ro.observe(scroller);
  }
  scroller.addEventListener("scroll", onScroll, { passive: true });

  const t0 = performance.now();
  function loop(now) {
    raf = requestAnimationFrame(loop);
    const wall = (now - t0) / 1000;
    let T = state.T;

    if (reduced.matches) {
      /* Sem a abertura animada e sem amortecimento: o tempo passa a ser
         exatamente onde a pessoa parou a rolagem. */
      introDone = true;
      T = target;
    } else if (!introDone) {
      T = tw(wall, 0.25, 1.5, 0, INTRO, eo3);
      if (wall > 1.85) introDone = true;
    } else {
      T = T + (target - T) * 0.16;
      if (Math.abs(target - T) < 0.002) T = target;
    }

    const dp = Math.abs(prog - state.prog);
    if (Math.abs(T - state.T) > 0.0008 || dp > 0.0005 || prog < 0.02) {
      state.T = T; state.wall = wall; state.prog = prog;
      render();
    }
  }
  raf = requestAnimationFrame(loop);
})();
