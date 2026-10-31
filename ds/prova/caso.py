"""As páginas de caso, montadas só com os componentes do Jeff DS.

É o modelo de Caso, a variação 4 (sumário e mosaico). O Sumário, o Topo e a
casca são os mesmos em todo caso, e o miolo de cada um mora no módulo dele,
em ds/prova/casos/, com o texto da página. O miolo do Omnichat também serve
ao modelo, em ds/prova/variacoes/v4.html.

Uso: python3 ds/prova/caso.py
Escreve na raiz do repositório a página de cada caso de CASOS.
"""
from pathlib import Path
import comum as c
from casos import omnichat, mapa, inpulse, processo, design_system

RAIZ = Path(__file__).resolve().parents[2]

# Os casos já migrados para o Jeff DS.
CASOS = [omnichat, mapa, inpulse, processo, design_system]


def sumario(pre, d):
    itens = "".join(
        f'<li><a class="sumario__item" href="#{i}">{c.icone(pre, ic, 32, cor=d.ACENTO)}<span class="sumario__num">0{n}</span><span class="sumario__nome">{r}</span></a></li>'
        for n, (i, ic, r) in enumerate(d.SECOES, 1))
    marcas = '<span class="sumario__seg" aria-hidden="true"></span>' * len(d.SECOES)
    return f'''<nav class="sumario" data-sumario aria-label="Neste caso">
    <p class="t-rotulo sumario__titulo">Neste caso</p>
    <ol class="sumario__lista" id="sumario-lista">{itens}</ol>
    <button class="sumario__botao" type="button" aria-expanded="false" aria-controls="sumario-lista" hidden><span class="sr">Seções deste caso</span>{marcas}</button>
    <span class="sumario__aviso" aria-hidden="true"></span>
  </nav>'''


def topo(pre, d):
    antes, depois, frase = d.SALTO
    return f"""<header class="topo">
      <div class="topo__texto">{c.badges(lista=d.BADGES)}<h1 class="t-display">{d.TITULO}</h1><p class="t-sub">{d.LEAD}</p></div>
      <div class="card topo__ficha" data-variant="muted"><p class="t-rotulo card__titulo">Ficha do projeto</p>{c.ficha(d.FICHA)}</div>
      <div class="card topo__salto" data-variant="acento">{c.salto(antes=antes, depois=depois, frase=frase)}{c.ilustracao(pre, "salto", caso=d.CENA)}</div>
    </header>"""


def main(pre, d=omnichat):
    return f"""
<main id="conteudo" class="container caso">
  {sumario(pre, d)}

  <div>
    {topo(pre, d)}

    {d.corpo(pre)}
  </div>
</main>"""


def pagina(d):
    return (c.cabeca("", d.TITULO_PAGINA, descricao=d.DESCRICAO, acento=d.ACENTO) + c.CARGA
            + c.cabecalho("", d.ARQUIVO, atual=d.ARQUIVO) + main("", d) + c.rodape("", d.ARQUIVO, atual=d.ARQUIVO))


if __name__ == "__main__":
    for d in CASOS:
        (RAIZ / d.ARQUIVO).write_text(pagina(d))
    print("ok")
