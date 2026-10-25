"""Estudo das barras do Gráfico. Três direções para o antes e depois.

As barras de hoje põem cada valor num trilho inteiro. O antes do Processo
enche o trilho de trama e parece só marcar o espaço, e o valor fica na
beira direita, longe da ponta da barra que ele mede. O depois pequeno não
conta que o tempo encolheu.

Cada direção monta as mesmas duas figuras, o tempo do Processo com IA (lime)
e os acessos do Mapa de experiência (azul), porque as duas páginas usam a
mesma peça. Uma conta uma queda e a outra um salto.

O CSS de cada direção mora aqui, preso à classe dela (.b1 a .b3). Nada daqui
vai para componentes.css antes de você escolher.

Uso: python3 ds/vitrine/estudo_barras.py
Escreve ds/vitrine/estudo/barras.html e barras-1.html a barras-3.html.
"""
from pathlib import Path
import sys

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import gerar as g  # noqa: E402
import estudo  # noqa: E402

c = g.c
pc = g.pc
P = g.P_SUB
SAIDA = AQUI / "estudo"

# ── Os dados, das páginas ────────────────────────────────────
# Cada grupo: nome, (antes escrito, antes de 0 a 100), (depois escrito,
# depois de 0 a 100), e para as unidades o tamanho de uma, o antes e o
# depois em unidades (mínimo e máximo, porque "1 a 2 meses" é uma faixa).
PROCESSO = ("lime", "Tempo antes e depois", [
    ("Discovery", ("1 a 2 meses", 100), ("~1 semana", 12.5), ("1 semana", (4, 8), (1, 1))),
    ("Refinamento semanal", ("4 a 5 h", 100), ("30 a 40 min", 13), ("10 minutos", (24, 30), (3, 4))),
])
MAPA = ("azul", "Usuários únicos no primeiro mês", [
    ("Sem e com o mapa de experiência", ("20", 2.2), ("890", 100), ("10 usuários", (2, 2), (89, 89))),
])


def secoes(figura):
    """O Resultado do Processo e o Resultado do Mapa, com o texto das páginas."""
    from casos import processo, mapa
    return [
        ("grafico", "Processo", processo.RESULTADO_TITULO, [pc.prosa(*processo.RESULTADO), figura(*PROCESSO)]),
        ("grafico", "Mapa", mapa.RESULTADO_TITULO, [pc.prosa(*mapa.RESULTADO), figura(*MAPA)]),
    ]


def figura_base(acento, titulo, grupos, classe, grupo):
    return f"""<figure class="chart {classe}" data-acento="{acento}" data-revelar>
  <figcaption class="t-rotulo">{titulo}</figcaption>
  <div class="chart__grupos">{"".join(grupo(*x) for x in grupos)}</div>
</figure>"""


# ── 1. Um trilho só ──────────────────────────────────────────
# O antes e o depois no mesmo trilho, como na escala. O antes é a área
# de muted com um fio de tinta na ponta, e o depois o acento por cima.
# Cada valor termina sobre a ponta da sua barra, na ordem das pontas.

