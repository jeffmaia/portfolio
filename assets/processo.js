(() => {
  /* Os artefatos que saem das habilidades do Claude. O que interessa em cada
     um não é o rascunho em si, é o destino dele depois de gerado. */
  const ARTIFACTS = [
    {
      name: "Visão de produto",
      title: "Vira direção antes de virar backlog",
      body: "A habilidade lê a transcrição do ritual e devolve um rascunho de visão. O time revisa e ajusta, em vez de escrever do zero depois da conversa."
    },
    {
      name: "PRD",
      title: "Chega pronto para discussão, não para redação",
      body: "Com o PRD já rascunhado, a Planning deixou de ser um rito frequente. Acontece só quando necessário, e a maior parte dela é feita de forma documentada e assíncrona."
    },
    {
      name: "Stories",
      title: "Entram no Kanban já documentadas",
      body: "O refinamento passou a ser só tirar dúvida sobre o que já está escrito na story e desenhado no protótipo. Foi o que derrubou o ritual de quatro ou cinco horas para trinta ou quarenta minutos."
    },
    {
      name: "Relatório de usabilidade",
      title: "Análise no lugar de rodada de teste",
      body: "Boa parte dos testes frequentes foi reduzida porque o Claude passou a apontar com assertividade onde um fluxo pode ter problema, com base em padrões como os de Norman e Nielsen e no comportamento já conhecido do público da Omni."
    },
    {
      name: "Protótipo",
      title: "Sai desenvolvido e segue direto para a engenharia",
      body: "O protótipo já nasce desenvolvido no Claude Design e vai para o Claude Code, que a engenharia assume dali em diante. Os designers usam o Claude Code para garantir que a biblioteca usada no Claude Design está fiel à do código, que é a referência principal."
    }
  ];

  const MOVES = [
    {
      id: "01",
      title: "Rituais redesenhados",
      body: "O formato de Scrum deixou de funcionar e o time migrou para Kanban. A Planning deixou de ser um rito frequente e acontece só quando necessário, com a maior parte dela documentada e assíncrona.",
      body2: "As dailies no formato antigo deixaram de existir, com participação ativa apenas da engenharia e de produto somente quando necessário. Os refinamentos, que chegavam a durar de quatro a cinco horas por semana, caíram para trinta a quarenta minutos.",
      effect: "A agenda parou de ser o lugar onde o trabalho acontece e virou o lugar onde a dúvida é resolvida."
    },
    {
      id: "02",
      title: "Design conectado à entrega",
      body: "O próprio protótipo já sai desenvolvido no Claude Design e segue direto para o Claude Code, que a engenharia assume a partir dali.",
      body2: "Os designers também usam o Claude Code para garantir que a biblioteca do Design System usada no Claude Design está fiel à biblioteca do código, que é a referência principal.",
      effect: "O caminho entre a decisão de design e o código deixou de ter uma etapa de tradução no meio."
    },
    {
      id: "03",
      title: "Usabilidade como habilidade de análise",
      body: "Boa parte dos testes de usabilidade que antes eram feitos com frequência foi reduzida, porque o Claude passou a fazer uma análise assertiva sobre onde um fluxo podia ter problema.",
      body2: "Isso virou uma habilidade de análise de usabilidade baseada em padrões como os de Norman e Nielsen, além do comportamento e do perfil já conhecidos do público da Omni.",
      effect: "A pesquisa com pessoa foi realocada para onde ela decide algo, não para confirmar o previsível."
    },
    {
      id: "04",
      title: "Métricas em conversa, não em dashboard",
      body: "As discussões de time passaram a focar muito mais em como medir o que está sendo lançado e quais são as métricas fundamentais.",
      body2: "A conexão direta com dados no Mixpanel reduziu o uso frequente de dashboards fixos, substituído por uma versão conversacional que já gera o artefato com a métrica que garante se a entrega foi um sucesso.",
      effect: "A pergunta “como vamos saber se deu certo” passou a ter resposta na mesma conversa em que ela aparece."
    }
  ];

  /* A largura da barra desenha o funil: o topo é largo porque entra muito
     sinal, e cada fase seguinte carrega menos coisa adiante. */
  const PHASES = [
    {
      id: "01",
      name: "Identificação de oportunidades",
      width: 100,
      body: "Mapeamentos internos, dados de produto, pesquisa e canais de feedback alimentam uma árvore de oportunidades que facilita a escolha do que entra em pauta.",
      owner: "Produto e design, com dados alimentando a árvore."
    },
    {
      id: "02",
      name: "Validação de desejabilidade e diferencial",
      width: 80,
      body: "Análise de mercado e de usuário para confirmar se a aposta faz sentido antes de o time gastar tempo desenhando a solução.",
      owner: "Produto e design."
    },
    {
      id: "03",
      name: "Definição e prototipagem",
      width: 62,
      body: "É aqui que nasce a maior parte da solução. O protótipo já sai desenvolvido e segue para a engenharia sem uma etapa de tradução no meio.",
      owner: "Produto, design e engenharia, com prototipação distribuída entre os três."
    },
    {
      id: "04",
      name: "Delivery",
      width: 44,
      body: "A fase alfa é responsabilidade da engenharia, que garante o funcionamento do que foi construído. A fase beta, aberta ou fechada, valida os experimentos antes da decisão de abrir para todos ou seguir para GTM.",
      owner: "Engenharia no alfa, time inteiro no beta."
    },
    {
      id: "05",
      name: "Depois do lançamento",
      width: 28,
      body: "O foco passa a ser satisfação e adoção do que acabou de ir ao ar, com a validação qualitativa acionada quando o dado quantitativo mostra desvio do esperado.",
      owner: "Produto, design e dados, junto de GA e GTM."
    }
  ];

  const COMPARE = [
    { label: "Prototipação", before: "Concentrada em design", after: "Distribuída entre produto, design e engenharia" },
    { label: "Validação qualitativa", before: "Quase sempre antes do desenvolvimento", after: "Depois do lançamento, quando o dado quantitativo mostra desvio do esperado" },
    { label: "Rituais", before: "Longos e presenciais na agenda", after: "Curtos e assíncronos" },
    { label: "Testes A/B", before: "Poucas variações, porque cada uma custava caro para construir", after: "Muito mais variações, porque desenvolver ficou ágil e barato" }
  ];

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* — fluxo: artefatos e seus destinos — */
  const flowChips = document.getElementById("flow-chips");
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

  function setArtifact(index) {
    chipRefs.forEach((chip, i) => chip.setAttribute("aria-selected", String(i === index)));
    noteTitle.textContent = ARTIFACTS[index].title;
    noteBody.textContent = ARTIFACTS[index].body;
  }

  /* — decisões do novo processo: lista no desktop, paginador no celular — */
  const movesList = document.getElementById("moves-list");
  const moveDots = document.getElementById("move-dots");
  const moveDetail = document.getElementById("move-detail");
  const moveId = document.getElementById("move-id");
  const moveTitle = document.getElementById("move-title");
  const moveBody = document.getElementById("move-body");
  const moveBody2 = document.getElementById("move-body2");
  const moveEffect = document.getElementById("move-effect");

  const moveRefs = MOVES.map((move, i) => {
    const item = document.createElement("button");
    item.type = "button";
    item.className = "blueprint layer-item";
    item.setAttribute("role", "tab");
    item.id = "move-tab-" + move.id;
    item.innerHTML = '<span class="layer-num"></span><span class="layer-title"></span>';
    item.querySelector(".layer-num").textContent = move.id;
    item.querySelector(".layer-title").textContent = move.title;
    item.addEventListener("click", () => setMove(i));
    movesList.appendChild(item);

    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "dot";
    dot.setAttribute("aria-label", "Decisão " + move.id);
    dot.addEventListener("click", () => setMove(i));
    moveDots.appendChild(dot);

    return { item, dot };
  });

  let activeMove = 0;

  function setMove(index) {
    activeMove = index;
    moveRefs.forEach((refs, i) => {
      const on = i === index;
      refs.item.setAttribute("aria-selected", String(on));
      refs.dot.setAttribute("aria-current", String(on));
    });

    const move = MOVES[index];
    moveDetail.setAttribute("aria-labelledby", "move-tab-" + move.id);
    moveId.textContent = move.id;
    moveTitle.textContent = move.title;
    moveBody.textContent = move.body;
    moveBody2.textContent = move.body2;
    moveEffect.textContent = move.effect;
  }

  document.getElementById("move-prev").addEventListener("click", () => {
    setMove((activeMove + MOVES.length - 1) % MOVES.length);
  });
  document.getElementById("move-next").addEventListener("click", () => {
    setMove((activeMove + 1) % MOVES.length);
  });

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
      '<span class="funnel__head"><span class="funnel__num"></span><span class="funnel__name"></span></span>' +
      '<span class="funnel__bar"><span class="funnel__fill"></span></span>';
    stage.querySelector(".funnel__num").textContent = phase.id;
    stage.querySelector(".funnel__name").textContent = phase.name;
    stage.addEventListener("click", () => setPhase(i));
    funnelList.appendChild(stage);
    return { stage, fill: stage.querySelector(".funnel__fill") };
  });

  function setPhase(index) {
    phaseRefs.forEach((refs, i) => refs.stage.setAttribute("aria-selected", String(i === index)));
    const phase = PHASES[index];
    funnelDetail.setAttribute("aria-labelledby", "phase-tab-" + phase.id);
    funnelId.textContent = phase.id;
    funnelTitle.textContent = phase.name;
    funnelBody.textContent = phase.body;
    funnelOwner.textContent = phase.owner;
  }

  /* As barras só crescem quando o funil aparece na tela: crescer fora de vista
     gastaria a única leitura que a animação tem para dar. */
  function growFunnel() {
    phaseRefs.forEach((refs, i) => { refs.fill.style.width = PHASES[i].width + "%"; });
  }

  if (reduceMotion || !("IntersectionObserver" in window)) {
    growFunnel();
  } else {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        growFunnel();
        observer.disconnect();
      });
    }, { threshold: 0.35 });
    observer.observe(funnelList);
  }

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

  document.getElementById("replay-time").addEventListener("click", () => playTime(260));

  setArtifact(0);
  setMove(0);
  setPhase(0);
  writeRows("before");
  playTime(520);
})();
