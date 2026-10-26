"""A Home, montada só com os componentes do Jeff DS.

O hero e a Lista de casos, na receita da Home (ds/RECEITAS.md). O desenho
dos dois mora em ds/prova/comum.py, que a vitrine também usa. A Home tem o
lime, e a cortina do Carregamento não monta a tela na chegada, porque o
hero faz esse papel (decisão 17 da Fase 6). Ela só desce ao sair.

Uso: python3 ds/prova/home.py
Escreve index.html na raiz do repositório.
"""
from pathlib import Path
import comum as c

RAIZ = Path(__file__).resolve().parents[2]
ARQUIVO = "index.html"
TITULO_PAGINA = "Jeff Maia · Product Design Manager"
# A descrição para a busca é a linha de apoio do hero, sem os espaços rígidos.
DESCRICAO = c.HERO_APOIO.replace("&nbsp;", " ")
CARGA = c.CARGA.replace('<div class="carga" aria-hidden="true">', '<div class="carga" aria-hidden="true" data-sem-chegada hidden>', 1)


def pagina():
    corpo = f"""
<main id="conteudo" class="container">
  {c.hero("")}
  {c.lista_casos("")}
</main>"""
    return (c.cabeca("", TITULO_PAGINA, descricao=DESCRICAO, acento="lime", script=c.HERO_ESPERA) + CARGA
            + c.cabecalho("", ARQUIVO, "Pular para o conteúdo", atual=ARQUIVO) + corpo + c.rodape("", ARQUIVO, atual=ARQUIVO))


if __name__ == "__main__":
    (RAIZ / ARQUIVO).write_text(pagina())
    print("ok")
