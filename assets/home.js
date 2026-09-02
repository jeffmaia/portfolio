/* Menu do topo no celular. O CSS esconde o painel acima de 940px,
   então o script só precisa cuidar do estado abaixo disso. */
(() => {
  const toggle = document.getElementById("nav-toggle");
  const links = document.getElementById("nav-links");
  const bar = document.querySelector(".nav");
  if (!toggle || !links || !bar) return;

  const largo = window.matchMedia("(min-width: 941px)");

  /* O painel abre logo abaixo da barra. Como a barra rola junto com
     a página, o que vale é onde ela está na tela neste instante —
     não a altura dela. Medido na abertura, e a rolagem trava logo
     em seguida, então o valor não envelhece. */
  const medirBarra = () =>
    bar.style.setProperty(
      "--nav-h",
      Math.max(0, bar.getBoundingClientRect().bottom) + "px"
    );

  function abrir(sim) {
    links.classList.toggle("is-open", sim);
    toggle.setAttribute("aria-expanded", String(sim));
    toggle.setAttribute("aria-label", sim ? "Fechar menu" : "Abrir menu");
    document.body.classList.toggle("nav-open", sim);
    if (sim) medirBarra();
  }

  toggle.addEventListener("click", () => {
    abrir(toggle.getAttribute("aria-expanded") !== "true");
  });

  /* Todo item leva para outro lugar, então o painel fecha no clique. */
  links.addEventListener("click", e => { if (e.target.closest("a")) abrir(false); });

  document.addEventListener("keydown", e => { if (e.key === "Escape") abrir(false); });

  /* Girar para paisagem pode cruzar o ponto de corte com o painel
     aberto, e a rolagem ficaria travada. */
  largo.addEventListener("change", e => { if (e.matches) abrir(false); });

  window.addEventListener("resize", medirBarra);
  medirBarra();
  abrir(false);
})();


/* ── Movimento ────────────────────────────────
   Quatro efeitos. Os três últimos são presos à rolagem: andam junto
   com a página, para frente e para trás, em vez de disparar uma vez.

   1. Reveal na entrada — cada peça marcada com data-revelar sobe e
      aparece quando cruza a borda de baixo da tela.

   2. Troca de foto dentro da máscara — cada moldura guarda duas
      fotos. A segunda sobe por dentro da janela da primeira conforme
      a moldura atravessa a tela, uma depois da outra, da esquerda
      para a direita. O JS só escreve --troca; quem recorta é o CSS.

   3. Parallax — a foto desliza dentro da moldura, que fica parada.
      Mover a moldura empurraria o texto vizinho.

   4. Onda entre seções — a borda entre uma seção e a seguinte é um
      recorte redesenhado a cada quadro: a fase acompanha a posição
      da página e a amplitude responde à velocidade da rolagem, com
      volta lenta ao repouso. As três ondas compartilham o mesmo
      caminho, por isso ele vai normalizado de 0 a 1.

   O estado escondido inicial é ligado aqui, não no CSS: se o script
   não rodar, nada fica invisível na página.
   ──────────────────────────────────────────────── */
