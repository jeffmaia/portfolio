"""A vitrine do Jeff DS no site. Cada onda da Fase 5 acrescenta as suas
peças, e as ondas que ainda não chegaram aparecem só com o que vão trazer.

Na vitrine cada peça aparece sozinha, numa amostra com todas as formas
dela, cada uma com o nome. A amostra é um quadro com uma página de verdade
que se vê em 390, 768 e 1440px e se testa com mouse, toque e teclado.

A ficha abre como página, convertida do Markdown de ds/fichas/. Em cima
dela vem o palco, a peça aplicada numa página com o texto real e outras
peças em volta, com a lista do que testar.

A vitrine é montada com a mesma casca das provas (ds/prova/comum.py), então
o Cabeçalho, o Sumário e o Rodapé dela também são as peças da Onda 1.

Uso: python3 ds/vitrine/gerar.py
Escreve ds/vitrine/index.html, ds/vitrine/amostra/, ds/vitrine/palco/ e
ds/vitrine/fichas/.
"""
from pathlib import Path
import html
import re
import sys

AQUI = Path(__file__).resolve().parent
FICHAS = AQUI.parent / "fichas"
sys.path.insert(0, str(AQUI.parent / "prova"))
import comum as c  # noqa: E402
import caso  # noqa: E402

P = "../../"
P_SUB = "../../../"

# As ondas, na ordem do Sumário: id, ícone, nome e o que trazem.
ONDAS = [
    ("casca", "janela", "Casca", ""),
    ("acao-e-texto", "lapis", "Ação e texto", ""),
    ("sequencia-e-comparacao", "rota", "Sequência", ""),
    ("dados", "grafico", "Dados", "Gráfico em <code>barras</code>, <code>pilhas</code> e <code>escala</code>."),
    ("midia-hero-e-home", "olho", "Mídia, hero e Home", "Imagem em <code>moldura</code>, <code>galeria</code> e <code>sangria</code>, o hero com o esboço que sobra e o Cartão da Lista de&nbsp;casos."),
]

# As peças da Onda 1: arquivo da ficha, nome, largura com que o palco abre
# quando cabe, e o que testar nele.
CASCA = [
    ("cabecalho", "Cabeçalho", 1440, [
        "Com mouse, passe sobre a marca, o botão Menu e os itens do menu aberto. O acento corre só atrás das&nbsp;palavras.",
        "Abra o menu. O painel desce, os itens chegam um a um e a página escurece. Fechar é mais rápido do que&nbsp;abrir.",
        "Pelo teclado, abra o menu e siga com Tab até depois do último link. O menu fecha sozinho. Esc também fecha e devolve o foco ao&nbsp;botão.",
        "Em 390, a marca fica só com Jeff Maia. O item Omnichat aparece como a página&nbsp;atual.",
    ]),
    ("sumario", "Sumário", 1440, [
        "Em 1440, role a página. A coluna fica fixa e a Seção da vez ganha a marca no acento e o ícone&nbsp;gira.",
        "Em 390 ou 768, role. O nome da Seção aparece ao lado das marcas na borda direita e some quando a rolagem&nbsp;para.",
        "Toque nas marcas. A lista entra de lado, e escolher uma Seção rola até ela e fecha a&nbsp;lista.",
        "Pelo teclado, abra o trilho. O foco vai para o primeiro item, e sair do Sumário com Tab fecha a&nbsp;lista.",
        "Role até o fim. Perto do Rodapé o trilho sai de&nbsp;cena.",
    ]),
    ("rodape", "Rodapé", 768, [
        "Role até o fim do palco. O Rodapé é a parada de tinta, com o foco e as bordas em&nbsp;papel.",
        "Com mouse, o Botão inverte e os Links ganham o acento atrás das&nbsp;palavras.",
        "Na lista de páginas, Omnichat é a atual, sem sublinhado e em&nbsp;negrito.",
        "Voltar ao topo rola até o começo do&nbsp;palco.",
    ]),
]

# Peças com um estudo de direções aberto, em ds/vitrine/estudo/.
ESTUDOS = {"passos": '\n        <a class="link" data-variant="seguir" href="estudo/index.html">Ver o estudo do Passos, seis direções <i aria-hidden="true">→</i></a>',
           "hero": '\n        <a class="link" data-variant="seguir" href="estudo/hero/index.html">Ver o estudo do hero, a frase em três momentos <i aria-hidden="true">→</i></a>'}

# A contração certa para "a ficha do Link" e "a ficha da Etiqueta".
DO = {"etiqueta": "da", "imagem": "da"}

# As peças da Onda 2.
ACAO = [
    ("link", "Link", 768, [
        "No fechamento, o link no meio da frase quebra junto com o texto. É a única exceção aos 44px, porque o alvo é a linha da&nbsp;frase.",
        "Com mouse, o acento corre atrás das palavras e a seta anda na direção do link. Para trás no Voltar, para a frente no Seguir, na diagonal no Externo e para cima no&nbsp;Topo.",
        "Em 390 ou 768, toque e segure. O acento aparece no toque, e os links com seta têm 44px de&nbsp;altura.",
        "Pelo teclado, o anel de foco aparece sem o acento por&nbsp;trás.",
        "No Rodapé, os mesmos links na tinta, com sublinhado e foco em&nbsp;papel.",
    ]),
    ("etiqueta", "Etiqueta", 1440, [
        "No Topo, três Etiquetas de assunto, e só a última no&nbsp;acento.",
        "No Antes e depois, o nome do lado com o ícone e o estado na&nbsp;tinta.",
        "No Destaque, a Etiqueta do acento sobre a tinta, sem&nbsp;contorno.",
        "Com leitor de tela, as Etiquetas do Topo são lidas uma a uma, como itens de uma&nbsp;lista.",
        "Nenhuma Etiqueta reage a mouse, toque ou foco. Ela nomeia, não&nbsp;age.",
    ]),
    ("destaque", "Destaque", 1440, [
        "Role o palco. São quatro Seções, cada uma com um Destaque só, e cada uma abre com&nbsp;texto.",
        "A nota tem o rótulo em cima no celular e ao lado do texto a partir de&nbsp;768.",
        "O atrito fica no fundo muted com o alerta. A partir de 768 o ícone vai para a margem&nbsp;esquerda.",
        "A frase no papel fica na margem do texto, sem caixa. A frase na tinta é a única parada escura antes do&nbsp;Rodapé.",
        "Os textos vêm do Inpulse, do Processo com IA e do&nbsp;Omnichat.",
    ]),
]

# As peças da Onda 3.
SEQUENCIA = [
    ("passos", "Passos", 1440, [
        "Role o palco. Cada Seção usa uma forma, com o texto do Processo com&nbsp;IA.",
        "Troque a largura. Três Cartões lado a lado só quando a Seção tem 900px. Em 768 e em 1280, onde o Sumário ocupa a coluna da esquerda, eles descem um embaixo do&nbsp;outro.",
        "Nos estágios, o do meio fica no acento e as setas apontam para o lado em fila e para baixo em coluna. As cinco entregas da saída se abrem nas Abas logo&nbsp;depois.",
        "No funil, cada Cartão é um pouco mais estreito que o anterior. Na trilha, o fio tracejado liga os&nbsp;adesivos.",
        "Nenhuma forma tem movimento próprio. Entram com o revelar da&nbsp;página.",
    ]),
    ("antes-e-depois", "Antes e depois", 1440, [
        "Role o palco. A citação do Inpulse, a conversa do Omnichat e o confronto do Processo, cada um na sua&nbsp;Seção.",
        "Na citação, a fala vem em Fraunces, e a autoria embaixo, sem&nbsp;nome.",
        "No confronto, a coluna do depois é a faixa do acento. Em 390 cada linha vira um bloco, com Antes e Depois escritos em cada&nbsp;célula.",
        "Com leitor de tela, o confronto é lido como tabela, com a dimensão e a coluna de cada&nbsp;célula.",
    ]),
]

# As peças da Onda 4.
DADOS = [
    ("grafico", "Gráfico", 1440, [
        "Role o palco. Cada Seção usa uma forma, com o texto do Inpulse, do Mapa de experiência e do Processo com&nbsp;IA.",
        "Quando o Gráfico entra na tela, o bloco sobe e logo depois o preenchimento corre da esquerda. Na escala, o percurso vai do antes ao depois, e só então aparece o ponto de&nbsp;depois.",
        "Nas barras, o antes é trama e o depois é o acento. Nas pilhas, entusiasta é o acento, receptivo é trama e indiferente é o papel. Nada depende só da&nbsp;cor.",
        "Troque a largura. Com menos de 600px de Seção o nome de cada pilha fica em cima da faixa, e os dois pares de barras ficam um embaixo do&nbsp;outro.",
        "Com leitor de tela, cada Gráfico é uma figura com título, e os valores são lidos como texto. As faixas ficam&nbsp;escondidas.",
        "Nenhuma forma reage a mouse, toque ou foco. O Gráfico mostra, não&nbsp;age.",
    ]),
]