CSS1 = """
.b1 .chart__grupos { display: grid; gap: var(--space-48) var(--grade-vao); }
.b1-grupo { display: grid; gap: var(--space-12); min-width: 0;
  --pmin: calc(min(var(--a), var(--d)) * 1%); --pmax: calc(max(var(--a), var(--d)) * 1%); }
.b1-marcos { display: grid; grid-template-columns: minmax(max-content, var(--pmin)) minmax(max-content, calc(var(--pmax) - var(--pmin))) 1fr; }
.b1-marco { grid-row: 1; display: flex; flex-direction: column-reverse; align-items: end; gap: var(--space-4); padding-inline-end: var(--space-4); text-align: end; }
.b1-marco[data-lado="1"] { grid-column: 1; }
.b1-marco[data-lado="2"] { grid-column: 2; }
.b1-num { font-weight: 700; font-size: var(--text-lead); line-height: 1.2; font-variant-numeric: tabular-nums; }
.b1-trilho { position: relative; height: 32px; border: var(--stroke) solid var(--border); border-radius: calc(var(--radius) / 2); background: var(--background); }
.b1-antes, .b1-depois { position: absolute; top: 0; bottom: 0; left: 0; }
.b1-antes { width: calc(var(--a) * 1%); background: var(--muted); }
.b1-depois { width: calc(max(4px, var(--d) * 1%)); background: var(--acento); border-right: var(--stroke) solid var(--border); }
.b1-depois[data-cheio] { border-right: 0; }
.b1-fio { position: absolute; top: -10px; bottom: -10px; left: calc(var(--a) * 1%); width: var(--stroke); background: var(--foreground); transform: translateX(-100%); }
.b1-legenda { display: flex; flex-wrap: wrap; gap: var(--space-8) var(--space-24); font-size: var(--text-apoio); }
.b1-legenda span { display: inline-flex; align-items: center; gap: var(--space-8); }
.b1-legenda i { width: 20px; height: 20px; border: var(--stroke) solid var(--border); border-radius: calc(var(--radius) / 3); }
.b1-legenda i[data-tom="antes"] { background: var(--muted); }
.b1-legenda i[data-tom="depois"] { background: var(--acento); }
.js-mov .b1 .b1-depois { transform: scaleX(0); transform-origin: left; transition: transform var(--dur-lenta) var(--ease-saida) var(--dur-media); }
.js-mov .b1.revelado .b1-depois { transform: none; }
"""


def b1():
    def grupo(nome, antes, depois, _):
        (ta, a), (td, d) = antes, depois
        menor, maior = (("depois", td), ("antes", ta)) if d < a else (("antes", ta), ("depois", td))
        marcos = "".join(
            f'<p class="b1-marco" data-lado="{n}"><span class="b1-num">{pc.valor(t)}</span><span class="t-rotulo">{q.capitalize()}</span></p>'
            for n, (q, t) in enumerate([menor, maior], 1))
        cheio = " data-cheio" if d >= 100 else ""
        return f"""<div class="b1-grupo" style="--a: {a}; --d: {d}">
    <h3 class="chart__nome">{nome}</h3>
    <div class="b1-marcos">{marcos}</div>
    <div class="b1-trilho" aria-hidden="true"><span class="b1-antes"></span><span class="b1-depois"{cheio}></span><span class="b1-fio"></span></div>
  </div>"""
    def figura(acento, titulo, grupos):
        legenda = '<p class="b1-legenda" aria-hidden="true"><span><i data-tom="antes"></i>Antes</span><span><i data-tom="depois"></i>Depois</span></p>'
        return figura_base(acento, titulo, grupos, "b1", grupo).replace("</figure>", f"  {legenda}\n</figure>")
    return secoes(figura)


# ── 2. Barras soltas ─────────────────────────────────────────
# Sem trilho vazio. Cada barra tem o tamanho do próprio valor, e o valor
# vem junto do rótulo, em cima. Na barra menor, um contorno tracejado vai
# até o tamanho da maior: é o que saiu, ou o que faltava. O mesmo
# tracejado das cenas do Inpulse e do Processo.

CSS2 = """
.b2 .chart__grupos { display: grid; gap: var(--space-48) var(--grade-vao); }
.b2-grupo { display: grid; gap: var(--space-16); min-width: 0; }
.b2-linha { display: grid; gap: var(--space-8); }
.b2-cabeca { display: flex; align-items: baseline; gap: var(--space-12); }
.b2-num { font-weight: 700; font-size: var(--text-lead); line-height: 1.2; font-variant-numeric: tabular-nums; }
.b2-barra { position: relative; height: 32px; }
.b2-cheio { position: absolute; top: 0; bottom: 0; left: 0; width: calc(max(6px, var(--v) * 1%)); border: var(--stroke) solid var(--border); border-radius: calc(var(--radius) / 2); }
.b2-linha[data-ponto="antes"] .b2-cheio { background: var(--muted); }
.b2-linha[data-ponto="depois"] .b2-cheio { background: var(--acento); }
.b2-fantasma { position: absolute; top: 0; bottom: 0; left: 0; width: calc(var(--o) * 1%); border: var(--stroke) dashed var(--border); border-radius: calc(var(--radius) / 2); }
.js-mov .b2 .b2-cheio { transform: scaleX(0); transform-origin: left; transition: transform var(--dur-lenta) var(--ease-saida) var(--dur-media); }
.js-mov .b2 .b2-linha + .b2-linha .b2-cheio { transition-delay: calc(var(--dur-media) + var(--dur-rapida)); }
.js-mov .b2.revelado .b2-cheio { transform: none; }
"""


