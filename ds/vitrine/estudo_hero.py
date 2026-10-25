"""Estudo do hero da Home. A frase é a própria cena.

Três momentos parados, antes de qualquer transição, para aprovar a forma de
cada um (ver ds/ROTEIRO-HERO.md).

1. Rascunho. A frase em Anton, em duas linhas e no maior tamanho que cabe,
   ainda em contorno, com a grade, as guias e a hachura de quem desenha.
2. Cores. As cores do Jeff DS entram desenhando a tipografia, sempre como
   fundo atrás das palavras. O texto continua tinta.
3. Ilustrações e ícones. Os adesivos e um pedaço de esboço completam a frase,
   os do ofício na primeira linha e os do jeito de fazer na segunda.

O CSS mora aqui, preso a .eh, e só vai para componentes.css depois da sua
escolha.

Uso: python3 ds/vitrine/estudo_hero.py
Escreve ds/vitrine/estudo/hero/index.html e cena-1.html a cena-3.html. As
imagens de cada cena saem de node ds/vitrine/fotografar.mjs.
"""
from pathlib import Path
import sys

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import gerar as g  # noqa: E402

c = g.c
P = "../../../../"
SAIDA = AQUI / "estudo" / "hero"

CENAS = [
    (1, "Rascunho", "A frase se forma como desenho de tipo. Contorno à mão, a grade, as guias de altura e de base, a hachura no que já está decidido e as notas de quem&nbsp;desenha."),
    (2, "Cores", "As cores do Jeff DS desenham a tipografia por trás. O lime marca o ofício, o azul abraça o mesmo, o verde sublinha o jeito de fazer, e o não fica na tinta. O texto nunca muda de&nbsp;cor."),
    (3, "Ilustrações e ícones", "Os adesivos completam a frase. Na primeira linha os do ofício, que ficam (lápis, lupa, pessoa). Na segunda os do jeito de fazer, que mudam (tela, conversa, celular, camadas), e um pedaço de esboço&nbsp;solto."),
]

