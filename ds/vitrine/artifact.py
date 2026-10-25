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

# Amostra, nome no artifact, grupo, altura, a frase do card e, quando não é
# o azul do Omnichat, o acento da página.
PECAS = [
    ("cabecalho", "SiteCabecalho", "Site · Casca", 600, "A barra fixa com a marca e o botão Menu. Abra o menu para ver os itens chegarem um a um."),
    ("sumario", "SiteSumario", "Site · Casca", 2200, "A coluna fixa com as Seções do caso. Abaixo de 1100px vira o trilho na borda direita."),
    ("rodape", "SiteRodape", "Site · Casca", 600, "A parada de tinta que fecha toda página. Omnichat marcada como a página atual."),
    ("link", "SiteLink", "Site · Ação e texto", 900, "No meio do texto sem variante, e sozinho com a seta que diz a direção. Na tinta, sublinhado e foco em papel."),
    ("etiqueta", "SiteEtiqueta", "Site · Ação e texto", 800, "O grupo do Topo, as três variantes, com ícone e na superfície tinta."),
    ("destaque", "SiteDestaque", "Site · Ação e texto", 1600, "Quatro formas. Frase no papel, nota, atrito e a frase na tinta, que é a parada escura da página."),
    ("passos", "SitePassos", "Site · Sequência", 3800, "Cada etapa num Cartão com o adesivo no canto. Sequência, par, estágios, funil, trilha e ritos."),
    ("antes-e-depois", "SiteAntesDepois", "Site · Sequência", 1900, "A conversa, a citação em Fraunces e o confronto como tabela, com o depois no acento."),
    ("grafico", "SiteGrafico", "Site · Dados", 1600, "Barras, pilhas e escala, cada uma no acento do caso de onde vem o número. O valor se distingue pelo tom, cheio, trama ou vazio."),
    ("imagem", "SiteImagem", "Site · Mídia e Home", 3800, "Moldura com o protótipo do Inpulse, a galeria das cinco telas do Mapa e a sangria das telas do Inpulse."),
    ("hero", "SiteHero", "Site · Mídia e Home", 2000, "A frase é a cena. Na chegada vai do rascunho à página pronta em uns 3s, e embaixo o fim parado.", "lime"),
    ("cartao-de-caso", "SiteCartaoCaso", "Site · Mídia e Home", 1500, "A Lista de casos da Home, um Cartão por caso, com o acento do caso só na base e as partes alinhadas lado a lado.", "lime"),
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
    # Rever a chegada do hero recarrega a amostra, e no card não há o que recarregar.
    miolo = re.sub(r'<p><a class="link" href="hero\.html">Rever a chegada</a></p>', "", miolo)
    return miolo.strip()


def previa(arq, nome, grupo, altura, frase, acento="azul"):
    _, fazer = g.AMOSTRAS[arq]
    return f"""<!-- @dsCard group="{grupo}" height={altura} width=1200 subtitle="{frase}" -->
<!doctype html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>{nome}</title></head>
<body>
<div class="site-previa" data-acento="{acento}">
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
    for arq, nome, grupo, altura, frase, *acento in PECAS:
        destino = saida / "components" / nome / "preview.html"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(previa(arq, nome, grupo, altura, frase, *acento))
        print(f"{nome}: {destino.stat().st_size // 1024} KB")
