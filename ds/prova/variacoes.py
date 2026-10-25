"""Seis variações editoriais da página do Omnichat.

Mesmo texto, mesma identidade (tokens e componentes do Jeff DS), seis
estruturas. Cada uma parte de um princípio de design editorial diferente,
descrito em ds/REFERENCIAS.md. O CSS de cada variação mora nela mesma e só
arruma a grade: cor, tipo e forma vêm todos dos tokens.

Uso: python3 ds/prova/variacoes.py
Escreve ds/prova/variacoes/v1.html a v6.html, o índice, e refaz
ds/prova/omnichat.html com o menu e o rodapé novos.
"""
from pathlib import Path
import comum as c
import caso

AQUI = Path(__file__).parent
OUT = AQUI / "variacoes"
P = "../../../"


def secao_rotulo(n, nome):
    return f'<p class="section__rotulo t-rotulo">0{n} · {nome}</p>'


# ============================================================ V1
# Grade suíça assimétrica. Doze colunas, alinhamento à esquerda, nada
# centralizado. O número de cada seção pendura na margem esquerda e o
# texto corre numa coluna estreita; o que é apoio (ficha, efeito) senta
# na coluna da direita, na mesma linha do que comenta.
def v1():
    css = """
.v1 .h1-grade { display: grid; gap: var(--space-24); padding-block: var(--space-48) var(--space-64); }
.v1 .h1-ilu { max-width: 560px; }
.v1 .h1-num { display: grid; gap: var(--space-8); }
.v1 .margem { display: grid; gap: var(--space-12); align-content: start; }
.v1 .margem__num { font-family: var(--font-display); font-size: var(--text-numero); line-height: .85; }
.v1 .linha-sec { border-top: var(--stroke) solid var(--border); padding-block: var(--space-48); display: grid; gap: var(--space-24); }
.v1 .camada { display: grid; gap: var(--space-12); padding-block: var(--space-24); border-top: var(--stroke) solid var(--border); }
.v1 .camada:last-child { border-bottom: var(--stroke) solid var(--border); }
.v1 .camada h3 { font-size: var(--text-lead); line-height: 1.3; }
.v1 .efeito { font-size: var(--text-apoio); }
.v1 .stats .stat { gap: var(--space-12); }
@media (min-width: 1100px) {
  .v1 .h1-grade { grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--grade-vao); row-gap: var(--space-32); align-items: end; }
  .v1 .h1-grade > * { grid-column: 1 / span 8; }
  .v1 .h1-ilu { grid-column: 9 / -1; grid-row: 1 / span 3; align-self: end; max-width: none; }
  .v1 .h1-lead { grid-column: 1 / span 4; }
  .v1 .h1-num { grid-column: 5 / span 4; }
  .v1 .linha-sec { grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .v1 .linha-sec > .margem { grid-column: 1 / span 2; }
  .v1 .linha-sec > .miolo { grid-column: 3 / span 6; display: grid; gap: var(--space-24); align-content: start; }
  .v1 .linha-sec > .apoio { grid-column: 10 / -1; align-self: start; }
  .v1 .linha-sec > .largo { grid-column: 3 / -1; }
  .v1 .camada { grid-template-columns: 2fr 4fr 5fr 3fr; column-gap: var(--grade-vao); align-items: start; }
}"""
    camadas = "".join(
        f"""<div class="camada">
  <div>{c.icone(P, ic, 48)}<span class="t-rotulo">0{i}</span></div>
  <h3>{tit}</h3>
  <p>{txt}</p>
  <p class="efeito"><span class="t-rotulo">Efeito</span><br>{ef}</p>
</div>""" for i, (_, ic, tit, txt, ef) in enumerate(c.CAMADAS, 1))
    origens = "".join(f'<li class="step">{c.icone(P, ic, 44, "icone step__icone")}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for ic, t, x in c.ORIGENS)
    stats = "".join(f'<div class="stat">{c.icone(P, ic, 40)}<span class="stat__valor">{v}</span><p class="stat__frase">{f}</p></div>' for ic, v, f in c.STATS)
    main = f"""
<main id="conteudo" class="container">
  <header class="h1-grade">
    {c.badges()}
    <h1 class="t-display">{c.TITULO}</h1>
    <p class="t-sub h1-lead">{c.LEAD}</p>
    {c.salto("h1-num")}
    {c.ilustracao(P, "fronteira", "ilustracao h1-ilu")}
  </header>

  <section class="linha-sec" aria-labelledby="v1-contexto">
    <div class="margem"><span class="margem__num" aria-hidden="true">01</span>{c.icone(P, "robo", 56)}<p class="t-rotulo" id="v1-contexto">Contexto</p></div>
    <div class="miolo"><p class="t-lead">{c.CONTEXTO}</p></div>
    <div class="apoio card" data-variant="muted"><p class="t-rotulo card__titulo">Ficha do projeto</p>{c.ficha()}</div>
  </section>

  <section class="linha-sec" aria-labelledby="v1-problema">
    <div class="margem"><span class="margem__num" aria-hidden="true">02</span>{c.icone(P, "fronteira", 56)}<p class="t-rotulo">O problema</p></div>
    <div class="miolo">
      <h2 class="t-titulo" id="v1-problema">{c.PROBLEMA_TITULO}</h2>
      <div class="prosa">{"".join(f"<p>{p}</p>" for p in c.PROBLEMA)}</div>
    </div>
    <ol class="apoio steps">{origens}</ol>
  </section>

  <section class="linha-sec" aria-labelledby="v1-camadas">
    <div class="margem"><span class="margem__num" aria-hidden="true">03</span>{c.icone(P, "camadas", 56)}<p class="t-rotulo">Processo</p></div>
    <div class="miolo"><h2 class="t-titulo" id="v1-camadas">{c.CAMADAS_TITULO}</h2></div>
    <div class="largo">{camadas}</div>
  </section>

  <section class="linha-sec" aria-labelledby="v1-conversa">
    <div class="margem"><span class="margem__num" aria-hidden="true">04</span>{c.icone(P, "dialogo", 56)}<p class="t-rotulo">Antes e depois</p></div>
    <div class="miolo"><h2 class="t-titulo" id="v1-conversa">{c.CONVERSA_TITULO}</h2><p class="t-apoio">{c.CONVERSA_LEGENDA}</p></div>
    <div class="largo">{c.conversa(P)}</div>
  </section>

  <section class="linha-sec" aria-labelledby="v1-resultado">
    <div class="margem"><span class="margem__num" aria-hidden="true">05</span>{c.icone(P, "grafico", 56)}<p class="t-rotulo">Resultado</p></div>
    <div class="miolo"><h2 class="t-titulo" id="v1-resultado">{c.RESULTADO_TITULO}</h2><div class="prosa">{"".join(f"<p>{p}</p>" for p in c.RESULTADO)}</div></div>
    <div class="largo stats">{stats}</div>
    <div class="largo">{c.callout()}</div>
    <div class="largo">{c.fechamento(P)}</div>
  </section>
</main>"""
    return "Grade suíça", css, main


# ============================================================ V2
# Coluna e margem. Uma coluna de leitura na medida ideal (60 a 66
# caracteres) e uma margem larga à direita para o que é secundário: a
# ficha, as origens, o efeito de cada camada, os números. É o padrão das
# notas de Tufte. No celular a margem vira uma caixa logo abaixo do
# parágrafo que ela comenta.
def v2():
    css = """
.v2 .h2-topo { display: grid; gap: var(--space-24); padding-block: var(--space-64) var(--space-32); max-width: 900px; }
.v2 .figura { position: relative; margin-block: var(--space-32) var(--space-64); }
.v2 .figura__palco { background: var(--muted); border: var(--stroke) solid var(--border); border-radius: var(--radius); padding: clamp(16px, 4vw, 48px) clamp(16px, 6vw, 96px) 0; overflow: hidden; }
.v2 .figura__palco .ilustracao { max-width: 760px; margin-inline: auto; }
.v2 .figura__num { margin-top: var(--space-16); }
.v2 figcaption { margin-top: var(--space-12); font-size: var(--text-apoio); max-width: 60ch; }
.v2 .corpo { display: grid; row-gap: var(--space-24); }
.v2 .corpo h2 { margin-top: var(--space-64); }
.v2 .corpo h3 { display: flex; align-items: center; gap: var(--space-12); margin-top: var(--space-32); font-size: var(--text-lead); line-height: 1.3; }
.v2 .nota { font-size: var(--text-apoio); line-height: 1.5; padding: var(--space-16); border-radius: var(--radius); background: var(--muted); color: var(--ink); display: grid; gap: var(--space-8); align-content: start; }
.v2 .nota--borda { background: transparent; border: var(--stroke) solid var(--border); }
.v2 .capitular::first-letter { float: left; font-family: var(--font-display); font-size: 4.6em; line-height: .82; padding: .06em .12em 0 0; }
.v2 .citacao-solta { font-family: var(--font-flare); font-weight: 300; font-size: var(--text-titulo); line-height: 1.12; padding-block: var(--space-24); border-block: var(--stroke) solid var(--border); }
.v2 .largo { margin-block: var(--space-32); }
@media (min-width: 1100px) {
  .v2 .corpo { grid-template-columns: minmax(0, 7fr) minmax(0, 1fr) minmax(0, 4fr); }
  .v2 .corpo > * { grid-column: 1; }
  .v2 .corpo > .nota { grid-column: 3; margin-top: 4px; }
  .v2 .corpo > .largo { grid-column: 1 / -1; }
  .v2 .corpo > .citacao-solta { grid-column: 1 / -1; font-size: var(--text-display); font-family: var(--font-display); text-transform: uppercase; line-height: var(--leading-display); }
  .v2 .figura__num { position: absolute; left: clamp(16px, 3vw, 40px); bottom: clamp(16px, 3vw, 40px); margin: 0; max-width: 360px; }
}"""
    # Cada nota vem logo depois do parágrafo que comenta; no desktop a
    # grade a puxa para a margem, na mesma linha.
    blocos = []
    for i, (_, ic, tit, txt, ef) in enumerate(c.CAMADAS, 1):
        blocos.append(f'<h3>{c.icone(P, ic, 40)}<span><span class="t-rotulo">0{i}</span><br>{tit}</span></h3>')
        blocos.append(f"<p>{txt}</p>")
        blocos.append(f'<aside class="nota"><span class="t-rotulo">Efeito da camada 0{i}</span>{ef}</aside>')
    stats = "".join(f'<aside class="nota nota--borda">{c.icone(P, ic, 36)}<span class="stat__valor" style="font-size:var(--text-titulo)">{v}</span>{f}</aside>' for ic, v, f in c.STATS)
    main = f"""
<main id="conteudo" class="container">
  <header class="h2-topo">
    {c.badges()}
    <h1 class="t-display">{c.TITULO}</h1>
    <p class="t-sub">{c.LEAD}</p>
  </header>

  <figure class="figura">
    <div class="figura__palco">{c.ilustracao(P, "fronteira")}</div>
    <div class="card figura__num" data-variant="acento">{c.salto()}</div>
    <figcaption>A fronteira de entrada. O lead chega pelo canal de origem e, do lado de dentro, a conversão das origens redesenhadas passa de 24% para 32%.</figcaption>
  </figure>

  <article class="corpo">
    <p class="section__rotulo t-rotulo">01 · Contexto</p>
    <p class="t-lead capitular">{c.CONTEXTO}</p>
    <aside class="nota"><span class="t-rotulo">Ficha do projeto</span>{c.ficha()}</aside>

    <h2 class="t-titulo">{c.PROBLEMA_TITULO}</h2>
    <p>{c.PROBLEMA[0]}</p>
    <aside class="nota nota--borda">{c.icone(P, c.ORIGENS[0][0], 40)}<span class="t-rotulo">Instagram</span>{c.ORIGENS[0][2]}</aside>
    <p>{c.PROBLEMA[1]}</p>
    <aside class="nota nota--borda">{c.icone(P, c.ORIGENS[1][0], 40)}<span class="t-rotulo">Disparos de WhatsApp</span>{c.ORIGENS[1][2]}</aside>

    <h2 class="t-titulo">{c.CAMADAS_TITULO}</h2>
    {"".join(blocos)}

    <h2 class="t-titulo">{c.CONVERSA_TITULO}</h2>
    <p class="t-apoio">{c.CONVERSA_LEGENDA}</p>
    <div class="largo">{c.conversa(P)}</div>

    <h2 class="t-titulo">{c.RESULTADO_TITULO}</h2>
    <p>{c.RESULTADO[0]}</p>
    {stats.split("</aside>")[0]}</aside>
    <p>{c.RESULTADO[1]}</p>
    {"</aside>".join(stats.split("</aside>")[1:])}
    <blockquote class="citacao-solta">{c.DECLARACAO}</blockquote>
    <p>{c.DECL_CORPO}</p>
    <div class="largo">{c.fechamento(P)}</div>
  </article>
</main>"""
    return "Coluna e margem", css, main


# ============================================================ V3
# Capítulos. Cada seção abre com uma página de capítulo: número enorme,
# ícone grande e título, com muito ar em volta. Depois, o conteúdo numa
# coluna só, centrada na medida. O ritmo vem da alternância entre
# abertura cheia e leitura estreita.
def v3():
    css = """
.v3 .h3-hero { display: grid; min-height: calc(100svh - 66px); border-bottom: var(--stroke) solid var(--border); }
.v3 .h3-texto { display: grid; gap: var(--space-24); align-content: center; padding: var(--space-48) var(--page-margem); }
.v3 .h3-palco { background: var(--muted); display: grid; align-items: end; padding: var(--space-32) var(--page-margem) 0; border-top: var(--stroke) solid var(--border); }
.v3 .capitulo { display: grid; gap: var(--space-24); padding-block: clamp(96px, 12vw, 192px) var(--space-48); }
.v3 .capitulo__num { font-family: var(--font-display); font-size: clamp(6rem, 3rem + 14vw, 14rem); line-height: .8; }
.v3 .capitulo .icone { --icone: clamp(72px, 8vw, 120px); }
.v3 .leitura { max-width: 680px; margin-inline: auto; display: grid; gap: var(--space-32); padding-bottom: var(--space-64); }
.v3 .zigue { display: grid; gap: var(--space-48); }
.v3 .zigue__item { display: grid; gap: var(--space-16); }
.v3 .zigue__marca { display: flex; align-items: center; gap: var(--space-16); }
.v3 .zigue__marca .t-display { font-size: var(--text-titulo); }
.v3 .stats-grande { display: grid; gap: var(--space-32); }
.v3 .stats-grande .stat__valor { font-size: var(--text-numero); }
@media (min-width: 900px) {
  .v3 .h3-hero { grid-template-columns: minmax(0, 6fr) minmax(0, 5fr); }
  .v3 .h3-palco { border-top: 0; border-left: var(--stroke) solid var(--border); }
  .v3 .capitulo { grid-template-columns: auto minmax(0, 1fr); align-items: end; column-gap: var(--space-48); }
  .v3 .capitulo__num { grid-row: span 2; }
  .v3 .zigue__item { grid-template-columns: 1fr 1fr; column-gap: var(--space-64); align-items: start; }
  .v3 .zigue__item:nth-child(even) .zigue__marca { order: 2; }
  .v3 .stats-grande { grid-template-columns: 1fr 1fr; }
}"""

    def capitulo(n, ic, rotulo, titulo, tid):
        return f"""<header class="capitulo">
  <span class="capitulo__num" aria-hidden="true">0{n}</span>
  <div>{c.icone(P, ic, 120)}</div>
  <div><p class="t-rotulo">{rotulo}</p><h2 class="t-titulo" id="{tid}">{titulo}</h2></div>
</header>"""
    zigue = "".join(
        f"""<div class="zigue__item">
  <div class="zigue__marca">{c.icone(P, ic, 72)}<span class="t-display">0{i}</span></div>
  <div class="prosa"><h3 class="step__titulo">{tit}</h3><p>{txt}</p><p class="tabs__efeito"><span class="t-rotulo">Efeito</span> {ef}</p></div>
</div>""" for i, (_, ic, tit, txt, ef) in enumerate(c.CAMADAS, 1))
    stats = "".join(f'<div class="stat">{c.icone(P, ic, 48)}<span class="stat__valor">{v}</span><p class="stat__frase">{f}</p></div>' for ic, v, f in c.STATS)
    origens = "".join(f'<li class="step">{c.icone(P, ic, 44, "icone step__icone")}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for ic, t, x in c.ORIGENS)
    main = f"""
<main id="conteudo">
  <header class="h3-hero">
    <div class="h3-texto">
      {c.badges()}
      <h1 class="t-display">{c.TITULO}</h1>
      <p class="t-sub">{c.LEAD}</p>
      {c.salto()}
    </div>
    <div class="h3-palco">{c.ilustracao(P, "fronteira")}</div>
  </header>

  <div class="container">
    <section aria-labelledby="v3-c1">
      {capitulo(1, "robo", "Contexto", "Um agente que tratava todo lead igual", "v3-c1")}
      <div class="leitura"><p class="t-lead">{c.CONTEXTO}</p><div class="card" data-variant="muted"><p class="t-rotulo card__titulo">Ficha do projeto</p>{c.ficha()}</div></div>
    </section>
    <section aria-labelledby="v3-c2">
      {capitulo(2, "fronteira", "O problema", c.PROBLEMA_TITULO, "v3-c2")}
      <div class="leitura"><div class="prosa">{"".join(f"<p>{p}</p>" for p in c.PROBLEMA)}</div><ol class="steps">{origens}</ol></div>
    </section>
    <section aria-labelledby="v3-c3">
      {capitulo(3, "camadas", "Processo", c.CAMADAS_TITULO, "v3-c3")}
      <div class="zigue">{zigue}</div>
    </section>
    <section aria-labelledby="v3-c4">
      {capitulo(4, "dialogo", "Antes e depois", c.CONVERSA_TITULO, "v3-c4")}
      <p class="t-apoio" style="margin-bottom:var(--space-32)">{c.CONVERSA_LEGENDA}</p>
      {c.conversa(P)}
    </section>
    <section aria-labelledby="v3-c5">
      {capitulo(5, "grafico", "Resultado", c.RESULTADO_TITULO, "v3-c5")}
      <div class="leitura"><div class="prosa">{"".join(f"<p>{p}</p>" for p in c.RESULTADO)}</div></div>
      <div class="stats-grande">{stats}</div>
      <div style="margin-block:var(--space-96) var(--space-48)">{c.callout()}</div>
      <div style="padding-bottom:var(--space-secao)">{c.fechamento(P)}</div>
    </section>
  </div>
</main>"""
    return "Capítulos", css, main


# ============================================================ V4
# Sumário e mosaico. Um sumário fixo à esquerda, que diz onde se está e
# deixa pular para qualquer parte, e o conteúdo em blocos de tamanhos
# diferentes, como um mosaico. É a leitura de quem escaneia antes de ler.
def v4():
    # A escolhida. O miolo mora em caso.py, que também gera a página
    # publicada, e usa só os componentes de assets/ds.
    return "Sumário e mosaico", "", caso.main(P)


# ============================================================ V5
# Pôster. A tipografia é a imagem. O indicador vira a manchete, em
# tamanho de cartaz, com a ilustração do salto entre o antes e o depois.
# A grade quebra de propósito: adesivos sobrepõem os cantos dos blocos e
# os blocos se deslocam de uma linha para a outra.
def v5():
    css = """
.v5 .cartaz { display: grid; gap: var(--space-24); padding-block: var(--space-48) var(--space-64); }
.v5 .cartaz .badges li:nth-child(1) .badge { transform: rotate(-3deg); }
.v5 .cartaz .badges li:nth-child(3) .badge { transform: rotate(2deg); }
.v5 .manchete { display: grid; align-items: end; gap: var(--space-16); grid-template-columns: auto minmax(0, 1fr); }
.v5 .manchete__antes, .v5 .manchete__depois { font-family: var(--font-display); line-height: .82; }
.v5 .manchete__antes { font-size: clamp(3rem, 1rem + 8vw, 9rem); text-decoration: line-through; text-decoration-thickness: .08em; }
.v5 .manchete__depois { font-size: clamp(6rem, 2rem + 17vw, 19rem); grid-column: 1 / -1; }
.v5 .manchete .ilustracao { max-width: 340px; justify-self: end; grid-row: 1; grid-column: 2; }
.v5 .cartaz h1 { max-width: 20ch; }
.v5 .grito-sec { font-family: var(--font-display); font-size: var(--text-display); line-height: var(--leading-display); text-transform: uppercase; max-width: 18ch; }
.v5 .faixa { display: grid; gap: var(--space-32); padding-block: var(--space-secao) 0; }
.v5 .adesivo-wrap { position: relative; }
.v5 .adesivo { position: absolute; top: -28px; right: -12px; transform: rotate(8deg); --icone: 72px; }
.v5 .degraus { display: grid; gap: var(--space-24); }
.v5 .degrau { position: relative; display: grid; gap: var(--space-12); padding: var(--space-32) var(--space-24) var(--space-24); }
.v5 .degrau__num { font-family: var(--font-display); font-size: var(--text-numero); line-height: .8; color: transparent; -webkit-text-stroke: 2px var(--ink); }
.v5 .muro { display: grid; gap: var(--grade-vao); }
.v5 .muro .stat { padding: var(--space-24); border: var(--stroke) solid var(--border); border-radius: var(--radius); }
.v5 .muro .stat:nth-child(1) { background: var(--acento); }
.v5 .muro .stat:nth-child(3) { background: var(--muted); }
.v5 .muro .stat__valor { font-size: var(--text-numero); }
@media (min-width: 900px) {
  .v5 .manchete { grid-template-columns: auto minmax(0, 1fr) auto; }
  .v5 .manchete__depois { grid-column: 3; }
  .v5 .manchete .ilustracao { grid-column: 2; justify-self: center; max-width: 420px; }
  .v5 .faixa { grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .v5 .faixa > * { grid-column: 1 / -1; }
  .v5 .faixa > .grito-sec { grid-column: 1 / span 7; }
  .v5 .faixa > .texto-desloc { grid-column: 7 / -1; }
  .v5 .degraus { grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .v5 .degrau:nth-child(1) { grid-column: 1 / span 6; }
  .v5 .degrau:nth-child(2) { grid-column: 5 / span 6; }
  .v5 .degrau:nth-child(3) { grid-column: 2 / span 7; }
  .v5 .degrau:nth-child(4) { grid-column: 7 / span 6; }
  .v5 .degrau:nth-child(5) { grid-column: 3 / span 6; }
  .v5 .muro { grid-template-columns: 2fr 1fr; }
  .v5 .muro .stat:nth-child(4) { grid-column: 2; }
}"""
    degraus = "".join(
        f"""<article class="card degrau"{' data-variant="acento"' if i == 3 else ""}>
  {c.icone(P, ic, 72, "icone adesivo")}
  <span class="degrau__num" aria-hidden="true">0{i}</span>
  <h3 class="t-sub">{tit}</h3><p>{txt}</p><p class="t-apoio"><b>Efeito.</b> {ef}</p>
</article>""" for i, (_, ic, tit, txt, ef) in enumerate(c.CAMADAS, 1))
    stats = "".join(f'<div class="stat"><span class="stat__valor">{v}</span><p class="stat__frase">{f}</p></div>' for _, v, f in c.STATS)
    main = f"""
<main id="conteudo" class="container">
  <header class="cartaz">
    {c.badges()}
    <h1 class="t-display">{c.TITULO}</h1>
    <div class="manchete" role="img" aria-label="Conversão de leads qualificados de 24% para 32%">
      <span class="manchete__antes" aria-hidden="true">24%</span>
      {c.ilustracao(P, "salto")}
      <span class="manchete__depois" aria-hidden="true">32%</span>
    </div>
    <p class="t-sub" style="max-width:34ch">{c.LEAD}</p>
    <p class="t-apoio" style="max-width:60ch">{c.SALTO_FRASE}</p>
  </header>

  <section class="faixa" aria-labelledby="v5-t1">
    <p class="section__rotulo t-rotulo">01 · Contexto</p>
    <h2 class="grito-sec" id="v5-t1">Todo lead era tratado como o&nbsp;primeiro.</h2>
    <div class="texto-desloc prosa"><p class="t-lead">{c.CONTEXTO}</p><div class="card adesivo-wrap" data-variant="muted" style="margin-top:var(--space-32)">{c.icone(P, "pessoa", 72, "icone adesivo")}<p class="t-rotulo card__titulo">Ficha do projeto</p>{c.ficha()}</div></div>
  </section>

  <section class="faixa" aria-labelledby="v5-t2">
    <p class="section__rotulo t-rotulo">02 · O problema</p>
    <h2 class="grito-sec" id="v5-t2">{c.PROBLEMA_TITULO}.</h2>
    <div class="texto-desloc prosa">{"".join(f"<p>{p}</p>" for p in c.PROBLEMA)}
      {"".join(f'<div class="card adesivo-wrap" style="margin-top:var(--space-48)">{c.icone(P, ic, 72, "icone adesivo")}<p class="t-rotulo card__titulo">{t}</p><p class="t-apoio">{x}</p></div>' for ic, t, x in c.ORIGENS)}
    </div>
  </section>

  <section class="faixa" aria-labelledby="v5-t3">
    <p class="section__rotulo t-rotulo">03 · Processo</p>
    <h2 class="grito-sec" id="v5-t3">{c.CAMADAS_TITULO}.</h2>
    <div class="degraus">{degraus}</div>
  </section>

  <section class="faixa" aria-labelledby="v5-t4">
    <p class="section__rotulo t-rotulo">04 · Antes e depois</p>
    <h2 class="grito-sec" id="v5-t4">Mesmo lead. Outra fronteira.</h2>
    <p class="texto-desloc t-apoio">{c.CONVERSA_LEGENDA}</p>
    {c.conversa(P)}
  </section>

  <section class="faixa" aria-labelledby="v5-t5" style="padding-bottom:var(--space-secao)">
    <p class="section__rotulo t-rotulo">05 · Resultado</p>
    <h2 class="grito-sec" id="v5-t5">{c.RESULTADO_TITULO}.</h2>
    <div class="texto-desloc prosa">{"".join(f"<p>{p}</p>" for p in c.RESULTADO)}</div>
    <div class="muro">{stats}</div>
    {c.callout()}
    {c.fechamento(P)}
  </section>
</main>"""
    return "Pôster", css, main


# ============================================================ V6
# Jornal. Manchete de largura cheia, linha fina de abertura, ficha como
# linha de crédito, texto em colunas com fio entre elas, quadro de dados
# com fios, e a conversa como transcrição de entrevista, sem balões.
def v6():
    css = """
.v6 .jornal { padding-block: var(--space-32) var(--space-secao); }
.v6 .cabeco { display: flex; flex-wrap: wrap; justify-content: space-between; gap: var(--space-8); padding-block: var(--space-12); border-block: var(--stroke) solid var(--border); }
.v6 .manchete { font-family: var(--font-flare); font-weight: 300; font-size: clamp(2.5rem, 1.2rem + 5.4vw, 6.25rem); line-height: 1.02; letter-spacing: -0.02em; margin-block: var(--space-32) var(--space-24); max-width: 20ch; }
.v6 .linha-fina { font-size: var(--text-lead); max-width: 52ch; }
.v6 .credito { display: grid; gap: var(--space-16); margin-block: var(--space-32); padding-block: var(--space-16); border-block: 1px solid var(--border); }
.v6 .credito div { display: grid; gap: var(--space-4); font-size: var(--text-apoio); }
.v6 .credito dt { font-size: var(--text-rotulo); font-weight: 700; letter-spacing: var(--tracking-rotulo); text-transform: uppercase; }
.v6 .colunas { column-gap: var(--space-48); column-rule: 1px solid var(--border); }
.v6 .colunas p { margin-bottom: var(--space-16); }
.v6 .colunas h2 { column-span: all; font-family: var(--font-flare); font-weight: 300; font-size: var(--text-titulo); line-height: 1.1; padding-top: var(--space-48); margin-bottom: var(--space-24); border-top: var(--stroke) solid var(--border); }
.v6 .gravura { break-inside: avoid; margin-bottom: var(--space-24); border: var(--stroke) solid var(--border); border-radius: var(--radius); overflow: hidden; }
.v6 .gravura figcaption { padding: var(--space-12) var(--space-16); border-top: var(--stroke) solid var(--border); font-size: var(--text-apoio); }
.v6 .quadro { break-inside: avoid; margin-bottom: var(--space-24); padding: var(--space-16); border: var(--stroke) solid var(--border); border-radius: var(--radius); background: var(--acento); color: var(--ink); }
.v6 .classificados { column-span: all; display: grid; gap: 0; margin-bottom: var(--space-32); }
.v6 .classificado { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: var(--space-8) var(--space-16); padding-block: var(--space-24); border-top: 1px solid var(--border); }
.v6 .classificado .icone { --icone: 40px; grid-row: span 3; }
.v6 .classificado h3 { font-size: var(--text-lead); line-height: 1.3; }
.v6 .transcricao { column-span: all; display: grid; gap: var(--space-32); margin-bottom: var(--space-32); }
.v6 .transcricao ol { display: grid; gap: var(--space-12); }
.v6 .transcricao li { display: grid; grid-template-columns: 7.5em minmax(0, 1fr); gap: var(--space-12); font-size: var(--text-apoio); }
.v6 .transcricao li .turno__nota { grid-column: 2; }
.v6 .transcricao .lado { padding-top: var(--space-16); border-top: var(--stroke) solid var(--border); display: grid; gap: var(--space-16); align-content: start; }
.v6 .tabela-dados { column-span: all; width: 100%; border-collapse: collapse; margin-bottom: var(--space-32); }
.v6 .tabela-dados th, .v6 .tabela-dados td { text-align: left; padding: var(--space-12) var(--space-8); border-bottom: 1px solid var(--border); vertical-align: baseline; }
.v6 .tabela-dados th { font-family: var(--font-display); font-weight: 400; font-size: var(--text-titulo); white-space: nowrap; }
.v6 .tabela-dados tr:first-child th, .v6 .tabela-dados tr:first-child td { border-top: var(--stroke) solid var(--border); }
.v6 .final { column-span: all; display: grid; gap: var(--space-32); }
@media (min-width: 720px) {
  .v6 .credito { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .v6 .credito div + div { border-left: 1px solid var(--border); padding-left: var(--space-16); }
  .v6 .colunas { column-count: 2; }
  .v6 .classificados { grid-template-columns: 1fr 1fr; column-gap: var(--space-48); }
  .v6 .transcricao { grid-template-columns: 1fr 1fr; column-gap: var(--space-48); }
}
@media (min-width: 1100px) {
  .v6 .colunas { column-count: 3; }
}"""

    def transc(lista):
        out = []
        for quem, fala, nota in lista:
            rot = "Agente" if quem == "agente" else "Lead"
            n = f'<span class="turno__nota">{nota}</span>' if nota else ""
            out.append(f'<li><span class="t-rotulo">{rot}</span><span>{fala}</span>{n}</li>')
        return "<ol>" + "".join(out) + "</ol>"
    classificados = "".join(
        f'<article class="classificado">{c.icone(P, ic, 40)}<span class="t-rotulo">Camada 0{i}</span><h3>{tit}</h3><p class="t-apoio">{txt} <b>Efeito.</b> {ef}</p></article>'
        for i, (_, ic, tit, txt, ef) in enumerate(c.CAMADAS, 1))
    tabela = "".join(f'<tr><th scope="row">{v}</th><td>{f}</td></tr>' for _, v, f in c.STATS)
    main = f"""
<main id="conteudo" class="container jornal">
  <p class="cabeco t-rotulo"><span>Caso 02 · Omnichat</span><span>Agentic Experience · Agentes conversacionais</span></p>
  <h1 class="manchete">{c.TITULO}</h1>
  <p class="linha-fina">{c.LEAD}</p>
  <dl class="credito">{"".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c.FICHA)}</dl>

  <div class="colunas">
    <figure class="gravura">{c.ilustracao(P, "fronteira")}<figcaption>A fronteira de entrada, com a conversão de antes e de depois.</figcaption></figure>
    <div class="quadro">{c.icone(P, "grafico", 40)}{c.salto()}</div>
    <p class="t-lead">{c.CONTEXTO}</p>
    {"".join(f"<p>{p}</p>" for p in c.PROBLEMA)}
    {"".join(f"<p><b>{t}.</b> {x}</p>" for _, t, x in c.ORIGENS)}

    <h2>{c.CAMADAS_TITULO}</h2>
    <div class="classificados">{classificados}</div>

    <h2>{c.CONVERSA_TITULO}</h2>
    <div class="transcricao">
      <div class="lado"><p class="t-rotulo">{c.icone(P, "xis", 24, "icone-inline")}Antes. Conversa abandonada</p>{transc(c.ANTES)}</div>
      <div class="lado"><p class="t-rotulo">{c.icone(P, "check", 24, "icone-inline")}Depois. Lead convertido</p>{transc(c.DEPOIS)}</div>
    </div>

    <h2>{c.RESULTADO_TITULO}</h2>
    {"".join(f"<p>{p}</p>" for p in c.RESULTADO)}
    <table class="tabela-dados"><caption class="sr">Números do resultado</caption><tbody>{tabela}</tbody></table>
    <div class="final">{c.callout()}{c.fechamento(P)}</div>
  </div>
</main>"""
    return "Jornal", css, main


VARIACOES = [v1, v2, v3, v4, v5, v6]
RESUMO = [
    ("Grade suíça", "Doze colunas assimétricas. O número da seção pendura na margem, o texto corre estreito e o apoio senta à direita, na mesma linha do que comenta."),
    ("Coluna e margem", "Uma coluna na medida de leitura e uma margem larga para notas, como em Tufte. A ilustração abre como figura com legenda, e o número senta sobre ela."),
    ("Capítulos", "Hero dividido ao meio e cada seção aberta por uma página de capítulo, com número enorme e ícone grande. Depois, leitura numa coluna só."),
    ("Sumário e mosaico", "Sumário fixo com ícones à esquerda e o conteúdo em blocos de tamanhos diferentes. No celular, o sumário vira um trilho na borda direita."),
    ("Pôster", "O indicador vira a manchete, em tamanho de cartaz, com a ilustração do salto entre os dois números. Grade quebrada, adesivos sobre os cantos."),
    ("Jornal", "Manchete, linha fina, crédito com fios, texto em colunas, quadro de dados e a conversa como transcrição de entrevista."),
]


def indice():
    itens = "".join(
        f'<li class="card" style="display:grid;gap:var(--space-12)"><span class="t-rotulo">Variação {i}{" · escolhida" if i == 4 else ""}</span><h2 class="t-sub">{t}</h2><p class="t-apoio">{d}</p><a class="link" data-variant="seguir" href="v{i}.html">Abrir a variação {i} <i aria-hidden="true">→</i></a></li>'
        for i, (t, d) in enumerate(RESUMO, 1))
    css = ".lista-var{display:grid;gap:var(--grade-vao);padding-block:var(--space-32) var(--space-secao)}@media(min-width:720px){.lista-var{grid-template-columns:1fr 1fr}}@media(min-width:1100px){.lista-var{grid-template-columns:repeat(3,1fr)}}"
    main = f"""
<main id="conteudo" class="container">
  <header style="display:grid;gap:var(--space-16);padding-top:var(--space-64)">
    <p class="t-rotulo">Prova · Fase 2</p>
    <h1 class="t-display">Seis jeitos de contar o&nbsp;Omnichat</h1>
    <p class="t-sub" style="max-width:40ch">A variação 4 virou o modelo de Caso, com o sumário em trilho no celular. As outras ficam como registro.</p>
  </header>
  <ol class="lista-var">{itens}</ol>
</main>"""
    return c.cabeca(P, "Variações · Omnichat no Jeff DS", css) + c.CARGA + c.cabecalho(P, "index.html") + main + c.rodape(P, "index.html")


OUT.mkdir(exist_ok=True)
for i, fn in enumerate(VARIACOES, 1):
    nome, css, main = fn()
    html = c.cabeca(P, f"Variação {i}, {nome} · Omnichat no Jeff DS", css, f"v{i}") + c.CARGA + c.cabecalho(P, f"v{i}.html") + main + c.rodape(P, f"v{i}.html")
    (OUT / f"v{i}.html").write_text(html)
for velho in ("v4-faixa.html", "v4-botao.html", "v4-trilho.html"):
    (OUT / velho).unlink(missing_ok=True)
(OUT / "index.html").write_text(indice())

# A prova de antes, com o menu e o rodapé novos.
base = (AQUI / "omnichat.html").read_text()
ini, fim = base.index("<main"), base.index("</main>") + len("</main>")
miolo = base[ini:fim]
miolo = '<main id="conteudo">' + miolo[miolo.index(">") + 1:]
miolo = miolo.replace('id="contexto" ', "", 1)
(AQUI / "omnichat.html").write_text(c.cabeca("../../", "Prova · Omnichat no Jeff DS") + c.CARGA + c.cabecalho("../../", "omnichat.html") + "\n" + miolo + "\n" + c.rodape("../../", "omnichat.html"))
print("ok")
