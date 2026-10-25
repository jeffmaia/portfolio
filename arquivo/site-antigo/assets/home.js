/* ============================================================
   Home

   Dois módulos, os dois presos à rolagem:

   1. Os selos do hero: cada fotografia dentro das frases guarda
      duas imagens. A segunda sobe por dentro da janela da primeira
      conforme a frase atravessa a tela, uma depois da outra, da
      esquerda para a direita. O JS só escreve --troca; quem recorta
      é o CSS. Por cima disso, um parallax curto: a foto desliza
      dentro do selo, que fica parado, porque mover o selo empurraria as
      palavras vizinhas.

   2. A cena dos casos: o palco gruda no alto da tela e a rolagem
      passa a trocar o que está dentro dele. Um caso de cada vez, o
      orbe descendo e pulsando nas passagens, o trilho dizendo
      onde se está.

   O menu, o reveal, as ondas e a passagem entre páginas vêm de
   base.js, carregada antes desta.
   ============================================================ */

const calmo = window.matchMedia("(prefers-reduced-motion: reduce)");


/* ── Os selos do hero ──────────────────────────────── */
(() => {
  const trocas = [...document.querySelectorAll("[data-troca]")].map((el, i) => ({
    el,
    /* Escalona os três: o da esquerda vira primeiro. O denominador
       devolve o último ao valor cheio no fim do percurso. */
    atraso: i * 0.12,
    valor: 0,
    escrito: -1,
    inicio: 0,
    percurso: 1
  }));
  const ESCALA = 1 - (trocas.length ? (trocas.length - 1) * 0.12 : 0);

  const pecas = [...document.querySelectorAll("[data-parallax]")].map(el => {
    const camada = el.closest(".selo__cam--nova");
    return {
      el,
      amp: parseFloat(el.dataset.parallax) || 0,
      /* Só a foto de cima sobe: é ela que está entrando na máscara. */
      sobe: camada ? trocas.find(t => t.el.contains(camada)) || null : null,
      subida: 0,
      usar: 0,
      sobra: 0,
      centro: 0,
      altura: 0
    };
  });
  if (!trocas.length && !pecas.length) return;

  let agendado = false;

  function medir() {
    for (const p of pecas) {
      p.el.style.transform = "";
      const r = p.el.getBoundingClientRect();
      /* A base é medida com o transform limpo: ler o retângulo já
         deslocado realimentaria a conta e o efeito se anularia.
         O `scale` do CSS é propriedade própria, não entra no
         transform, então continua valendo aqui. */
      p.centro = r.top + window.scrollY + r.height / 2;
      p.altura = r.height;

      /* Quanto a imagem pode deslizar antes de descobrir o canto do
         selo é a sobra de escala, e ela muda com o corpo do texto.
         Medir e limitar aqui evita reajustar a amplitude a cada
         ponto de corte. */
      const moldura = p.el.parentElement;
      const sobra = moldura
        ? (r.height - moldura.getBoundingClientRect().height) / 2 - 1
        : 0;
      /* `scale` é propriedade própria e o CSS a aplica DEPOIS do
         transform, então o que se escreve aqui chega na tela
         multiplicado por ela. Sem dividir, o deslocamento estoura a
         borda do selo. */
      const esc = parseFloat(getComputedStyle(p.el).scale) || 1;
      p.sobra = Math.max(0, sobra) / esc;
      p.usar = Math.sign(p.amp) * Math.min(Math.abs(p.amp), p.sobra);
      /* A subida divide a mesma sobra com o parallax; a soma dos dois
         é limitada na hora de escrever, então nunca aparece borda. */
      p.subida = p.sobra * 0.8;
    }
    /* A troca é medida no percurso do próprio selo: começa quando o
       topo dele chega a 80% da tela e termina meia tela depois.
       Meia tela é curto de propósito: os três precisam terminar de
       trocar enquanto a frase ainda está à vista. */
    const vh0 = window.innerHeight || 800;
    for (const t of trocas) {
      const r = t.el.getBoundingClientRect();
      t.inicio = Math.max(0, r.top + window.scrollY - vh0 * 0.80);
      t.percurso = vh0 * 0.5;
    }
  }

  function desenhar() {
    agendado = false;
    const vh = window.innerHeight;
    const y = window.scrollY;

    /* Troca de foto */
    for (const tr of trocas) {
      let u = (y - tr.inicio) / tr.percurso;
      u = (u - tr.atraso) / ESCALA;
      u = u < 0 ? 0 : u > 1 ? 1 : u;
      tr.valor = u * u * (3 - 2 * u);            // suaviza as pontas
      const arred = Math.round(tr.valor * 500) / 500;
      if (arred !== tr.escrito) {
        tr.el.style.setProperty("--troca", String(arred));
        tr.escrito = arred;
      }
    }

    /* Parallax, com a subida somada no mesmo deslocamento */
    const meio = vh / 2;
    for (const p of pecas) {
      const rel = p.centro - y;
      if (rel < -p.altura - 200 || rel > vh + 200) continue;   // fora da tela
      let prog = (meio - rel) / (meio + p.altura / 2);
      if (prog > 1) prog = 1; else if (prog < -1) prog = -1;
      let d = prog * p.usar;
      if (p.sobe) d += (1 - p.sobe.valor) * p.subida;
      if (d > p.sobra) d = p.sobra; else if (d < -p.sobra) d = -p.sobra;
      p.el.style.transform = "translate3d(0," + d.toFixed(2) + "px,0)";
    }
  }

  function laco() {
    if (!agendado) { agendado = true; requestAnimationFrame(desenhar); }
  }

  function remedir() { medir(); laco(); }

  function limpar() {
    for (const p of pecas) p.el.style.transform = "";
    /* Volta ao mesmo estado de quem carrega a página sem JS: a foto
       de cima recolhida, só a primeira à vista. */
    for (const tr of trocas) { tr.el.style.removeProperty("--troca"); tr.escrito = -1; }
  }

  function ligar() {
    if (calmo.matches) {
      limpar();
      window.removeEventListener("scroll", laco);
      window.removeEventListener("resize", remedir);
      return;
    }
    window.addEventListener("scroll", laco, { passive: true });
    window.addEventListener("resize", remedir);
    remedir();
  }

  calmo.addEventListener("change", ligar);
  ligar();

  /* As fontes chegam depois e mudam o corpo das frases, e com ele o
     tamanho dos selos: sem remedir, as bases ficariam erradas. */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(remedir);
  window.addEventListener("load", remedir);
})();


