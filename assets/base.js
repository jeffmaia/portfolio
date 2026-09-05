/* ============================================================
   Base: o que toda página do site divide

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

   O que é de uma página só mora no script dela
   (home.js, caso.js), carregado depois deste.
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
     barra, ela inverte; do contrário a marca preta some. */
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

  /* A barra atravessa de cor em 0,35s quando o fundo debaixo dela
     troca. Na primeira pintura não há travessia nenhuma a fazer: ela
     tem que nascer já na cor do fundo. Sem isso, uma página que abre
     no escuro passa esse terço de segundo com a marca preta em cima
     de preto, invisível. */
  let primeira = true;

  function pintar() {
    if (primeira) {
      primeira = false;
      barra.classList.add("nav--sem-travessia");
      requestAnimationFrame(() => barra.classList.remove("nav--sem-travessia"));
    }

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

  /* O módulo da passagem precisa fechar o painel no tempo dele. */
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
     roda e o observador pode não disparar; o setTimeout roda. */
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
   trás, em vez de disparar uma vez. As ondas de seção dividem um
   recorte só: são desenhadas no mesmo quadro e na mesma fase, e o
   clipPath em objectBoundingBox estica a mesma forma até a largura
   de cada seção. Por isso o caminho vai em coordenadas de 0 a 1, e
   não em pixels.

   Três coisas mexem na forma:
     fase    segue a posição da página, então a onda caminha de
             lado conforme se rola;
     energia segue a velocidade, e engrossa a onda na mão pesada;
     deriva  segue o SENTIDO. Rolando para baixo a linha inteira
             desce; para cima, sobe. É o que faz a onda dizer para
             onde a página está indo, e não só que ela se mexeu.

   Duas ondas não são iguais às outras: as que carregam uma seta.
   Nelas a curva incha num morro no meio da largura, e a seta fica
   dentro do morro. Cada uma tem o seu recorte porque o morro do
   rodapé cresce com a rolagem e o da cena não.
   ──────────────────────────────────────────────── */
(() => {
  const recorte = document.getElementById("onda-caminho");
  const bolha = document.getElementById("onda-caminho-bolha");
  const subirCaminho = document.getElementById("onda-caminho-subir");
  const subir = document.querySelector(".subir");

  const ondas = [...document.querySelectorAll(".onda")].map(el => ({ el, topo: 0, altura: 0 }));
  if (!recorte && !bolha && !subirCaminho) return;

  const ONDA_MEIO = 0.5167, ONDA_N = 40;
  /* Uma onda com bolha tem o dobro da altura de uma comum. Para a
     linha de repouso cair no mesmo lugar da página, ela desce para
     a média entre a de sempre e o pé do elemento, e a amplitude
     inteira vale metade. */
  const BOLHA_MEIO = (ONDA_MEIO + 1) / 2;
  const BOLHA_X = 0.5;
  /* O morro tem largura em pixels, não em fração: uma tela larga
     não deve ganhar um morro largo, senão ele deixa de ser um
     morro e vira a onda toda.

     Em tela estreita a conta se inverte. A altura do morro para de
     encolher antes da tela, porque --onda-bolha-h tem um mínimo (a
     seta que mora dentro dele não encolhe), então os mesmos 40px de
     largura viram um espeto. Abaixo de 900px a largura abre até
     47px, e o morro volta a ser morro. */
  const BOLHA_SIG_PX = 40, BOLHA_SIG_PX_ESTREITO = 47, BOLHA_ESTREITO = 900, BOLHA_CURSO = 420;
  /* O morro da cena não muda de tamanho. O do rodapé cresce de
     BOLHA_MIN a BOLHA_MAX conforme a página chega ao fim, e é esse
     crescimento que levanta a seta: ela não sobe por conta, ela
     senta no topo do morro e sobe porque o morro subiu. */
  const BOLHA_MAX = 0.55, BOLHA_MIN = 0.28;

  let fase = 0, energia = 0, deriva = 0;
  let ultimoY = window.scrollY, agendado = false;
  let sig = 0.03, amostras = [];
  let pEscrito = -1;

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

  /* Amostragem desigual: passo largo na onda inteira e passo curto
     na faixa do morro, que é onde a curva muda depressa. Uniforme,
     ou o morro sairia poligonal, ou a onda inteira sairia cara. */
  function medirAmostras() {
    const largura = (ondas.length && ondas[0].el.getBoundingClientRect().width) || window.innerWidth;
    const abre = Math.min(1, Math.max(0, (BOLHA_ESTREITO - largura) / BOLHA_CURSO));
    const sigPx = BOLHA_SIG_PX + (BOLHA_SIG_PX_ESTREITO - BOLHA_SIG_PX) * abre;
    sig = Math.min(0.14, Math.max(0.014, sigPx / (largura || 1)));
    const a = Math.max(0, BOLHA_X - 3.6 * sig), b = Math.min(1, BOLHA_X + 3.6 * sig);
    const xs = [];
    for (let i = 0; i <= 48; i++) { const x = i / 48; if (x <= a || x >= b) xs.push(x); }
    for (let i = 0; i <= 40; i++) xs.push(a + ((b - a) * i) / 40);
    xs.sort((p, q) => p - q);
    amostras = xs;
  }

  /* `alt` é a altura do morro em unidades do próprio elemento, que
     tem duas alturas de onda.

     Devolve onde ficou o alto do morro, medido do pé do elemento
     para cima. Quem carrega a seta é esse número: a onda oscila, e
     uma seta presa a uma distância fixa acabaria fora do preto na
     primeira rolagem forte. Presa ao topo, ela nunca sai de dentro
     do morro. */
  function desenharBolha(caminho, amp, desl, alt) {
    let d = "M0,1 L", topo = 1;
    for (const x of amostras) {
      const a = x * 6.283185;
      const t = (x - BOLHA_X) / sig;
      const y = BOLHA_MEIO + desl * 0.5
        - amp * 0.5 * Math.sin(a + fase)
        - amp * 0.5 * 0.34 * Math.sin(a * 2 - fase * 1.4)
        - alt * Math.exp(-0.5 * t * t);
      if (y < topo) topo = y;
      d += x.toFixed(4) + "," + y.toFixed(4) + " L";
    }
    caminho.setAttribute("d", d + "1,1 Z");
    return 1 - topo;
  }

  /* Um número por morro, no documento inteiro: a seta da cena mora
     no hero, e não dentro da seção que carrega a onda dela. */
  const raiz = document.documentElement;
  let picoCena = -1, picoSubir = -1;
  function anotarPico(nome, guardado, valor) {
    const arred = Math.round(valor * 1000) / 1000;
    if (arred !== guardado) raiz.style.setProperty(nome, String(arred));
    return arred;
  }

  function medir() {
    for (const o of ondas) {
      const r = o.el.getBoundingClientRect();
      o.topo = r.top + window.scrollY;
      o.altura = r.height;
    }
    medirAmostras();
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

    let visivel = false;
    for (const o of ondas) {
      const rel = o.topo - y;
      if (rel < -o.altura - 100 || rel > vh + 100) continue;
      visivel = true;
      break;
    }

    /* Uma altura de onda vale 1 aqui, então tanto a amplitude
       quanto o deslocamento vão na mesma escala. */
    const amp = 0.1 + energia * 0.1417, desl = deriva * 0.15;
    if (visivel) {
      if (recorte) desenharOnda(amp, desl);
      if (bolha) picoCena = anotarPico("--pico-cena", picoCena, desenharBolha(bolha, amp, desl, BOLHA_MAX));
      vivo = true;
    }

    /* A seta de voltar ao topo e o morro que a carrega. Quem manda
       é a posição da própria seta, não a do rodapé: assim ela sobe
       exatamente enquanto atravessa a tela, e não antes de
       aparecer. No chão quando o topo dela encosta na borda de
       baixo; no alto do morro meia tela acima disso. */
    if (subirCaminho && subir) {
      const r = subir.getBoundingClientRect();
      const curso = Math.min(vh * 0.6, 460) || 1;
      let p = (vh - r.top) / curso;
      p = p < 0 ? 0 : p > 1 ? 1 : p;
      const arred = Math.round(p * 200) / 200;
      if (arred !== pEscrito || visivel) {
        pEscrito = arred;
        const alt = BOLHA_MIN + (BOLHA_MAX - BOLHA_MIN) * arred;
        picoSubir = anotarPico("--pico-subir", picoSubir, desenharBolha(subirCaminho, amp, desl, alt));
        if (arred > 0 && arred < 1) vivo = true;
      }
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
         HTML: a mesma que aparece quando o script não roda. */
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

  /* As fontes chegam depois e mudam a altura das seções: sem
     remedir, as bases ficariam alguns pixels erradas. */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(remedir);
  window.addEventListener("load", remedir);
})();


/* ── A passagem de uma página para outra ────────────────────────
   Ao clicar num link interno: a tela fica coberta, o que estava
   escrito se apaga, o J entra e o traço debaixo dele enche. Só
   então a página seguinte é pedida. Do outro lado o J sai, a cortina sai atrás
   dele e a página nova aparece por baixo.

   Quem cobre depende de onde veio o clique. De dentro do menu, é o
   painel crescendo até a tela toda; de um link da página, é a
   cortina aparecendo por cima.

   O que diz à página seguinte que ela deve entrar assim é uma
   marca no sessionStorage, lida por um script no <head> dela. Se
   qualquer parte disso falhar, o navegador só navega, que é o
   comportamento normal do link.
   ──────────────────────────────────────────────── */
(() => {
  const cortina = document.querySelector(".transicao");
  if (!cortina || CALMO.matches) return;

  /* Fixo, e não medido: a barra debaixo do J não sabe nada sobre a
     página que vem, então o que ela mostra é sempre o mesmo tempo.
     1000ms é o traço terminando de encher; os 40ms de sobra são
     para ele ser visto cheio antes de a página trocar. */
  const ESPERA = 1040;

  /* A volta pelo histórico pode devolver a página do cache com a
     cortina ainda por cima; limpar aí é obrigatório. Só aí: numa
     entrada normal o pageshow dispara junto com o carregamento, e
     limpar nele apagaria a cortina de chegada antes de ela sair. */
  window.addEventListener("pageshow", e => {
    if (!e.persisted) return;
    cortina.classList.remove("saindo");
    document.documentElement.classList.remove("chegando", "saindo--menu");
    destravar();
  });

  /* O painel cresce por medida escrita nele, não por regra de
     folha: height:auto não transiciona, então a altura de partida
     precisa ser um número. Isso deixa três propriedades presas no
     elemento, e voltar do cache do histórico com elas presas
     entregaria o painel do tamanho da tela. */
  function destravar() {
    const menu = window.__menu;
    if (!menu) return;
    menu.painel.style.height = "";
    menu.painel.style.minHeight = "";
    menu.painel.style.maxHeight = "";
  }

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
     clique e se fecharia sozinho. A marca posta aqui primeiro é o
     que o faz desistir, porque na passagem o painel não fecha, ele
     cresce até cobrir a tela. */
  document.addEventListener("click", e => {
    if (e.defaultPrevented || e.button !== 0) return;
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;

    const a = e.target.closest("a");
    const destino = interno(a);
    if (!destino) return;

    e.preventDefault();
    a.dataset.passagem = "1";

    const raiz = document.documentElement;

    /* Saindo de dentro do menu, quem cobre a tela é o painel. Ele
       precisa de três medidas antes de a altura começar a andar:
       onde o miolo está, para prendê-lo ali; e a altura de agora,
       porque uma transição de altura precisa de um número dos dois
       lados. O reflow no meio é o que separa os dois números em
       dois estados; sem ele o navegador vê só o segundo. */
    const menu = window.__menu;
    if (menu && menu.estaAberto()) {
      const painel = menu.painel;
      const miolo = painel.querySelector(".menu__inner");
      if (miolo) painel.style.setProperty("--saida-topo", miolo.offsetTop + "px");
      painel.style.height = painel.offsetHeight + "px";
      painel.style.minHeight = "0px";
      painel.style.maxHeight = "none";
      raiz.classList.add("saindo--menu");
      void painel.offsetHeight;
      painel.style.height = "calc(100vh + var(--onda-h))";
    }

    cortina.classList.add("saindo");
    try { sessionStorage.setItem("jm-passagem", "1"); } catch (_) {}

    /* O pedido sai agora, um segundo antes da troca, e não em
       file://, onde ele só daria erro. Não é otimização de carga: é
       o que faz o buraco preto entre uma página e outra ser sempre
       do mesmo tamanho. A parte roteirizada da passagem já tem tempo
       fixo; a espera pela rede é a única coisa que ainda variava. */
    if (location.protocol === "http:" || location.protocol === "https:") {
      try { fetch(destino, { credentials: "same-origin" }).catch(() => {}); } catch (_) {}
    }

    setTimeout(() => { location.href = destino; }, ESPERA);

    /* Se a navegação não acontecer (pedido recusado, destino que
       não responde), a cortina não pode ficar cobrindo a página
       para sempre. */
    setTimeout(() => {
      cortina.classList.remove("saindo");
      raiz.classList.remove("saindo--menu");
      destravar();
    }, ESPERA + 4000);
  }, true);
})();