# As peças da Onda 5.
MIDIA = [
    ("imagem", "Imagem", 1440, [
        "Role o palco. A moldura do protótipo do Inpulse, a galeria do Mapa de experiência e a sangria do resultado do Inpulse, cada uma na sua&nbsp;Seção.",
        "Na moldura, o protótipo se navega ali mesmo. Em retrato ele para de crescer em 400px, e o Link logo abaixo abre o protótipo em tela&nbsp;cheia.",
        "Na galeria, a primeira tela ocupa a linha inteira e as outras quatro vão duas a duas quando a Seção tem 600px. Abaixo disso, uma debaixo da&nbsp;outra.",
        "Na sangria, a faixa vai até a beira da tela. Em 1440 ela sangra só para a direita, porque a coluna da esquerda é do Sumário. Nenhuma largura abre rolagem para o&nbsp;lado.",
        "Nenhuma forma reage a mouse, toque ou foco. Entram com o revelar da&nbsp;página.",
    ]),
    ("hero", "Hero da Home", 1440, [
        "Abra a página e não role. Em uns 3s a frase vai do rascunho à página pronta. A grade e o contorno à mão com as guias, a hachura no ofício, as notas e o não circulado. Depois a tinta, as cores atrás das palavras e por fim os&nbsp;adesivos.",
        "A sequência roda uma vez só e para no fim. Para rever, recarregue a&nbsp;página.",
        "Role devagar. A primeira linha quase não se move, a segunda sobe um pouco mais, e os adesivos mais que a frase. Nada gira nem muda de&nbsp;cor.",
        "Em 390 a frase quebra em seis linhas e os adesivos descem pelo vão da direita. Do tablet para cima são duas linhas, e no desktop o começo da Lista de casos aparece embaixo da&nbsp;frase.",
        "Sem JS ou com movimento reduzido, a página chega pronta, como no segundo hero da&nbsp;amostra.",
    ]),
    ("cartao-de-caso", "Cartão de caso", 1440, [
        "Role até os casos. São quatro, na ordem da fila, e cada Cartão leva o acento do próprio caso só na base, com o&nbsp;número.",
        "Em 390 um debaixo do outro, e dois por linha a partir de 768. As bases ficam no pé do Cartão, e o que sobra de altura fica no&nbsp;papel.",
        "Com mouse, o Link Ver o caso ganha a marca em papel, porque o acento sobre o acento não se veria. No toque ele tem&nbsp;44px.",
        "Com leitor de tela, cada Cartão é um artigo com o título do caso, e o Link diz qual caso&nbsp;abre.",
        "O Cartão não é alvo. Só o Link leva para a página do&nbsp;caso.",
    ]),
]

# Peças que ainda não têm ficha, porque a ficha só se escreve depois que a
# interface é aprovada: o nome shadcn e a frase que a ficha vai abrir.
SEM_FICHA = {}

# Peça da vitrine que mora na ficha de outro componente: o Cartão de caso é
# uma variante do Cartão, e a ficha do Cartão mostra o palco dele.
FICHA_DE = {"cartao-de-caso": ("cartao", "Cartão")}
PALCO_DE = {v[0]: k for k, v in FICHA_DE.items()}

ESTILO = """
.peca { display: grid; gap: var(--space-16); padding-top: var(--space-32); }
.peca + .peca { margin-top: var(--space-32); border-top: var(--stroke) solid var(--border); }
.peca > h3 { font-size: var(--text-lead); line-height: 1.3; }
.palco { display: grid; gap: var(--space-12); }
.palco__barra { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--space-8) var(--space-16); }
.palco__larguras { display: flex; gap: var(--space-8); }
html:not(.js) .palco__larguras { display: none; }
.palco__janela {
  height: 640px;
  overflow: hidden;
  border: var(--stroke) solid var(--border);
  border-radius: var(--radius);
  background: var(--background);
  transition: width var(--dur-media) var(--ease-troca), height var(--dur-media) var(--ease-troca);
}
.palco__janela iframe {
  display: block;
  width: 100%;
  height: 100%;
  border: 0;
  transform-origin: 0 0;
  transition: transform var(--dur-media) var(--ease-troca);
}
.amostra { display: grid; gap: var(--space-48); padding-block: var(--space-32) var(--space-48); }
.amostra__item { display: grid; gap: var(--space-16); container-type: inline-size; }
.amostra__nome { display: flex; flex-wrap: wrap; align-items: baseline; gap: var(--space-8) var(--space-12); }
.amostra__tinta { display: grid; gap: var(--space-24); padding: var(--space-32); border-radius: var(--radius); }
.amostra__fileira { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-16) var(--space-32); }
.amostra__rolar { min-height: 60vh; }
.amostra__vazio { display: grid; place-items: center; min-height: 360px; border-radius: var(--radius); background: var(--muted); color: var(--ink); font-size: var(--text-apoio); }
.ficha-pagina__palco { display: grid; gap: var(--space-16); }
.ficha-pagina__palco > h2 { font-size: var(--text-lead); font-weight: 700; line-height: 1.3; }
.testar { display: grid; gap: var(--space-8); padding-left: 1.2em; list-style: disc; font-size: var(--text-apoio); max-width: var(--leitura); }

.palco-pagina { padding-block: var(--space-32) var(--space-secao); }
.palco-pagina > div { display: grid; gap: var(--space-32); }
.links-soltos { display: flex; flex-wrap: wrap; gap: var(--space-8) var(--space-24); }
.ficha-pagina { display: grid; gap: var(--space-32); padding-block: var(--space-32) var(--space-secao); }
.ficha-pagina__topo { display: grid; gap: var(--space-16); justify-items: start; }
.ficha-pagina__topo .t-sub { max-width: 40ch; }
.doc { display: grid; gap: var(--space-16); max-width: 820px; }
.doc h2 { font-size: var(--text-lead); font-weight: 700; line-height: 1.3; margin-top: var(--space-24); }
.doc ul, .doc ol { display: grid; gap: var(--space-8); padding-left: 1.4em; }
.doc ul { list-style: disc; }
.doc ol { list-style: decimal; }
.doc .tabela { overflow-x: auto; border: var(--stroke) solid var(--border); border-radius: var(--radius); }
.doc table { width: 100%; border-collapse: collapse; font-size: var(--text-apoio); }
.doc th, .doc td { padding: var(--space-8) var(--space-12); border-bottom: 1px solid var(--border); text-align: left; vertical-align: top; }
.doc tr:last-child td { border-bottom: 0; }
.doc th { background: var(--muted); font-size: var(--text-rotulo); letter-spacing: var(--tracking-rotulo); text-transform: uppercase; }
.doc pre { overflow-x: auto; padding: var(--space-16); border: var(--stroke) solid var(--border); border-radius: var(--radius); background: var(--muted); font-size: 13px; line-height: 1.5; }
code { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; font-size: .9em; }
:not(pre) > code { padding: 1px 5px; border-radius: 4px; background: var(--muted); }
"""


# ── Ficha em Markdown para HTML ──────────────────────────────
# Só o que as fichas usam: títulos, parágrafos, listas, tabelas, blocos
# de código, negrito e código no meio da linha.

def inline(texto):
    texto = html.escape(texto, quote=False)
    texto = re.sub(r"`([^`]+)`", r"<code>\1</code>", texto)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)


def celulas(linha):
    return [x.strip() for x in linha.strip().strip("|").split("|")]


def markdown(texto):
    saida, linhas, i = [], texto.split("\n"), 0
    while i < len(linhas):
        linha = linhas[i]
        if linha.startswith("```"):
            fim = linhas.index("```", i + 1)
            codigo = html.escape("\n".join(linhas[i + 1:fim]), quote=False)
            saida.append(f"<pre><code>{codigo}</code></pre>")
            i = fim + 1
        elif linha.startswith("## "):
            saida.append(f"<h2>{inline(linha[3:])}</h2>")
            i += 1
        elif linha.startswith("|"):
            bloco = []
            while i < len(linhas) and linhas[i].startswith("|"):
                bloco.append(celulas(linhas[i]))
                i += 1
            cabeca = "".join(f"<th>{inline(x)}</th>" for x in bloco[0])
            corpo = "".join("<tr>" + "".join(f"<td>{inline(x)}</td>" for x in r) + "</tr>" for r in bloco[2:])
            saida.append(f'<div class="tabela"><table><thead><tr>{cabeca}</tr></thead><tbody>{corpo}</tbody></table></div>')
        elif re.match(r"(- |\d+\. )", linha):
            ordem = not linha.startswith("- ")
            # Cada item guarda o texto e os subitens, que vêm recuados com "- ".
            itens = []
            while i < len(linhas) and (re.match(r"(- |\d+\. )", linhas[i]) or (linhas[i].startswith("  ") and itens)):
                if linhas[i].startswith("  ") and linhas[i].strip().startswith("- "):
                    itens[-1][1].append(linhas[i].strip()[2:])
                elif linhas[i].startswith("  "):
                    itens[-1][0] += " " + linhas[i].strip()
                else:
                    itens.append([re.sub(r"^(- |\d+\. )", "", linhas[i]), []])
                i += 1
            tag = "ol" if ordem else "ul"
            def item(texto, subs):
                sub = "<ul>" + "".join(f"<li>{inline(s)}</li>" for s in subs) + "</ul>" if subs else ""
                return f"<li>{inline(texto)}{sub}</li>"
            saida.append(f"<{tag}>" + "".join(item(*x) for x in itens) + f"</{tag}>")
        elif linha.strip():
            par = []
            while i < len(linhas) and linhas[i].strip() and not re.match(r"(```|## |\||- |\d+\. )", linhas[i]):
                par.append(linhas[i].strip())
                i += 1
            saida.append(f"<p>{inline(' '.join(par))}</p>")
        else:
            i += 1
    return "\n".join(saida)


