"""As prévias do grupo Site no artifact do Jeff DS, feitas das amostras da vitrine.

O quadro de cada card do artifact já traz o próprio <head>, com os tokens e o
bundle.css do sistema, e da prévia aproveita só um elemento raiz e um <script>.
Por isso cada prévia leva tudo dentro do elemento raiz: os tokens e os
componentes do site, o estilo da vitrine, o acento da página e os ícones como
data URI. O comportamento vem num <script> só, com o componentes.js inteiro.

A prévia é a amostra da vitrine, a peça sozinha com todas as formas. O que
você aprovou na vitrine é o que vai para o artifact.

Uso: python3 ds/vitrine/artifact.py <pasta>
Escreve <pasta>/components/Site<Nome>/preview.html para cada amostra.
"""
from pathlib import Path
import base64
import re
import sys

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
sys.path.insert(0, str(AQUI))
import gerar as g  # noqa: E402

# Amostra, nome no artifact, grupo, altura e a frase do card.
PECAS = [
    ("cabecalho", "SiteCabecalho", "Site · Casca", 600, "A barra fixa com a marca e o botão Menu. Abra o menu para ver os itens chegarem um a um."),
    ("sumario", "SiteSumario", "Site · Casca", 2200, "A coluna fixa com as Seções do caso. Abaixo de 1100px vira o trilho na borda direita."),
    ("rodape", "SiteRodape", "Site · Casca", 600, "A parada de tinta que fecha toda página. Omnichat marcada como a página atual."),
    ("link", "SiteLink", "Site · Ação e texto", 900, "No meio do texto sem variante, e sozinho com a seta que diz a direção. Na tinta, sublinhado e foco em papel."),
    ("etiqueta", "SiteEtiqueta", "Site · Ação e texto", 800, "O grupo do Topo, as três variantes, com ícone e na superfície tinta."),
    ("destaque", "SiteDestaque", "Site · Ação e texto", 1600, "Quatro formas. Frase no papel, nota, atrito e a frase na tinta, que é a parada escura da página."),
    ("passos", "SitePassos", "Site · Sequência", 3800, "Cada etapa num Cartão com o adesivo no canto. Sequência, par, estágios, funil, trilha e ritos."),
    ("antes-e-depois", "SiteAntesDepois", "Site · Sequência", 1900, "A conversa, a citação em Fraunces e o confronto como tabela, com o depois no acento."),
]

TOKENS = (RAIZ / "assets/ds/tokens.css").read_text()
COMPONENTES = (RAIZ / "assets/ds/componentes.css").read_text()
SCRIPT = (RAIZ / "assets/ds/componentes.js").read_text()
for nome, texto in (("tokens.css", TOKENS), ("componentes.css", COMPONENTES), ("componentes.js", SCRIPT)):
    if re.search(r"</style|</script|<!--", texto, re.I):
        sys.exit(f"{nome} tem uma sequência que fecharia o elemento inline.")


def data_uri(caminho):
    arq = RAIZ / caminho
    return "data:image/svg+xml;base64," + base64.b64encode(arq.read_bytes()).decode()


def corpo(html):
    """O miolo do <body> da amostra, sem scripts e com as imagens embutidas."""
    inicio = html.index(">", html.index("<body")) + 1
    miolo = html[inicio:html.rindex("</body>")]
    miolo = re.sub(r"<script\b[^>]*>.*?</script>", "", miolo, flags=re.S)
    miolo = re.sub(r'src="(?:\.\./)+(assets/ds/[^"]+\.svg)"', lambda m: f'src="{data_uri(m.group(1))}"', miolo)
    # Os links levam a páginas do site, que não existem no artifact.
    miolo = re.sub(r'href="(?:\.\./)+[^"#]*"', 'href="#"', miolo)
    return miolo.strip()


def previa(arq, nome, grupo, altura, frase):
    _, fazer = g.AMOSTRAS[arq]
    return f"""<!-- @dsCard group="{grupo}" height={altura} width=1200 subtitle="{frase}" -->
<!doctype html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>{nome}</title></head>
<body>
<div class="site-previa" data-acento="azul">
<style>
{TOKENS}
{COMPONENTES}
{g.ESTILO}
.site-previa {{ min-height: 100%; background: var(--background); color: var(--foreground); font-family: var(--font-texto); font-size: var(--text-corpo); line-height: var(--leading-corpo); }}
</style>
{corpo(fazer())}
</div>
<script>
document.documentElement.classList.add("js");
{SCRIPT}
</script>
</body>
</html>
"""


if __name__ == "__main__":
    saida = Path(sys.argv[1])
    for arq, nome, grupo, altura, frase in PECAS:
        destino = saida / "components" / nome / "preview.html"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(previa(arq, nome, grupo, altura, frase))
        print(f"{nome}: {destino.stat().st_size // 1024} KB")
