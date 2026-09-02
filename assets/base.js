/* ============================================================
   Base — o que toda página do site divide

   1. O menu: uma barra fixa que vive fechada, a marca que encolhe
      até a inicial ao rolar, e o painel em contorno que abre por
      cima de parte da tela.
   2. O reveal na entrada: cada peça marcada com data-revelar sobe
      e aparece quando cruza a borda de baixo da tela.
   3. As ondas: a borda de cada seção é um recorte redesenhado a
      cada quadro. A fase segue a posição da página, a amplitude
      responde à velocidade e a linha inteira sobe ou desce
      conforme o sentido da rolagem. É a onda que diz para onde a
      página está indo.
   4. A passagem de uma página para outra.

   O que é de uma página só mora no script dela — home.js, caso.js
   —, carregado depois deste.
   ============================================================ */

const CALMO = window.matchMedia("(prefers-reduced-motion: reduce)");


/* ── A barra e o menu ────────────────────────────────
   O painel é o menu inteiro, em qualquer largura de tela. Sem
   script a folha de estilo o deixa aberto no fluxo e esconde o
   botão, então nenhum link fica inalcançável.
   ──────────────────────────────────────────────── */
(() => {
  const barra = document.querySelector(".nav");
  const botao = document.getElementById("menu-btn");
  const painel = document.getElementById("menu");
  if (!barra || !botao || !painel) return;

  /* Os fundos escuros da página. Quando um deles passa debaixo da
     barra, ela inverte — do contrário a marca preta some. */
  const escuros = [...document.querySelectorAll(
    '[data-fundo="escuro"], .tinta, .footer, .cena'
  )];
  let faixas = [];

  function medir() {
    faixas = escuros.map(el => {
      const r = el.getBoundingClientRect();
      return { topo: r.top + window.scrollY, base: r.bottom + window.scrollY };
    });
  }

  let aberto = false;

  function abrir(sim) {
    aberto = sim;
    painel.classList.toggle("aberto", sim);
    botao.setAttribute("aria-expanded", String(sim));
    botao.setAttribute("aria-label", sim ? "Fechar menu" : "Abrir menu");
    painel.setAttribute("aria-hidden", String(!sim));
    document.body.classList.toggle("menu-aberto", sim);
    barra.classList.toggle("nav--aberta", sim);
    pintar();
  }

  function pintar() {
    const y = window.scrollY;
    barra.classList.toggle("nav--rolada", y > 8);
    barra.classList.toggle("nav--reduzida", y > 90);

    /* Com o painel aberto o fundo debaixo da barra é o painel, que
       já é escuro: não adianta consultar a página. */
    if (aberto) { barra.classList.add("nav--tinta"); return; }

    const linha = y + barra.getBoundingClientRect().height * 0.55;
    let tinta = false;
    for (const f of faixas) {
      if (linha >= f.topo && linha < f.base) { tinta = true; break; }
    }
    barra.classList.toggle("nav--tinta", tinta);
  }

  botao.addEventListener("click", () => abrir(!aberto));

  /* Todo item leva para outro lugar; o painel fecha no clique.
     Quem cuida da saída em si é o módulo da passagem, abaixo. */
  painel.addEventListener("click", e => {
    const a = e.target.closest("a");
    if (a && !a.dataset.passagem) abrir(false);
  });

  document.addEventListener("keydown", e => { if (e.key === "Escape" && aberto) abrir(false); });

  let agendado = false;
  const laco = () => {
    if (agendado) return;
    agendado = true;
    requestAnimationFrame(() => { agendado = false; pintar(); });
  };

  window.addEventListener("scroll", laco, { passive: true });
  window.addEventListener("resize", () => { medir(); pintar(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { medir(); pintar(); });
  window.addEventListener("load", () => { medir(); pintar(); });

  medir();
  abrir(false);

  /* O módulo da passagem precisa fechar o painel e crescê-lo. */
  window.__menu = { abrir, painel, estaAberto: () => aberto };
})();


/* ── Reveal na entrada ────────────────────────────────
   O estado escondido inicial é ligado aqui, não no CSS: se o script
   não rodar, nada fica invisível na página.
   ──────────────────────────────────────────────── */
(() => {
  const alvos = [...document.querySelectorAll("[data-revelar]")];
  if (!alvos.length || CALMO.matches || !("IntersectionObserver" in window)) return;

  document.documentElement.classList.add("js-mov");

  for (const el of alvos) {
    const n = parseInt(el.dataset.revelarAtraso || "0", 10);
    if (n) el.style.setProperty("--atraso", n * 90 + "ms");
  }

  const pendentes = new Set(alvos);

  function mostrar(el) {
    el.classList.add("revelado");
    pendentes.delete(el);
    olho.unobserve(el);          // revela uma vez e sai do caminho
  }

  const olho = new IntersectionObserver(entradas => {
    for (const e of entradas) if (e.isIntersecting) mostrar(e.target);
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0.05 });

  for (const el of alvos) olho.observe(el);

  /* Rede de segurança. Deixar conteúdo preso em opacidade zero é
     uma falha grave demais para depender de um caminho só: esta
     varredura repete a decisão do observador na unha e é chamada
     por tempo e por rolagem também. Em aba de fundo o rAF não
     roda e o observador pode não disparar — o setTimeout roda. */
  function varrer() {
    if (!pendentes.size) return;
    const limite = window.innerHeight * 0.98;
    for (const el of [...pendentes]) {
      if (el.getBoundingClientRect().top < limite) mostrar(el);
    }
  }

  setTimeout(varrer, 400);
  setTimeout(varrer, 1500);
  window.addEventListener("scroll", varrer, { passive: true });
  window.addEventListener("resize", varrer);
})();


/* ── As ondas ────────────────────────────────
   Presas à rolagem: andam junto com a página, para frente e para
   trás, em vez de disparar uma vez. Todas as ondas de seção
   dividem um recorte só — são desenhadas no mesmo quadro e na
   mesma fase, e o clipPath em objectBoundingBox estica a mesma
   forma até a largura de cada seção. Por isso o caminho vai em
   coordenadas de 0 a 1, e não em pixels.

   Três coisas mexem na forma:
     fase    — segue a posição da página, então a onda caminha de
               lado conforme se rola;
     energia — segue a velocidade, e engrossa a onda na mão pesada;
     deriva  — segue o SENTIDO. Rolando para baixo a linha inteira
               desce; para cima, sobe. É o que faz a onda dizer
               para onde a página está indo, e não só que ela se
               mexeu.

   A água do botão de voltar ao topo é desenhada aqui também: mesma
   fase, mesma onda, outro copo.
   ──────────────────────────────────────────────── */
(() => {
  const recorte = document.getElementById("onda-caminho");
  const agua = document.getElementById("onda-agua");
  const subir = document.querySelector(".subir");

  const ondas = [...document.querySelectorAll(".onda")].map(el => ({ el, topo: 0, altura: 0 }));
  if (!recorte && !agua) return;

  const ONDA_MEIO = 0.5167, ONDA_N = 40;
  const AGUA_N = 18;
  let fase = 0, energia = 0, deriva = 0;
  let ultimoY = window.scrollY, agendado = false;
  let pEscrito = -1, aguaVazia = false;

  function desenharOnda(amp, desl) {
    let d = "M0,1 L";
    for (let i = 0; i <= ONDA_N; i++) {
      const x = i / ONDA_N;
      const a = x * 6.283185;
      const y = ONDA_MEIO + desl
        - amp * Math.sin(a + fase)
        - amp * 0.34 * Math.sin(a * 2 - fase * 1.4);
      d += x.toFixed(4) + "," + y.toFixed(4) + " L";
    }
    recorte.setAttribute("d", d + "1,1 Z");
  }

  /* O copo tem 72 de lado. A linha da água vai de 78 (vazio, logo
     abaixo do círculo) a -6 (cheio, logo acima dele). */
  function desenharAgua(p, amp) {
    const base = 78 - p * 84;
    let d = "M-6," + (base + 2).toFixed(2) + " L";
    for (let i = 0; i <= AGUA_N; i++) {
      const x = -6 + (84 * i) / AGUA_N;
      const a = (i / AGUA_N) * 6.283185;
      const y = base - amp * Math.sin(a * 1.5 + fase) - amp * 0.4 * Math.sin(a * 3 - fase);
      d += x.toFixed(2) + "," + y.toFixed(2) + " L";
    }
    agua.setAttribute("d", d + "78,84 L-6,84 Z");
  }

  function medir() {
    for (const o of ondas) {
      const r = o.el.getBoundingClientRect();
      o.topo = r.top + window.scrollY;
      o.altura = r.height;
    }
  }

  function desenhar(t) {
    agendado = false;
    const vh = window.innerHeight;
    const y = window.scrollY;

    const v = y - ultimoY;
    ultimoY = y;
    /* Sobe depressa com a rolagem e volta devagar ao repouso: é
       essa assimetria que faz a onda parecer acompanhar a mão. */
    const alvo = Math.min(1, Math.abs(v) / 55);
    energia += (alvo - energia) * (alvo > energia ? 0.4 : 0.05);
    if (energia < 0.002) energia = 0;

    /* O sentido some mais devagar que a energia: a onda ainda está
       voltando ao meio quando a rolagem já parou, e é essa sobra
       que se lê como o gesto. */
    const sentido = v > 0.5 ? 1 : v < -0.5 ? -1 : 0;
    const alvoD = sentido * Math.min(1, Math.abs(v) / 40);
    deriva += (alvoD - deriva) * (Math.abs(alvoD) > Math.abs(deriva) ? 0.28 : 0.06);
    if (Math.abs(deriva) < 0.002) deriva = 0;

    /* A fase segue a posição da página; a deriva lenta no tempo
       mantém a onda viva mesmo com a página parada. */
    fase = y * 0.0022 + (t || 0) * 0.00016;

    let vivo = energia > 0.002 || Math.abs(deriva) > 0.002;

    if (recorte) {
      let visivel = false;
      for (const o of ondas) {
        const rel = o.topo - y;
        if (rel < -o.altura - 100 || rel > vh + 100) continue;
        visivel = true;
        break;
      }
      /* Uma altura de onda vale 1 aqui, então tanto a amplitude
         quanto o deslocamento vão na mesma escala. */
      if (visivel) desenharOnda(0.1 + energia * 0.1417, deriva * 0.15);
      vivo = vivo || visivel;
    }

    /* — A água do voltar ao topo — */
    if (agua && subir) {
      const r = subir.getBoundingClientRect();
      /* Quem manda é a posição do próprio copo, não a do rodapé:
         assim a água sobe exatamente enquanto ele atravessa a tela,
         e não antes de ele aparecer. Vazio quando o topo dele
         encosta na borda de baixo, cheio meia tela acima disso. */
      const curso = Math.min(vh * 0.6, 460) || 1;
      let p = (vh - r.top) / curso;
      p = p < 0 ? 0 : p > 1 ? 1 : p;
      const arred = Math.round(p * 200) / 200;
      if (arred !== pEscrito) {
        subir.style.setProperty("--subir", String(arred));
        pEscrito = arred;
      }
      if (p > 0) { desenharAgua(p, 2.4 + energia * 2); aguaVazia = false; vivo = true; }
      else if (!aguaVazia) { desenharAgua(0, 2.4); aguaVazia = true; }
    }

    if (vivo) laco();
  }

  function laco() {
    if (!agendado) { agendado = true; requestAnimationFrame(desenhar); }
  }

  function remedir() { medir(); laco(); }

  function ligar() {
    if (CALMO.matches) {
      /* Sem movimento, tudo fica na forma que já veio desenhada no
         HTML — a mesma que aparece quando o script não roda. */
      window.removeEventListener("scroll", laco);
      window.removeEventListener("resize", remedir);
      return;
    }
    window.addEventListener("scroll", laco, { passive: true });
    window.addEventListener("resize", remedir);
    remedir();
  }

  CALMO.addEventListener("change", ligar);
  ligar();

  /* As fontes de display chegam depois e mudam a altura das seções:
     sem remedir, as bases ficariam alguns pixels erradas. */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(remedir);
  window.addEventListener("load", remedir);
})();


/* ── A passagem de uma página para outra ────────────────────────
   Ao clicar num link interno: o painel cresce até cobrir a tela, a
   cortina desce por cima com a marca e a barra que carrega, e só
   então a página seguinte é pedida. Do outro lado ela continua o
   mesmo movimento — sai por baixo, não volta por cima.

   O que diz à página seguinte que ela deve entrar assim é uma
   marca no sessionStorage, lida por um script no <head> dela. Se
   qualquer parte disso falhar, o navegador só navega, que é o
   comportamento normal do link.
   ──────────────────────────────────────────────── */
(() => {
  const cortina = document.querySelector(".transicao");
  if (!cortina || CALMO.matches) return;

  const ESPERA = 560;   // cobre (420ms) e segura um instante

  /* A volta pelo histórico pode devolver a página do cache com a
     cortina ainda por cima; limpar aí é obrigatório. Só aí: numa
     entrada normal o pageshow dispara junto com o carregamento, e
     limpar nele apagaria a cortina de chegada antes de ela sair. */
  window.addEventListener("pageshow", e => {
    if (!e.persisted) return;
    cortina.classList.remove("saindo");
    document.documentElement.classList.remove("chegando");
  });

  function interno(a) {
    if (!a || !a.href) return false;
    if (a.target && a.target !== "_self") return false;
    if (a.hasAttribute("download")) return false;
    const u = new URL(a.href, location.href);
    if (u.origin !== location.origin) return false;
    if (!/\.html?$/.test(u.pathname) && !u.pathname.endsWith("/")) return false;
    /* Âncora na mesma página é rolagem, não passagem. */
    if (u.pathname === location.pathname && u.search === location.search) return false;
    return u.href;
  }

  /* Na captura, e não na subida: o painel do menu também escuta o
     clique, e é este módulo que precisa marcar o link primeiro —
     é a marca que diz ao painel para crescer em vez de fechar. */
  document.addEventListener("click", e => {
    if (e.defaultPrevented || e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    const a = e.target.closest("a");
    const destino = interno(a);
    if (!destino) return;

    e.preventDefault();
    a.dataset.passagem = "1";

    /* Se a saída foi de dentro do menu, é ele que começa o
       movimento: cresce até a tela toda e a cortina continua. */
    const menu = window.__menu;
    if (menu && menu.estaAberto()) menu.painel.classList.add("crescendo");

    cortina.classList.add("saindo");
    try { sessionStorage.setItem("jm-passagem", "1"); } catch (_) {}

    setTimeout(() => { location.href = destino; }, ESPERA);

    /* Se a navegação não acontecer — pedido recusado, destino que
       não responde —, a cortina não pode ficar cobrindo a página
       para sempre. */
    setTimeout(() => {
      cortina.classList.remove("saindo");
      if (menu) menu.painel.classList.remove("crescendo");
    }, ESPERA + 4000);
  }, true);
})();