def b2():
    def linha(quando, texto, v, outro):
        fantasma = f'<span class="b2-fantasma" style="--o: {outro}"></span>' if outro > v else ""
        return f"""<div class="b2-linha" data-ponto="{quando}">
      <p class="b2-cabeca"><span class="t-rotulo">{quando.capitalize()}</span><span class="b2-num">{pc.valor(texto)}</span></p>
      <div class="b2-barra" aria-hidden="true" style="--v: {v}">{fantasma}<span class="b2-cheio"></span></div>
    </div>"""
    def grupo(nome, antes, depois, _):
        (ta, a), (td, d) = antes, depois
        return f"""<div class="b2-grupo">
    <h3 class="chart__nome">{nome}</h3>
    {linha("antes", ta, a, d)}
    {linha("depois", td, d, a)}
  </div>"""
    return secoes(lambda *x: figura_base(*x, "b2", grupo))


# ── 3. Unidades ──────────────────────────────────────────────
# O tempo contado em pedaços iguais, como as semanas do calendário da
# cena. Um quadrado por unidade, cheio até o mínimo e em trama até o
# máximo da faixa ("1 a 2 meses" são de 4 a 8 semanas). A legenda diz
# quanto vale um quadrado.

CSS3 = """
.b3 .chart__grupos { display: grid; gap: var(--space-48) var(--grade-vao); }
.b3-grupo { display: grid; gap: var(--space-16); min-width: 0; align-content: start; }
.b3-linha { display: grid; gap: var(--space-8); }
.b3-cabeca { display: flex; align-items: baseline; gap: var(--space-12); }
.b3-num { font-weight: 700; font-size: var(--text-lead); line-height: 1.2; font-variant-numeric: tabular-nums; }
.b3-unidades { display: flex; flex-wrap: wrap; gap: 4px; }
.b3-unidades i { width: 18px; height: 18px; border: var(--stroke) solid var(--border); border-radius: 4px; }
.b3-linha[data-ponto="antes"] i { background: var(--muted); }
.b3-linha[data-ponto="depois"] i { background: var(--acento); }
.b3-unidades i[data-faixa] { background: repeating-linear-gradient(135deg, var(--foreground) 0 1.5px, transparent 1.5px 5px) var(--background) !important; }
.b3-chave { font-size: var(--text-apoio); }
.js-mov .b3 .b3-unidades i { opacity: 0; transition: opacity var(--dur-rapida) var(--ease-saida) calc(var(--dur-media) + var(--i) * 12ms); }
.js-mov .b3.revelado .b3-unidades i { opacity: 1; }
"""


def b3():
    def linha(quando, texto, faixa):
        mn, mx = faixa
        quadros = "".join(f'<i style="--i: {k}"{" data-faixa" if k >= mn else ""}></i>' for k in range(mx))
        return f"""<div class="b3-linha" data-ponto="{quando}">
      <p class="b3-cabeca"><span class="t-rotulo">{quando.capitalize()}</span><span class="b3-num">{pc.valor(texto)}</span></p>
      <div class="b3-unidades" aria-hidden="true">{quadros}</div>
    </div>"""
    def grupo(nome, antes, depois, unid):
        (ta, _), (td, _) = antes, depois
        um, fa, fd = unid
        faixa = " Em trama, o&nbsp;que&nbsp;vai do mínimo ao máximo da&nbsp;faixa." if fa[0] < fa[1] or fd[0] < fd[1] else ""
        return f"""<div class="b3-grupo">
    <h3 class="chart__nome">{nome}</h3>
    {linha("antes", ta, fa)}
    {linha("depois", td, fd)}
    <p class="b3-chave" aria-hidden="true">Cada quadrado é {um}.{faixa}</p>
  </div>"""
    return secoes(lambda *x: figura_base(*x, "b3", grupo))


