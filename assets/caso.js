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
