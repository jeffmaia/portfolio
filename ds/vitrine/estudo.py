"""Estudo do Passos. Seis direções para as seis formas do componente.

O mesmo método das seis variações de página (ds/prova/variacoes.py e
ds/REFERENCIAS.md). Mesmo texto, mesmos tokens e ícones do Jeff DS, e cada
direção parte de um princípio editorial diferente. Cada direção monta as seis
formas (sequência, par, estágios, funil, trilha e ritos) numa página com o
Sumário, para a peça ter a largura que tem no caso.

O CSS de cada direção mora aqui, preso à classe dela (.d1 a .d6). Nada daqui
vai para componentes.css antes de você escolher.

Uso: python3 ds/vitrine/estudo.py
Escreve ds/vitrine/estudo/index.html e ds/vitrine/estudo/d1.html a d6.html.
"""
from pathlib import Path
import sys

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import gerar as g  # noqa: E402

c = g.c
P = g.P_SUB
SAIDA = AQUI / "estudo"


def ic(nome, classe="icone"):
    return c.icone(P, nome, 56, classe)


# ── O texto, das páginas publicadas ──────────────────────────

# Mapa de experiência, Seção 03. Ícone, título, parágrafos e consequência.
SEQ = [
    ("grafico", "Entender os&nbsp;dados do&nbsp;NPS",
     ["Clusterizamos os comentários do NPS em grandes eixos e subcategorias, com uma divisão entre semestres. Era preciso um relatório que ilustrasse a jornada do aluno do início ao fim da graduação, para que a ação surtisse efeito no período específico de cada problema."],
     "A insatisfação deixou de ser uma nota única e&nbsp;passou a ter lugar e momento na jornada."),
    ("pessoa", "Completar o&nbsp;que a&nbsp;reclamação não&nbsp;contava",
     ["As informações que tínhamos não bastavam, e fomos atrás dos alunos para preencher outros aspectos da vida deles. Um aluno que mora longe sofre muito mais com um cancelamento de aula em cima da hora, e nada disso aparece na nota."],
     "As ações passaram a considerar o contexto de&nbsp;vida do&nbsp;aluno, não só a&nbsp;reclamação registrada."),
    ("rota", "Achar um&nbsp;formato que&nbsp;obrigue a&nbsp;percorrer",
     ["O tabuleiro foi escolhido porque obriga quem lê a&nbsp;andar por semestre e&nbsp;por&nbsp;eixo, e&nbsp;é nesse trajeto que o time reconhece o próprio aluno e&nbsp;propõe ação."],
     "O formato virou parte da solução, não a&nbsp;embalagem da pesquisa."),
]

# Processo com IA, Seção 02.
PAR = [
    ("dialogo", "O&nbsp;trabalho vivia em&nbsp;reunião", "A gente discutia bem e decidia bem. Depois alguém tinha que transformar aquilo em PRD, story, relatório e protótipo. Esse alguém sempre demorava."),
    ("calendario", "A&nbsp;garantia prévia custava semanas", "Como construir era caro, quase toda validação acontecia antes do desenvolvimento. Fazia sentido, e consumia semanas."),
]

# Processo com IA, Seção 03. A saída abre nas cinco entregas.
EST = [
    ("Entrada", "dialogo", "Transcrição dos rituais", "O que o time já falava em reunião, agora capturado como matéria&nbsp;prima."),
    ("Camada", "robo", "Habilidades no&nbsp;Claude", "Habilidades que a gente criou leem a transcrição e devolvem os rascunhos."),
    ("Saída", "janela", "Cinco entregas", ""),
]
ENTREGAS = ["Visão de produto", "PRD", "User stories", "Relatório de usabilidade", "Protótipo"]

# Processo com IA, Seção 06.
FUNIL = [
    ("lupa", "Identificação de oportunidades", "Dado de produto, pesquisa e canais de feedback alimentam uma árvore de oportunidades que facilita escolher o que entra em pauta.", "Produto e design, com&nbsp;dados alimentando a&nbsp;árvore."),
    ("alvo", "Validação de desejabilidade e&nbsp;diferencial", "Confirmamos se a aposta faz sentido antes de o time gastar tempo desenhando a solução.", "Produto e design."),
    ("lapis", "Definição e&nbsp;prototipagem", "É aqui que nasce a maior parte da solução. O&nbsp;protótipo já sai desenvolvido e segue para a&nbsp;engenharia sem etapa de tradução no&nbsp;meio.", "Produto, design e engenharia."),
    ("celular", "Delivery", "Alfa na engenharia, que garante o funcionamento do que foi construído. Beta, aberto ou fechado, validando o experimento antes de abrir para todos.", "Engenharia no alfa, time inteiro no beta."),
    ("grafico", "Depois do lançamento", "O foco vira satisfação e adoção. A&nbsp;validação qualitativa entra quando o&nbsp;dado quantitativo mostra desvio do&nbsp;esperado.", "Produto, design e dados."),
]

# Processo com IA, Seção 07.
TRILHA = [
    ("lampada", "Criação", "Novo componente nasce a partir de uma&nbsp;necessidade do&nbsp;produto."),
    ("olho", "Comportamento e&nbsp;uso", "Definição escrita pensando também na&nbsp;leitura do&nbsp;Claude."),
    ("verifica", "Aprovação no&nbsp;código", "Validação direto no&nbsp;código, antes de subir para o repositório no&nbsp;GitHub."),
]

# Processo com IA, Seção 04.
RITOS = [
    ("calendario", "Planning", "Virou assíncrona e sob&nbsp;demanda, não&nbsp;mais um rito&nbsp;semanal."),
    ("pessoa", "Daily", "Ficou só com engenharia. Produto entra quando&nbsp;precisa."),
    ("lupa", "Refinamento", "De 4 horas para 40&nbsp;minutos, porque virou tirar dúvida sobre o&nbsp;que já&nbsp;está escrito."),
]