def pagina_ficha(arq):
    pronta = {x[0]: x for x in CASCA + ACAO + SEQUENCIA + DADOS + MIDIA}
    if arq in SEM_FICHA:
        titulo = pronta[arq][1]
        nome_shadcn, frase = SEM_FICHA[arq]
        doc = "<p>A ficha se escreve depois que a interface for aprovada na&nbsp;vitrine.</p>"
    else:
        texto = (FICHAS / f"{arq}.md").read_text()
        titulo = texto.split("\n", 1)[0][2:]
        resto = texto.split("\n", 1)[1].lstrip("\n")
        abertura, corpo = resto.split("\n", 1)
        nome_shadcn, frase = abertura.split(" · ", 1)
        doc = markdown(corpo)
    peca_ = PALCO_DE.get(arq, arq)
    volta = f"../index.html#peca-{peca_}" if peca_ in pronta else "../index.html"
    na_pagina = ""
    if peca_ in pronta:
        _, nome, largura, testar = pronta[peca_]
        itens = "".join(f"<li>{x}</li>" for x in testar)
        na_pagina = f"""
  <section class="ficha-pagina__palco" aria-labelledby="na-pagina">
    <h2 id="na-pagina">Na página</h2>
    <p class="t-apoio prosa">A peça montada numa página com o texto real e outras peças em&nbsp;volta.</p>
    {palco(f"../palco/{peca_}.html", f"{nome}, na página", largura, 800)}
    <p class="t-rotulo">O que testar</p>
    <ul class="testar">{itens}</ul>
  </section>"""
    main = f"""
<main id="conteudo" class="container ficha-pagina">
  <header class="ficha-pagina__topo">
    <a class="link" data-variant="voltar" href="{volta}"><i aria-hidden="true">←</i> Vitrine</a>
    <span class="badge">{inline(nome_shadcn)}</span>
    <h1 class="t-display">{titulo}</h1>
    <p class="t-sub">{frase[0].upper() + frase[1:] if arq in SEM_FICHA else inline(frase[0].upper() + frase[1:])}</p>
  </header>{na_pagina}
  <article class="doc">
{doc}
  </article>
</main>"""
    pagina = c.cabeca(P_SUB, f"{titulo}, ficha · Jeff DS no site", ESTILO) + c.cabecalho(P_SUB, None, "Pular para a ficha") + main + c.rodape(P_SUB, None)
    if na_pagina:
        pagina = pagina.replace("</body>", '<script src="../vitrine.js"></script>\n</body>')
    return pagina


# ── Palcos ───────────────────────────────────────────────────
# Páginas pequenas e de verdade, uma por peça, sem o Carregamento para o
# palco não esperar 1,6s a cada troca de largura. O item Omnichat aponta
# para o próprio palco, para a página atual aparecer marcada.

def prosa(*pars):
    return f'<div class="prosa">{"".join(f"<p>{p}</p>" for p in pars)}</div>'


