"""O HTML das peças que levam conteúdo, para a vitrine e as páginas montarem
a mesma peça pelo mesmo código. Cada função recebe o texto e devolve a peça
pronta. O texto de cada caso mora no módulo do caso, em ds/prova/casos/.

`pre` é o caminho da página até a raiz, e `cor` é o acento dos ícones.
"""
import html
import textwrap

import comum as c


def valor(v):
    # O til de aproximação é lido como "til". Quem ouve recebe "cerca de".
    if v.startswith("~"):
        return f'<span aria-hidden="true">~</span><span class="sr">cerca de </span>{v[1:]}'
    return v


def sinal(n):
    """Um número com sinal, com o menos tipográfico."""
    return f"−{-n}" if n < 0 else f"+{n}"


# ---------------------------------------------------------------- Passos
def passo(pre, icone, titulo, *pars, num=None, marca="", efeito=None, i=None, depois="", cor="azul"):
    """Um Cartão do Passos: o adesivo no canto, o número vazado, o rótulo
    do estágio, o nome, o texto e o efeito."""
    estilo = f' style="--i: {i}"' if i is not None else ""
    n = f'<span class="step__num" aria-hidden="true">{num:02d}</span>' if num else ""
    m = f'<span class="t-rotulo">{marca}</span>' if marca else ""
    ef = f'<p class="step__efeito"><span class="t-rotulo">{efeito[0]}</span> {efeito[1]}</p>' if efeito else ""
    return (f'<li class="step"{estilo}>{c.icone(pre, icone, 64, "icone step__icone", cor)}{n}{m}'
            f'<h3 class="step__titulo">{titulo}</h3>{"".join(f"<p>{x}</p>" for x in pars)}{depois}{ef}</li>')


def sequencia(pre, itens, efeito="Consequência", cor="azul"):
    """O Passos em sequência, numerado, com o efeito de cada etapa.
    `itens` é uma lista de (ícone, título, parágrafos, efeito)."""
    return '<ol class="steps">' + "".join(
        passo(pre, ic, tit, *pars, num=n, efeito=(efeito, ef), cor=cor)
        for n, (ic, tit, pars, ef) in enumerate(itens, 1)) + "</ol>"


def par(pre, itens, cor="azul"):
    """Dois Passos lado a lado, sem ordem. `itens` é (ícone, título, texto)."""
    return '<ul class="steps" data-layout="par">' + "".join(passo(pre, ic, tit, txt, cor=cor) for ic, tit, txt in itens) + "</ul>"


def estagios(pre, itens, cor="azul"):
    """Entrada, camada e saída. `itens` é (ícone, título, texto ou None,
    marca, lista ou None), e a lista vira os itens da saída."""
    def um(ic, tit, txt, marca, lista):
        depois = '<ul class="step__lista">' + "".join(f"<li>{x}</li>" for x in lista) + "</ul>" if lista else ""
        return passo(pre, ic, tit, *([txt] if txt else []), marca=marca, depois=depois, cor=cor)
    return '<ol class="steps" data-layout="estagios">' + "".join(um(*x) for x in itens) + "</ol>"


def funil(pre, fases, icones, efeito="Quem conduz", cor="azul"):
    """As fases que estreitam. `fases` é (nome, texto, quem conduz)."""
    return '<ol class="steps" data-layout="funil">' + "".join(
        passo(pre, icones[i], nome, txt, num=i + 1, efeito=(efeito, quem), i=i, cor=cor)
        for i, (nome, txt, quem) in enumerate(fases)) + "</ol>"


def trilha(pre, itens, cor="azul"):
    """Um caminho numerado na horizontal. `itens` é (ícone, título, texto)."""
    return '<ol class="steps" data-layout="trilha">' + "".join(
        passo(pre, ic, tit, txt, num=n, cor=cor) for n, (ic, tit, txt) in enumerate(itens, 1)) + "</ol>"


def ritos(pre, itens, cor="azul"):
    return '<ul class="steps" data-layout="ritos">' + "".join(rito(pre, *x, cor=cor) for x in itens) + "</ul>"


def rito(pre, icone, nome, texto, cor="azul"):
    return f'<li class="step"><div class="step__topo">{c.icone(pre, icone, 40, "icone step__icone", cor)}<h3 class="step__titulo">{nome}</h3></div><p>{texto}</p></li>'