FORMAS = [
    ("rota", "Sequência", "Etapas em ordem, com o texto do&nbsp;Mapa"),
    ("camadas", "Par", "Duas coisas ao mesmo tempo, com o&nbsp;Processo"),
    ("robo", "Estágios", "Entrada, meio e&nbsp;saída, com o&nbsp;Processo"),
    ("alvo", "Funil", "Cada etapa filtra a&nbsp;anterior, com o&nbsp;Processo"),
    ("lampada", "Trilha", "Um caminho curto, com o&nbsp;Processo"),
    ("calendario", "Ritos", "Ritos de time, com o&nbsp;Processo"),
]


def nn(i):
    return f"{i:02d}"


def ps(pars):
    return "".join(f"<p>{x}</p>" for x in pars)


def efeito(rotulo, texto):
    return f'<p class="step__efeito"><span class="t-rotulo">{rotulo}</span> {texto}</p>'


SETA = '<svg class="seta" viewBox="0 0 40 24" width="40" height="24" aria-hidden="true"><path d="M3 12h32M27 4l8 8-8 8" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def entregas_lista():
    return '<ul class="entregas">' + "".join(f'<li><span class="badge">{e}</span></li>' for e in ENTREGAS) + "</ul>"


# ============================================================ D1
# Tabela suíça. Grade modular, réguas de tinta e o número em Anton pendurado
# na primeira coluna. A forma de cada Passos é uma tabela tipográfica, e o
# funil vira um gráfico de barras que encolhe.
D1_CSS = """
.d1 .tabela { border-top: var(--stroke) solid var(--border); }
.d1 .tabela > li { display: grid; gap: var(--space-8) var(--grade-vao); padding-block: var(--space-24); border-bottom: 1px solid var(--border); }
.d1 .num { font-family: var(--font-display); font-size: var(--text-display); line-height: .85; }
.d1 .tabela .icone { --icone: 40px; }
.d1 .cabeca { display: flex; align-items: center; gap: var(--space-12); }
.d1 .barra { height: 20px; width: calc(100% - var(--i) * 15%); border: var(--stroke) solid var(--border); background: var(--acento); }
.d1 .eixo { display: grid; gap: var(--space-24); }
.d1 .eixo > li { display: grid; gap: var(--space-8); padding-top: var(--space-16); border-top: var(--stroke) solid var(--border); position: relative; }
.d1 .eixo > li::before { content: ""; position: absolute; top: -7px; left: 0; width: 12px; height: 12px; background: var(--ink); }
.d1 .ritos { display: grid; gap: var(--space-24); }
.d1 .ritos > li { display: grid; gap: var(--space-8); padding-top: var(--space-16); border-top: var(--stroke) solid var(--border); }
.d1 .ritos h3 { font-family: var(--font-flare); font-weight: 300; font-size: var(--text-sub); line-height: 1.1; }
.d1 .est { display: grid; border-top: var(--stroke) solid var(--border); border-bottom: var(--stroke) solid var(--border); }
.d1 .est > li { display: grid; gap: var(--space-8); align-content: start; padding: var(--space-24) var(--space-16); }
.d1 .est > li + li { border-top: 1px solid var(--border); }
.d1 .est > li:nth-child(2) { background: var(--acento); }
.d1 .entregas { display: flex; flex-wrap: wrap; gap: var(--space-8); }
@media (min-width: 720px) {
  .d1 .tabela > li { grid-template-columns: minmax(0, 1fr) minmax(0, 3fr) minmax(0, 4fr); align-items: baseline; }
  .d1 .tabela > li > .num { grid-row: 1 / span 2; }
  .d1 .tabela > li > .texto { grid-column: 3; grid-row: 1 / span 2; display: grid; gap: var(--space-12); }
  .d1 .par.tabela > li { grid-template-columns: minmax(0, 1fr) minmax(0, 3fr); }
  .d1 .par.tabela { display: grid; grid-template-columns: 1fr 1fr; column-gap: var(--grade-vao); }
  .d1 .funil.tabela > li { grid-template-columns: minmax(0, 3fr) minmax(0, 3fr) minmax(0, 2fr); }
  .d1 .funil.tabela > li > .barra { grid-column: 1 / -1; }
  .d1 .eixo, .d1 .ritos { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .d1 .est { grid-template-columns: minmax(0, 1fr) minmax(0, 1.4fr) minmax(0, 1fr); }
  .d1 .est > li + li { border-top: 0; border-left: 1px solid var(--border); }
}
"""


def d1():
    seq = '<ol class="tabela">' + "".join(
        f'<li><span class="num" aria-hidden="true">{nn(i)}</span><h3 class="step__titulo">{t}</h3><div class="texto">{ps(p)}{efeito("Consequência", e)}</div></li>'
        for i, (_, t, p, e) in enumerate(SEQ, 1)) + "</ol>"
    par = '<ul class="par tabela">' + "".join(
        f'<li><span class="cabeca">{ic(i_)}</span><div class="texto"><h3 class="step__titulo">{t}</h3><p>{x}</p></div></li>'
        for i_, t, x in PAR) + "</ul>"
    est = '<ol class="est">' + "".join(
        f'<li><span class="cabeca">{ic(i_)}<span class="t-rotulo">{m}</span></span><h3 class="step__titulo">{t}</h3>{f"<p>{x}</p>" if x else entregas_lista()}</li>'
        for m, i_, t, x in EST) + "</ol>"
    funil = '<ol class="funil tabela">' + "".join(
        f'<li style="--i: {i}"><span class="barra" aria-hidden="true"></span><h3 class="step__titulo">{nn(i + 1)} {t}</h3><p>{x}</p><p class="t-apoio"><span class="t-rotulo">Quem conduz</span><br>{q}</p></li>'
        for i, (_, t, x, q) in enumerate(FUNIL)) + "</ol>"
    trilha = '<ol class="eixo">' + "".join(
        f'<li><span class="t-rotulo">{nn(i)}</span><h3 class="step__titulo">{t}</h3><p>{x}</p></li>'
        for i, (_, t, x) in enumerate(TRILHA, 1)) + "</ol>"
    ritos = '<ul class="ritos">' + "".join(f'<li><h3>{t}</h3><p>{x}</p></li>' for _, t, x in RITOS) + "</ul>"
    return [seq, par, est, funil, trilha, ritos]


