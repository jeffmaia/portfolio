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
      decision: "A primeira ideia do time era fazer o agente sempre pedir confirmação antes de ofertar. Descartamos porque isso adicionava um turno em toda conversa e derrubava a conversão de quem já chegava com intenção clara. Optamos por um limite condicionado à origem. Com a intenção confirmada o agente segue com a oferta sozinho, e havendo sinal de ambiguidade ele para e verifica antes de agir.",
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
    { author: "Agente", side: "bot", text: "Oi! Você chegou pelo anúncio da campanha de inverno. É sobre isso que quer falar, ou é outro assunto?", layer: 1 },
    { author: "Lead · Instagram", side: "lead", text: "É sobre isso mesmo" },
    { author: "Agente", side: "bot", text: "Fechado. Antes de te passar valores, só confirmando: é para uso próprio ou para revenda?", layer: 2 },
    { author: "Lead · Instagram", side: "lead", text: "Uso próprio" },
    { author: "Agente", side: "bot", text: "Então a opção que faz sentido é a que estava no anúncio, com entrega para a sua região. Quero já reservar para você?", layer: 2 },
    { author: "Lead · Instagram", side: "lead", text: "Pode reservar sim" }
  ];

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const state = { active: 0, shown: reduceMotion ? AFTER.length : 0 };
  let timer = null;

  const layersList = document.getElementById("layers-list");
  const layerDots = document.getElementById("layer-dots");
  const detail = document.getElementById("layer-detail");
  const detailId = document.getElementById("detail-id");
  const detailTitle = document.getElementById("detail-title");
  const detailDecision = document.getElementById("detail-decision");
  const detailEffect = document.getElementById("detail-effect");
  const beforeList = document.getElementById("before-list");
  const afterList = document.getElementById("after-list");
  const replayBtn = document.getElementById("replay-btn");

  const layerItems = LAYERS.map((layer, i) => {
    const item = document.createElement("button");
    item.type = "button";
    item.className = "blueprint layer-item";
    item.setAttribute("role", "tab");
    item.id = "layer-tab-" + layer.id;
    item.innerHTML = '<span class="layer-num"></span><span class="layer-title"></span>';
    item.querySelector(".layer-num").textContent = layer.id;
    item.querySelector(".layer-title").textContent = layer.title;
    item.addEventListener("click", () => setActive(i));
    layersList.appendChild(item);

    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "dot";
    dot.setAttribute("aria-label", "Camada " + layer.id);
    dot.addEventListener("click", () => setActive(i));
    layerDots.appendChild(dot);

    return { item, dot };
  });

  function setActive(index) {
    state.active = index;
    layerItems.forEach((refs, i) => {
      const on = i === index;
      refs.item.setAttribute("aria-selected", String(on));
      refs.dot.setAttribute("aria-current", String(on));
    });

    const layer = LAYERS[index];
    detail.setAttribute("aria-labelledby", "layer-tab-" + layer.id);
    detailId.textContent = layer.id;
    detailTitle.textContent = layer.title;
    detailDecision.textContent = layer.decision;
    detailEffect.textContent = layer.effect;
  }

  document.getElementById("layer-prev").addEventListener("click", () => {
    setActive((state.active + LAYERS.length - 1) % LAYERS.length);
  });
  document.getElementById("layer-next").addEventListener("click", () => {
    setActive((state.active + 1) % LAYERS.length);
  });

  function messageRow(m, i) {
    const bot = m.side === "bot";
    const row = document.createElement("div");
    row.className = "msg-row " + (bot ? "msg-row--bot" : "msg-row--lead") + (i < state.shown ? " visible" : "");

    const bubble = document.createElement("div");
    bubble.className = "msg-bubble";

    const author = document.createElement("span");
    author.className = "msg-author";
    author.textContent = m.author;

    const text = document.createElement("div");
    text.className = "msg-text";
    text.textContent = m.text;

    bubble.append(author, text);

    if (m.note) {
      const note = document.createElement("span");
      note.className = "msg-note";
      note.textContent = m.note;
      bubble.appendChild(note);
    }

    if (m.layer != null) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn-ghost";
      btn.textContent = "camada " + LAYERS[m.layer].id;
      btn.addEventListener("click", () => {
        setActive(m.layer);
        detail.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "center" });
      });
      bubble.appendChild(btn);
    }

    row.appendChild(bubble);
    return row;
  }

  function renderChat() {
    beforeList.replaceChildren(...BEFORE.map(messageRow));
    afterList.replaceChildren(...AFTER.map(messageRow));
  }

  function play() {
    clearInterval(timer);
    if (reduceMotion) {
      state.shown = AFTER.length;
      renderChat();
      return;
    }
    state.shown = 0;
    renderChat();
    timer = setInterval(() => {
      state.shown += 1;
      renderChat();
      if (state.shown >= AFTER.length) clearInterval(timer);
    }, 620);
  }

  replayBtn.addEventListener("click", play);

  setActive(0);
  play();
})();
