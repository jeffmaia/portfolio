/* ============================================================
   Caso — o que a página de um caso faz por cima da base

   Duas coisas, e nenhuma delas carrega conteúdo:

   1. A régua de leitura no topo.
   2. As barras de tempo, que crescem quando entram na tela.

   Tudo o que se lê está no HTML, aberto. Esta página não tem aba,
   acordeão nem troca de estado: cinco entregas, cinco fases e as
   quatro dimensões do antes e depois ficam todas à vista, e é o
   arranjo da grade que separa uma da outra.

   O menu, o reveal e a onda vêm de base.js, carregada antes desta.
   ============================================================ */

/* ── 1. Régua de leitura ──────────────────────────── */
(() => {
  const regua = document.getElementById("regua");
  if (!regua) return;

  let agendado = false;

  function medir() {
    agendado = false;
    const rolavel = document.documentElement.scrollHeight - window.innerHeight;
    const lido = rolavel > 0 ? window.scrollY / rolavel : 0;
    regua.style.setProperty("--lido", Math.min(1, Math.max(0, lido)).toFixed(4));
  }

  function pedir() {
    if (!agendado) { agendado = true; requestAnimationFrame(medir); }
  }

  window.addEventListener("scroll", pedir, { passive: true });
  window.addEventListener("resize", pedir);
  medir();
})();


/* ── 2. As barras de tempo ────────────────────────────
   Nascem em zero e crescem quando o bloco entra na tela. Sem JS a
   largura final já está no HTML e elas aparecem prontas.
   ──────────────────────────────────────────────── */
(() => {
  const blocos = [...document.querySelectorAll("[data-barras]")];
  if (!blocos.length || !("IntersectionObserver" in window)) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  const olho = new IntersectionObserver(entradas => {
    for (const e of entradas) {
      if (!e.isIntersecting) continue;
      /* Um pouco depois do reveal do bloco, para as duas coisas não
         acontecerem no mesmo quadro. */
      setTimeout(() => e.target.classList.add("crescido"), 260);
      olho.unobserve(e.target);
    }
  }, { rootMargin: "0px 0px -15% 0px", threshold: 0.2 });

  for (const b of blocos) olho.observe(b);

  /* Mesma rede de segurança do reveal: barra vazia é conteúdo
     perdido, então uma varredura por tempo repete a decisão. */
  setTimeout(() => {
    for (const b of blocos) {
      if (b.getBoundingClientRect().top < window.innerHeight) b.classList.add("crescido");
    }
  }, 1500);
})();


/* ── 3. As abas da saída ────────────────────────────
   Cinco entregas que saem da mesma camada. Empilhadas elas viravam
   uma lista de cinco itens quase iguais; em abas os cinco nomes
   ficam à vista de uma vez e quem escolhe o que ler é o leitor.

   Sem JS nada se esconde: os cinco painéis aparecem um debaixo do
   outro, cada um com o próprio nome em cima. A classe que a folha
   de estilo espera para esconder os painéis é escrita aqui, então
   ela só existe quando existe alguém para trocar de aba.
   ──────────────────────────────────────────────── */
(() => {
  for (const caixa of document.querySelectorAll("[data-abas]")) {
    const abas = [...caixa.querySelectorAll('[role="tab"]')];
    const paineis = abas.map(a => document.getElementById(a.getAttribute("aria-controls")));
    if (abas.length < 2 || paineis.some(p => !p)) continue;

    caixa.classList.add("abas--js");

    function mostrar(i, comFoco) {
      abas.forEach((aba, j) => {
        const ativa = j === i;
        aba.setAttribute("aria-selected", String(ativa));
        /* Uma parada de tabulação para o conjunto, não cinco: dentro
           da fila quem anda é a seta. */
        aba.tabIndex = ativa ? 0 : -1;
        paineis[j].hidden = !ativa;
      });
      if (comFoco) abas[i].focus();
    }

    abas.forEach((aba, i) => {
      aba.addEventListener("click", () => mostrar(i));
      aba.addEventListener("keydown", e => {
        const n = abas.length;
        let alvo = null;
        if (e.key === "ArrowRight" || e.key === "ArrowDown") alvo = (i + 1) % n;
        else if (e.key === "ArrowLeft" || e.key === "ArrowUp") alvo = (i - 1 + n) % n;
        else if (e.key === "Home") alvo = 0;
        else if (e.key === "End") alvo = n - 1;
        if (alvo === null) return;
        e.preventDefault();
        mostrar(alvo, true);
      });
    });

    mostrar(0);
  }
})();