# ============================================================ D2
# Coluna e margem. O marcador (adesivo e número) mora na margem, o texto
# corre na medida de leitura, e o efeito vira nota em Fraunces. O meio dos
# estágios ganha corpo de título, e a trilha vira uma frase.
D2_CSS = """
.d2 .marg { display: grid; gap: var(--space-32); }
.d2 .marg > li { display: grid; gap: var(--space-12); }
.d2 .margem { display: flex; align-items: center; gap: var(--space-12); }
.d2 .margem .num { font-family: var(--font-display); font-size: 2rem; line-height: 1; }
.d2 .corpo { display: grid; gap: var(--space-12); max-width: 60ch; }
.d2 .nota { font-family: var(--font-flare); font-weight: 300; font-style: italic; font-size: var(--text-lead); line-height: 1.35; }
.d2 .nota .t-rotulo { display: block; font-family: var(--font-texto); font-style: normal; margin-bottom: var(--space-4); }
.d2 .meio h3 { font-family: var(--font-flare); font-weight: 300; font-size: var(--text-titulo); line-height: 1.05; }
.d2 .meio h3 span { background: var(--acento); box-decoration-break: clone; -webkit-box-decoration-break: clone; padding-inline: .1em; }
.d2 .duas { display: grid; gap: var(--space-24); }
.d2 .frase { font-family: var(--font-flare); font-weight: 300; font-size: var(--text-sub); line-height: 1.25; }
.d2 .frase b { font-weight: 400; }
.d2 .frase .seta { display: inline-block; vertical-align: middle; margin-inline: .2em; }
.d2 .estreita { display: block; height: 10px; margin-top: var(--space-8); width: calc(100% - var(--i) * 15%); background: var(--acento); border: var(--stroke) solid var(--border); }
.d2 .entregas { display: flex; flex-wrap: wrap; gap: var(--space-8); }
@media (min-width: 720px) {
  .d2 .marg > li { grid-template-columns: minmax(0, 1fr) minmax(0, 3fr); column-gap: var(--grade-vao); }
  .d2 .margem { flex-direction: column; align-items: flex-start; align-self: start; }
  .d2 .duas { grid-template-columns: 1fr 1fr; column-gap: var(--grade-vao); }
}
"""


def d2():
    seq = '<ol class="marg">' + "".join(
        f'<li><div class="margem">{ic(i_)}<span class="num" aria-hidden="true">{nn(i)}</span></div><div class="corpo"><h3 class="step__titulo">{t}</h3>{ps(p)}<p class="nota"><span class="t-rotulo">Consequência</span>{e}</p></div></li>'
        for i, (i_, t, p, e) in enumerate(SEQ, 1)) + "</ol>"
    par = f'<ul class="marg"><li><div class="margem"><span class="t-rotulo">Ao mesmo tempo</span></div><div class="duas">{"".join(f"<div class=corpo>{ic(i_)}<h3 class=step__titulo>{t}</h3><p>{x}</p></div>" for i_, t, x in PAR)}</div></li></ul>'
    est = '<ol class="marg">' + "".join(
        f'<li class="{"meio" if k == 1 else ""}"><div class="margem">{ic(i_)}<span class="t-rotulo">{m}</span></div><div class="corpo"><h3 class="{"" if k == 1 else "step__titulo"}">{"<span>" + t + "</span>" if k == 1 else t}</h3>{f"<p>{x}</p>" if x else entregas_lista()}</div></li>'
        for k, (m, i_, t, x) in enumerate(EST)) + "</ol>"
    funil = '<ol class="marg">' + "".join(
        f'<li style="--i: {i}"><div class="margem" style="display:block;width:100%"><span class="num" aria-hidden="true">{nn(i + 1)}</span><span class="estreita" aria-hidden="true"></span></div><div class="corpo"><h3 class="step__titulo">{t}</h3><p>{x}</p><p class="nota"><span class="t-rotulo">Quem conduz</span>{q}</p></div></li>'
        for i, (_, t, x, q) in enumerate(FUNIL)) + "</ol>"
    frase = f' {SETA} '.join(f"<b>{t}</b>" for _, t, _ in TRILHA)
    trilha = f'''<div class="marg"><div style="display:grid;gap:var(--space-24)">
      <p class="frase" aria-hidden="true">{frase}</p>
      <ol class="duas" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">{"".join(f'<li class="corpo"><span class="t-rotulo">{nn(i)} · {t}</span><p>{x}</p></li>' for i, (_, t, x) in enumerate(TRILHA, 1))}</ol>
    </div></div>'''
    ritos = '<ul class="marg">' + "".join(
        f'<li><div class="margem">{ic(i_)}<span class="frase">{t}</span></div><div class="corpo"><p>{x}</p></div></li>'
        for i_, t, x in RITOS) + "</ul>"
    return [seq, par, est, funil, trilha, ritos]