# ---------------------------------------------------------------- Gráfico
def barras(titulo, grupos):
    """O antes e o depois no mesmo trilho. `grupos` é uma lista de
    (nome ou None, antes, depois), e cada momento é (rótulo, valor
    escrito, valor de 0 a 100). A chave usa os rótulos do primeiro."""
    def marco(quando, rotulo, escrito):
        return f'<div class="chart__marco" data-ponto="{quando}"><dt class="t-rotulo">{rotulo}</dt><dd class="chart__valor">{valor(escrito)}</dd></div>'
    def grupo(nome, antes, depois):
        cab = f'<h3 class="chart__nome">{nome}</h3>' if nome else ""
        queda = ' data-sentido="queda"' if depois[2] < antes[2] else ""
        return (f'<div class="chart__grupo"{queda} style="--antes: {antes[2]}; --depois: {depois[2]}">{cab}'
                f'<dl class="chart__marcos">{marco("antes", *antes[:2])}{marco("depois", *depois[:2])}</dl>'
                '<div class="chart__barra" aria-hidden="true"><div class="chart__trilho"><span class="chart__antes"></span><span class="chart__preenche"></span></div></div></div>')
    _, (ra, _, _), (rd, _, _) = grupos[0]
    return f"""<figure class="chart" data-variant="barras" data-revelar>
  <figcaption class="t-rotulo">{titulo}</figcaption>
  <div class="chart__grupos">{"".join(grupo(*g) for g in grupos)}</div>
  <p class="chart__chave" aria-hidden="true"><span><span class="chart__amostra" data-tom="muted"></span>{ra}</span><span><span class="chart__amostra" data-tom="cheio"></span>{rd}</span></p>
</figure>"""


def escala(titulo, antes, depois):
    """Antes e depois numa escala de −100 a +100. Numa queda o depois
    fica à esquerda, e os valores trocam de lado com os pontos."""
    queda = ' data-sentido="queda"' if depois < antes else ""
    return f"""<figure class="chart" data-variant="escala"{queda} style="--antes: {antes}; --depois: {depois}" data-revelar>
  <figcaption class="t-rotulo">{titulo}<span class="sr">, numa escala de −100 a +100</span></figcaption>
  <div class="chart__escala">
    <p class="chart__marco" data-ponto="antes"><span class="chart__numero">{sinal(antes)}</span><span class="t-rotulo">Antes</span></p>
    <p class="chart__marco" data-ponto="depois"><span class="chart__numero">{sinal(depois)}</span><span class="t-rotulo">Depois</span></p>
    <div class="chart__eixo" aria-hidden="true"><span class="chart__percurso"></span><span class="chart__zero"></span><span class="chart__ponto" data-ponto="antes"></span><span class="chart__ponto" data-ponto="depois"></span></div>
    <p class="chart__regua t-rotulo" aria-hidden="true"><span>−100</span><span>0</span><span>+100</span></p>
  </div>
</figure>"""


def pilhas(titulo, niveis, reacoes):
    """A proporção de respostas em cada grupo, com a legenda antes.
    `niveis` é (tom, nome, singular, plural, o que quer dizer), e
    `reacoes` é (grupo, contagem de cada nível, na ordem dos níveis)."""
    legenda = "".join(
        f'<div><dt><span class="chart__amostra" data-tom="{tom}" aria-hidden="true"></span>{nome}</dt><dd>{desc}</dd></div>'
        for tom, nome, _, _, desc in niveis)
    def pilha(nome, contas):
        partes = "".join(f'<span class="chart__parte" data-tom="{niveis[i][0]}" style="--n: {n}"></span>' for i, n in enumerate(contas) if n)
        conta = " · ".join(f"{n} {niveis[i][2] if n == 1 else niveis[i][3]}" for i, n in enumerate(contas) if n)
        return f'<li class="chart__pilha"><p class="chart__nome">{nome}</p><div class="chart__trilho" aria-hidden="true">{partes}</div><p class="chart__conta">{conta}</p></li>'
    return f"""<figure class="chart" data-variant="pilhas" data-revelar>
  <figcaption class="t-rotulo">{titulo}</figcaption>
  <dl class="chart__legenda">{legenda}</dl>
  <ol class="chart__pilhas">{"".join(pilha(*x) for x in reacoes)}</ol>
</figure>"""


# ---------------------------------------------------------------- Antes e depois
def citacao(pre, antes, depois, cor="azul"):
    """A fala de quem usou, antes e depois. Cada lado é (fala, autoria)."""
    def lado(variante, ic, quando, fala, autoria):
        return f"""<div class="card compare__lado" data-variant="{variante}">
    <p class="compare__cabeca"><span class="badge">{c.icone(pre, ic, 20, "icone-inline", cor)}{quando}</span></p>
    <figure class="compare__citacao">
      <blockquote><p>{fala}</p></blockquote>
      <figcaption>{autoria}</figcaption>
    </figure>
  </div>"""
    return f"""<div class="compare" data-variant="citacao">
  {lado("muted", "xis", "Antes", *antes)}
  {lado("acento", "check", "Depois", *depois)}
</div>"""