/* ── A cena dos casos ────────────────────────────────
   O palco só gruda quando há espaço para ele: uma cena presa numa
   tela baixa esconde metade do caso, e presa num celular briga com
   a barra do navegador, que muda de altura ao rolar. Fora dessas
   condições (e sem script, e com movimento reduzido) os quatro
   casos ficam empilhados no fluxo, cada um inteiro.
   ──────────────────────────────────────────────── */
(() => {
  const cena = document.querySelector(".cena");
  if (!cena) return;

  const atos = [...cena.querySelectorAll(".ato")];
  const valores = [...cena.querySelectorAll("[data-orbe-valor]")];
  const legendas = [...cena.querySelectorAll("[data-orbe-legenda]")];
  const orbe = cena.querySelector(".cena__orbe");
  const disco = cena.querySelector(".orbe__disco");
  const contador = cena.querySelector("[data-contador]");
  const marcas = [...cena.querySelectorAll("[data-ir]")];
  const N = atos.length;
  if (N < 2) return;

  cena.style.setProperty("--atos", String(N));

  /* Espaço suficiente para um caso inteiro caber de pé. */
  const cabe = window.matchMedia("(min-width: 940px) and (min-height: 700px)");

  let viva = false, agendado = false, atual = -1;
  let topo = 0, curso = 1;

  function medir() {
    const r = cena.getBoundingClientRect();
    topo = r.top + window.scrollY;
    curso = Math.max(1, cena.offsetHeight - window.innerHeight);
  }

  function desenhar() {
    agendado = false;
    if (!viva) return;

    let p = (window.scrollY - topo) / curso;
    p = p < 0 ? 0 : p > 1 ? 1 : p;
    const pos = p * (N - 1);

    for (let i = 0; i < N; i++) {
      const d = pos - i;
      /* Some antes de o vizinho chegar: a fresta escura no meio da
         passagem é o que dá o corte entre um caso e outro. */
      let t = 1 - Math.abs(d) * 1.55;
      t = t < 0 ? 0 : t > 1 ? 1 : t;
      const e = t * t * (3 - 2 * t);
      const a = atos[i];
      a.style.opacity = e.toFixed(3);
      a.style.transform = "translate3d(0," + (d * -44).toFixed(1) + "px,0)";
      a.classList.toggle("ato--frente", t > 0.5);
      /* inert e não aria-hidden: o ato apagado tem um link dentro, e
         esconder do leitor de tela sem tirar do caminho do Tab
         deixaria um link invisível e alcançável. inert faz as duas
         coisas de uma vez. */
      a.inert = t <= 0.5;
      if (valores[i]) valores[i].style.opacity = e.toFixed(3);
      if (legendas[i]) legendas[i].style.opacity = e.toFixed(3);
    }

    /* O orbe desce ao longo da cena inteira e encolhe no meio de
       cada passagem: cheio parado, menor em movimento. */
    if (orbe) orbe.style.setProperty("--orbe-y", p.toFixed(4));
    if (disco) {
      const frac = pos - Math.floor(pos);
      disco.style.setProperty("--orbe-esc", (1 - 0.34 * Math.sin(Math.PI * frac)).toFixed(3));
    }

    const i = Math.round(pos);
    if (i !== atual) {
      atual = i;
      if (contador) contador.textContent = String(i + 1).padStart(2, "0");
      for (let k = 0; k < marcas.length; k++) {
        marcas[k].setAttribute("aria-current", k === i ? "true" : "false");
      }
    }
  }

  function laco() {
    if (!agendado) { agendado = true; requestAnimationFrame(desenhar); }
  }

  /* O primeiro desenho é síncrono de propósito. Em aba de fundo o
     rAF pode não rodar por muito tempo, e como o CSS zera a
     opacidade dos quatro atos no modo cena, esperar por um quadro
     que talvez nunca venha deixaria a seção em branco. */
  function remedir() { medir(); desenhar(); }

  function limpar() {
    for (const a of atos) {
      a.style.opacity = "";
      a.style.transform = "";
      a.classList.remove("ato--frente");
      a.inert = false;
    }
    for (const v of valores) v.style.opacity = "";
    for (const l of legendas) l.style.opacity = "";
    if (orbe) orbe.style.removeProperty("--orbe-y");
    if (disco) disco.style.removeProperty("--orbe-esc");
    atual = -1;
  }

  function ligar() {
    const querido = cabe.matches && !calmo.matches;
    if (querido === viva) return;
    viva = querido;
    cena.classList.toggle("cena--viva", viva);

    if (!viva) {
      limpar();
      window.removeEventListener("scroll", laco);
      window.removeEventListener("resize", remedir);
      return;
    }
    window.addEventListener("scroll", laco, { passive: true });
    window.addEventListener("resize", remedir);
    remedir();
  }

  /* Cada traço do trilho leva direto ao seu ato. */
  for (const b of marcas) {
    b.addEventListener("click", () => {
      if (!viva) {
        atos[+b.dataset.ir].scrollIntoView({ behavior: calmo.matches ? "auto" : "smooth", block: "center" });
        return;
      }
      window.scrollTo({
        top: topo + (+b.dataset.ir / (N - 1)) * curso,
        behavior: calmo.matches ? "auto" : "smooth"
      });
    });
  }

  cabe.addEventListener("change", ligar);
  calmo.addEventListener("change", ligar);
  ligar();

  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { if (viva) remedir(); });
  window.addEventListener("load", () => { if (viva) remedir(); });
})();