# ============================================================ D3
# Adesivos. A iconografia na frente. Cada etapa é um Cartão com o ícone
# adesivo grande sobre o canto e o número em Anton vazado. Os estágios se
# ligam por setas desenhadas, o funil empilha Cartões que estreitam e os
# ritos viram folhas de agenda.
D3_CSS = """
.d3 .cartoes { display: grid; gap: var(--space-48) var(--grade-vao); padding-top: var(--space-24); }
.d3 .cartao { position: relative; display: grid; gap: var(--space-12); align-content: start; padding: var(--space-48) var(--space-24) var(--space-24); border: var(--stroke) solid var(--border); border-radius: var(--radius); background: var(--background); }
.d3 .cartao > .icone { position: absolute; top: -30px; left: var(--space-16); --icone: 64px; }
.d3 .cartao > .num { position: absolute; top: var(--space-12); right: var(--space-16); font-family: var(--font-display); font-size: 2.5rem; line-height: 1; color: transparent; -webkit-text-stroke: 1.5px var(--ink); }
.d3 .cartao--acento { background: var(--acento); color: var(--ink); }
.d3 .fila { display: grid; gap: var(--space-16); justify-items: center; }
.d3 .fila > .seta { transform: rotate(90deg); }
.d3 .fila > .cartao { width: 100%; }
.d3 .funil { display: grid; gap: var(--space-48); justify-items: center; padding-top: var(--space-24); }
.d3 .funil > .cartao { width: calc(100% - var(--i) * 9%); }
.d3 .agenda { display: grid; gap: var(--space-24); }
.d3 .folha { border: var(--stroke) solid var(--border); border-radius: var(--radius); overflow: hidden; background: var(--background); }
.d3 .folha__topo { display: flex; align-items: center; gap: var(--space-12); padding: var(--space-12) var(--space-16); background: var(--acento); color: var(--ink); border-bottom: var(--stroke) solid var(--border); }
.d3 .folha__topo .icone { --icone: 40px; }
.d3 .folha__topo h3 { font-family: var(--font-display); font-weight: 400; font-size: 1.5rem; text-transform: uppercase; line-height: 1; }
.d3 .folha p { padding: var(--space-16); }
.d3 .cartao p { max-width: var(--leitura); }
/* A saída lista as entregas com fios, porque o nome mais longo não cabe
   numa pílula na largura de um terço. */
.d3 .entregas { display: grid; font-size: var(--text-apoio); }
.d3 .entregas li { padding-block: var(--space-8); border-top: 1px solid var(--border); }
.d3 .entregas li:last-child { border-bottom: 1px solid var(--border); }
/* A trilha liga os adesivos por um fio tracejado, que só aparece entre
   os Cartões: vertical até 1099px, horizontal depois. */
.d3 .trilha { position: relative; }
.d3 .trilha::before { content: ""; position: absolute; top: 0; bottom: 0; left: 47px; border-left: var(--stroke) dashed var(--border); }
/* O arranjo segue a largura da Seção, não a da tela. A partir de 1100px
   o Sumário ocupa a coluna da esquerda, e a Seção volta a ter uns 750px,
   a mesma largura do tablet. */
.d3 .section { container-type: inline-size; }
@container (min-width: 600px) {
  .d3 .cartoes--par { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .d3 .agenda { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
/* Três Cartões lado a lado só com 900px de Seção. Abaixo disso cada um
   fica com menos de 250px e o conteúdo de dentro não cabe. */
@container (min-width: 900px) {
  .d3 .cartoes { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .d3 .cartoes--par { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .d3 .fila { grid-template-columns: minmax(0, 1fr) auto minmax(0, 1.3fr) auto minmax(0, 1fr); align-items: center; }
  .d3 .fila > .seta { transform: none; }
  .d3 .fila > .cartao { align-self: stretch; }
  .d3 .trilha::before { top: 50%; bottom: auto; left: 0; right: 0; border-left: 0; border-top: var(--stroke) dashed var(--border); }
}
"""


def d3():
    def cartao(i_, num, corpo, extra=""):
        n = f'<span class="num" aria-hidden="true">{num}</span>' if num else ""
        return f'<li class="cartao {extra}">{ic(i_)}{n}{corpo}</li>'
    seq = '<ol class="cartoes">' + "".join(
        cartao(i_, nn(i), f'<h3 class="step__titulo">{t}</h3>{ps(p)}{efeito("Consequência", e)}')
        for i, (i_, t, p, e) in enumerate(SEQ, 1)) + "</ol>"
    par = '<ul class="cartoes cartoes--par">' + "".join(cartao(i_, "", f'<h3 class="step__titulo">{t}</h3><p>{x}</p>') for i_, t, x in PAR) + "</ul>"
    lista_saida = '<ul class="entregas">' + "".join(f"<li>{e}</li>" for e in ENTREGAS) + "</ul>"
    partes = []
    for k, (m, i_, t, x) in enumerate(EST):
        if k:
            partes.append(SETA)
        corpo = f'<span class="t-rotulo">{m}</span><h3 class="step__titulo">{t}</h3>{f"<p>{x}</p>" if x else lista_saida}'
        partes.append(f'<div class="cartao {"cartao--acento" if k == 1 else ""}">{ic(i_)}{corpo}</div>')
    est = f'<div class="fila" role="list">{"".join(p if p == SETA else p.replace("<div class=", "<div role=listitem class=", 1) for p in partes)}</div>'
    funil = '<ol class="funil">' + "".join(
        f'<li class="cartao" style="--i: {i}">{ic(i_)}<span class="num" aria-hidden="true">{nn(i + 1)}</span><h3 class="step__titulo">{t}</h3><p>{x}</p>{efeito("Quem conduz", q)}</li>'
        for i, (i_, t, x, q) in enumerate(FUNIL)) + "</ol>"
    trilha = '<ol class="cartoes trilha">' + "".join(cartao(i_, nn(i), f'<h3 class="step__titulo">{t}</h3><p>{x}</p>') for i, (i_, t, x) in enumerate(TRILHA, 1)) + "</ol>"
    ritos = '<ul class="agenda">' + "".join(
        f'<li class="folha"><div class="folha__topo">{c.icone(P, i_, 40, "icone")}<h3>{t}</h3></div><p>{x}</p></li>'
        for i_, t, x in RITOS) + "</ul>"
    return [seq, par, est, funil, trilha, ritos]


