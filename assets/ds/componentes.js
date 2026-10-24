/* ============================================================
   Jeff DS, superfície Site. Comportamento dos componentes.

   Cinco módulos, todos opcionais: sem este arquivo o conteúdo
   inteiro continua legível e navegável.

   0. Carregamento, a tela que se monta enquanto a página chega.
   1. Revelar na entrada.
   2. Sheet, o menu que desce por cima da página.
   3. Tabs, só a partir de 720px. Abaixo disso a lista aberta lê
      melhor que qualquer aba.
   4. Sumário, que marca a seção na tela e, no celular, abre e
      fecha a lista.
   ============================================================ */

const calmo = window.matchMedia("(prefers-reduced-motion: reduce)");

// Uma duração de tokens.css em milissegundos, para o script
// esperar o mesmo tempo que o CSS anima.
const duracao = (nome) => parseFloat(getComputedStyle(document.documentElement).getPropertyValue(nome)) || 0;


/* ── 0. Carregamento ─────────────────────────────────────
   A animação manda no tempo, não a rede: a cortina fica no mínimo
   o tempo de as camadas chegarem (ou saírem, na volta) e só então
   sai, se a página já tiver carregado. Ao clicar num link interno,
   ela desce antes de trocar de página, e a próxima continua dali.
   Voltando pelo histórico, a animação roda de trás para a frente.
   ──────────────────────────────────────────────── */
(() => {
  const carga = document.querySelector(".carga");
  if (!carga) return;
  if (calmo.matches) { carga.remove(); return; }
  const MINIMO = { ida: 1600, volta: 1950 };

  function sair(modo, inicio) {
    const falta = Math.max(0, MINIMO[modo] - (performance.now() - inicio));
    setTimeout(() => {
      carga.classList.add("carga--pronta");
      setTimeout(() => {
        carga.classList.add("carga--saindo");
        carga.addEventListener("transitionend", () => { carga.hidden = true; }, { once: true });
      }, 220);
    }, falta);
  }
  const modo = document.documentElement.classList.contains("volta") ? "volta" : "ida";
  if (document.readyState === "complete") sair(modo, 0);
  else window.addEventListener("load", () => sair(modo, 0), { once: true });

  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[href]");
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target === "_blank") return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || url.pathname === location.pathname) return;
    e.preventDefault();
    carga.hidden = false;
    carga.className = "carga carga--cobrindo";
    requestAnimationFrame(() => requestAnimationFrame(() => carga.classList.add("carga--desce")));
    setTimeout(() => { location.href = url.href; }, 380);
  });

  // Voltando pelo histórico, a página sai do cache do navegador
  // ainda com a cortina baixada. Dali ela se desmonta ao contrário.
  window.addEventListener("pageshow", (e) => {
    if (!e.persisted) return;
    carga.hidden = false;
    carga.className = "carga";
    void carga.offsetWidth;
    carga.className = "carga carga--volta";
    sair("volta", performance.now());
  });
})();


/* ── 1. Revelar na entrada ─────────────────────────────── */
(() => {
  const alvos = [...document.querySelectorAll("[data-revelar]")];
  if (!alvos.length || calmo.matches || !("IntersectionObserver" in window)) return;
  document.documentElement.classList.add("js-mov");
  const io = new IntersectionObserver((itens) => {
    for (const item of itens) {
      if (!item.isIntersecting) continue;
      item.target.classList.add("revelado");
      io.unobserve(item.target);
    }
  }, { rootMargin: "0px 0px -8% 0px" });
  alvos.forEach((el) => io.observe(el));
})();


/* ── 2. Sheet ──────────────────────────────────────────── */
(() => {
  const botao = document.querySelector("[data-sheet-botao]");
  const sheet = botao && document.getElementById(botao.getAttribute("aria-controls"));
  if (!sheet) return;

  // O fundo escurecido por trás do painel. Um toque nele fecha.
  const fundo = document.createElement("div");
  fundo.className = "sheet__fundo";
  sheet.after(fundo);

  // O painel não usa hidden, porque hidden não deixa animar. Fechado,
  // ele fica com visibility hidden, que também tira os links do Tab.
  function abrir(sim) {
    botao.setAttribute("aria-expanded", String(sim));
    sheet.classList.toggle("sheet--aberto", sim);
    fundo.classList.toggle("sheet__fundo--aberto", sim);
    if (sim) sheet.querySelector("a")?.focus({ preventScroll: true });
  }
  abrir(false);
  botao.addEventListener("click", () => abrir(botao.getAttribute("aria-expanded") !== "true"));
  fundo.addEventListener("click", () => abrir(false));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && botao.getAttribute("aria-expanded") === "true") {
      abrir(false);
      botao.focus();
    }
  });
  // O foco saiu do menu, pelo Tab depois do último link ou por
  // outro caminho: o menu fecha, para não sobrar aberto por cima
  // do que o foco alcançou.
  document.addEventListener("focusin", (e) => {
    if (botao.getAttribute("aria-expanded") === "true" && !sheet.contains(e.target) && e.target !== botao) abrir(false);
  });
})();


