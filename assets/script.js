(() => {
  const LAYERS = [
    {
      id: "01",
      title: "A arquitetura de prompt como superfície de design",
      decision: "Parar de tratar o prompt como configuração técnica. Cada ponto em que o agente decide algo — continuar a conversa, pedir mais contexto ou escalar para um vendedor — passou a ser um ponto de decisão desenhado com intenção, no mesmo nível de uma interface visual.",
      effect: "Tornou a conversa um objeto de design, com pontos de falha localizáveis em vez de um resultado opaco."
    },
    {
      id: "02",
      title: "Jornada mapeada por origem do lead",
      decision: "Em vez de um fluxo único, a entrada da conversa virou uma fronteira distinta por canal. Leads de Instagram passaram a receber uma pergunta inicial que resgata o contexto do anúncio. Leads de disparos de WhatsApp ganharam uma etapa extra de verificação de intenção.",
      effect: "Recuperou contexto que antes se perdia no primeiro turno, justamente nas duas origens de maior perda."
    },
    {
      id: "03",
      title: "Limites de decisão do agente redesenhados",
      decision: "Definimos com clareza o que o agente decide sozinho — seguir com a oferta quando a intenção está confirmada — e em que ponto ele precisa parar e verificar antes de agir, quando há sinal de ambiguidade na origem da conversa.",
      effect: "Reduziu ofertas erradas apresentadas cedo demais, um dos principais pontos de abandono."
    },
    {
      id: "04",
      title: "Leitura de desvio em vez de leitura completa",
      decision: "O time passou a revisar apenas os pontos em que a conversa fugiu do padrão esperado para aquela origem, em vez de ler transcrições inteiras.",
      effect: "Permitiu revisar volume alto de conversas em pouco tempo e ajustar a fronteira de entrada com base em dado real."
    },
    {
      id: "05",
      title: "Teste controlado em produção",
      decision: "Rodar o redesenho em produção com testes controlados, comparando taxa de conversão por origem antes e depois, em vez de validar a mudança isolada em ambiente de teste.",
      effect: "Isolou o ganho de 8% na conversão de leads qualificados por origem de lead."
    }
  ];

  const BEFORE = [
    { author: "Lead · Instagram", side: "lead", text: "Oi, vi aqui no Instagram e queria saber mais" },
    { author: "Agente", side: "bot", text: "Olá! Tudo bem? Posso te ajudar com informações sobre nossos produtos. Qual o seu nome?", note: "Trata a primeira mensagem como pergunta genérica." },
    { author: "Lead · Instagram", side: "lead", text: "É sobre aquilo que apareceu no anúncio" },
    { author: "Agente", side: "bot", text: "Temos várias opções disponíveis. Quer fechar o plano anual em 12x sem juros?", note: "Oferta apresentada antes de a intenção existir." },
    { author: "Lead · Instagram", side: "lead", text: "…", note: "Conversa abandonada no quarto turno." }
  ];

  const AFTER = [
    { author: "Lead · Instagram", side: "lead", text: "Oi, vi aqui no Instagram e queria saber mais" },
    { author: "Agente", side: "bot", text: "Oi! Você chegou pelo anúncio da campanha de inverno. É sobre isso que quer falar, ou é outro assunto?", layer: 0 },
    { author: "Lead · Instagram", side: "lead", text: "É sobre isso mesmo" },
    { author: "Agente", side: "bot", text: "Fechado. Antes de te passar valores, só confirmando: é para uso próprio ou para revenda?", layer: 1 },
    { author: "Lead · Instagram", side: "lead", text: "Uso próprio" },
    { author: "Agente", side: "bot", text: "Então a opção que faz sentido é a que estava no anúncio, com entrega para a sua região. Quero já reservar para você?", layer: 1 },
    { author: "Lead · Instagram", side: "lead", text: "Pode reservar sim" }
  ];

  const START_LAYER = 1; // matches original startLayer=2 (1-based) -> index 1

  const state = { active: START_LAYER, shown: 0 };
  let timer = null;

  const layersList = document.getElementById("layers-list");
  const detailId = document.getElementById("detail-id");
  const detailTitle = document.getElementById("detail-title");
  const detailDecision = document.getElementById("detail-decision");
  const detailEffect = document.getElementById("detail-effect");
  const beforeList = document.getElementById("before-list");
  const afterList = document.getElementById("after-list");
  const replayBtn = document.getElementById("replay-btn");

  function setActive(index) {
    state.active = index;
    renderLayers();
    renderDetail();
  }

  function renderLayers() {
    layersList.innerHTML = "";
    LAYERS.forEach((l, i) => {
      const item = document.createElement("div");
      item.className = "blueprint layer-item" + (i === state.active ? " active" : "");
      item.innerHTML = `
        <i class="corner tl"></i><i class="corner tr"></i><i class="corner bl"></i><i class="corner br"></i>
        <span class="layer-num">${l.id}</span>
        <span class="layer-title">${l.title}</span>
      `;
      item.addEventListener("click", () => setActive(i));
      layersList.appendChild(item);
    });
  }

  function renderDetail() {
    const l = LAYERS[state.active];
    detailId.textContent = l.id;
    detailTitle.textContent = l.title;
    detailDecision.textContent = l.decision;
    detailEffect.textContent = l.effect;
  }

  function messageRow(m, i) {
    const bot = m.side === "bot";
    const row = document.createElement("div");
    row.className = "msg-row" + (i < state.shown ? " visible" : "");
    row.style.justifyContent = bot ? "flex-start" : "flex-end";

    const bubble = document.createElement("div");
    bubble.className = "msg-bubble";
    bubble.style.alignItems = bot ? "flex-start" : "flex-end";

    const author = document.createElement("span");
    author.className = "msg-author";
    author.textContent = m.author;

    const text = document.createElement("div");
    text.className = "msg-text";
    text.style.background = bot ? "color-mix(in srgb, var(--color-accent) 12%, transparent)" : "transparent";
    text.style.borderColor = bot ? "var(--color-accent-400)" : "var(--color-divider)";
    text.textContent = m.text;

    bubble.appendChild(author);
    bubble.appendChild(text);

    if (m.note) {
      const note = document.createElement("span");
      note.className = "msg-note";
      note.textContent = m.note;
      bubble.appendChild(note);
    }

    if (m.layer != null) {
      const btn = document.createElement("button");
      btn.className = "layer-link";
      btn.textContent = "camada " + LAYERS[m.layer].id;
      btn.addEventListener("click", () => setActive(m.layer));
      bubble.appendChild(btn);
    }

    row.appendChild(bubble);
    return row;
  }

  function renderChat() {
    beforeList.innerHTML = "";
    BEFORE.forEach((m, i) => beforeList.appendChild(messageRow(m, i)));
    afterList.innerHTML = "";
    AFTER.forEach((m, i) => afterList.appendChild(messageRow(m, i)));
  }

  function play() {
    clearInterval(timer);
    state.shown = 0;
    renderChat();
    timer = setInterval(() => {
      if (state.shown >= 7) {
        clearInterval(timer);
        return;
      }
      state.shown += 1;
      renderChat();
    }, 620);
  }

  replayBtn.addEventListener("click", play);

  renderLayers();
  renderDetail();
  renderChat();
  play();
})();