ESTILO = """
.eh {
  container-type: inline-size;
  position: relative;
  display: grid;
  align-content: center;
  gap: var(--space-48);
  /* A primeira tela deixa ver o começo da Lista de casos, o rótulo e o
     alto dos primeiros Cartões, para ficar claro que a página continua. */
  min-height: calc(100svh - var(--altura-cabecalho) - 9rem);
  padding-block: var(--space-48);
}
/* A frase do tamanho da coluna. A primeira linha, a mais longa, ocupa
   10,8 vezes o tamanho da fonte em Anton, e 9cqi deixa uma folga. */
.eh__frase {
  position: relative;
  z-index: 1;
  font-family: var(--font-display);
  font-weight: 400;
  font-size: min(9cqi, 8.5rem);
  line-height: var(--leading-display);
  letter-spacing: 0.005em;
  text-transform: uppercase;
}
.eh__linha { position: relative; display: block; width: fit-content; white-space: nowrap; }
.eh__q { position: relative; }
.eh__p { position: relative; display: inline-block; isolation: isolate; }
.eh__apoio { position: relative; z-index: 1; max-width: 34ch; }
.eh__adesivo { position: absolute; z-index: 2; width: max(36px, var(--t, .6em)); height: auto; transform: rotate(var(--g, 0deg)); }
/* Os adesivos do ofício sentam na primeira linha, e os do jeito de
   fazer embaixo da segunda. */
.eh__a--lapis   { --t: .62em; --g: -14deg; left: -.34em; top: -.46em; }
.eh__a--lupa    { --t: .56em; --g: 9deg;   left: 54%;    top: -.52em; }
.eh__a--pessoa  { --t: .6em;  --g: -6deg;  right: -.42em; top: -.5em; }
.eh__a--janela  { --t: .56em; --g: -10deg; left: 50%;    top: 2.3em; }
.eh__a--dialogo { --t: .52em; --g: 8deg;   left: 64%;    top: 2.42em; }
.eh__a--celular { --t: .54em; --g: 12deg;  left: 77%;    top: 2.26em; }
.eh__a--camadas { --t: .5em;  --g: -8deg;  right: -.3em; top: 2.32em; }
.eh__a--esboco  { --t: .86em; --g: 7deg;   right: 3%;    top: 1.08em; }
/* No celular cada frase quebra em três linhas, para a frase ganhar o
   peso que tem no desktop. A linha mais larga, "O MESMO.", ocupa 3,8
   vezes o tamanho da fonte, e 23cqi deixa uma folga. As linhas curtas
   deixam espaço à direita, e os adesivos descem pela tela nesse vão,
   os do ofício nas três primeiras e os do jeito de fazer nas três
   últimas. */
@media (max-width: 719px) {
  .eh { min-height: 0; padding-block: var(--space-48) var(--space-64); }
}
@container (max-width: 599px) {
  .eh__frase { font-size: 23cqi; }
  .eh__linha { width: auto; white-space: normal; }
  .eh__q { display: block; width: fit-content; }
  .eh__linha + .eh__linha { margin-top: .22em; }
  .eh .eh__p--emenda::before { right: -.08em !important; border-right: var(--stroke) solid var(--ink) !important; border-radius: .06em !important; }
  .eh .eh__p--jeito:not(.eh__p--emenda)::before { left: -.08em; border-left: var(--stroke) solid var(--ink) !important; border-radius: .06em; }
  .eh__linha + .eh__linha > .eh__q:last-child { margin-top: .14em; }
  .eh[data-cena="1"] .eh__frase { -webkit-text-stroke: 1.5px var(--ink); margin-top: .5em; }
  .eh[data-cena="1"] .eh__hachura { background-image: repeating-linear-gradient(135deg, var(--ink) 0 1.5px, transparent 1.5px 7px); }
  .eh[data-cena="1"] .eh__linha::before, .eh[data-cena="1"] .eh__linha::after { display: none; }
  .eh[data-cena="1"] .eh__q::before,
  .eh[data-cena="1"] .eh__q::after { content: ""; position: absolute; left: -2cqi; width: 104cqi; border-top: 1.5px dashed rgb(0 0 0 / .45); }
  .eh[data-cena="1"] .eh__q::before { top: .25em; }
  .eh[data-cena="1"] .eh__q::after { top: 1.02em; }
  .eh__nota { font-size: 15px; }
  .eh__nota--topo { right: auto !important; left: 0; top: -1.6em !important; }
  .eh__adesivo { --t: 48px; }
  .eh__a--pessoa  { left: auto;  right: 0;    top: .38em; }
  .eh__a--lapis   { left: auto;  right: 16%;  top: .26em; }
  .eh__a--lupa    { left: auto;  right: 0;    top: 1.52em; }
  .eh__a--janela  { left: auto;  right: 15%;  top: 4.02em; }
  .eh__a--dialogo { left: auto;  right: 0;    top: 4.22em; }
  .eh__a--celular { left: auto;  right: 1%;   top: 5.32em; }
  .eh__a--camadas { left: 2.1em; right: auto; top: 6.58em; }
  .eh__a--esboco  { --t: 76px;   right: 0;    top: 6.2em; }
}
.eh__rotulo { position: absolute; font-family: var(--font-texto); }

/* 1. Rascunho */
.eh[data-cena="1"]::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgb(0 0 0 / .14) 1px, transparent 1px) 0 0 / calc((100% + var(--grade-vao)) / 12) 100%;
  pointer-events: none;
}
.eh[data-cena="1"] .eh__frase { color: transparent; -webkit-text-stroke: 2px var(--ink); filter: url(#tremor); }
.eh[data-cena="1"] .eh__linha::before,
.eh[data-cena="1"] .eh__linha::after {
  content: "";
  position: absolute;
  left: -2cqi;
  width: 104cqi;
  border-top: 1.5px dashed rgb(0 0 0 / .45);
}
.eh[data-cena="1"] .eh__linha::before { top: .25em; }
.eh[data-cena="1"] .eh__linha::after { top: 1.02em; }
.eh__hachura { background: repeating-linear-gradient(135deg, var(--ink) 0 2px, transparent 2px 9px); -webkit-background-clip: text; background-clip: text; }
.eh[data-cena="1"] .eh__p--nao::after {
  content: "";
  position: absolute;
  inset: -.06em -.2em -.02em -.16em;
  border: 3px solid var(--ink);
  border-radius: 50%;
  transform: rotate(-4deg);
}
.eh__nota { position: absolute; font-family: var(--font-flare); font-weight: 300; font-size: max(16px, .2em); line-height: 1.1; letter-spacing: 0; text-transform: none; -webkit-text-stroke: 0; color: var(--ink); white-space: nowrap; }
.eh__esboco-apoio { width: min(100%, 520px); height: auto; }

/* 2 e 3. Cores. O fundo de cada palavra é um adesivo com contorno de
   tinta, atrás do texto. */
.eh[data-cena="2"] .eh__p::before, .eh[data-cena="3"] .eh__p::before {
  content: "";
  position: absolute;
  z-index: -1;
  border: var(--stroke) solid var(--ink);
}
.eh__p--oficio::before { inset: .14em -.1em .08em; background: var(--lime); border-radius: .1em; transform: rotate(-2deg); }
.eh__p--mesmo::before { width: 1.15em; aspect-ratio: 1; right: -.28em; top: -.08em; background: var(--azul); border-radius: 50%; }
.eh__p--jeito::before { left: -.08em; right: -.08em; bottom: .02em; height: .36em; background: var(--verde); border-radius: .06em; transform: skewX(-12deg); }
/* No desktop os dois pedaços de "jeito de fazer," são uma faixa só:
   o primeiro cobre o espaço, e os contornos de dentro somem. */
.eh__p--emenda::before { right: -.4em !important; border-right: 0 !important; border-radius: .06em 0 0 .06em !important; }
.eh__p--jeito:not(.eh__p--emenda)::before { left: 0; border-left: 0 !important; border-radius: 0 .06em .06em 0; }
.eh__p--nao::before { inset: -.12em -.12em .06em; background: var(--ink); border-radius: .1em; transform: rotate(3deg); }
.eh[data-cena="2"] .eh__p--nao, .eh[data-cena="3"] .eh__p--nao { color: var(--paper); }
"""