# ============================================================ D4
# Diagrama. A forma é desenhada na gramática dos adesivos, com traço de
# tinta, corpo no acento e sombra sólida. A sequência sobe como escada, o
# funil é um funil de verdade ao lado do texto, a trilha é uma estrada com
# os marcos em cima, e os ritos fecham um laço.
D4_CSS = """
.d4 .escada { display: grid; gap: var(--space-32); }
.d4 .degrau { display: grid; gap: var(--space-12); align-content: start; }
.d4 .degrau__base { display: flex; align-items: flex-end; padding-top: 28px; }
.d4 .degrau__bloco { height: 72px; }
.d4 .degrau__base > .degrau__bloco { width: 100%; }
.d4 .degrau__bloco { position: relative; display: grid; place-items: end start; height: calc(56px + var(--i) * 40px); padding: var(--space-12); border: var(--stroke) solid var(--border); border-radius: var(--radius) var(--radius) 0 0; background: var(--acento); color: var(--ink); filter: drop-shadow(4px 4px 0 var(--ink)); }
.d4 .degrau__bloco .icone { position: absolute; top: -28px; right: var(--space-12); --icone: 56px; }
.d4 .degrau__bloco .num { font-family: var(--font-display); font-size: 2.5rem; line-height: 1; }
.d4 .trilhos { display: grid; gap: var(--space-32); }
.d4 .trilhos > li { display: grid; gap: var(--space-12); }
.d4 .trilho { position: relative; display: flex; align-items: center; height: 56px; }
.d4 .trilho::before { content: ""; position: absolute; left: 28px; right: 10px; height: var(--stroke); background: var(--ink); }
.d4 .trilho::after { content: ""; position: absolute; right: 0; border: 8px solid transparent; border-left: 12px solid var(--ink); border-right: 0; }
.d4 .trilho .icone { position: relative; --icone: 56px; }
.d4 .maquina { display: grid; gap: var(--space-16); justify-items: center; }
.d4 .maquina > .seta { transform: rotate(90deg); }
.d4 .modulo { display: grid; gap: var(--space-8); justify-items: center; text-align: center; padding: var(--space-24); width: 100%; border: var(--stroke) solid var(--border); border-radius: var(--radius); }
.d4 .modulo .icone { --icone: 64px; }
.d4 .modulo--meio { background: var(--acento); color: var(--ink); filter: drop-shadow(4px 4px 0 var(--ink)); }
.d4 .modulo--meio .icone { --icone: 96px; }
.d4 .entregas { display: grid; gap: var(--space-4); justify-items: center; }
.d4 .funil { display: grid; }
.d4 .funil > li { display: grid; grid-template-columns: 88px minmax(0, 1fr); column-gap: var(--space-16); }
.d4 .funil__forma { position: relative; }
.d4 .funil__forma svg { position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible; filter: drop-shadow(3px 3px 0 var(--ink)); }
.d4 .funil__forma .num { position: absolute; top: var(--space-16); left: 0; right: 0; text-align: center; font-family: var(--font-display); font-size: 1.5rem; line-height: 1; }
.d4 .funil__texto { display: grid; gap: var(--space-8); padding-block: var(--space-16); }
.d4 .estrada { display: none; }
.d4 .marcos { display: grid; gap: var(--space-24); position: relative; padding-left: 72px; }
.d4 .marcos::before { content: ""; position: absolute; left: 20px; top: 0; bottom: 0; width: 16px; border-inline: var(--stroke) solid var(--ink); background: var(--acento) linear-gradient(var(--paper) 50%, transparent 0) center / 2px 14px repeat-y; }
.d4 .marcos > li { position: relative; display: grid; gap: var(--space-8); min-height: 56px; }
.d4 .marcos > li .icone { position: absolute; left: -72px; top: 0; --icone: 56px; }
.d4 .laco { display: grid; gap: var(--space-24); }
.d4 .laco > li { display: grid; gap: var(--space-8); justify-items: start; }
.d4 .laco > li .icone { --icone: 56px; }
.d4 .laco__volta { display: none; }
@media (min-width: 720px) {
  .d4 .escada { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .d4 .degrau__base { height: calc(56px + 2 * 40px + 28px); }
  .d4 .degrau__bloco { height: calc(56px + var(--i) * 40px); }
  .d4 .trilhos { grid-template-columns: 1fr 1fr; column-gap: var(--grade-vao); }
  .d4 .maquina { grid-template-columns: minmax(0, 1fr) auto minmax(0, 1.3fr) auto minmax(0, 1fr); align-items: center; }
  .d4 .maquina > .seta { transform: none; }
  .d4 .funil > li { grid-template-columns: 200px minmax(0, 1fr); column-gap: var(--grade-vao); }
  .d4 .estrada { display: block; width: 100%; height: 120px; margin-bottom: calc(-1 * var(--space-48)); }
  .d4 .marcos { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); padding-left: 0; }
  .d4 .marcos::before { display: none; }
  .d4 .marcos > li { justify-items: center; text-align: center; padding-top: 72px; }
  .d4 .marcos > li .icone { left: 50%; top: 0; transform: translateX(-50%); }
  .d4 .laco { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .d4 .laco__volta { display: block; grid-column: 1 / -1; height: 48px; margin-inline: 28px; border: var(--stroke) solid var(--ink); border-top: 0; border-radius: 0 0 24px 24px; position: relative; }
  .d4 .laco__volta::after { content: ""; position: absolute; left: -10px; top: -14px; border: 9px solid transparent; border-bottom: 14px solid var(--ink); border-top: 0; }
}
"""


def faixa_funil(i, n):
    passo = 60 / n
    a, b = 100 - i * passo, 100 - (i + 1) * passo
    pts = f"{50 - a / 2},0 {50 + a / 2},0 {50 + b / 2},100 {50 - b / 2},100"
    return f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"><polygon points="{pts}" fill="var(--acento)" stroke="var(--ink)" stroke-width="2.6" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>'


