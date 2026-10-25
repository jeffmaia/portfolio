/* ============================================================
   Caso: o que a página de um caso faz por cima da base

   Quatro coisas, e nenhuma delas carrega conteúdo:

   1. A régua de leitura no topo.
   2. As barras de tempo, que crescem quando entram na tela.
   3. As abas da saída, que no celular viram carrossel.
   4. As trilhas que deitam no celular.

   Tudo o que se lê está no HTML, aberto. Nada aqui escreve texto,
   esconde texto que não tenha outro lugar por onde ser alcançado,
   nem inventa peça de interface: sem script os cinco painéis e as
   cinco fases aparecem todos à vista, um debaixo do outro, e é o
   arranjo da grade que separa um do outro.

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


/* ── 3. As abas da saída, e o carrossel que elas viram ──
   Cinco entregas que saem da mesma camada. Empilhadas elas viravam
   uma lista de cinco itens quase iguais; em abas os cinco nomes
   ficam à vista de uma vez e quem escolhe o que ler é o leitor.

   No celular a fila de nomes não cabe deitada, então ela descia em
   índice e o painel abria embaixo: uma lista de cinco frases longas
   e, depois dela, o texto de uma só. O índice comia a tela antes de
   a leitura começar. Abaixo de 720 o componente troca de natureza:
   os cinco painéis viram cartões lado a lado, o índice sai, e quem
   nomeia cada cartão é o título que já existe dentro dele, o mesmo
   que aparece quando não há script.

   As duas formas são o mesmo HTML. O que muda de uma para a outra é
   o papel de cada peça, e o papel é escrito aqui, não no arquivo:
   sem script nada se esconde e nada rola de lado, os cinco painéis
   aparecem um debaixo do outro com o nome de cada um em cima.
   ──────────────────────────────────────────────── */
(() => {
  const estreito = window.matchMedia("(max-width: 719px)");

  for (const caixa of document.querySelectorAll("[data-abas]")) {
    const lista = caixa.querySelector(".abas__lista");
    const trilha = caixa.querySelector(".abas__paineis");
    const abas = [...caixa.querySelectorAll(".aba")];
    const paineis = abas.map(a => document.getElementById(a.getAttribute("aria-controls")));
    if (!lista || !trilha || abas.length < 2 || paineis.some(p => !p)) continue;

    const rotulo = lista.getAttribute("aria-label") || "";
    let atual = 0;
    let modo = null;

    function mostrar(i, comFoco) {
      atual = i;
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

    function virarAbas() {
      caixa.classList.remove("abas--carrossel");
      caixa.classList.add("abas--js");
      lista.hidden = false;
      lista.setAttribute("role", "tablist");
      trilha.removeAttribute("role");
      trilha.removeAttribute("aria-label");
      trilha.removeAttribute("tabindex");
      abas.forEach(a => a.setAttribute("role", "tab"));
      paineis.forEach((p, j) => {
        p.setAttribute("role", "tabpanel");
        p.setAttribute("aria-labelledby", abas[j].id);
        p.tabIndex = 0;
      });
      mostrar(atual);
    }

    function virarCarrossel() {
      caixa.classList.remove("abas--js");
      caixa.classList.add("abas--carrossel");
      /* O índice sai inteiro. Os cinco nomes voltam para dentro dos
         cartões, e duas listas dos mesmos cinco nomes na mesma tela
         seria uma a mais. Ele sai da árvore de acessibilidade junto:
         botão que não aparece e não leva a lugar nenhum é ruído. */
      lista.hidden = true;
      lista.removeAttribute("role");
      abas.forEach(a => {
        a.removeAttribute("role");
        a.removeAttribute("aria-selected");
        a.tabIndex = -1;
      });
      /* Os painéis deixam de ser painéis de aba: os cinco estão à
         vista ao mesmo tempo, e chamar de tabpanel o que não se
         esconde é mentir para o leitor de tela. Viram cinco blocos
         com título, que é o que eles são. */
      paineis.forEach(p => {
        p.hidden = false;
        p.removeAttribute("role");
        p.removeAttribute("aria-labelledby");
        p.removeAttribute("tabindex");
      });
      /* Quem rola agora é a trilha, então é ela que precisa de nome
         e de uma parada de tabulação: sem isso o que passou da
         beirada não existe para quem anda de teclado. */
      trilha.setAttribute("role", "group");
      if (rotulo) trilha.setAttribute("aria-label", rotulo);
      trilha.tabIndex = 0;
      trilha.scrollLeft = 0;
    }

    function ajustar() {
      const alvo = estreito.matches ? "carrossel" : "abas";
      if (alvo === modo) return;
      modo = alvo;
      if (alvo === "carrossel") virarCarrossel();
      else virarAbas();
    }

    abas.forEach((aba, i) => {
      aba.addEventListener("click", () => { if (modo === "abas") mostrar(i); });
      aba.addEventListener("keydown", e => {
        if (modo !== "abas") return;
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

    ajustar();
    estreito.addEventListener("change", ajustar);
    /* Rede de segurança: no WebKit o evento da media query nem sempre
       chega quando a janela muda de largura duas vezes seguidas, e a
       forma errada numa tela girada é pior do que uma comparação a
       mais por quadro. ajustar sai na primeira linha quando o modo
       não mudou, então o custo disto é uma leitura de matches. */
    window.addEventListener("resize", ajustar);
  }
})();


/* ── 4. As trilhas que deitam no celular ────────────
   O funil não tem aba nenhuma: são cinco fases numa lista, e no
   celular a lista também deita e vira carrossel. Aqui não há papel
   nenhum para trocar, só a consequência de a lista passar a rolar
   por dentro: ela precisa de nome e de uma parada de tabulação,
   senão o que está além da beirada não existe para quem anda de
   teclado. Nas larguras em que ela não rola, os dois saem, porque
   uma parada de tabulação que não leva a nada é uma a mais.
   ──────────────────────────────────────────────── */
(() => {
  const trilhas = [...document.querySelectorAll("[data-carrossel]")];
  if (!trilhas.length) return;

  const estreito = window.matchMedia("(max-width: 719px)");
  let deitado = null;

  function ajustar() {
    if (estreito.matches === deitado) return;
    deitado = estreito.matches;
    for (const t of trilhas) {
      if (deitado) {
        t.tabIndex = 0;
        const rotulo = t.getAttribute("data-carrossel");
        if (rotulo) t.setAttribute("aria-label", rotulo);
      } else {
        t.removeAttribute("tabindex");
        t.removeAttribute("aria-label");
      }
    }
  }

  ajustar();
  estreito.addEventListener("change", ajustar);
  window.addEventListener("resize", ajustar);
})();
