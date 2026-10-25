"""O caso do Omnichat. O texto mora em ds/prova/comum.py, porque as
variações e a vitrine também usam, e o miolo é o do modelo de Caso, a
variação 4, idêntico ao aprovado."""
import comum as c
import pecas as p

ARQUIVO = "case-omnichat.html"
ACENTO = "azul"
TITULO_PAGINA = "Verificação de intenção dos agentes conversacionais · Jeff Maia"
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

BADGES = c.BADGES
TITULO = c.TITULO
LEAD = c.LEAD
FICHA = c.FICHA
SALTO = ("24%", "32%", c.SALTO_FRASE)
CENA = "omnichat"


def rotulo(n, attrs=""):
    return p.rotulo(SECOES, n, attrs)


def revelar(bloco):
    # Põe data-revelar na primeira etiqueta de um bloco pronto do comum.py.
    fim = bloco.index(">")
    return bloco[:fim] + " data-revelar" + bloco[fim:]


def corpo(pre):
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
        f'<div class="card" data-tamanho="meio">{c.icone(pre, ic, 48)}<div class="stat"><span class="stat__valor">{p.valor(v)}</span><p class="stat__frase">{f}</p></div></div>'
        for ic, v, f in c.STATS)
    return f"""<section class="section" id="contexto" aria-labelledby="contexto-rotulo">
      {rotulo(1, ' id="contexto-rotulo"')}
      <p class="t-lead prosa" data-revelar>{c.CONTEXTO}</p>
    </section>

    <section class="section" id="problema" aria-labelledby="problema-titulo">
      {rotulo(2)}
      <h2 class="t-titulo" id="problema-titulo" data-revelar>{c.PROBLEMA_TITULO}</h2>
      <div class="prosa" data-revelar>{"".join(f"<p>{x}</p>" for x in c.PROBLEMA)}</div>
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
      <div class="prosa" data-revelar>{"".join(f"<p>{x}</p>" for x in c.RESULTADO)}</div>
      <div class="cards" data-layout="mosaico" data-revelar>{stats}</div>
      {revelar(c.callout())}
      {revelar(c.fechamento(pre))}
    </section>"""