ESTRADA = '''<svg class="estrada" viewBox="0 0 900 120" preserveAspectRatio="none" aria-hidden="true">
  <path d="M0 60 Q75 10 150 60 T300 60 T450 60 T600 60 T750 60 T900 60" fill="none" stroke="var(--ink)" stroke-width="22" vector-effect="non-scaling-stroke"/>
  <path d="M0 60 Q75 10 150 60 T300 60 T450 60 T600 60 T750 60 T900 60" fill="none" stroke="var(--acento)" stroke-width="16" vector-effect="non-scaling-stroke"/>
  <path d="M0 60 Q75 10 150 60 T300 60 T450 60 T600 60 T750 60 T900 60" fill="none" stroke="var(--paper)" stroke-width="2" stroke-dasharray="10 10" vector-effect="non-scaling-stroke"/>
</svg>'''


def d4():
    seq = '<ol class="escada">' + "".join(
        f'<li class="degrau" style="--i: {i}"><div class="degrau__base" aria-hidden="true"><div class="degrau__bloco">{ic(i_)}<span class="num">{nn(i + 1)}</span></div></div><h3 class="step__titulo">{t}</h3>{ps(p)}{efeito("Consequência", e)}</li>'
        for i, (i_, t, p, e) in enumerate(SEQ)) + "</ol>"
    par = '<ul class="trilhos">' + "".join(
        f'<li><div class="trilho" aria-hidden="true">{ic(i_)}</div><h3 class="step__titulo">{t}</h3><p>{x}</p></li>'
        for i_, t, x in PAR) + "</ul>"
    partes = []
    for k, (m, i_, t, x) in enumerate(EST):
        if k:
            partes.append(SETA)
        corpo = f'{ic(i_)}<span class="t-rotulo">{m}</span><h3 class="step__titulo">{t}</h3>{f"<p>{x}</p>" if x else "<ul class=entregas>" + "".join(f"<li class=t-apoio>{e}</li>" for e in ENTREGAS) + "</ul>"}'
        partes.append(f'<div role="listitem" class="modulo {"modulo--meio" if k == 1 else ""}">{corpo}</div>')
    est = f'<div class="maquina" role="list">{"".join(partes)}</div>'
    funil = '<ol class="funil">' + "".join(
        f'<li><div class="funil__forma">{faixa_funil(i, len(FUNIL))}<span class="num" aria-hidden="true">{nn(i + 1)}</span></div><div class="funil__texto"><h3 class="step__titulo">{t}</h3><p>{x}</p>{efeito("Quem conduz", q)}</div></li>'
        for i, (_, t, x, q) in enumerate(FUNIL)) + "</ol>"
    trilha = f'''<div>{ESTRADA}<ol class="marcos">{"".join(
        f'<li>{ic(i_)}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for i_, t, x in TRILHA)}</ol></div>'''
    ritos = '<ul class="laco">' + "".join(
        f'<li>{ic(i_)}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for i_, t, x in RITOS) + '<li class="laco__volta" aria-hidden="true"></li></ul>'
    return [seq, par, est, funil, trilha, ritos]


# ============================================================ D5
# Linha do tempo. Uma espinha de tinta liga as etapas, e cada nó é o ícone
# adesivo num disco. No funil os nós encolhem, nos estágios o nó do meio é
# o maior, e a trilha corre na horizontal.
D5_CSS = """
.d5 .espinha { position: relative; display: grid; gap: var(--space-32); padding-left: 88px; }
.d5 .espinha::before { content: ""; position: absolute; left: 35px; top: 8px; bottom: 8px; width: var(--stroke); background: var(--ink); }
.d5 .espinha > li { position: relative; display: grid; gap: var(--space-8); }
.d5 .espinha > li > p { max-width: var(--leitura); }
.d5 .no { position: absolute; left: -88px; top: -4px; display: grid; place-items: center; width: 72px; height: 72px; border: var(--stroke) solid var(--border); border-radius: 50%; background: var(--background); }
.d5 .no .icone { --icone: 44px; }
.d5 .no--num { background: var(--acento); font-family: var(--font-display); font-size: 1.5rem; }
.d5 .espinha--funil .no { width: calc(72px - var(--i) * 8px); height: calc(72px - var(--i) * 8px); left: calc(-88px + var(--i) * 4px); }
.d5 .espinha .grande { width: 96px; height: 96px; left: -100px; background: var(--acento); }
.d5 .espinha .grande .icone { --icone: 64px; }
.d5 .meio { padding: var(--space-16) var(--space-24); border: var(--stroke) solid var(--border); border-radius: var(--radius); background: var(--acento); color: var(--ink); }
.d5 .duas { display: grid; gap: var(--space-32); }
.d5 .rotulo-par { display: block; margin-bottom: var(--space-16); }
.d5 .entregas { display: flex; flex-wrap: wrap; gap: var(--space-8); }
.d5 .ritos { display: grid; gap: var(--space-24); }
.d5 .ritos > li { display: grid; grid-template-columns: 72px minmax(0, 1fr); gap: var(--space-8) var(--space-16); align-items: start; }
.d5 .ritos .no { position: static; }
.d5 .ritos h3, .d5 .ritos p { grid-column: 2; }
.d5 .ritos .no { grid-row: 1 / span 2; }
@media (min-width: 720px) {
  .d5 .duas { grid-template-columns: 1fr 1fr; column-gap: var(--grade-vao); }
  .d5 .horizontal { padding-left: 0; padding-top: 96px; grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .d5 .horizontal::before { left: 36px; right: 36px; top: 36px; bottom: auto; width: auto; height: var(--stroke); }
  .d5 .horizontal .no { left: 0; top: -96px; }
  .d5 .ritos { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
}
"""


def d5():
    def no(i_, cls=""):
        return f'<span class="no {cls}" aria-hidden="true">{c.icone(P, i_, 44, "icone")}</span>'
    seq = '<ol class="espinha">' + "".join(
        f'<li>{no(i_)}<h3 class="step__titulo">{t}</h3>{ps(p)}{efeito("Consequência", e)}</li>'
        for i_, t, p, e in SEQ) + "</ol>"
    par = '<div class="duas">' + "".join(
        f'<div><span class="t-rotulo rotulo-par">Frente {nn(k)}</span><ol class="espinha"><li>{no(i_)}<h3 class="step__titulo">{t}</h3><p>{x}</p></li></ol></div>'
        for k, (i_, t, x) in enumerate(PAR, 1)) + "</div>"
    est = '<ol class="espinha">' + "".join(
        f'<li>{no(i_, "grande" if k == 1 else "")}<div class="{"meio" if k == 1 else ""}" style="display:grid;gap:var(--space-8)"><span class="t-rotulo">{m}</span><h3 class="step__titulo">{t}</h3>{f"<p>{x}</p>" if x else entregas_lista()}</div></li>'
        for k, (m, i_, t, x) in enumerate(EST)) + "</ol>"
    funil = '<ol class="espinha espinha--funil">' + "".join(
        f'<li style="--i: {i}"><span class="no no--num" aria-hidden="true">{nn(i + 1)}</span><h3 class="step__titulo">{t}</h3><p>{x}</p>{efeito("Quem conduz", q)}</li>'
        for i, (_, t, x, q) in enumerate(FUNIL)) + "</ol>"
    trilha = '<ol class="espinha horizontal">' + "".join(
        f'<li>{no(i_)}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for i_, t, x in TRILHA) + "</ol>"
    ritos = '<ul class="ritos">' + "".join(
        f'<li>{no(i_)}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for i_, t, x in RITOS) + "</ul>"
    return [seq, par, est, funil, trilha, ritos]


# ============================================================ D6
# Jornal. Fios finos, numerais em Fraunces itálico, texto em colunas e o
# quadro. O funil é uma pirâmide invertida de texto, em que a própria
# mancha estreita, e os estágios cabem num quadro dividido por fios.
D6_CSS = """
.d6 .numerado { display: grid; gap: var(--space-24); }
.d6 .numerado > li { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: var(--space-4) var(--space-16); padding-top: var(--space-16); border-top: 1px solid var(--border); }
.d6 .numeral { grid-row: 1 / span 4; font-family: var(--font-flare); font-style: italic; font-weight: 300; font-size: 3.5rem; line-height: .9; }
.d6 .numerado > li > :not(.numeral) { grid-column: 2; }
.d6 .efeito6 { font-size: var(--text-apoio); font-family: var(--font-flare); font-style: italic; }
.d6 .duas { display: grid; gap: var(--space-24); }
.d6 .duas > li { display: grid; gap: var(--space-8); }
.d6 .duas .icone { --icone: 40px; }
.d6 .quadro { display: grid; border: var(--stroke) solid var(--border); }
.d6 .quadro > li { display: grid; gap: var(--space-8); align-content: start; padding: var(--space-16); }
.d6 .quadro > li + li { border-top: 1px solid var(--border); }
.d6 .quadro > li:nth-child(2) { background: var(--acento); color: var(--ink); }
.d6 .quadro .icone { --icone: 40px; }
.d6 .entregas { display: grid; gap: 2px; font-size: var(--text-apoio); }
.d6 .entregas li::before { content: "· "; }
.d6 .piramide { display: grid; gap: 0; justify-items: center; text-align: center; }
.d6 .piramide > li { display: grid; gap: var(--space-8); width: calc(100% - var(--i) * 14%); padding-block: var(--space-16); border-top: 1px solid var(--border); }
.d6 .piramide > li:last-child { border-bottom: 1px solid var(--border); }
.d6 .piramide .numeral { font-size: 2rem; }
.d6 .linha { display: grid; gap: var(--space-16); border-block: 1px solid var(--border); padding-block: var(--space-16); }
.d6 .linha > li { display: grid; gap: var(--space-4); }
.d6 .linha h3 { font-family: var(--font-flare); font-weight: 300; font-size: var(--text-sub); line-height: 1.1; }
.d6 .caixa { border: var(--stroke) solid var(--border); padding: var(--space-24); display: grid; gap: var(--space-16); }
.d6 .caixa dl { display: grid; gap: var(--space-12); }
.d6 .caixa dl > div { display: grid; gap: var(--space-4); padding-top: var(--space-12); border-top: 1px solid var(--border); }
.d6 .caixa dt { font-weight: 700; }
.d6 .caixa dd { margin: 0; }
@media (min-width: 720px) {
  .d6 .numerado { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .d6 .duas { grid-template-columns: 1fr 1fr; column-gap: 0; }
  .d6 .duas > li:first-child { padding-right: var(--grade-vao); border-right: 1px solid var(--border); }
  .d6 .duas > li:last-child { padding-left: var(--grade-vao); }
  .d6 .quadro { grid-template-columns: minmax(0, 1fr) minmax(0, 1.3fr) minmax(0, 1fr); }
  .d6 .quadro > li + li { border-top: 0; border-left: 1px solid var(--border); }
  .d6 .linha { grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: var(--grade-vao); }
  .d6 .linha > li + li { padding-left: var(--grade-vao); border-left: 1px solid var(--border); }
  .d6 .caixa dl > div { grid-template-columns: minmax(0, 1fr) minmax(0, 3fr); column-gap: var(--grade-vao); }
}
"""


def d6():
    seq = '<ol class="numerado">' + "".join(
        f'<li><span class="numeral" aria-hidden="true">{i}</span><h3 class="step__titulo">{t}</h3>{ps(p)}<p class="efeito6">{e}</p></li>'
        for i, (_, t, p, e) in enumerate(SEQ, 1)) + "</ol>"
    par = '<ul class="duas">' + "".join(
        f'<li>{ic(i_)}<h3 class="step__titulo">{t}</h3><p>{x}</p></li>' for i_, t, x in PAR) + "</ul>"
    est = '<ol class="quadro">' + "".join(
        f'<li>{ic(i_)}<span class="t-rotulo">{m}</span><h3 class="step__titulo">{t}</h3>{f"<p>{x}</p>" if x else "<ul class=entregas>" + "".join(f"<li>{e}</li>" for e in ENTREGAS) + "</ul>"}</li>'
        for m, i_, t, x in EST) + "</ol>"
    funil = '<ol class="piramide">' + "".join(
        f'<li style="--i: {i}"><span class="numeral" aria-hidden="true">{i + 1}</span><h3 class="step__titulo">{t}</h3><p>{x}</p><p class="efeito6">{q}</p></li>'
        for i, (_, t, x, q) in enumerate(FUNIL)) + "</ol>"
    trilha = '<ol class="linha">' + "".join(
        f'<li><span class="t-rotulo">{nn(i)}</span><h3>{t}</h3><p class="t-apoio">{x}</p></li>' for i, (_, t, x) in enumerate(TRILHA, 1)) + "</ol>"
    ritos = f'<div class="caixa"><p class="t-rotulo">Os ritos, depois da mudança</p><dl>{"".join(f"<div><dt>{t}</dt><dd>{x}</dd></div>" for _, t, x in RITOS)}</dl></div>'
    return [seq, par, est, funil, trilha, ritos]


DIRECOES = [
    ("Tabela suíça", "Grade modular", D1_CSS, d1,
     "Réguas de tinta e o número em Anton pendurado na primeira coluna. Cada forma é uma tabela tipográfica, e o funil vira um gráfico de barras que&nbsp;encolhe."),
    ("Coluna e margem", "Notas de Tufte", D2_CSS, d2,
     "O adesivo e o número moram na margem, o texto corre na medida de leitura e o efeito vira nota em Fraunces. O meio dos estágios ganha corpo de título, e a trilha vira uma&nbsp;frase."),
    ("Adesivos", "Iconografia na frente", D3_CSS, d3,
     "Cada etapa é um Cartão com o ícone grande sobre o canto e o número vazado. Setas desenhadas ligam os estágios, o funil empilha Cartões que estreitam e os ritos viram folhas de&nbsp;agenda."),
    ("Diagrama", "A forma desenhada", D4_CSS, d4,
     "A forma de cada Passos é desenhada na gramática dos adesivos. A sequência sobe como escada, o funil é um funil de verdade ao lado do texto, a trilha é uma estrada e os ritos fecham um&nbsp;laço."),
    ("Linha do tempo", "Espinha e nós", D5_CSS, d5,
     "Uma espinha de tinta liga as etapas, e cada nó é o ícone num disco. No funil os nós encolhem, nos estágios o nó do meio é o maior, e a trilha corre na&nbsp;horizontal."),
    ("Jornal", "Fios e colunas", D6_CSS, d6,
     "Fios finos, numerais em Fraunces itálico, texto em colunas e o quadro. O funil é uma pirâmide invertida de texto, em que a própria mancha&nbsp;estreita."),
]

COMUM_CSS = """
.estudo-topo { display: grid; gap: var(--space-16); padding-bottom: var(--space-16); }
.estudo-topo .t-sub { max-width: 44ch; }
"""


def pagina(n):
    nome, principio, css, fazer, resumo = DIRECOES[n - 1]
    pecas = fazer()
    topo = f"""
    <header class="estudo-topo">
      <a class="link" data-variant="voltar" href="index.html"><i aria-hidden="true">←</i> Estudo do Passos</a>
      <p class="t-rotulo">Direção {n} · {principio}</p>
      <h1 class="t-display">{nome}</h1>
      <p class="t-sub">{resumo}</p>
    </header>"""
    secoes = [(fic, fnome, ftit, [peca]) for (fic, fnome, ftit), peca in zip(FORMAS, pecas)]
    corpo = g.caso_palco("Nesta direção", secoes, topo)
    html = c.cabeca(P, f"Direção {n}, {nome} · Estudo do Passos", g.ESTILO + COMUM_CSS + css, f"d{n}") + c.cabecalho(P, None, "Pular para o estudo") + corpo + c.rodape(P, None)
    return html


def indice():
    itens = "".join(f"""
      <div class="peca" id="d{n}">
        <h3>{n}. {nome}</h3>
        <p class="t-apoio prosa"><strong>{principio}.</strong> {resumo}</p>
        {g.palco(f"d{n}.html", f"Direção {n}, {nome}", 1440, 900)}
      </div>""" for n, (nome, principio, _, _, resumo) in enumerate(DIRECOES, 1))
    main = f"""
<main id="conteudo" class="container palco-pagina">
  <div>
    <header class="estudo-topo">
      <a class="link" data-variant="voltar" href="../index.html#peca-passos"><i aria-hidden="true">←</i> Vitrine</a>
      <p class="t-rotulo">Estudo · Onda 3</p>
      <h1 class="t-display">Seis jeitos de&nbsp;fazer o&nbsp;Passos</h1>
      <p class="t-sub">O mesmo método das seis variações de página. Mesmo texto, mesmos tokens e ícones, e cada direção parte de um princípio editorial&nbsp;diferente.</p>
    </header>
    <div class="prosa"><p>Cada direção monta as seis formas, sequência, par, estágios, funil, trilha e ritos, numa página com o Sumário, na largura que a peça tem no caso. Troque a largura do quadro, ou abra a direção em página inteira. Dá para escolher uma direção inteira ou misturar formas de direções&nbsp;diferentes.</p></div>
    {itens}
  </div>
</main>"""
    html = c.cabeca(P, "Estudo do Passos · Jeff DS no site", g.ESTILO + COMUM_CSS) + c.cabecalho(P, None, "Pular para o estudo") + main + c.rodape(P, None)
    return html.replace("</body>", '<script src="../vitrine.js"></script>\n</body>')


if __name__ == "__main__":
    SAIDA.mkdir(exist_ok=True)
    for n in range(1, len(DIRECOES) + 1):
        (SAIDA / f"d{n}.html").write_text(pagina(n))
    (SAIDA / "index.html").write_text(indice())