/* ── 3. Tabs ───────────────────────────────────────────── */
(() => {
  const largo = window.matchMedia("(min-width: 720px)");

  for (const caixa of document.querySelectorAll("[data-tabs]")) {
    const lista = caixa.querySelector(".tabs__lista");
    const abas = [...caixa.querySelectorAll(".tab")];
    const paineis = abas.map((a) => document.getElementById(a.getAttribute("aria-controls")));
    if (!lista || abas.length < 2 || paineis.some((p) => !p)) continue;
    let atual = 0;

    function escolher(i, comFoco) {
      atual = i;
      abas.forEach((aba, j) => {
        aba.setAttribute("aria-selected", String(j === i));
        aba.tabIndex = j === i ? 0 : -1;
        paineis[j].hidden = j !== i;
      });
      if (comFoco) abas[i].focus();
    }

    function aplicar() {
      if (largo.matches) {
        caixa.classList.add("tabs--js");
        lista.setAttribute("role", "tablist");
        paineis.forEach((p, j) => {
          p.setAttribute("role", "tabpanel");
          p.setAttribute("aria-labelledby", abas[j].id);
        });
        escolher(atual, false);
      } else {
        caixa.classList.remove("tabs--js");
        lista.removeAttribute("role");
        paineis.forEach((p) => {
          p.hidden = false;
          p.removeAttribute("role");
          p.removeAttribute("aria-labelledby");
        });
      }
    }

    abas.forEach((aba, i) => aba.addEventListener("click", () => escolher(i, false)));
    lista.addEventListener("keydown", (e) => {
      const mapa = { ArrowDown: atual + 1, ArrowRight: atual + 1, ArrowUp: atual - 1, ArrowLeft: atual - 1, Home: 0, End: abas.length - 1 };
      if (!(e.key in mapa)) return;
      e.preventDefault();
      escolher((mapa[e.key] + abas.length) % abas.length, true);
    });
    largo.addEventListener("change", aplicar);
    aplicar();
  }
})();


/* ── 4. Sumário ────────────────────────────────────────────
   Marca com aria-current a seção que está na tela: a última cujo
   começo já passou de um terço da altura da janela. No celular,
   pinta as marcas do trilho, mostra o nome da seção enquanto a
   página rola e abre e fecha a lista.
   ──────────────────────────────────────────────── */
(() => {
  const nav = document.querySelector("[data-sumario]");
  if (!nav) return;
  const itens = [...nav.querySelectorAll(".sumario__item")];
  const secoes = itens.map((a) => document.getElementById(a.hash.slice(1)));
  if (!itens.length || secoes.some((s) => !s)) return;
  const botao = nav.querySelector(".sumario__botao");
  const aviso = nav.querySelector(".sumario__aviso");
  const segs = [...nav.querySelectorAll(".sumario__seg")];
  let vez = -2;
  let pedido = 0;
  let calmaria;
  const espera = duracao("--dur-lenta");

  function marcar() {
    pedido = 0;
    const linha = innerHeight / 3;
    let i = -1;
    secoes.forEach((s, j) => { if (s.getBoundingClientRect().top <= linha) i = j; });
    if (i === vez) return;
    vez = i;
    itens.forEach((a, j) => (j === i ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current")));
    segs.forEach((s, j) => { s.dataset.estado = j < i ? "lido" : j === i ? "atual" : ""; });
    if (aviso) aviso.textContent = i < 0 ? "Neste caso" : [...itens[i].children].map((e) => e.textContent).filter(Boolean).join(" ");
  }

  addEventListener("scroll", () => {
    if (!pedido) pedido = requestAnimationFrame(marcar);
    if (aviso) {
      nav.classList.add("sumario--rolando");
      clearTimeout(calmaria);
      calmaria = setTimeout(() => nav.classList.remove("sumario--rolando"), espera);
    }
  }, { passive: true });
  addEventListener("resize", () => { vez = -2; marcar(); });
  marcar();

  if (!botao) return;
  // Abrindo, o foco vai para o primeiro item, como no menu. A lista
  // vem antes do botão no HTML, e sem isso o próximo Tab sairia
  // direto para o conteúdo.
  function abrir(sim) {
    nav.classList.toggle("sumario--aberto", sim);
    botao.setAttribute("aria-expanded", String(sim));
    if (sim) itens[0].focus({ preventScroll: true });
  }
  botao.hidden = false;
  botao.addEventListener("click", () => abrir(botao.getAttribute("aria-expanded") !== "true"));
  itens.forEach((a) => a.addEventListener("click", () => abrir(false)));
  document.addEventListener("click", (e) => { if (!nav.contains(e.target)) abrir(false); });
  document.addEventListener("focusin", (e) => { if (!nav.contains(e.target)) abrir(false); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && botao.getAttribute("aria-expanded") === "true") {
      abrir(false);
      botao.focus();
    }
  });

  // Perto do rodapé, o trilho sai de cena para não
  // cobrir o que está lá.
  const rodape = document.querySelector(".footer");
  if (rodape && "IntersectionObserver" in window) {
    new IntersectionObserver(([e]) => {
      nav.classList.toggle("sumario--escondido", e.isIntersecting);
      if (e.isIntersecting) abrir(false);
    }).observe(rodape);
  }
})();