SVG_TREMOR = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <filter id="tremor"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="3.5"/></filter>
</svg>"""


def ic(nome, acento):
    return f'<img class="eh__adesivo eh__a--{nome}" src="{P}assets/ds/icones/{nome}-{acento}.svg" alt="" width="96" height="96">'


def esboco_solto():
    """Um pedaço do esboço da tela, como folha solta sobre a frase."""
    linha = 'stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"'
    return (f'<svg class="eh__adesivo eh__a--esboco" viewBox="0 0 120 140" fill="none" aria-hidden="true" focusable="false">'
            f'<g {linha}><path d="{c._rabisco(6, 6, 114, 134, 1)}" fill="#f9f9f7"/><path d="{c._rabisco(18, 20, 102, 64, 3)}"/>'
            f'<path d="M22 24l76 36M98 22L20 62"/><path d="{c._linha(18, 82, 96, 2)}"/><path d="{c._linha(18, 96, 74, 5)}"/>'
            f'<path d="{c._pilula(18, 110, 70, 124, 6)}"/></g></svg>')


def frase(cena):
    oficio = 'o&nbsp;<span class="eh__p eh__p--oficio' + (' eh__hachura' if cena == 1 else '') + '">ofício</span>'
    mesmo = '<span class="eh__p eh__p--mesmo">mesmo.</span>'
    # "jeito de fazer," vira dois pedaços, porque no celular ele quebra
    # depois de "jeito". No desktop a faixa do primeiro cobre o espaço e
    # emenda com a do segundo.
    jeito = '<span class="eh__p eh__p--jeito eh__p--emenda">jeito</span>'
    fazer = '<span class="eh__p eh__p--jeito">de&nbsp;fazer,</span>'
    nao = '<span class="eh__p eh__p--nao">não.</span>'
    q = lambda t: f'<span class="eh__q">{t}</span>'
    l1 = f'<span class="eh__linha">{q(oficio)} {q("continua")} {q("o&nbsp;" + mesmo)}</span>'
    l2 = f'<span class="eh__linha">{q("o&nbsp;" + jeito)} {q(fazer)} {q(nao)}</span>'
    extra = ""
    if cena == 1:
        extra = ('<span class="eh__nota eh__nota--topo" aria-hidden="true" style="right: -1cqi; top: -.42em">Anton, o maior da tela</span>'
                 '<span class="eh__nota" aria-hidden="true" style="right: 0; bottom: -.5em">o não fica</span>')
    if cena == 3:
        a = "lime"
        extra = "".join([
            ic("lapis", a),
            ic("lupa", a),
            ic("pessoa", a),
            ic("janela", a),
            ic("dialogo", a),
            ic("celular", a),
            ic("camadas", a),
            esboco_solto(),
        ])
    return f'<h1 class="eh__frase" id="eh-frase">{l1}{l2}{extra}</h1>'


def apoio(cena):
    if cena == 1:
        linha = 'stroke="#000" stroke-width="2.5" stroke-linecap="round"'
        return (f'<svg class="eh__esboco-apoio" viewBox="0 0 520 90" fill="none" aria-hidden="true" focusable="false"><g {linha} filter="url(#tremor)">'
                f'<path d="{c._linha(4, 14, 470, 1)}"/><path d="{c._linha(4, 46, 500, 3)}"/><path d="{c._linha(4, 78, 300, 5)}"/></g></svg>'
                f'<p class="sr">{c.HERO_APOIO}</p>')
    return f'<p class="t-sub eh__apoio">{c.HERO_APOIO}</p>'


def cena(n):
    return f"""<section class="eh" data-cena="{n}" aria-labelledby="eh-frase">
  {frase(n)}
  {apoio(n)}
