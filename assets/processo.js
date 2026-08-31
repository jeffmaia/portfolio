(() => {
  /* Os artefatos que saem das habilidades do Claude. O que interessa em cada
     um não é o rascunho em si, é o destino dele depois de gerado. */
  const ARTIFACTS = [
    {
      name: "Visão de produto",
      title: "Vira direção antes de virar backlog",
      body: "A habilidade lê a transcrição do ritual e devolve o rascunho da visão. O time revisa e ajusta, em vez de escrever do zero depois da conversa."
    },
    {
      name: "PRD",
      title: "Chega pronto para discussão, não para redação",
      body: "Com o PRD já rascunhado, a Planning deixou de ser um rito semanal. Acontece sob demanda, e a maior parte dela é assíncrona."
    },
    {
      name: "User stories (US)",
      title: "Entram no Kanban já documentadas",
      body: "O refinamento virou tirar dúvida sobre o que já está escrito na story e desenhado no protótipo. Foi o que derrubou o ritual de quatro horas para quarenta minutos."
    },
    {
      name: "Relatório de usabilidade",
      title: "Análise no lugar de rodada de teste",
      body: "O Claude aponta problema de fluxo com consistência, usando heurística de Norman e Nielsen mais o que a gente já sabe do público da Omni."
    },
    {
      name: "Protótipo",
      title: "Nasce desenvolvido e segue direto para a engenharia",
      body: "O protótipo sai do Claude Design e vai para o Claude Code, de onde a engenharia assume. Design usa o Claude Code para manter a biblioteca fiel à do código, que é a referência principal."
    }
  ];

  const PHASES = [
    {
      id: "01",
      name: "Identificação de oportunidades",
      body: "Dado de produto, pesquisa e canais de feedback alimentam uma árvore de oportunidades que facilita escolher o que entra em pauta.",
      owner: "Produto e design, com dados alimentando a árvore."
    },
    {
      id: "02",
      name: "Validação de desejabilidade e diferencial",
      body: "Confirmamos se a aposta faz sentido antes de o time gastar tempo desenhando a solução.",
      owner: "Produto e design."
    },
    {
      id: "03",
      name: "Definição e prototipagem",
      body: "É aqui que nasce a maior parte da solução. O protótipo já sai desenvolvido e segue para a engenharia sem etapa de tradução no meio.",
      owner: "Produto, design e engenharia, com prototipação distribuída entre os três."
    },
    {
      id: "04",
      name: "Delivery",
      body: "Alfa na engenharia, que garante o funcionamento do que foi construído. Beta, aberto ou fechado, validando o experimento antes de abrir para todos.",
      owner: "Engenharia no alfa, time inteiro no beta."
    },
    {
      id: "05",
      name: "Depois do lançamento",
      body: "O foco vira satisfação e adoção. A validação qualitativa entra quando o dado quantitativo mostra desvio do esperado.",
      owner: "Produto, design e dados, junto de GA e GTM."
    }
  ];

  const COMPARE = [
    { label: "Prototipação", before: "Concentrada em design", after: "Distribuída entre produto, design e engenharia" },
    { label: "Validação qualitativa", before: "Quase sempre antes do desenvolvimento", after: "Depois do lançamento, quando o dado mostra desvio do esperado" },
    { label: "Rituais", before: "Longos e na agenda", after: "Curtos e assíncronos" },
    { label: "Testes A/B", before: "Poucas variações, porque cada uma custava caro para construir", after: "Muitas variações, porque desenvolver ficou ágil e barato" }
  ];

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* — fluxo: artefatos e seus destinos — */
  const flowChips = document.getElementById("flow-chips");
  const noteEl = document.getElementById("flow-note");
  const noteTitle = document.getElementById("flow-note-title");
  const noteBody = document.getElementById("flow-note-body");

  const chipRefs = ARTIFACTS.map((artifact, i) => {
    const chip = document.createElement("button");
    chip.type = "button";
    chip.className = "flow-chip";
    chip.setAttribute("role", "tab");
    chip.textContent = artifact.name;
    chip.addEventListener("click", () => setArtifact(i));
    flowChips.appendChild(chip);
    return chip;
  });

  function renderNote(index) {
    noteTitle.textContent = ARTIFACTS[index].title;
    noteBody.textContent = ARTIFACTS[index].body;
  }

  let activeArtifact = 0;

  function setArtifact(index) {
    activeArtifact = index;
    chipRefs.forEach((chip, i) => chip.setAttribute("aria-selected", String(i === index)));
    renderNote(index);
  }

  /* No celular o mesmo conteúdo vira acordeão: o destino abre colado no artefato
     clicado, em vez de aparecer num painel abaixo da lista inteira. */
  const accordion = document.getElementById("flow-accordion");

  const accRefs = ARTIFACTS.map((artifact, i) => {
    const item = document.createElement("div");
    item.className = "flow-acc__item";
    item.innerHTML =
      '<button class="flow-acc__head" type="button" aria-expanded="false"></button>' +
      '<div class="flow-acc__panel" hidden><span class="flow-acc__title"></span><p></p></div>';

    const head = item.querySelector(".flow-acc__head");
    const panel = item.querySelector(".flow-acc__panel");
    head.id = "acc-head-" + i;
    panel.id = "acc-panel-" + i;
    head.setAttribute("aria-controls", panel.id);
    panel.setAttribute("role", "region");
    panel.setAttribute("aria-labelledby", head.id);
    head.textContent = artifact.name;
    panel.querySelector(".flow-acc__title").textContent = artifact.title;
    panel.querySelector("p").textContent = artifact.body;
    head.addEventListener("click", () => toggleAcc(i));
    accordion.appendChild(item);
    return { head, panel };
  });

  /* Um aberto por vez: com todos abertos a seção vira o texto corrido que o
     acordeão existe para evitar. */
  function toggleAcc(index) {
    const willOpen = accRefs[index].head.getAttribute("aria-expanded") !== "true";
    accRefs.forEach((refs, i) => {
      const on = i === index && willOpen;
      refs.head.setAttribute("aria-expanded", String(on));
      refs.panel.hidden = !on;
    });
  }

  /* — funil — */
  const funnelList = document.getElementById("funnel-list");
  const funnelDetail = document.getElementById("funnel-detail");
  const funnelId = document.getElementById("funnel-id");
  const funnelTitle = document.getElementById("funnel-title");
  const funnelBody = document.getElementById("funnel-body");
  const funnelOwner = document.getElementById("funnel-owner");

  const phaseRefs = PHASES.map((phase, i) => {
    const stage = document.createElement("button");
    stage.type = "button";
    stage.className = "funnel__stage";
    stage.setAttribute("role", "tab");
    stage.id = "phase-tab-" + phase.id;
    stage.innerHTML =
      '<span class="funnel__head"><span class="funnel__num"></span><span class="funnel__name"></span></span>';
    stage.querySelector(".funnel__num").textContent = phase.id;
    stage.querySelector(".funnel__name").textContent = phase.name;
    stage.addEventListener("click", () => setPhase(i));
    funnelList.appendChild(stage);
    return { stage };
  });

  const phaseDots = document.getElementById("phase-dots");

  const dotRefs = PHASES.map((phase, i) => {
    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "dot";
    dot.setAttribute("aria-label", "Fase " + phase.id);
    dot.addEventListener("click", () => setPhase(i));
    phaseDots.appendChild(dot);
    return dot;
  });

  let activePhase = 0;

  function renderPhase(index) {
    const phase = PHASES[index];
    funnelDetail.setAttribute("aria-labelledby", "phase-tab-" + phase.id);
    funnelId.textContent = phase.id;
    funnelTitle.textContent = phase.name;
    funnelBody.textContent = phase.body;
    funnelOwner.textContent = phase.owner;
  }

  function setPhase(index) {
    activePhase = index;
    phaseRefs.forEach((refs, i) => refs.stage.setAttribute("aria-selected", String(i === index)));
    dotRefs.forEach((dot, i) => dot.setAttribute("aria-current", String(i === index)));
    renderPhase(index);
  }

  document.getElementById("phase-prev").addEventListener("click", () => {
    setPhase((activePhase + PHASES.length - 1) % PHASES.length);
  });
  document.getElementById("phase-next").addEventListener("click", () => {
    setPhase((activePhase + 1) % PHASES.length);
  });

  /* — antes e depois — */
  const compare = document.getElementById("compare");
  const compareRows = document.getElementById("compare-rows");
  const tabBefore = document.getElementById("compare-before");
  const tabAfter = document.getElementById("compare-after");

  const rowRefs = COMPARE.map(row => {
    const el = document.createElement("div");
    el.className = "blueprint compare__row";
    el.innerHTML = '<span class="compare__label"></span><p class="compare__text"></p>';
    el.querySelector(".compare__label").textContent = row.label;
    compareRows.appendChild(el);
    return { el, text: el.querySelector(".compare__text") };
  });

  let compareState = "before";
  let swapTimer = null;

  function writeRows(state) {
    rowRefs.forEach((refs, i) => { refs.text.textContent = COMPARE[i][state]; });
  }

  function setCompare(state) {
    if (state === compareState) return;
    compareState = state;
    const isAfter = state === "after";
    compare.classList.toggle("is-after", isAfter);
    tabBefore.setAttribute("aria-selected", String(!isAfter));
    tabAfter.setAttribute("aria-selected", String(isAfter));

    /* O texto sai, troca no escuro e volta, para a leitura não pular de uma
       frase para outra no meio da transição. */
    if (reduceMotion) { writeRows(state); return; }
    clearTimeout(swapTimer);
    rowRefs.forEach(refs => refs.el.classList.add("is-swapping"));
    swapTimer = setTimeout(() => {
      writeRows(state);
      rowRefs.forEach(refs => refs.el.classList.remove("is-swapping"));
    }, 280);
  }

  tabBefore.addEventListener("click", () => setCompare("before"));
  tabAfter.addEventListener("click", () => setCompare("after"));

  /* — gráfico de tempo — */
  const timeFills = Array.from(document.querySelectorAll(".access-fill"));
  let timeTimer = null;

  const growTime = () => timeFills.forEach(fill => { fill.style.width = fill.dataset.width + "%"; });
  const resetTime = () => timeFills.forEach(fill => { fill.style.width = "0%"; });

  function playTime(delay) {
    clearTimeout(timeTimer);
    if (reduceMotion) { growTime(); return; }
    resetTime();
    timeTimer = setTimeout(growTime, delay);
  }

  /* Cada painel fica do tamanho do seu estado mais alto. Sem isso a caixa
     encolhe e cresce a cada troca, e o que está abaixo dela pula junto; travar
     por rolagem interna resolveria a altura mas esconderia texto. */
  function lockHeight(el, count, render) {
    el.style.minHeight = "";
    let tallest = 0;
    for (let i = 0; i < count; i++) {
      render(i);
      tallest = Math.max(tallest, el.getBoundingClientRect().height);
    }
    el.style.minHeight = Math.ceil(tallest) + "px";
  }

  function lockAll() {
    lockHeight(noteEl, ARTIFACTS.length, renderNote);
    renderNote(activeArtifact);
    lockHeight(funnelDetail, PHASES.length, renderPhase);
    renderPhase(activePhase);
    /* Uma altura só para as quatro dimensões, tirada do texto mais longo entre
       todas: no celular elas ficam empilhadas, e caixas de tamanhos diferentes
       fariam a troca parecer que mudou mais do que o texto. */
    let tallestRow = 0;
    rowRefs.forEach((refs, i) => {
      refs.el.style.minHeight = "";
      ["before", "after"].forEach(state => {
        refs.text.textContent = COMPARE[i][state];
        tallestRow = Math.max(tallestRow, refs.el.getBoundingClientRect().height);
      });
    });
    rowRefs.forEach((refs, i) => {
      refs.el.style.minHeight = Math.ceil(tallestRow) + "px";
      refs.text.textContent = COMPARE[i][compareState];
    });
  }

  setArtifact(0);
  toggleAcc(0);
  setPhase(0);
  writeRows("before");
  playTime(520);
  lockAll();

  /* A altura mais alta muda quando a linha quebra em outro ponto, então ela é
     recalculada quando a largura muda e quando a fonte real substitui a de
     fallback. */
  let lockTimer = null;
  let lastWidth = window.innerWidth;
  window.addEventListener("resize", () => {
    if (window.innerWidth === lastWidth) return;
    lastWidth = window.innerWidth;
    clearTimeout(lockTimer);
    lockTimer = setTimeout(lockAll, 180);
  });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(lockAll);
})();
