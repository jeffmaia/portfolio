"""Ilustrações do caso Omnichat, na gramática das cenas do Jeff DS.

As cenas do kit (pergunta, quadro, escada, mesa, conversa) têm três regras.
A moldura é um arco, casa ou círculo no acento, com uma trama de pontos leve.
As pessoas não têm contorno: são traços grossos de cor. A linha preta é só
dos objetos e do chão.

Duas ilustrações, as duas presas ao indicador do caso (24% para 32%).

- fronteira: o lead chega pelo celular e entra pelo arco, que é a fronteira de
  entrada. Do lado de dentro, as duas barras do antes e do depois, na
  proporção 24 para 32, com os 8 pontos de ganho em listras.
- salto: só as duas barras, com a pessoa passando de uma para a outra. É a
  versão que senta ao lado do número, quando o número é o herói.

Nenhuma das duas escreve o número: ele mora no HTML, que é quem o leitor de
tela ouve e quem tem a fonte certa. A ilustração só repete a proporção.

Uso: python3 ds/ilustracoes/gerar.py (depois de ds/icones/gerar.py)
"""
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ICONES = RAIZ / "assets/ds/icones"
SAIDA = RAIZ / "assets/ds/ilustracoes"

AZUL, LIME, PAPEL, PELE = "#bed4fb", "#edfe5e", "#f9f9f7", "#c98b5e"
OBJ = 'stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"'
ESCALA = 9  # px por ponto percentual nas barras

DEFS = (
    '<defs><pattern id="pontos" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.6" fill="#000"/></pattern>'
    '<pattern id="listras" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="5" height="14" fill="#000" opacity=".9"/></pattern></defs>'
)


def icone(nome, x, y, tam):
    """Um ícone adesivo dentro da cena, como as cenas do kit fazem."""
    svg = (ICONES / f"{nome}.svg").read_text()
    miolo = re.sub(r"^<svg[^>]*>|</svg>$", "", svg)
    return f'<g transform="translate({x} {y})"><svg width="{tam}" height="{tam}" viewBox="-2 -2 54 54" fill="none">{miolo}</svg></g>'


def barras(x, chao, larg, vao):
    """Antes (24) em papel, depois (32) no lime, e os 8 pontos em listras."""
    a, d = 24 * ESCALA, 32 * ESCALA
    xa, xd = x, x + larg + vao
    return (
        f'<rect x="{xa}" y="{chao - a}" width="{larg}" height="{a}" fill="{PAPEL}" {OBJ}/>'
        f'<rect x="{xd}" y="{chao - d}" width="{larg}" height="{d}" fill="{LIME}" {OBJ}/>'
        f'<rect x="{xd}" y="{chao - d}" width="{larg}" height="{d - a}" fill="url(#listras)" opacity=".85"/>'
        f'<rect x="{xd}" y="{chao - d}" width="{larg}" height="{d}" fill="none" {OBJ}/>'
        # O nível de antes atravessando as duas barras: é a régua do ganho.
        f'<path d="M{xa - 14} {chao - a}H{xd + larg + 14}" stroke="#000" stroke-width="2.5" stroke-dasharray="2 8" stroke-linecap="round"/>'
    )


def pessoa_andando(x, chao, celular=True):
    """A pessoa da cena escada, com os dois pés no chão e o celular na mão.
    Fora do arco o fundo é papel, então a calça vai no azul, como na cena conversa."""
    pe = lambda px, py: f'<path d="M{px - 12} {py - 4}h22a12 12 0 0 1 12 12v2H{px - 14}v-4a10 10 0 0 1 2-10Z" fill="#000"/>'
    braco_cel = (
        '<line x1="18" y1="-278" x2="50" y2="-236" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="50" y1="-236" x2="66" y2="-282" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<rect x="54" y="-322" width="26" height="42" rx="6" fill="#000"/>'
        f'<rect x="59" y="-315" width="16" height="24" rx="2" fill="{AZUL}"/>'
        f'<circle cx="66" cy="-282" r="10" fill="{PELE}"/>'
    ) if celular else (
        '<line x1="18" y1="-278" x2="40" y2="-224" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="40" y1="-224" x2="46" y2="-174" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<circle cx="46" cy="-174" r="10" fill="{PELE}"/>'
    )
    return (
        f'<g transform="translate({x} {chao})">'
        f'<polyline points="-4,-168 -18,-90 -30,-16" fill="none" stroke="{AZUL}" stroke-width="27" stroke-linejoin="round"/>'
        + pe(-30, -16) +
        '<line x1="-16" y1="-278" x2="-34" y2="-222" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="-34" y1="-222" x2="-40" y2="-172" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<circle cx="-40" cy="-172" r="10" fill="{PELE}"/>'
        f'<polyline points="6,-168 22,-90 30,-16" fill="none" stroke="{AZUL}" stroke-width="27" stroke-linejoin="round"/>'
        + pe(30, -16) +
        '<path d="M-34 -276q0-16 18-16h32q18 0 18 16l-6 116q-1 12-14 12h-28q-13 0-14-12Z" fill="#000"/>'
        f'<rect x="-7" y="-306" width="15" height="20" rx="4" fill="{PELE}"/>'
        '<g transform="translate(2 -320)">'
        '<path d="M-24 34c-6-22-6-42 4-54 10-10 32-8 40 4 2 4 3 8 3 12-10-4-20-4-28 0 0 14-2 28-6 40Z" fill="#2a1a12"/>'
        f'<circle r="22" fill="{PELE}"/><circle cx="21" cy="3" r="5" fill="{PELE}"/><circle cx="-6" cy="4" r="5" fill="{PELE}"/></g>'
        + braco_cel + "</g>"
    )