def confronto(dimensoes, legenda):
    """A tabela do antes e depois. `dimensoes` é (dimensão, antes, depois)."""
    linhas = "".join(f"""
    <tr role="row">
      <th role="rowheader" scope="row">{d}</th>
      <td role="cell"><span class="t-rotulo compare__marca" aria-hidden="true">Antes</span>{a}</td>
      <td role="cell"><span class="t-rotulo compare__marca" aria-hidden="true">Depois</span>{b}</td>
    </tr>""" for d, a, b in dimensoes)
    return f"""<table class="compare" data-variant="confronto" role="table">
  <caption class="sr">{legenda}</caption>
  <thead>
    <tr role="row">
      <th role="columnheader" scope="col"><span class="t-rotulo">Dimensão</span></th>
      <th role="columnheader" scope="col"><span class="badge">Antes</span></th>
      <th role="columnheader" scope="col"><span class="badge">Depois</span></th>
    </tr>
  </thead>
  <tbody>{linhas}
  </tbody>
</table>"""


# ---------------------------------------------------------------- Abas
def abas(pre, itens, prefixo, nome, cor="azul"):
    """Abas verticais, numeradas, com o ícone. `itens` é (id, ícone, nome,
    a frase em negrito, o texto)."""
    lista, paineis = [], []
    for i, (cid, ic, tit, sub, txt) in enumerate(itens, 1):
        lista.append(f'<button class="tab" type="button" role="tab" id="{prefixo}-{cid}" aria-controls="{prefixo}-painel-{cid}">{c.icone(pre, ic, 32, "icone-inline", cor)}<span class="t-rotulo">0{i}</span>{tit}</button>')
        paineis.append(f"""<div class="tabs__painel" id="{prefixo}-painel-{cid}" tabindex="0">
  <h3 class="tabs__painel-titulo">{c.icone(pre, ic, 32, "icone-inline", cor)}<span class="t-rotulo">0{i}</span>{tit}</h3>
  <p><strong>{sub}</strong> {txt}</p>
</div>""")
    return f"""<div class="tabs" data-tabs>
  <div class="tabs__lista" aria-label="{nome}" aria-orientation="vertical">{"".join(lista)}</div>
  <div class="tabs__paineis">{"".join(paineis)}</div>
</div>"""


# ---------------------------------------------------------------- Imagem
def tela(id_, alt, larg=4320, alt_=3072):
    return f'<img src="https://framerusercontent.com/images/{id_}.png" alt="{alt}" width="{larg}" height="{alt_}" loading="lazy" decoding="async">'


def externo(link):
    return f'<a class="link" data-variant="externo" href="{link[0]}" target="_blank" rel="noopener">{link[1]} <i aria-hidden="true">↗</i></a>'


def prototipo(embed, titulo):
    return f'<iframe src="{embed}" title="{titulo}" allowfullscreen loading="lazy"></iframe>'


def moldura(quadro, legenda=None, retrato=False, link=None, zoom=None):
    """Uma tela ou um protótipo pousado no papel. `quadro` é o `img` ou o
    `iframe`, e `link` é (destino, texto) do Link que abre o todo. Com
    `zoom` a moldura fica em 16:9 e a imagem cresce por dentro, centrada,
    até o fundo em volta sair do quadro."""
    formato = ' data-formato="retrato"' if retrato else ""
    if zoom:
        formato += f' data-recorte style="--zoom: {zoom}"'
    leg = f'\n  <figcaption class="figure__legenda">{legenda}</figcaption>' if legenda else ""
    fora = f"\n{externo(link)}" if link else ""
    return f"""<figure class="figure" data-variant="moldura"{formato} data-revelar>
  <div class="figure__quadro">{quadro}</div>{leg}
</figure>{fora}"""


def ao_lado(texto, peca):
    """O texto à esquerda e a tela de celular à direita, com o Link dela
    embaixo. A peça entra sem revelar próprio, porque o bloco já tem."""
    peca = peca.replace(" data-revelar", "", 1)
    return '<div class="figure-ao-lado">\n' + textwrap.indent(texto + "\n" + peca, "  ") + "\n</div>"


def galeria(telas, link=None):
    """As telas na ordem do percurso, a primeira na linha inteira.
    `telas` é uma lista de (id no Framer, alt, legenda), e `link` é
    (destino, texto) do Link que abre o todo."""
    itens = "".join(
        f'<li><figure><div class="figure__quadro">{tela(id_, alt)}</div><figcaption class="figure__legenda"><span class="t-rotulo">Fig. 0{n}</span>{leg}</figcaption></figure></li>'
        for n, (id_, alt, leg) in enumerate(telas, 1))
    fora = f"\n{externo(link)}" if link else ""
    return f"""<div class="figure" data-variant="galeria" data-abertura data-revelar>
  <ol class="figure__lista">{itens}</ol>
</div>{fora}"""