DIRECOES = [
    ("Um trilho só", "Antes e depois no mesmo lugar", CSS1, b1,
     "O antes e o depois dividem o mesmo trilho, como na escala. O muted é o tamanho do antes, o acento por cima é o depois, e cada valor termina sobre a ponta da sua barra. A queda se vê como o que sobrou de muted, e o salto como o acento passando do fio do&nbsp;antes."),
    ("Barras soltas", "Cada barra do tamanho do valor", CSS2, b2,
     "Sem trilho vazio. Cada barra tem só o próprio tamanho, e o valor vem junto do rótulo, em cima. Na barra menor, o contorno tracejado vai até o tamanho da outra. É o tempo que saiu, ou o acesso que faltava, no mesmo tracejado das&nbsp;cenas."),
    ("Unidades", "O tempo contado em pedaços", CSS3, b3,
     "Um quadrado por semana, ou por dez minutos, como as semanas do calendário da cena. Cheio até o mínimo e em trama até o máximo da faixa, porque &ldquo;1 a 2 meses&rdquo; são de 4 a 8 semanas. Conta bem o tempo, e no Mapa vira uma&nbsp;contagem."),
]


def pagina(n):
    nome, principio, css, fazer, resumo = DIRECOES[n - 1]
    topo = f"""
    <header class="estudo-topo">
      <a class="link" data-variant="voltar" href="barras.html"><i aria-hidden="true">←</i> Estudo das barras</a>
      <p class="t-rotulo">Direção {n} · {principio}</p>
      <h1 class="t-display">{nome}</h1>
      <p class="t-sub">{resumo}</p>
    </header>"""
    corpo = g.caso_palco("Nesta direção", fazer(), topo)
    return (c.cabeca(P, f"Direção {n}, {nome} · Estudo das barras", g.ESTILO + estudo.COMUM_CSS + css)
            + c.cabecalho(P, None, "Pular para o estudo") + corpo + c.rodape(P, None))


def indice():
    itens = "".join(f"""
      <div class="peca" id="b{n}">
        <h3>{n}. {nome}</h3>
        <p class="t-apoio prosa"><strong>{principio}.</strong> {resumo}</p>
        {g.palco(f"barras-{n}.html", f"Direção {n}, {nome}", 1440, 900)}
      </div>""" for n, (nome, principio, _, _, resumo) in enumerate(DIRECOES, 1))
    main = f"""
<main id="conteudo" class="container palco-pagina">
  <div>
    <header class="estudo-topo">
      <a class="link" data-variant="voltar" href="../index.html#peca-grafico"><i aria-hidden="true">←</i> Vitrine</a>
      <p class="t-rotulo">Estudo · Fase 6</p>
      <h1 class="t-display">Três jeitos de&nbsp;fazer as&nbsp;barras</h1>
      <p class="t-sub">O antes e depois do Gráfico, com o tempo do Processo e os acessos do Mapa. Uma figura conta uma queda e a outra um&nbsp;salto.</p>
    </header>
    <div class="prosa"><p>Hoje cada valor ocupa um trilho inteiro. O antes do Processo enche o trilho de trama e parece só marcar o espaço, e o valor fica na beira direita, longe da ponta da barra. Cada direção resolve isso de um jeito. Troque a largura do quadro, ou abra a direção em página&nbsp;inteira.</p></div>
    {itens}
  </div>
</main>"""
    html = c.cabeca(P, "Estudo das barras · Jeff DS no site", g.ESTILO + estudo.COMUM_CSS) + c.cabecalho(P, None, "Pular para o estudo") + main + c.rodape(P, None)
    return html.replace("</body>", '<script src="../vitrine.js"></script>\n</body>')


if __name__ == "__main__":
    SAIDA.mkdir(exist_ok=True)
    for n in range(1, len(DIRECOES) + 1):
        (SAIDA / f"barras-{n}.html").write_text(pagina(n))
    (SAIDA / "barras.html").write_text(indice())
    print("ok")