</section>"""


def pagina(n, nome):
    corpo = f"""{SVG_TREMOR}
<main id="conteudo" class="container">
  {cena(n)}
  {c.lista_casos(P, revelar=False)}
</main>"""
    html = (c.cabeca(P, f"Hero, cena {n}, {nome} · Estudo da vitrine", g.ESTILO + ESTILO)
            + c.cabecalho(P, None, "Pular para o conteúdo") + corpo + c.rodape(P, None))
    return html.replace('data-acento="azul"', 'data-acento="lime"', 1)


def indice():
    itens = "".join(f"""
    <section class="section" aria-labelledby="c{n}">
      <p class="section__rotulo t-rotulo">Cena {n}</p>
      <h2 class="t-titulo" id="c{n}">{nome}</h2>
      <p class="prosa">{texto}</p>
      <div class="figure"><div class="figure__quadro"><img src="cena-{n}-1440.png" alt="A cena {n} do hero em 1440px." width="1440" height="900" loading="lazy"></div></div>
      <div class="figure" data-formato="retrato" style="max-width: 320px"><div class="figure__quadro"><img src="cena-{n}-390.png" alt="A cena {n} do hero em 390px." width="390" height="844" loading="lazy"></div></div>
      <a class="link" data-variant="seguir" href="cena-{n}.html">Abrir a cena {n} ao vivo <i aria-hidden="true">→</i></a>
    </section>""" for n, nome, texto in CENAS)
    corpo = f"""
<main id="conteudo" class="container palco-pagina">
  <div>
    <header class="ficha-pagina__topo">
      <a class="link" data-variant="voltar" href="../../index.html#midia-hero-e-home"><i aria-hidden="true">←</i> Vitrine</a>
      <h1 class="t-display">Estudo do&nbsp;hero</h1>
      <p class="t-sub">A frase é a cena. Três momentos parados, antes das&nbsp;transições.</p>
    </header>{itens}
  </div>
</main>"""
    return c.cabeca(P, "Estudo do hero · Vitrine", g.ESTILO) + c.cabecalho(P, None, "Pular para o estudo") + corpo + c.rodape(P, None)


if __name__ == "__main__":
    SAIDA.mkdir(parents=True, exist_ok=True)
    for n, nome, _ in CENAS:
        (SAIDA / f"cena-{n}.html").write_text(pagina(n, nome))
    (SAIDA / "index.html").write_text(indice())
