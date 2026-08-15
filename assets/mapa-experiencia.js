(() => {
  const STEPS = [
    {
      id: "01",
      title: "Entender os dados do NPS",
      body: "Clusterizamos os comentários do NPS em grandes eixos e subcategorias, realizando uma divisão entre semestres.",
      body2: "Era preciso um relatório que ilustrasse a jornada do aluno do início ao fim da graduação, para que as ações pudessem surtir efeito nos períodos específicos de cada problema.",
      effect: "A insatisfação deixou de ser uma nota única e passou a ter lugar e momento na jornada."
    },
    {
      id: "02",
      title: "Complementar os dados",
      body: "Percebemos que as informações presentes não eram suficientes e fomos atrás dos alunos para preencher outros aspectos da vida desse aluno. Focar apenas no que estavam reclamando não era suficiente para propor ações. Acreditávamos que aspectos da vida pessoal desse aluno poderiam colaborar com alguns dos pontos negativos levantados.",
      body2: "Um exemplo, um aluno que mora muito longe da instituição sofre muito mais com um cancelamento de aula em cima da hora do que um aluno que mora perto do campus.",
      effect: "As ações passaram a considerar o contexto de vida do aluno, não só a reclamação registrada."
    },
    {
      id: "03",
      title: "Ideação",
      body: "O time de pesquisadores e produto vinha há um bom tempo tentando achar um formato de entrega de dados que fugisse do tradicional relatório. A maioria deles não era lida nem utilizada na hora de idealizar soluções e propor ações, mesmo com esforços grandes de divulgação, apresentação e colaboração com as áreas.",
      body2: "Antes disso testamos dois formatos mais óbvios, um dashboard de indicadores e um resumo executivo de duas páginas por campus. Os dois falharam pelo mesmo motivo, entregavam a conclusão pronta e ninguém precisava percorrer a jornada do aluno para chegar nela. O tabuleiro foi escolhido porque obriga quem lê a andar por semestre e por eixo, e é nesse trajeto que o time reconhece o próprio aluno e propõe ação. Esse mapa precisava trazer informações resumidas de fácil consulta, assim como em profundidade.",
      effect: "O formato virou parte da solução, não apenas a embalagem da pesquisa."
    }
  ];

  const SHOT_BASE = "https://framerusercontent.com/images/";
  const SHOTS = [
    { file: "jB0FYWxzKTWaMHwYRuFkT0OR8.png", alt: "Fig. 01" },
    { file: "2u2l4cvOcOdO1jQGPl637PRYmWI.png", alt: "Fig. 02" },
    { file: "Gt20MHEWr6seNOXMahLIqb4plQ.png", alt: "Fig. 03" },
    { file: "3IY6aXgfkDIxVCej0xa2DWhplw.png", alt: "Fig. 04" },
    { file: "D6BfM2dEe92QhBtCV7Q9lTCTu0.png", alt: "Fig. 05" }
  ];

  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* — etapas do processo — */
  const stepsList = document.getElementById("steps-list");
  const stepDots = document.getElementById("step-dots");
  const stepDetail = document.getElementById("step-detail");
  const detailId = document.getElementById("detail-id");
  const detailTitle = document.getElementById("detail-title");
  const detailBody = document.getElementById("detail-body");
  const detailBody2 = document.getElementById("detail-body2");
  const detailEffect = document.getElementById("detail-effect");

  const stepRefs = STEPS.map((step, i) => {
    const item = document.createElement("button");
    item.type = "button";
    item.className = "blueprint layer-item";
    item.setAttribute("role", "tab");
    item.id = "step-tab-" + step.id;
    item.innerHTML = '<span class="layer-num"></span><span class="layer-title"></span>';
    item.querySelector(".layer-num").textContent = step.id;
    item.querySelector(".layer-title").textContent = step.title;
    item.addEventListener("click", () => setStep(i));
    stepsList.appendChild(item);

    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "dot";
    dot.setAttribute("aria-label", "Etapa " + step.id);
    dot.addEventListener("click", () => setStep(i));
    stepDots.appendChild(dot);

    return { item, dot };
  });

  let activeStep = 0;

  function setStep(index) {
    activeStep = index;
    stepRefs.forEach((refs, i) => {
      const on = i === index;
      refs.item.setAttribute("aria-selected", String(on));
      refs.dot.setAttribute("aria-current", String(on));
    });

    const step = STEPS[index];
    stepDetail.setAttribute("aria-labelledby", "step-tab-" + step.id);
    detailId.textContent = step.id;
    detailTitle.textContent = step.title;
    detailBody.textContent = step.body;
    detailBody2.textContent = step.body2;
    detailEffect.textContent = step.effect;
  }

  document.getElementById("step-prev").addEventListener("click", () => {
    setStep((activeStep + STEPS.length - 1) % STEPS.length);
  });
  document.getElementById("step-next").addEventListener("click", () => {
    setStep((activeStep + 1) % STEPS.length);
  });

  /* — gráficos: escala de NPS e acessos — */
  const npsRange = document.getElementById("nps-range");
  const accessFills = Array.from(document.querySelectorAll(".access-fill"));
  let growTimer = null;

  function grow() {
    npsRange.classList.add("is-grown");
    accessFills.forEach(fill => { fill.style.width = fill.dataset.width + "%"; });
  }

  function resetCharts() {
    npsRange.classList.remove("is-grown");
    accessFills.forEach(fill => { fill.style.width = "0%"; });
  }

  function playCharts(delay) {
    clearTimeout(growTimer);
    if (reduceMotion) { grow(); return; }
    resetCharts();
    growTimer = setTimeout(grow, delay);
  }

  document.getElementById("replay-nps").addEventListener("click", () => playCharts(260));

  /* — carrossel do mapa + lightbox — */
  const shotImg = document.getElementById("shot-img");
  const shotCaption = document.getElementById("shot-caption");
  const shotDots = document.getElementById("shot-dots");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");

  const shotDotRefs = SHOTS.map((shot, i) => {
    const dot = document.createElement("button");
    dot.type = "button";
    dot.className = "dot";
    dot.setAttribute("aria-label", shot.alt);
    dot.addEventListener("click", () => setShot(i));
    shotDots.appendChild(dot);
    return dot;
  });

  let activeShot = 0;

  function setShot(index) {
    activeShot = index;
    const shot = SHOTS[index];
    shotImg.src = SHOT_BASE + shot.file;
    shotImg.alt = shot.alt;
    shotCaption.textContent = shot.alt + " · " + (index + 1) + " de " + SHOTS.length;
    shotDotRefs.forEach((dot, i) => dot.setAttribute("aria-current", String(i === index)));
  }

  document.getElementById("shot-prev").addEventListener("click", () => {
    setShot((activeShot + SHOTS.length - 1) % SHOTS.length);
  });
  document.getElementById("shot-next").addEventListener("click", () => {
    setShot((activeShot + 1) % SHOTS.length);
  });

  document.getElementById("shot-figure").addEventListener("click", () => {
    const shot = SHOTS[activeShot];
    lightboxImg.src = SHOT_BASE + shot.file;
    lightboxImg.alt = shot.alt;
    lightboxCaption.textContent = shot.alt + " · clique para fechar";
    lightbox.hidden = false;
  });

  lightbox.addEventListener("click", () => { lightbox.hidden = true; });
  window.addEventListener("keydown", e => {
    if (e.key === "Escape") lightbox.hidden = true;
  });

  setStep(0);
  setShot(0);
  playCharts(520);
})();