def palco_cabecalho():
    corpo = f"""
<main id="conteudo" class="container palco-pagina">
  <div>
    <section class="section" aria-labelledby="p-titulo">
      <p class="section__rotulo t-rotulo">01 · Contexto</p>
      <h2 class="t-titulo" id="p-titulo">{c.PROBLEMA_TITULO}</h2>
      <p class="t-lead prosa">{c.CONTEXTO}</p>
      {prosa(*c.PROBLEMA)}
      {prosa(*c.RESULTADO)}
    </section>
  </div>
</main>
<script src="{P_SUB}assets/ds/componentes.js"></script>
</body>
</html>
"""
    return c.cabeca(P_SUB, "Cabeçalho · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "cabecalho.html") + corpo


def palco_sumario():
    return c.cabeca(P_SUB, "Sumário · Palco da vitrine") + c.cabecalho(P_SUB, "sumario.html") + caso.main(P_SUB) + c.rodape(P_SUB, "sumario.html")


def palco_rodape():
    corpo = f"""
<main id="conteudo" class="container palco-pagina">
  <div>
    <section class="section" aria-labelledby="p-titulo">
      <p class="section__rotulo t-rotulo">05 · Resultado</p>
      <h2 class="t-titulo" id="p-titulo">{c.RESULTADO_TITULO}</h2>
      {prosa(*c.RESULTADO)}
      {c.fechamento(P_SUB)}
    </section>
  </div>
</main>"""
    return c.cabeca(P_SUB, "Rodapé · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "rodape.html") + corpo + c.rodape(P_SUB, "rodape.html")


def secao(n, nome, titulo, *partes):
    return f"""
    <section class="section" id="s{n}" aria-labelledby="s{n}-titulo">
      <p class="section__rotulo t-rotulo">0{n} · {nome}</p>
      <h2 class="t-titulo" id="s{n}-titulo">{titulo}</h2>
      {"".join(partes)}
    </section>"""


def caso_palco(rotulo, secoes, topo=""):
    """Um caso pequeno, com o Sumário ao lado, para a peça ter a largura
    que tem no caso. `secoes` é uma lista de (ícone, nome, título, partes)."""
    itens = "".join(
        f'<li><a class="sumario__item" href="#s{n}">{c.icone(P_SUB, ic, 32)}<span class="sumario__num">0{n}</span><span class="sumario__nome">{nome}</span></a></li>'
        for n, (ic, nome, _, _) in enumerate(secoes, 1))
    marcas = '<span class="sumario__seg" aria-hidden="true"></span>' * len(secoes)
    corpo = "".join(secao(n, nome, tit, *partes) for n, (_, nome, tit, partes) in enumerate(secoes, 1))
    return f"""
<main id="conteudo" class="container caso">
  <nav class="sumario" data-sumario aria-label="{rotulo}">
    <p class="t-rotulo sumario__titulo">{rotulo}</p>
    <ol class="sumario__lista" id="sumario-lista">{itens}</ol>
    <button class="sumario__botao" type="button" aria-expanded="false" aria-controls="sumario-lista" hidden><span class="sr">Seções deste palco</span>{marcas}</button>
    <span class="sumario__aviso" aria-hidden="true"></span>
  </nav>
  <div>{topo}{corpo}
  </div>
</main>"""


def palco_link():
    corpo = f"""
<main id="conteudo" class="container palco-pagina">
  <div>
    <p><a class="link" data-variant="voltar" href="{P_SUB}index.html"><i aria-hidden="true">←</i> Todos os casos</a></p>
    {secao(5, "Resultado", c.RESULTADO_TITULO, prosa(*c.RESULTADO), c.fechamento(P_SUB))}
    <p class="links-soltos">
      <a class="link" data-variant="seguir" href="{P_SUB}case-inpulse.html">Ver o caso do Inpulse <i aria-hidden="true">→</i></a>
      <a class="link" data-variant="externo" href="https://www.linkedin.com/in/maiajeff/" target="_blank" rel="noopener">linkedin.com/in/maiajeff <i aria-hidden="true">↗</i></a>
    </p>
  </div>
</main>"""
    return c.cabeca(P_SUB, "Link · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "link.html") + corpo + c.rodape(P_SUB, "link.html")


def palco_etiqueta():
    topo = f"""
    <header class="topo">
      <div class="topo__texto">{c.badges()}<h1 class="t-display">{c.TITULO}</h1><p class="t-sub">{c.LEAD}</p></div>
      <div class="card topo__ficha" data-variant="muted"><p class="t-rotulo card__titulo">Ficha do projeto</p>{c.ficha()}</div>
      <div class="card topo__salto" data-variant="acento">{c.salto()}{c.ilustracao(P_SUB, "salto")}</div>
    </header>"""
    corpo = caso_palco("Neste palco", [
        ("dialogo", "Antes e depois", c.CONVERSA_TITULO, [c.conversa(P_SUB)]),
        ("grafico", "Resultado", c.RESULTADO_TITULO, [prosa(c.RESULTADO[0]), c.callout()]),
    ], topo)
    return c.cabeca(P_SUB, "Etiqueta · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "etiqueta.html") + corpo + c.rodape(P_SUB, "etiqueta.html")


def destaques():
    nota = f"""<div class="callout" data-variant="nota">
        <p class="t-rotulo callout__rotulo">O aluno de medicina</p>
        <p>O curso é integral e exige muito. Devolver tempo para&nbsp;o&nbsp;que&nbsp;importa, o&nbsp;estudo e&nbsp;o&nbsp;descanso, era o&nbsp;critério que&nbsp;separava uma boa solução de&nbsp;uma&nbsp;solução bonita.</p>
      </div>"""
    papel = """<div class="callout">
        <p class="callout__frase">O calendário doía mais que&nbsp;o&nbsp;boletim.</p>
        <p class="callout__legenda">De 10 funcionalidades testadas, 4 tiveram entusiasta espontâneo, e&nbsp;o&nbsp;boletim completo, que era a&nbsp;aposta inicial do&nbsp;time, ficou atrás delas.</p>
      </div>"""
    atrito = f"""<div class="callout" data-variant="atrito">
        {c.icone(P_SUB, "alerta", 48)}
        <h3>Aqui eu cortei rápido&nbsp;demais</h3>
        {prosa("A análise pegava tudo que é padrão de interface e não pegou a única coisa que travava um fluxo de configuração de agente, que era o nome de um campo no vocabulário de quem trabalha dentro de um varejista. Heurística não pega linguagem de domínio.",
               "Hoje a regra é que teste com gente continua obrigatório quando a entrega traz vocabulário novo ou muda modelo mental.")}
      </div>"""
    return nota, papel, atrito


def palco_destaque():
    nota, papel, atrito = destaques()
    corpo = caso_palco("Neste palco", [
        ("lupa", "Descoberta", "Qual a&nbsp;melhor maneira de&nbsp;entregar um&nbsp;boletim que&nbsp;o&nbsp;aluno use",
         [prosa("Depois de analisar o NPS, as pesquisas que o time já tinha feito e um dia na vida conduzido por um dos designers, ficou claro que esse aluno está sempre em movimento e precisava de algo de fácil acesso, que estivesse com ele o&nbsp;tempo todo."), nota]),
        ("lampada", "Experimento", "Qual funcionalidade o&nbsp;aluno quer primeiro",
         [prosa("Estruturamos um experimento para medir a desejabilidade de&nbsp;cada funcionalidade, e assim priorizar o que já sabíamos ser dor do&nbsp;aluno e da&nbsp;empresa."), papel]),
        ("calendario", "Rituais", "Saímos de&nbsp;Scrum para&nbsp;Kanban",
         [prosa("Com o rascunho já pronto antes do encontro, o que sobrou para a agenda foi&nbsp;dúvida, não&nbsp;redação.",
                "Reduzimos bastante teste de usabilidade, porque o Claude passou a apontar problema de fluxo com consistência, usando heurística de Norman e Nielsen mais o que a gente já sabe do&nbsp;nosso público."), atrito]),
        ("grafico", "Resultado", c.RESULTADO_TITULO, [prosa(*c.RESULTADO), c.callout()]),
    ])
    return c.cabeca(P_SUB, "Destaque · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "destaque.html") + corpo + c.rodape(P_SUB, "destaque.html")


# ── Amostras ─────────────────────────────────────────────────
# A peça sozinha, com todas as formas dela e o nome de cada uma. É o que a
# vitrine mostra. A aplicação numa página fica no palco, dentro da ficha.

def amostra(titulo, corpo, antes="", depois=""):
    """`antes` e `depois` são a casca que a peça precisa em volta (o
    Cabeçalho e o Rodapé são a própria casca)."""
    return (c.cabeca(P_SUB, f"{titulo} · Amostra da vitrine", ESTILO) + antes
            + f'\n<main id="conteudo" class="container amostra">{corpo}\n</main>\n'
            + (depois or f'<script src="{P_SUB}assets/ds/componentes.js"></script>\n</body>\n</html>\n'))


def item(nome, codigo, conteudo):
    cod = f"<code>{html.escape(codigo, quote=False)}</code>" if codigo else ""
    return f"""
  <div class="amostra__item">
    <p class="amostra__nome"><span class="t-rotulo">{nome}</span>{cod}</p>
    {conteudo}
  </div>"""


def amostra_cabecalho():
    return (c.cabeca(P_SUB, "Cabeçalho · Amostra da vitrine", ESTILO) + c.cabecalho(P_SUB, "cabecalho.html")
            + f'\n<main id="conteudo"></main>\n<script src="{P_SUB}assets/ds/componentes.js"></script>\n</body>\n</html>\n')


def amostra_sumario():
    vazio = '<div class="amostra__vazio">Conteúdo da Seção</div>'
    corpo = caso_palco("Neste caso", [
        ("fronteira", "O problema", c.PROBLEMA_TITULO, [vazio]),
        ("camadas", "Processo", c.CAMADAS_TITULO, [vazio]),
        ("dialogo", "Antes e depois", c.CONVERSA_TITULO, [vazio]),
        ("grafico", "Resultado", c.RESULTADO_TITULO, [vazio]),
    ])
    return (c.cabeca(P_SUB, "Sumário · Amostra da vitrine", ESTILO) + corpo
            + f'\n<script src="{P_SUB}assets/ds/componentes.js"></script>\n</body>\n</html>\n')


def amostra_rodape():
    return c.cabeca(P_SUB, "Rodapé · Amostra da vitrine", ESTILO) + '\n<main id="conteudo"></main>' + c.rodape(P_SUB, "rodape.html")


def amostra_link():
    def solto(variante, seta, texto, href="#", fora=False):
        alvo = ' target="_blank" rel="noopener"' if fora else ""
        if variante == "voltar":
            return f'<a class="link" data-variant="voltar" href="{href}"{alvo}><i aria-hidden="true">{seta}</i> {texto}</a>'
        return f'<a class="link" data-variant="{variante}" href="{href}"{alvo}>{texto} <i aria-hidden="true">{seta}</i></a>'
    return amostra("Link", "".join([
        item("Sem variante, no meio do texto", "", f'<p class="prosa">{c.FECHO}</p>'),
        item("Voltar", 'data-variant="voltar"', solto("voltar", "←", "Todos os casos")),
        item("Seguir", 'data-variant="seguir"', solto("seguir", "→", "Ver o caso do Inpulse")),
        item("Externo", 'data-variant="externo"', solto("externo", "↗", "linkedin.com/in/maiajeff", "https://www.linkedin.com/in/maiajeff/", True)),
        item("Topo", 'data-variant="topo"', solto("topo", "↑", "Voltar ao topo", "#conteudo")),
        item("Na superfície tinta", 'class="superficie-tinta"', f"""<div class="amostra__tinta superficie-tinta">
      <p class="prosa">Se&nbsp;esse tipo de&nbsp;camada é um problema no seu produto, <a class="link" href="#">me&nbsp;chama no&nbsp;WhatsApp</a>.</p>
      <div class="amostra__fileira">{solto("externo", "↗", "linkedin.com/in/maiajeff")}{solto("topo", "↑", "Voltar ao topo", "#conteudo")}</div>
    </div>"""),
    ]))


def amostra_etiqueta():
    def b(texto, variante="", ic=""):
        v = f' data-variant="{variante}"' if variante else ""
        return f'<span class="badge"{v}>{c.icone(P_SUB, ic, 20, "icone-inline") if ic else ""}{texto}</span>'
    return amostra("Etiqueta", "".join([
        item("Grupo do Topo", 'ul.badges', c.badges()),
        item("Sem atributo", "", f'<div class="amostra__fileira">{b("Omnichat")}</div>'),
        item("Acento", 'data-variant="acento"', f'<div class="amostra__fileira">{b("Agentes conversacionais", "acento")}</div>'),
        item("Tinta", 'data-variant="tinta"', f'<div class="amostra__fileira">{b("Lead convertido", "tinta")}</div>'),
        item("Com ícone, no Antes e depois", "", f'<div class="amostra__fileira"><p class="compare__cabeca">{b("Antes", "", "xis")}{b("Conversa abandonada", "tinta")}</p><p class="compare__cabeca">{b("Depois", "", "check")}{b("Lead convertido", "tinta")}</p></div>'),
        item("Na superfície tinta", 'class="superficie-tinta"', f'<div class="amostra__tinta superficie-tinta"><div class="amostra__fileira">{b("O que eu levo daqui", "acento")}{b("Omnichat")}</div></div>'),
    ]))


def amostra_destaque():
    nota, papel, atrito = destaques()
    return amostra("Destaque", "".join([
        item("Frase no papel", ".callout", papel),
        item("Nota", 'data-variant="nota"', nota),
        item("Atrito", 'data-variant="atrito"', atrito),
        item("Frase na tinta", ".callout.superficie-tinta", c.callout()),
    ]))


# ── Onda 3, com o texto das páginas publicadas ───────────────

def passo(icone, titulo, *pars, num=None, marca="", efeito=None, i=None, depois=""):
    """Um Cartão do Passos: o adesivo no canto, o número vazado, o rótulo
    do estágio, o nome, o texto e o efeito."""
    estilo = f' style="--i: {i}"' if i is not None else ""
    n = f'<span class="step__num" aria-hidden="true">{num:02d}</span>' if num else ""
    m = f'<span class="t-rotulo">{marca}</span>' if marca else ""
    ef = f'<p class="step__efeito"><span class="t-rotulo">{efeito[0]}</span> {efeito[1]}</p>' if efeito else ""
    return (f'<li class="step"{estilo}>{c.icone(P_SUB, icone, 64, "icone step__icone")}{n}{m}'
            f'<h3 class="step__titulo">{titulo}</h3>{"".join(f"<p>{x}</p>" for x in pars)}{depois}{ef}</li>')


def passos_padrao():
    return '<ol class="steps">' + "".join([
        passo("grafico", "Entender os&nbsp;dados do&nbsp;NPS",
              "Clusterizamos os comentários do NPS em grandes eixos e subcategorias, com uma divisão entre semestres. Era preciso um relatório que ilustrasse a jornada do aluno do início ao fim da graduação, para que a ação surtisse efeito no período específico de cada problema.",
              num=1, efeito=("Consequência", "A insatisfação deixou de ser uma nota única e&nbsp;passou a ter lugar e momento na jornada.")),
        passo("pessoa", "Completar o&nbsp;que a&nbsp;reclamação não&nbsp;contava",
              "As informações que tínhamos não bastavam, e fomos atrás dos alunos para preencher outros aspectos da vida deles. Um aluno que mora longe da instituição sofre muito mais com um cancelamento de aula em cima da hora do que um aluno que mora perto do campus, e nada disso aparece na nota.",
              num=2, efeito=("Consequência", "As ações passaram a considerar o contexto de&nbsp;vida do&nbsp;aluno, não só a&nbsp;reclamação registrada.")),
        passo("rota", "Achar um&nbsp;formato que&nbsp;obrigue a&nbsp;percorrer",
              "Antes do tabuleiro testamos dois formatos mais óbvios, um dashboard de indicadores e um resumo executivo de duas páginas por campus. Os dois falharam pelo mesmo motivo. Entregavam a conclusão pronta, e ninguém precisava percorrer a jornada do aluno para chegar nela.",
              "O tabuleiro foi escolhido porque obriga quem lê a&nbsp;andar por semestre e&nbsp;por&nbsp;eixo, e&nbsp;é nesse trajeto que o time reconhece o próprio aluno e&nbsp;propõe ação.",
              num=3, efeito=("Consequência", "O formato virou parte da solução, não a&nbsp;embalagem da pesquisa.")),
    ]) + "</ol>"


def passos_par():
    return '<ul class="steps" data-layout="par">' + "".join([
        passo("dialogo", "O&nbsp;trabalho vivia em&nbsp;reunião", "A gente discutia bem e decidia bem. Depois alguém tinha que transformar aquilo em PRD, story, relatório e protótipo. Esse alguém sempre demorava."),
        passo("calendario", "A&nbsp;garantia prévia custava semanas", "Como construir era caro, quase toda validação acontecia antes do desenvolvimento. Fazia sentido, e consumia semanas."),
    ]) + "</ul>"


ENTREGAS = [
    ("visao", "lampada", "Visão de produto", "Vira direção antes de virar backlog.", "A habilidade lê a transcrição do ritual e devolve o rascunho da visão. O time revisa e ajusta, em vez de escrever do zero depois da conversa."),
    ("prd", "lapis", "PRD", "Chega pronto para discussão, não para redação.", "Com o PRD já rascunhado, a Planning deixou de ser um rito semanal. Acontece sob demanda, e a maior parte dela é assíncrona."),
    ("us", "janela", "User stories", "Entram no Kanban já documentadas.", "O refinamento virou tirar dúvida sobre o que já está escrito na story e desenhado no protótipo. Foi o que derrubou o ritual de quatro horas para quarenta minutos."),
    ("usabilidade", "lupa", "Relatório de usabilidade", "Análise no lugar de rodada de teste.", "O Claude aponta problema de fluxo com consistência, usando heurística de Norman e Nielsen mais o que a gente já sabe do público da Omni."),
    ("prototipo", "celular", "Protótipo", "Nasce desenvolvido e segue direto para a&nbsp;engenharia.", "O protótipo sai do Claude Design e vai para o Claude Code, de onde a engenharia assume. Design usa o Claude Code para manter a biblioteca fiel à do código, que é a referência principal."),
]


def entregas(prefixo):
    abas, paineis = [], []
    for i, (cid, ic, nome, sub, txt) in enumerate(ENTREGAS, 1):
        abas.append(f'<button class="tab" type="button" role="tab" id="{prefixo}-{cid}" aria-controls="{prefixo}-painel-{cid}">{c.icone(P_SUB, ic, 32, "icone-inline")}<span class="t-rotulo">0{i}</span>{nome}</button>')
        paineis.append(f"""<div class="tabs__painel" id="{prefixo}-painel-{cid}" tabindex="0">
  <h3 class="tabs__painel-titulo">{c.icone(P_SUB, ic, 32, "icone-inline")}<span class="t-rotulo">0{i}</span>{nome}</h3>
  <p><strong>{sub}</strong> {txt}</p>
</div>""")
    return f"""<div class="tabs" data-tabs>
  <div class="tabs__lista" aria-label="Entregas da saída" aria-orientation="vertical">{"".join(abas)}</div>
  <div class="tabs__paineis">{"".join(paineis)}</div>
</div>"""


def passos_estagios():
    lista = '<ul class="step__lista">' + "".join(f"<li>{nome}</li>" for _, _, nome, _, _ in ENTREGAS) + "</ul>"
    return '<ol class="steps" data-layout="estagios">' + "".join([
        passo("dialogo", "Transcrição dos rituais", "O que o time já falava em reunião, agora capturado como matéria&nbsp;prima.", marca="Entrada"),
        passo("robo", "Habilidades no&nbsp;Claude", "Habilidades que a gente criou leem a transcrição e devolvem os rascunhos.", marca="Camada"),
        passo("janela", "Cinco entregas", marca="Saída", depois=lista),
    ]) + "</ol>"


FASES = [
    ("Identificação de oportunidades", "Dado de produto, pesquisa e canais de feedback alimentam uma árvore de oportunidades que facilita escolher o que entra em pauta.", "Produto e design, com&nbsp;dados alimentando a&nbsp;árvore."),
    ("Validação de desejabilidade e diferencial", "Confirmamos se a aposta faz sentido antes de o time gastar tempo desenhando a solução.", "Produto e design."),
    ("Definição e prototipagem", "É aqui que nasce a maior parte da solução. O&nbsp;protótipo já sai desenvolvido e segue para a&nbsp;engenharia sem etapa de tradução no&nbsp;meio.", "Produto, design e engenharia, com&nbsp;prototipação distribuída entre os&nbsp;três."),
    ("Delivery", "Alfa na engenharia, que garante o funcionamento do que foi construído. Beta, aberto ou fechado, validando o experimento antes de abrir para todos.", "Engenharia no alfa, time inteiro no beta."),
    ("Depois do lançamento", "O foco vira satisfação e adoção. A&nbsp;validação qualitativa entra quando o&nbsp;dado quantitativo mostra desvio do&nbsp;esperado.", "Produto, design e dados, junto de GA e GTM."),
]


FASE_ICONES = ["lupa", "alvo", "lapis", "celular", "grafico"]


def passos_funil():
    return '<ol class="steps" data-layout="funil">' + "".join(
        passo(FASE_ICONES[i], nome, txt, num=i + 1, efeito=("Quem conduz", quem), i=i)
        for i, (nome, txt, quem) in enumerate(FASES)) + "</ol>"


def passos_trilha():
    return '<ol class="steps" data-layout="trilha">' + "".join([
        passo("lampada", "Criação", "Novo componente nasce a partir de uma&nbsp;necessidade do&nbsp;produto.", num=1),
        passo("olho", "Comportamento e&nbsp;uso", "Definição escrita pensando também na&nbsp;leitura do&nbsp;Claude.", num=2),
        passo("verifica", "Aprovação no&nbsp;código", "Validação direto no&nbsp;código, antes de subir para o repositório no&nbsp;GitHub.", num=3),
    ]) + "</ol>"


def rito(icone, nome, texto):
    return f'<li class="step"><div class="step__topo">{c.icone(P_SUB, icone, 40, "icone step__icone")}<h3 class="step__titulo">{nome}</h3></div><p>{texto}</p></li>'


def passos_ritos():
    return '<ul class="steps" data-layout="ritos">' + "".join([
        rito("calendario", "Planning", "Virou assíncrona e sob&nbsp;demanda, não&nbsp;mais um rito&nbsp;semanal."),
        rito("pessoa", "Daily", "Ficou só com engenharia. Produto entra quando&nbsp;precisa."),
        rito("lupa", "Refinamento", "De 4 horas para 40&nbsp;minutos, porque virou tirar dúvida sobre o&nbsp;que já&nbsp;está escrito."),
    ]) + "</ul>"


def citacao():
    def lado(variante, ic, quando, fala, autoria):
        return f"""<div class="card compare__lado" data-variant="{variante}">
    <p class="compare__cabeca"><span class="badge">{c.icone(P_SUB, ic, 20, "icone-inline")}{quando}</span></p>
    <figure class="compare__citacao">
      <blockquote><p>{fala}</p></blockquote>
      <figcaption>{autoria}</figcaption>
    </figure>
  </div>"""
    return f"""<div class="compare" data-variant="citacao">
  {lado("muted", "xis", "Antes", "“Precisamos correr atrás de&nbsp;nota, elas levam dias para&nbsp;sair, e quando saem a gente tem que&nbsp;anotar pra ver todas em&nbsp;um&nbsp;mesmo lugar. Difícil se preparar dessa maneira.”", "Nota 2 no NPS, de uma estudante no 3º semestre.")}
  {lado("acento", "check", "Depois", "“Com o Inpulse eu não preciso ficar anotando as&nbsp;notas dos complexos temáticos, e isso facilitou pra eu achar o&nbsp;que devo estudar para&nbsp;as recuperações.”", "Aluna do 5º semestre de medicina.")}
</div>"""


DIMENSOES = [
    ("Prototipação", "Concentrada em design", "Distribuída entre produto, design e engenharia"),
    ("Validação qualitativa", "Quase sempre antes do desenvolvimento", "Depois do lançamento, quando o dado mostra desvio do esperado"),
    ("Rituais", "Longos e na agenda", "Curtos e assíncronos"),
    ("Testes A/B", "Poucas variações, porque cada uma custava caro para construir", "Muitas variações, porque desenvolver ficou ágil e barato"),
]


def confronto():
    linhas = "".join(f"""
    <tr role="row">
      <th role="rowheader" scope="row">{d}</th>
      <td role="cell"><span class="t-rotulo compare__marca" aria-hidden="true">Antes</span>{a}</td>
      <td role="cell"><span class="t-rotulo compare__marca" aria-hidden="true">Depois</span>{b}</td>
    </tr>""" for d, a, b in DIMENSOES)
    return f"""<table class="compare" data-variant="confronto" role="table">
  <caption class="sr">O trabalho do time antes e depois, em quatro dimensões</caption>
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


def amostra_passos():
    return amostra("Passos", "".join([
        item("Sequência, com efeito", "ol.steps", passos_padrao()),
        item("Par", 'data-layout="par"', passos_par()),
        item("Estágios", 'data-layout="estagios"', passos_estagios()),
        item("Funil", 'data-layout="funil"', passos_funil()),
        item("Trilha", 'data-layout="trilha"', passos_trilha()),
        item("Ritos", 'data-layout="ritos"', passos_ritos()),
    ]))


def amostra_antes_e_depois():
    return amostra("Antes e depois", "".join([
        item("Conversa", "ol.turnos", c.conversa(P_SUB)),
        item("Citação", 'data-variant="citacao"', citacao()),
        item("Confronto", 'data-variant="confronto"', confronto()),
    ]))


def palco_passos():
    corpo = caso_palco("Neste palco", [
        ("fronteira", "O problema", "O&nbsp;trabalho vivia em&nbsp;reunião", [passos_par()]),
        ("camadas", "O que a gente fez", "Da&nbsp;transcrição ao&nbsp;entregável", [passos_estagios(), entregas("palco")]),
        ("calendario", "Rituais", "Saímos de&nbsp;Scrum para&nbsp;Kanban",
         [prosa("Com o rascunho já pronto antes do encontro, o que sobrou para a agenda foi&nbsp;dúvida, não&nbsp;redação."), passos_ritos()]),
        ("rota", "O novo funil", "Cinco fases, do&nbsp;sinal ao&nbsp;pós-lançamento", [passos_funil()]),
        ("janela", "Fluxo paralelo", "O&nbsp;Design System corre por&nbsp;fora do&nbsp;funil",
         [prosa("Em paralelo ao funil roda o fluxo do Design System, com componente aprovado direto no código antes de subir para o&nbsp;GitHub.",
                "Hoje áreas fora de design também prototipam, CS inclusive, o que abriu uma discussão interna sobre controle. Resolvi separando o que cada protótipo pode prometer, não restringindo quem&nbsp;cria."), passos_trilha()]),
    ])
    return c.cabeca(P_SUB, "Passos · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "passos.html") + corpo + c.rodape(P_SUB, "passos.html")


def palco_antes_e_depois():
    corpo = caso_palco("Neste palco", [
        ("pessoa", "Contexto", "O&nbsp;que o&nbsp;aluno dizia", [citacao()]),
        ("dialogo", "Antes e depois", c.CONVERSA_TITULO, [f'<p class="t-apoio">{c.CONVERSA_LEGENDA}</p>', c.conversa(P_SUB)]),
        ("camadas", "O novo time", "O&nbsp;mesmo time, com&nbsp;o&nbsp;eixo do&nbsp;trabalho deslocado", [confronto()]),
    ])
    return c.cabeca(P_SUB, "Antes e depois · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "antes-e-depois.html") + corpo + c.rodape(P_SUB, "antes-e-depois.html")


# ── Onda 4, com o texto das páginas publicadas ───────────────

def valor(v):
    # O til de aproximação é lido como "til". Quem ouve recebe "cerca de".
    if v.startswith("~"):
        return f'<span aria-hidden="true">~</span><span class="sr">cerca de </span>{v[1:]}'
    return v


def barras(titulo, grupos):
    """`grupos` é uma lista de (nome ou None, linhas), e cada linha é
    (rótulo, valor escrito, valor de 0 a 100, tom)."""
    def linha(rotulo, escrito, num, tom):
        return (f'<div class="chart__linha"><dt class="chart__rotulo">{rotulo}</dt><dd class="chart__valor">{valor(escrito)}</dd>'
                f'<dd class="chart__trilho" aria-hidden="true"><span class="chart__preenche" data-tom="{tom}" style="--valor: {num}"></span></dd></div>')
    def grupo(nome, linhas):
        cab = f'<h3 class="chart__nome">{nome}</h3>' if nome else ""
        return f'<div class="chart__grupo">{cab}<dl class="chart__linhas">{"".join(linha(*x) for x in linhas)}</dl></div>'
    return f"""<figure class="chart" data-variant="barras" data-revelar>
  <figcaption class="t-rotulo">{titulo}</figcaption>
  <div class="chart__grupos">{"".join(grupo(*g) for g in grupos)}</div>
</figure>"""


def barras_processo():
    return barras("Tempo antes e depois", [
        ("Discovery", [("Antes", "1 a 2 meses", 100, "trama"), ("Depois", "~1 semana", 12.5, "cheio")]),
        ("Refinamento semanal", [("Antes", "4 a 5 h", 100, "trama"), ("Depois", "30 a 40 min", 13, "cheio")]),
    ])


def barras_mapa():
    return barras("Usuários únicos no primeiro mês", [
        (None, [("Sem o mapa de experiência", "20", 2.2, "trama"), ("Com o mapa de experiência", "890", 100, "cheio")]),
    ])


NIVEIS = [
    ("cheio", "Entusiasta", "entusiasta", "entusiastas", "Demonstra interesse de maneira espontânea."),
    ("trama", "Receptivo", "receptivo", "receptivos", "Demonstra interesse a partir de uma interação ou pergunta do&nbsp;facilitador."),
    ("vazio", "Indiferente", "indiferente", "indiferentes", "Verbaliza a falta de interesse, ou ignora que a funcionalidade&nbsp;existe."),
]

# Reações de 10 participantes por funcionalidade: entusiasta, receptivo e
# indiferente, na ordem da página do Inpulse.
REACOES = [
    ("Próximas avaliações", (0, 8, 2)),
    ("Faltas", (0, 10, 0)),
    ("Situação atual", (1, 9, 0)),
    ("Últimas avaliações", (1, 8, 1)),
    ("Calendário", (3, 7, 0)),
    ("Planejar estudos", (1, 8, 1)),
]


def pilhas():
    legenda = "".join(
        f'<div><dt><span class="chart__amostra" data-tom="{tom}" aria-hidden="true"></span>{nome}</dt><dd>{desc}</dd></div>'
        for tom, nome, _, _, desc in NIVEIS)
    def pilha(nome, contas):
        partes = "".join(f'<span class="chart__parte" data-tom="{NIVEIS[i][0]}" style="--n: {n}"></span>' for i, n in enumerate(contas) if n)
        conta = " · ".join(f"{n} {NIVEIS[i][2] if n == 1 else NIVEIS[i][3]}" for i, n in enumerate(contas) if n)
        return f'<li class="chart__pilha"><p class="chart__nome">{nome}</p><div class="chart__trilho" aria-hidden="true">{partes}</div><p class="chart__conta">{conta}</p></li>'
    return f"""<figure class="chart" data-variant="pilhas" data-revelar>
  <figcaption class="t-rotulo">Reações de 10 participantes, em seis das dez funcionalidades testadas</figcaption>
  <dl class="chart__legenda">{legenda}</dl>
  <ol class="chart__pilhas">{"".join(pilha(*x) for x in REACOES)}</ol>
</figure>"""


def escala():
    return """<figure class="chart" data-variant="escala" style="--antes: -33; --depois: 15" data-revelar>
  <figcaption class="t-rotulo">Nota geral de NPS<span class="sr">, numa escala de −100 a +100</span></figcaption>
  <div class="chart__escala">
    <p class="chart__marco" data-ponto="antes"><span class="chart__numero">−33</span><span class="t-rotulo">Antes</span></p>
    <p class="chart__marco" data-ponto="depois"><span class="chart__numero">+15</span><span class="t-rotulo">Depois</span></p>
    <div class="chart__eixo" aria-hidden="true"><span class="chart__percurso"></span><span class="chart__zero"></span><span class="chart__ponto" data-ponto="antes"></span><span class="chart__ponto" data-ponto="depois"></span></div>
    <p class="chart__regua t-rotulo" aria-hidden="true"><span>−100</span><span>0</span><span>+100</span></p>
  </div>
</figure>"""


def amostra_grafico():
    def no(acento, conteudo):
        return f'<div data-acento="{acento}">{conteudo}</div>'
    return amostra("Gráfico", "".join([
        item("Barras, um par, no azul do Mapa", 'data-variant="barras"', no("azul", barras_mapa())),
        item("Barras, dois pares, no lime do Processo", 'data-variant="barras"', no("lime", barras_processo())),
        item("Pilhas, com a legenda, no verde do Inpulse", 'data-variant="pilhas"', no("verde", pilhas())),
        item("Escala, no azul do Mapa", 'data-variant="escala"', no("azul", escala())),
    ]))


def palco_grafico():
    corpo = caso_palco("Neste palco", [
        ("lampada", "Experimento", "Qual funcionalidade o&nbsp;aluno quer primeiro",
         [prosa("Estruturamos um experimento para medir a desejabilidade de&nbsp;cada funcionalidade, e assim priorizar o que já sabíamos ser dor do&nbsp;aluno e da&nbsp;empresa.",
                "Usamos a estrutura de um teste de usabilidade, com tarefas oferecidas aos participantes, mas não para medir facilidade. Era para registrar a reação espontânea a cada&nbsp;funcionalidade."), pilhas()]),
        ("alvo", "O que move a nota", "Um&nbsp;mapa não move NPS sozinho",
         [prosa("Quem move é a ação que cada campus toma, e o que&nbsp;estava travado era a leitura da pesquisa. Nos semestres anteriores o&nbsp;relatório chegava e não&nbsp;virava plano.",
                "Com o mapa, os&nbsp;16 campus construíram planos a&nbsp;partir do&nbsp;mesmo material, e a nota geral saiu de&nbsp;33 negativos para 15 positivos no&nbsp;ciclo seguinte."), escala()]),
        ("grafico", "Resultado", "Sobrou tempo justamente onde o&nbsp;produto precisa de&nbsp;experimentação",
         [prosa("E muito mais experimento rodando, que é o que decide a qualidade da conversa em produção.", "Design segue revisando tudo que vira PR."), barras_processo()]),
    ])
    return c.cabeca(P_SUB, "Gráfico · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "grafico.html") + corpo + c.rodape(P_SUB, "grafico.html")


# ── Onda 5, com as telas e o texto das páginas publicadas ────

FIGMA_INPULSE = "https://www.figma.com/proto/w5TixfaNOqjwjYoY8hZ0cg/Painel-Longitudinal---Aluno?page-id=2891%3A23975&amp;node-id=2891-27267&amp;p=f&amp;viewport=521%2C589%2C0.07&amp;t=N9ol2L7UQFaCxwX8-1&amp;scaling=scale-down&amp;content-scaling=fixed&amp;starting-point-node-id=2891%3A27267"
EMBED_INPULSE = "https://embed.figma.com/proto/w5TixfaNOqjwjYoY8hZ0cg/Painel-Longitudinal---Aluno?page-id=2891%3A23975&amp;node-id=2891-27267&amp;starting-point-node-id=2891%3A27267&amp;scaling=scale-down&amp;content-scaling=fixed&amp;embed-host=share"
FIGMA_MAPA = "https://www.figma.com/proto/8fvE9ztg50OQFqWIqGfH3y/Mapa-de-Experie%CC%82ncia-Estudante-Medicina?page-id=221%3A2&amp;node-id=288-1762&amp;starting-point-node-id=288%3A1762&amp;t=rEOOuyzD3vuwNv1m-1"

TELAS_MAPA = [
    ("jB0FYWxzKTWaMHwYRuFkT0OR8", "O tabuleiro do mapa, com as 12 etapas da graduação distribuídas do START ao FINISH.", "O tabuleiro, do primeiro ao último&nbsp;semestre"),
    ("2u2l4cvOcOdO1jQGPl637PRYmWI", "Uma etapa aberta sobre o tabuleiro, com o achado da pesquisa e a régua de sentimento na base da tela.", "Uma etapa aberta, com a régua de&nbsp;sentimento"),
    ("Gt20MHEWr6seNOXMahLIqb4plQ", "Visão ampla institucional, com experiência, sugestões, apps e oportunidades cruzados com os pares de etapas.", "Visão ampla, lado&nbsp;institucional"),
    ("3IY6aXgfkDIxVCej0xa2DWhplw", "Visão ampla pessoal, com mental, físico, financeiro, futuro e dores cruzados com os pares de etapas.", "Visão ampla, lado&nbsp;pessoal"),
    ("D6BfM2dEe92QhBtCV7Q9lTCTu0", "Gráfico de sentimento com três linhas, financeiro, físico e mental, ao longo dos seis pares de etapas.", "O sentimento por eixo ao longo do&nbsp;curso"),
]


def tela(id_, alt, larg=4320, alt_=3072):
    return f'<img src="https://framerusercontent.com/images/{id_}.png" alt="{alt}" width="{larg}" height="{alt_}" loading="lazy" decoding="async">'


def moldura_prototipo():
    return f"""<figure class="figure" data-variant="moldura" data-formato="retrato" data-revelar>
  <div class="figure__quadro"><iframe src="{EMBED_INPULSE}" title="Protótipo do aplicativo Inpulse" allowfullscreen loading="lazy"></iframe></div>
  <figcaption class="figure__legenda">Navegue pelo app aqui mesmo, ou abra o protótipo em&nbsp;tela&nbsp;cheia.</figcaption>
</figure>
<a class="link" data-variant="externo" href="{FIGMA_INPULSE}" target="_blank" rel="noopener">Abrir o protótipo completo <i aria-hidden="true">↗</i></a>"""


def moldura_tela():
    id_, alt, leg = TELAS_MAPA[1]
    return f"""<figure class="figure" data-variant="moldura" data-revelar>
  <div class="figure__quadro">{tela(id_, alt)}</div>
  <figcaption class="figure__legenda">{leg[0].upper() + leg[1:]}</figcaption>
</figure>"""


def galeria():
    itens = "".join(
        f'<li><figure><div class="figure__quadro">{tela(id_, alt)}</div><figcaption class="figure__legenda"><span class="t-rotulo">Fig. 0{n}</span>{leg}</figcaption></figure></li>'
        for n, (id_, alt, leg) in enumerate(TELAS_MAPA, 1))
    return f"""<div class="figure" data-variant="galeria" data-abertura data-revelar>
  <ol class="figure__lista">{itens}</ol>
</div>
<a class="link" data-variant="externo" href="{FIGMA_MAPA}" target="_blank" rel="noopener">Abrir o mapa completo <i aria-hidden="true">↗</i></a>"""


def sangria():
    return f"""<figure class="figure" data-variant="sangria" data-revelar>
  <div class="figure__quadro">{tela("aV4KtUaueCwZ17TJ4mz299XAw", "Telas do aplicativo Inpulse, com o boletim por complexo temático, o calendário acadêmico e a situação atual do aluno.", 1600, 900)}</div>
</figure>"""


STATS_INPULSE = [
    ("celular", "93%", "dos alunos acessando o&nbsp;app"),
    ("calendario", "45%", "acessando ao menos uma&nbsp;vez por&nbsp;dia"),
    ("check", "4,8", "de CSAT na&nbsp;primeira versão"),
    ("grafico", "−25%", "de recuperação por&nbsp;semestre por&nbsp;aluno"),
]


def amostra_imagem():
    return amostra("Imagem", "".join([
        item("Moldura, retrato, com o protótipo do Inpulse", 'data-variant="moldura" data-formato="retrato"', moldura_prototipo()),
        item("Moldura, com uma tela do Mapa de experiência", 'data-variant="moldura"', moldura_tela()),
        item("Galeria, com abertura, as cinco telas do Mapa", 'data-variant="galeria" data-abertura', galeria()),
        item("Sangria, as telas do Inpulse", 'data-variant="sangria"', sangria()),
    ]))


def palco_imagem():
    stats = "".join(
        f'<div class="card" data-tamanho="meio">{c.icone(P_SUB, ic, 48)}<div class="stat"><span class="stat__valor">{v}</span><p class="stat__frase">{f}</p></div></div>'
        for ic, v, f in STATS_INPULSE)
    corpo = caso_palco("Neste palco", [
        ("lupa", "Descoberta", "Qual a&nbsp;melhor maneira de&nbsp;entregar um&nbsp;boletim que&nbsp;o&nbsp;aluno use",
         [prosa("Depois de analisar o NPS, as pesquisas que o time já tinha feito e um dia na vida conduzido por um dos designers, ficou claro que esse aluno está sempre em movimento e precisava de algo de fácil acesso, que estivesse com ele o&nbsp;tempo todo.",
                "Depois de várias sessões de cocriação com&nbsp;a&nbsp;área acadêmica e&nbsp;com&nbsp;todo o&nbsp;time de produto e desenvolvimento, saímos com&nbsp;um&nbsp;protótipo navegável de alta fidelidade, pronto para&nbsp;validação."), moldura_prototipo()]),
        ("rota", "Solução", "Um&nbsp;tabuleiro com&nbsp;as&nbsp;12 etapas da&nbsp;graduação",
         [prosa("Cada instituição recebeu um mapa interativo para transitar por&nbsp;toda a jornada do estudante, com visualização por&nbsp;semestre e por&nbsp;eixo da vida do&nbsp;aluno.",
                "O mesmo material resume a variação de sentimento entre semestres e&nbsp;as&nbsp;palavras-chave que aparecem em cada cruzamento de&nbsp;eixo e&nbsp;etapa."), galeria()]),
        ("grafico", "Resultado", "Agora o&nbsp;aluno tem mais tempo para&nbsp;estudar",
         [prosa("O aluno passou a ter acesso rápido e&nbsp;real à&nbsp;informação de&nbsp;aula, com&nbsp;as&nbsp;notas centralizadas num lugar&nbsp;só.",
                "A primeira versão já mostrou números de&nbsp;engajamento altos no&nbsp;primeiro semestre de&nbsp;lançamento."), sangria(),
          f'<div class="cards" data-layout="mosaico" data-revelar>{stats}</div>']),
    ])
    return c.cabeca(P_SUB, "Imagem · Palco da vitrine", ESTILO) + c.cabecalho(P_SUB, "imagem.html") + corpo + c.rodape(P_SUB, "imagem.html")


def na_home(pagina, aqui):
    """A Home tem o lime, e o item Home do menu e do Rodapé é a página
    atual, apontando para o próprio palco."""
    pagina = pagina.replace('data-acento="azul"', 'data-acento="lime"', 1)
    pagina = pagina.replace(f'class="sheet__item" href="{P_SUB}index.html"', f'class="sheet__item" href="{aqui}" aria-current="page"')
    return pagina.replace(f'<a class="link" href="{P_SUB}index.html">Home</a>', f'<a class="link" href="{aqui}" aria-current="page">Home</a>')


def amostra_hero():
    return na_home(amostra("Hero da Home", "".join([
        item("Com movimento, na chegada e na rolagem", ".hero", c.hero(P_SUB) + '<p><a class="link" href="hero.html">Rever a chegada</a></p>'),
        item("Parado, sem JS ou com movimento reduzido", "data-parado", c.hero(P_SUB, parado=True, id_="hero-frase-parado")),
        '<div class="amostra__rolar" aria-hidden="true"></div>',
    ])), "hero.html")


def amostra_cartao_de_caso():
    return na_home(amostra("Cartão de caso", item("Lista de casos, na ordem da fila", 'data-variant="caso" data-acento', c.lista_casos(P_SUB, revelar=False))), "cartao-de-caso.html")


def palco_home(aqui):
    corpo = f"""
<main id="conteudo" class="container">
  {c.hero(P_SUB)}
  {c.lista_casos(P_SUB)}
</main>"""
    titulo = "Hero da Home" if aqui == "hero.html" else "Cartão de caso"
    return na_home(c.cabeca(P_SUB, f"{titulo} · Palco da vitrine") + c.cabecalho(P_SUB, None, "Pular para o conteúdo") + corpo + c.rodape(P_SUB, None), aqui)


# Peça, altura do quadro da amostra e a página.
AMOSTRAS = {
    "cabecalho": (560, amostra_cabecalho),
    "sumario": (720, amostra_sumario),
    "rodape": (600, amostra_rodape),
    "link": (720, amostra_link),
    "etiqueta": (640, amostra_etiqueta),
    "destaque": (900, amostra_destaque),
    "passos": (900, amostra_passos),
    "antes-e-depois": (900, amostra_antes_e_depois),
    "grafico": (900, amostra_grafico),
    "imagem": (900, amostra_imagem),
    "hero": (900, amostra_hero),
    "cartao-de-caso": (900, amostra_cartao_de_caso),
}


PALCOS = {"cabecalho": palco_cabecalho, "sumario": palco_sumario, "rodape": palco_rodape,
          "link": palco_link, "etiqueta": palco_etiqueta, "destaque": palco_destaque,
          "passos": palco_passos, "antes-e-depois": palco_antes_e_depois, "grafico": palco_grafico,
          "imagem": palco_imagem, "hero": lambda: palco_home("hero.html"), "cartao-de-caso": lambda: palco_home("cartao-de-caso.html")}


# ── A vitrine ────────────────────────────────────────────────

def sumario():
    itens = "".join(
        f'<li><a class="sumario__item" href="#{i}">{c.icone(P, ic, 32)}<span class="sumario__num">0{n}</span><span class="sumario__nome">{nome}</span></a></li>'
        for n, (i, ic, nome, _) in enumerate(ONDAS, 1))
    marcas = '<span class="sumario__seg" aria-hidden="true"></span>' * len(ONDAS)
    return f'''<nav class="sumario" data-sumario aria-label="Nesta vitrine">
    <p class="t-rotulo sumario__titulo">Nesta vitrine</p>
    <ol class="sumario__lista" id="sumario-lista">{itens}</ol>
    <button class="sumario__botao" type="button" aria-expanded="false" aria-controls="sumario-lista" hidden><span class="sr">Ondas da vitrine</span>{marcas}</button>
    <span class="sumario__aviso" aria-hidden="true"></span>
  </nav>'''


def frase_da_ficha(arq):
    if arq in SEM_FICHA:
        frase = SEM_FICHA[arq][1]
        return frase[0].upper() + frase[1:]
    linha = (FICHAS / f"{arq}.md").read_text().split("\n")[2]
    frase = linha.split(" · ", 1)[1]
    return inline(frase[0].upper() + frase[1:])


def frase_da_variante(arq):
    """A frase da peça que é variante de outro componente."""
    return {"cartao-de-caso": "Um caso na Lista de casos da Home, com o número que ele promete e o caminho para a&nbsp;página. É a variante <code>caso</code> do&nbsp;Cartão."}[arq]


def palco(src, titulo, largura, altura):
    """O quadro com os botões de largura. O vitrine.js põe a página na
    largura escolhida e reduz quando ela não cabe na coluna."""
    botoes = "".join(
        f'<button class="button" type="button" data-variant="outline" data-largura="{w}" aria-pressed="false">{w}</button>'
        for w in (390, 768, 1440))
    return f"""<div class="palco" data-palco data-largura-inicial="{largura}" data-altura="{altura}">
          <div class="palco__barra">
            <div class="palco__larguras" role="group" aria-label="Largura do quadro, em pixels">{botoes}</div>
            <a class="link" data-variant="seguir" href="{src}">Abrir em página inteira <i aria-hidden="true">→</i></a>
          </div>
          <div class="palco__janela"><iframe src="{src}" title="{titulo}" loading="lazy"></iframe></div>
        </div>"""


def peca(arq, nome, largura, testar):
    altura, _ = AMOSTRAS[arq]
    return f"""
      <div class="peca" id="peca-{arq}" data-revelar>
        <h3>{nome}</h3>
        <p class="t-apoio prosa">{frase_da_ficha(arq) if arq not in FICHA_DE else frase_da_variante(arq)}</p>
        {palco(f"amostra/{arq}.html", f"{nome}, todas as formas", largura, altura)}
        <a class="link" data-variant="seguir" href="fichas/{FICHA_DE.get(arq, (arq,))[0]}.html">Ver na página e ler a ficha {DO.get(arq, "do")} {FICHA_DE.get(arq, (arq, nome))[1]} <i aria-hidden="true">→</i></a>{ESTUDOS.get(arq, "")}
      </div>"""


def onda_futura(n):
    i, _, nome, traz = ONDAS[n - 1]
    return f"""
    <section class="section" id="{i}" aria-labelledby="{i}-rotulo">
      <p class="section__rotulo t-rotulo" id="{i}-rotulo" data-revelar>0{n} · {nome}</p>
      <p class="prosa" data-revelar>{traz} Chega na Onda&nbsp;{n}.</p>
    </section>"""


def main():
    return f"""
<main id="conteudo" class="container caso">
  {sumario()}

  <div>
    <header class="topo">
      <div class="topo__texto"><h1 class="t-display">Vitrine do Jeff&nbsp;DS</h1><p class="t-sub">Cada peça do site ao vivo, onda a&nbsp;onda, com a ficha ao&nbsp;lado.</p></div>
    </header>

    <section class="section" id="casca" aria-labelledby="casca-titulo">
      <p class="section__rotulo t-rotulo" data-revelar>01 · Casca</p>
      <h2 class="t-titulo" id="casca-titulo" data-revelar>A casca que toda página&nbsp;divide</h2>
      <div class="prosa" data-revelar><p>Cada peça aparece sozinha, com todas as formas e o nome de cada uma. Troque a largura do quadro e use mouse, toque e teclado. A peça aplicada numa página fica na ficha dela. A própria vitrine também usa as três&nbsp;peças.</p></div>
      {"".join(peca(*x) for x in CASCA)}
    </section>

    <section class="section" id="acao-e-texto" aria-labelledby="acao-titulo">
      <p class="section__rotulo t-rotulo" data-revelar>02 · Ação e texto</p>
      <h2 class="t-titulo" id="acao-titulo" data-revelar>O que leva, o que nomeia e o que&nbsp;fica</h2>
      <div class="prosa" data-revelar><p>O Link leva a outro lugar, a Etiqueta nomeia e o Destaque separa o trecho que a Seção existe para carregar. O Botão já estava pronto desde o modelo de Caso e aparece nas páginas das&nbsp;fichas.</p></div>
      {"".join(peca(*x) for x in ACAO)}
    </section>

    <section class="section" id="sequencia-e-comparacao" aria-labelledby="sequencia-titulo">
      <p class="section__rotulo t-rotulo" data-revelar>03 · Sequência</p>
      <h2 class="t-titulo" id="sequencia-titulo" data-revelar>O que vem em&nbsp;ordem e o&nbsp;que&nbsp;mudou</h2>
      <div class="prosa" data-revelar><p>O Antes e depois ganha a citação e o confronto. O Passos segue a direção 3 do estudo, Adesivos, e o estudo com as seis direções continua no link logo depois da&nbsp;amostra.</p></div>
      {"".join(peca(*x) for x in SEQUENCIA)}
    </section>

    <section class="section" id="dados" aria-labelledby="dados-titulo">
      <p class="section__rotulo t-rotulo" data-revelar>04 · Dados</p>
      <h2 class="t-titulo" id="dados-titulo" data-revelar>O valor que se lê ao&nbsp;lado de&nbsp;outro</h2>
      <div class="prosa" data-revelar><p>O Gráfico em três formas, com os números reais dos casos. Cada amostra está no acento do caso de onde o número vem, para ver o Gráfico no lime, no azul e no&nbsp;verde.</p></div>
      {"".join(peca(*x) for x in DADOS)}
    </section>

    <section class="section" id="midia-hero-e-home" aria-labelledby="midia-titulo">
      <p class="section__rotulo t-rotulo" data-revelar>05 · Mídia, hero e Home</p>
      <h2 class="t-titulo" id="midia-titulo" data-revelar>OO&nbsp;que se&nbsp;vê, e&nbsp;a&nbsp;porta de&nbsp;entradanbsp;que seO&nbsp;que se&nbsp;vê, e&nbsp;a&nbsp;porta de&nbsp;entradanbsp;vê eO&nbsp;que se&nbsp;vê, e&nbsp;a&nbsp;porta de&nbsp;entradanbsp;por onde seO&nbsp;que se&nbsp;vê, e&nbsp;a&nbsp;porta de&nbsp;entradanbsp;entra</h2>
      <div class="prosa" data-revelar><p>A Imagem em três formas, com as telas reais do Inpulse e do Mapa de experiência. O hero, em que a frase é a própria cena e vai do rascunho à página pronta, e o Cartão de caso, que monta a Lista de casos da Home. As três foram aprovadas e têm&nbsp;ficha.</p></div>
      {"".join(peca(*x) for x in MIDIA)}
    </section>
{"".join(onda_futura(n) for n in range(6, len(ONDAS) + 1))}
  </div>
</main>"""


if __name__ == "__main__":
    (AQUI / "palco").mkdir(exist_ok=True)
    (AQUI / "amostra").mkdir(exist_ok=True)
    for arq, (_, fazer) in AMOSTRAS.items():
        (AQUI / "amostra" / f"{arq}.html").write_text(fazer())
    (AQUI / "fichas").mkdir(exist_ok=True)
    for arq, fazer in PALCOS.items():
        (AQUI / "palco" / f"{arq}.html").write_text(fazer())
    for md in sorted(FICHAS.glob("*.md")):
        if not md.name.startswith("_"):
            (AQUI / "fichas" / f"{md.stem}.html").write_text(pagina_ficha(md.stem))
    for arq in SEM_FICHA:
        (AQUI / "fichas" / f"{arq}.html").write_text(pagina_ficha(arq))
    vitrine = (c.cabeca(P, "Vitrine · Jeff DS no site", ESTILO) + c.CARGA + c.cabecalho(P, None, "Pular para a vitrine")
               + main() + c.rodape(P, None))
    vitrine = vitrine.replace("</body>", '<script src="vitrine.js"></script>\n</body>')
    (AQUI / "index.html").write_text(vitrine)