def pessoa_subindo(x, chao_tras, chao_frente):
    """A pose da cena escada: um pé no degrau de antes, o outro no de depois."""
    d = chao_tras - chao_frente
    pe = lambda px, py: f'<path d="M{px - 12} {py - 4}h22a12 12 0 0 1 12 12v2H{px - 14}v-4a10 10 0 0 1 2-10Z" fill="#000"/>'
    return (
        f'<g transform="translate({x} {chao_tras})">'
        f'<polyline points="-4,-168 -16,-86 -26,-16" fill="none" stroke="{PAPEL}" stroke-width="27" stroke-linejoin="round"/>'
        + pe(-26, -16) +
        '<line x1="-16" y1="-278" x2="-46" y2="-228" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="-46" y1="-228" x2="-66" y2="-178" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<circle cx="-66" cy="-178" r="10" fill="{PELE}"/>'
        f'<polyline points="6,-168 46,-{110 + d // 2} 44,-{d + 16}" fill="none" stroke="{PAPEL}" stroke-width="27" stroke-linejoin="round"/>'
        + pe(44, -(d + 16)) +
        '<path d="M-34 -276q0-16 18-16h32q18 0 18 16l-6 116q-1 12-14 12h-28q-13 0-14-12Z" fill="#000"/>'
        f'<rect x="-7" y="-306" width="15" height="20" rx="4" fill="{PELE}"/>'
        '<g transform="translate(2 -320)">'
        '<path d="M-24 34c-6-22-6-42 4-54 10-10 32-8 40 4 2 4 3 8 3 12-10-4-20-4-28 0 0 14-2 28-6 40Z" fill="#2a1a12"/>'
        f'<circle r="22" fill="{PELE}"/><circle cx="21" cy="3" r="5" fill="{PELE}"/><circle cx="-6" cy="4" r="5" fill="{PELE}"/></g>'
        '<line x1="18" y1="-278" x2="52" y2="-232" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="52" y1="-232" x2="82" y2="-262" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<circle cx="82" cy="-262" r="10" fill="{PELE}"/>'
        "</g>"
    )


def planta(x, chao, esc=0.85):
    return (
        f'<g transform="translate({x} {chao}) scale({esc})">'
        '<path d="M0-60C-30-90-34-130-10-170 0-130 4-95 0-60Z" fill="#31e992"/>'
        '<path d="M0-60C24-84 46-110 44-150 20-128 6-100 0-60Z" fill="#000"/>'
        '<path d="M0-60C-14-70-40-80-56-112-26-110-8-92 0-60Z" fill="#31e992"/>'
        f'<path d="M-24-62h48l-7 62h-34Z" fill="{PAPEL}" {OBJ}/></g>'
    )


def chao(x1, x2, y=600):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" {OBJ}/>'


def fronteira():
    arco = "M372 600V372A226 226 0 0 1 824 372V600Z"
    corpo = (
        f'<path d="{arco}" fill="{AZUL}"/><path d="{arco}" fill="url(#pontos)" opacity=".12"/>'
        + barras(470, 600, 120, 26)
        + icone("verifica-azul", 610, 214, 92)
        # O caminho do lead até a fronteira.
        + '<path d="M300 556C350 556 362 520 400 520" stroke="#000" stroke-width="2.5" stroke-dasharray="2 9" stroke-linecap="round"/>'
        + '<path d="M392 508l12 12-12 12" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'
        + pessoa_andando(232, 600)
        + icone("dialogo-azul", 150, 150, 104)
        + planta(78, 600)
        + chao(30, 870)
    )
    return f'<svg width="900" height="640" viewBox="0 0 900 640" fill="none" xmlns="http://www.w3.org/2000/svg" role="presentation">{DEFS}{corpo}</svg>'


def salto():
    a, d = 24 * ESCALA, 32 * ESCALA
    corpo = (
        f'<circle cx="320" cy="350" r="250" fill="{AZUL}"/><circle cx="320" cy="350" r="250" fill="url(#pontos)" opacity=".12"/>'
        + barras(150, 600, 160, 0)
        + pessoa_subindo(300, 600 - a, 600 - d)
        + icone("grafico-azul", 470, 150, 92)
        + chao(30, 610)
    )
    return f'<svg width="640" height="640" viewBox="0 0 640 640" fill="none" xmlns="http://www.w3.org/2000/svg" role="presentation">{DEFS}{corpo}</svg>'


SAIDA.mkdir(parents=True, exist_ok=True)
(SAIDA / "omnichat-fronteira.svg").write_text(fronteira())
(SAIDA / "omnichat-salto.svg").write_text(salto())
print("ok")