(() => {
  const calmo = window.matchMedia("(prefers-reduced-motion: reduce)");
  const raiz = document.documentElement;

  /* ── 1. Reveal ── */
  const alvos = [...document.querySelectorAll("[data-revelar]")];
  let varrer = () => {};

  if (alvos.length && !calmo.matches && "IntersectionObserver" in window) {
    raiz.classList.add("js-mov");

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
    varrer = () => {
      if (!pendentes.size) return;
      const limite = window.innerHeight * 0.98;
      for (const el of [...pendentes]) {
        if (el.getBoundingClientRect().top < limite) mostrar(el);
      }
    };

    setTimeout(varrer, 400);
    setTimeout(varrer, 1500);
    window.addEventListener("scroll", varrer, { passive: true });
    window.addEventListener("resize", varrer);
  }

  /* ── 2 e 3. Troca de foto e parallax ── */

  const trocas = [...document.querySelectorAll("[data-troca]")].map((el, i) => ({
    el,
    /* Escalona as três: a da esquerda vira primeiro. O denominador
       devolve a última ao valor cheio no fim do percurso. */
    atraso: i * 0.12,
    valor: 0,
    escrito: -1,
    inicio: 0,
    percurso: 1
  }));
  const ESCALA = 1 - (trocas.length ? (trocas.length - 1) * 0.12 : 0);

  const pecas = [...document.querySelectorAll("[data-parallax]")].map(el => {
    const camada = el.closest(".foto__cam--nova");
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

  /* ── 4. Onda ── */
  /* As três dividem um recorte só: são desenhadas no mesmo quadro e
     na mesma fase, e o clipPath em objectBoundingBox estica a mesma
     forma até a largura de cada seção. Por isso o caminho vai em
     coordenadas de 0 a 1, e não em pixels. */
  const ondas = [...document.querySelectorAll(".onda")].map(el => ({
    el,
    topo: 0,
    altura: 0
  }));
  const recorte = document.getElementById("onda-caminho");

  const ONDA_MEIO = 0.5167, ONDA_N = 40;
  let fase = 0, energia = 0, ultimoY = window.scrollY;

  function desenharOnda(amp) {
    let d = "M0,1 L";
    for (let i = 0; i <= ONDA_N; i++) {
      const x = i / ONDA_N;
      const a = x * 6.283185;
      const y = ONDA_MEIO
        - amp * Math.sin(a + fase)
        - amp * 0.34 * Math.sin(a * 2 - fase * 1.4);
      d += x.toFixed(4) + "," + y.toFixed(4) + " L";
    }
    recorte.setAttribute("d", d + "1,1 Z");
  }

  /* ── Medida e desenho ── */

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

      /* Quanto a imagem pode deslizar antes de descobrir o canto da
         moldura é a sobra de escala, e ela muda com a largura da
         tela. Medir e limitar aqui evita ter que reajustar a
         amplitude a cada ponto de corte. */
      const moldura = p.el.parentElement;
      const sobra = moldura
        ? (r.height - moldura.getBoundingClientRect().height) / 2 - 1
        : 0;
      /* `scale` é propriedade própria e o CSS a aplica DEPOIS do
         transform, então o que se escreve aqui chega na tela
         multiplicado por ela. Sem dividir, um deslocamento de 30px
         vira 36,6px e descobre a borda da moldura. */
      const esc = parseFloat(getComputedStyle(p.el).scale) || 1;
      p.sobra = Math.max(0, sobra) / esc;
      p.usar = Math.sign(p.amp) * Math.min(Math.abs(p.amp), p.sobra);
      /* A subida divide a mesma sobra com o parallax; a soma dos dois
         é limitada na hora de escrever, então nunca aparece borda. */
      p.subida = p.sobra * 0.8;
    }
    /* A troca é medida no percurso da própria moldura: começa quando
       o topo dela chega a 80% da tela e termina meia tela depois.
       Meia tela é curto de propósito — as três precisam terminar de
       trocar enquanto ainda estão à vista, não na hora em que a
       faixa já está saindo pelo topo. */
    const vh0 = window.innerHeight || 800;
    for (const t of trocas) {
      const r = t.el.getBoundingClientRect();
      t.inicio = Math.max(0, r.top + window.scrollY - vh0 * 0.80);
      t.percurso = vh0 * 0.5;
    }
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

    /* — Troca de foto — */
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

    /* — Parallax, com a subida somada no mesmo deslocamento — */
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

    /* — Onda — */
    let ondaVisivel = false;
    if (recorte && ondas.length) {
      const v = y - ultimoY;
      ultimoY = y;
      /* Sobe depressa com a rolagem e volta devagar ao repouso: é
         essa assimetria que faz a onda parecer acompanhar a mão. */
      const alvo = Math.min(1, Math.abs(v) / 55);
      energia += (alvo - energia) * (alvo > energia ? 0.4 : 0.05);
      if (energia < 0.002) energia = 0;
      /* A fase segue a posição da página; a deriva lenta no tempo
         mantém a onda viva mesmo com a página parada. */
      fase = y * 0.0022 + (t || 0) * 0.00016;
      for (const o of ondas) {
        const rel = o.topo - y;
        if (rel < -o.altura - 100 || rel > vh + 100) continue;
        ondaVisivel = true;
        break;
      }
      /* Uma altura de onda vale 1 aqui, então a amplitude vai na
         mesma escala: 12 de 120 na forma em repouso. */
      if (ondaVisivel) desenharOnda(0.1 + energia * 0.1417);
    }

    /* O laço só continua enquanto houver onda na tela ou sobra de
       energia. Fora disso a página fica parada e nada roda. */
    if (ondaVisivel || energia > 0) laco();
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
      /* Sem movimento não há troca: fica a primeira foto de cada
         moldura, igual ao que aparece quando o script não roda. */
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

  /* As fontes de display e as fotos chegam depois e mudam a altura
     do hero: sem remedir, as bases ficariam alguns pixels erradas. */
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(remedir);
  window.addEventListener("load", remedir);
})();
