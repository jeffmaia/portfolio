"""A página de caso do Omnichat, montada só com os componentes do Jeff DS.

É o modelo de Caso, a variação 4 (sumário e mosaico), idêntico ao que foi
aprovado, com o revelar na entrada a mais. O mesmo miolo serve ao modelo, em ds/prova/variacoes/v4.html, e à página
publicada, case-omnichat.html na raiz.

Uso: python3 ds/prova/caso.py
Escreve case-omnichat.html na raiz do repositório.
"""
from pathlib import Path
import comum as c

RAIZ = Path(__file__).resolve().parents[2]

TITULO = "Redesenhando a verificação de intenção dos agentes conversacionais · Jeff Maia"
DESCRICAO = (
    "A maior perda de conversão não estava na interface. Estava na&nbsp;camada onde a intenção do lead "
    "entra no sistema. A conversão de leads qualificados saiu de 24% para 32% nas origens redesenhadas, "
    "medida em produção ao longo de 8 semanas."
)

# As seções, na ordem do Sumário: id, ícone e nome.
SECOES = [
    ("contexto", "robo", "Contexto"),
    ("problema", "fronteira", "O problema"),
    ("processo", "camadas", "Processo"),
    ("antes-e-depois", "dialogo", "Antes e depois"),
    ("resultado", "grafico", "Resultado"),
]


def sumario(pre):
    itens = "".join(
        f'<li><a class="sumario__item" href="#{i}">{c.icone(pre, ic, 32)}<span class="sumario__num">0{n}</span><span class="sumario__nome">{r}</span></a></li>'
        for n, (i, ic, r) in enumerate(SECOES, 1))
    marcas = '<span class="sumario__seg" aria-hidden="true"></span>' * len(SECOES)
    return f'''<nav class="sumario" data-sumario aria-label="Neste caso">
    <p class="t-rotulo sumario__titulo">Neste caso</p>
    <ol class="sumario__lista" id="sumario-lista">{itens}</ol>
    <button class="sumario__botao" type="button" aria-expanded="false" aria-controls="sumario-lista" hidden><span class="sr">Seções deste caso</span>{marcas}</button>
    <span class="sumario__aviso" aria-hidden="true"></span>
  </nav>'''


def rotulo(n, attrs=""):
    return f'<p class="section__rotulo t-rotulo"{attrs} data-revelar>0{n} · {SECOES[n - 1][2]}</p>'


def valor(v):
    # O til de aproximação é lido como "til". Quem ouve recebe "cerca de".
    if v.startswith("~"):
        return f'<span aria-hidden="true">~</span><span class="sr">cerca de </span>{v[1:]}'
    return v


def revelar(bloco):
    # Põe data-revelar na primeira etiqueta de um bloco pronto do comum.py.
    fim = bloco.index(">")
    return bloco[:fim] + " data-revelar" + bloco[fim:]


def main(pre):
    origens = "".join(
        f'<article class="card" data-tamanho="meio">{c.icone(pre, ic, 48)}<h3>{t}</h3><p class="t-apoio">{x}</p></article>'
        for ic, t, x in c.ORIGENS)
    tamanhos = ["dois-tercos", "terco", "terco", "terco", "terco"]
    camadas = "".join(
        f"""<article class="card" data-tamanho="{tamanhos[i - 1]}"{' data-variant="acento"' if i == 1 else ""}>
  {c.icone(pre, ic, 48)}<span class="t-rotulo">Camada 0{i}</span><h3>{tit}</h3><p class="t-apoio">{txt}</p>
  <p class="card__efeito"><span class="t-rotulo">Efeito</span> {ef}</p>
</article>""" for i, (_, ic, tit, txt, ef) in enumerate(c.CAMADAS, 1))
    stats = "".join(
        f'<div class="card" data-tamanho="meio">{c.icone(pre, ic, 48)}<div class="stat"><span class="stat__valor">{valor(v)}</span><p class="stat__frase">{f}</p></div></div>'
        for ic, v, f in c.STATS)
    return f"""
<main id="conteudo" class="container caso">
  {sumario(pre)}

  <div>
    <header class="topo">
      <div class="topo__texto">{c.badges()}<h1 class="t-display">{c.TITULO}</h1><p class="t-sub">{c.LEAD}</p></div>
      <div class="card topo__ficha" data-variant="muted"><p class="t-rotulo card__titulo">Ficha do projeto</p>{c.ficha()}</div>
      <div class="card topo__salto" data-variant="acento">{c.salto()}{c.ilustracao(pre, "salto")}</div>
    </header>

    <section class="section" id="contexto" aria-labelledby="contexto-rotulo">
      {rotulo(1, ' id="contexto-rotulo"')}
      <p class="t-lead prosa" data-revelar>{c.CONTEXTO}</p>
    </section>

    <section class="section" id="problema" aria-labelledby="problema-titulo">
      {rotulo(2)}
      <h2 class="t-titulo" id="problema-titulo" data-revelar>{c.PROBLEMA_TITULO}</h2>
      <div class="prosa" data-revelar>{"".join(f"<p>{p}</p>" for p in c.PROBLEMA)}</div>
      <div class="cards" data-layout="mosaico" data-revelar>{origens}</div>
    </section>

    <section class="section" id="processo" aria-labelledby="processo-titulo">
      {rotulo(3)}
      <h2 class="t-titulo" id="processo-titulo" data-revelar>{c.CAMADAS_TITULO}</h2>
      <div class="cards" data-layout="mosaico" data-revelar>{camadas}</div>
    </section>

    <section class="section" id="antes-e-depois" aria-labelledby="antes-e-depois-titulo">
      {rotulo(4)}
      <h2 class="t-titulo" id="antes-e-depois-titulo" data-revelar>{c.CONVERSA_TITULO}</h2>
      <p class="t-apoio" data-revelar>{c.CONVERSA_LEGENDA}</p>
      {revelar(c.conversa(pre))}
    </section>

    <section class="section" id="resultado" aria-labelledby="resultado-titulo">
      {rotulo(5)}
      <h2 class="t-titulo" id="resultado-titulo" data-revelar>{c.RESULTADO_TITULO}</h2>
      <div class="prosa" data-revelar>{"".join(f"<p>{p}</p>" for p in c.RESULTADO)}</div>
      <div class="cards" data-layout="mosaico" data-revelar>{stats}</div>
      {revelar(c.callout())}
      {revelar(c.fechamento(pre))}
    </section>
  </div>
</main>"""


def pagina():
    aqui = "case-omnichat.html"
    return c.cabeca("", TITULO, descricao=DESCRICAO) + c.CARGA + c.cabecalho("", aqui) + main("") + c.rodape("", aqui)


if __name__ == "__main__":
    (RAIZ / "case-omnichat.html").write_text(pagina())
    print("ok")