# ---------------------------------------------------------------- Arquivo
def arquivo(nome, texto, selo=None, componente=None, legenda=None):
    """Um arquivo de texto como ele é, com o nome na barra e, em cima, o
    `img` do componente que ele descreve. `texto` é o Markdown cru, e as
    linhas de título saem em negrito. `selo` é a Etiqueta da barra."""
    def linha(l):
        l = html.escape(l, quote=False)
        return f"<b>{l}</b>" if l.startswith("#") else l
    corpo = "\n".join(linha(l) for l in textwrap.dedent(texto).strip("\n").split("\n"))
    sel = f'<span class="badge">{selo}</span>' if selo else ""
    comp = f'<div class="arquivo__componente">{componente}</div>' if componente else ""
    leg = f'\n  <figcaption class="figure__legenda">{legenda}</figcaption>' if legenda else ""
    return f"""<figure class="arquivo" data-revelar>
  <div class="arquivo__corpo">{comp}<div class="arquivo__doc"><p class="arquivo__barra"><span class="arquivo__nome">{nome}</span>{sel}</p><pre class="arquivo__texto">{corpo}</pre></div></div>{leg}
</figure>"""


# ---------------------------------------------------------------- Seção
def prosa(*pars):
    return f'<div class="prosa">{"".join(f"<p>{p}</p>" for p in pars)}</div>'


def revelar(bloco):
    """Põe data-revelar em cada bloco de primeiro nível que ainda não tem.
    Um bloco pode ser uma peça seguida do Link dela."""
    def um(b):
        fim = b.index(">")
        return b if "data-revelar" in b[:fim] else b[:fim] + " data-revelar" + b[fim:]
    return "\n".join(um(b) for b in _blocos(bloco))


def _blocos(html):
    # Divide nos começos de linha que abrem um elemento de primeiro nível.
    partes, atual = [], []
    for linha in html.split("\n"):
        if atual and linha.startswith("<") and not linha.startswith("</"):
            partes.append("\n".join(atual))
            atual = []
        atual.append(linha)
    partes.append("\n".join(atual))
    return partes


def rotulo(secoes, n, attrs=""):
    return f'<p class="section__rotulo t-rotulo"{attrs} data-revelar>0{n} · {secoes[n - 1][2]}</p>'


def secao(secoes, n, *partes, titulo=None):
    """Uma Seção do caso: o rótulo numerado, o título e as partes, cada uma
    com o revelar. Sem título (o Contexto) ela é rotulada pelo rótulo."""
    id_ = secoes[n - 1][0]
    if titulo:
        cab = f'{rotulo(secoes, n)}\n      <h2 class="t-titulo" id="{id_}-titulo" data-revelar>{titulo}</h2>'
        rot = f"{id_}-titulo"
    else:
        cab = rotulo(secoes, n, f' id="{id_}-rotulo"')
        rot = f"{id_}-rotulo"
    corpo = "".join(f"\n      {revelar(p)}" for p in partes)
    return f"""<section class="section" id="{id_}" aria-labelledby="{rot}">
      {cab}{corpo}
    </section>"""


def dados(pre, itens, tamanho="meio", cor="azul"):
    """O Dado em grupo, um Cartão por número. `itens` é (ícone, valor, frase)."""
    cards = "".join(
        f'<div class="card" data-tamanho="{tamanho}">{c.icone(pre, ic, 48, cor=cor)}<div class="stat"><span class="stat__valor">{valor(v)}</span><p class="stat__frase">{f}</p></div></div>'
        for ic, v, f in itens)
    return f'<div class="cards" data-layout="mosaico">{cards}</div>'


def nota(rotulo_, texto):
    return f"""<div class="callout" data-variant="nota">
  <p class="t-rotulo callout__rotulo">{rotulo_}</p>
  <p>{texto}</p>
</div>"""


def atrito(pre, titulo, pars, cor="azul"):
    """O Destaque do que deu errado, no muted com o ícone de alerta."""
    return f"""<div class="callout" data-variant="atrito">
  {c.icone(pre, "alerta", 48, cor=cor)}
  <h3>{titulo}</h3>
  {prosa(*pars)}
</div>"""


def frase(texto, legenda):
    """O Destaque com a frase no papel, a virada da Seção."""
    return f"""<div class="callout">
  <p class="callout__frase">{texto}</p>
  <p class="callout__legenda">{legenda}</p>
</div>"""


def etiquetas(lista, nome):
    """Etiquetas no papel, em lista. O `nome` diz ao leitor de tela o que
    a lista é, e o texto antes dela diz o mesmo a quem vê."""
    return (f'<ul class="badges" role="list" aria-label="{nome}">'
            + "".join(f'<li><span class="badge">{b}</span></li>' for b in lista) + "</ul>")
