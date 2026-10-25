"""Ilustrações dos casos, na gramática das cenas do Jeff DS.

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

No Mapa de experiência, presa ao indicador (−33 para +15).

- mapa-salto: o chão é o zero da escala. O antes é um poço de 33 pontos
  cavado abaixo dele, e o depois um degrau de 15 pontos acima, no lime,
  com a pessoa de pé em cima. A linha tracejada é o percurso de um para o
  outro, como no Gráfico `escala`.

No Inpulse, presa ao indicador (8 em 10 para 6 em 10 recuperações).

- inpulse-salto: as recuperações são folhas de prova empilhadas. O antes é
  uma pilha de oito folhas no papel, e o depois uma de seis no lime, com o
  contorno tracejado das duas que saíram. A aluna ao lado olha o celular,
  que é o app, com a tela no lime do depois.

No Processo com IA, preso ao indicador (Discovery de 2 meses para 1 semana).

- processo-salto: um calendário de parede com oito semanas, os dois meses
  do antes. Uma semana fica no lime, a do depois, e as outras sete só com o
  contorno tracejado, como as folhas que saíram no Inpulse. A pessoa ao
  lado olha o celular, e o robô é o Claude que fez o rascunho.

Nenhuma ilustração escreve o número: ele mora no HTML, que é quem o leitor de
tela ouve e quem tem a fonte certa. A ilustração só repete a proporção.

Uso: python3 ds/ilustracoes/gerar.py (depois de ds/icones/gerar.py)
"""
import re
import math
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ICONES = RAIZ / "assets/ds/icones"
SAIDA = RAIZ / "assets/ds/ilustracoes"

AZUL, LIME, PAPEL, PELE, VERDE = "#bed4fb", "#edfe5e", "#f9f9f7", "#c98b5e", "#31e992"
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


def pessoa_andando(x, chao, celular=True, calca=None, tela=None):
    """A pessoa da cena escada, com os dois pés no chão e o celular na mão.
    Fora do arco o fundo é papel, então a calça vai no azul, como na cena conversa.
    Dentro do arco ela vai no papel, como na cena escada."""
    calca, tela = calca or AZUL, tela or AZUL
    pe = lambda px, py: f'<path d="M{px - 12} {py - 4}h22a12 12 0 0 1 12 12v2H{px - 14}v-4a10 10 0 0 1 2-10Z" fill="#000"/>'
    braco_cel = (
        '<line x1="18" y1="-278" x2="50" y2="-236" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="50" y1="-236" x2="66" y2="-282" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<rect x="54" y="-322" width="26" height="42" rx="6" fill="#000"/>'
        f'<rect x="59" y="-315" width="16" height="24" rx="2" fill="{tela}"/>'
        f'<circle cx="66" cy="-282" r="10" fill="{PELE}"/>'
    ) if celular else (
        '<line x1="18" y1="-278" x2="40" y2="-224" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="40" y1="-224" x2="46" y2="-174" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<circle cx="46" cy="-174" r="10" fill="{PELE}"/>'
    )
    return (
        f'<g transform="translate({x} {chao})">'
        f'<polyline points="-4,-168 -18,-90 -30,-16" fill="none" stroke="{calca}" stroke-width="27" stroke-linejoin="round"/>'
        + pe(-30, -16) +
        '<line x1="-16" y1="-278" x2="-34" y2="-222" stroke="#000" stroke-width="22" stroke-linecap="round"/>'
        f'<line x1="-34" y1="-222" x2="-40" y2="-172" stroke="{PELE}" stroke-width="15" stroke-linecap="round"/>'
        f'<circle cx="-40" cy="-172" r="10" fill="{PELE}"/>'
        f'<polyline points="6,-168 22,-90 30,-16" fill="none" stroke="{calca}" stroke-width="27" stroke-linejoin="round"/>'
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


def percurso(ponta, c1, c2, fim, braco=18, abertura=38):
    """Uma curva tracejada que sai do vértice de uma seta. A seta aponta na
    direção em que a linha chega, e a linha entra pelo meio da abertura."""
    (px, py), (cx, cy) = ponta, c1
    d = math.hypot(px - cx, py - cy)
    ux, uy = (cx - px) / d, (cy - py) / d  # da ponta para trás, ao longo da linha
    def braco_em(g):
        a = math.radians(g)
        return px + braco * (ux * math.cos(a) - uy * math.sin(a)), py + braco * (ux * math.sin(a) + uy * math.cos(a))
    (ax, ay), (bx, by) = braco_em(abertura), braco_em(-abertura)
    return (f'<path d="M{px} {py}C{cx} {cy} {c2[0]} {c2[1]} {fim[0]} {fim[1]}" stroke="#000" stroke-width="2.5" stroke-dasharray="2 9" stroke-linecap="round"/>'
            f'<path d="M{ax:.1f} {ay:.1f}L{px} {py}L{bx:.1f} {by:.1f}" stroke="#000" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')


def mapa_salto():
    e = 4  # px por ponto de NPS
    zero, x_poco, x_degrau, larg = 460, 120, 320, 150
    fundo, topo = zero + 33 * e, zero - 15 * e
    corpo = (
        f'<circle cx="320" cy="350" r="250" fill="{AZUL}"/><circle cx="320" cy="350" r="250" fill="url(#pontos)" opacity=".12"/>'
        # O poço do antes, aberto em cima, cavado no chão.
        + f'<path d="M{x_poco} {zero}V{fundo}H{x_poco + larg}V{zero}" fill="{PAPEL}" {OBJ}/>'
        # O degrau do depois, no lime.
        + f'<rect x="{x_degrau}" y="{topo}" width="{larg}" height="{zero - topo}" fill="{LIME}" {OBJ}/>'
        # O percurso do fundo do poço até o alto do degrau. Ele é desenhado
        # a partir da ponta, para o primeiro traço cair no vértice da seta.
        + percurso((x_degrau + 20, topo - 30), (x_degrau - 30, topo - 90), (x_poco + larg / 2, zero - 150), (x_poco + larg / 2, fundo - 22))
        + pessoa_andando(x_degrau + larg / 2 + 10, topo, celular=False, calca=PAPEL)
        + icone("rota-azul", 500, 130, 92)
        # O chão é o zero, interrompido pela boca do poço.
        + chao(30, x_poco, zero) + chao(x_poco + larg, 610, zero)
    )
    return f'<svg width="640" height="640" viewBox="0 0 640 640" fill="none" xmlns="http://www.w3.org/2000/svg" role="presentation">{DEFS}{corpo}</svg>'


def pilha(x, chao, folhas, cor, saiu=0, larg=150, alt=24):
    """Folhas de prova empilhadas, com um leve desalinho. As que saíram
    ficam no topo só com o contorno tracejado."""
    desvio = [0, 6, -4, 3, -6, 4, -2, 5, -5, 2]
    out = ""
    for i in range(folhas + saiu):
        y, dx = chao - (i + 1) * alt, desvio[i % len(desvio)]
        if i < folhas:
            out += f'<rect x="{x + dx}" y="{y}" width="{larg}" height="{alt}" rx="4" fill="{cor}" {OBJ}/>'
            out += f'<path d="M{x + dx + 16} {y + alt / 2}H{x + dx + 64}" {OBJ}/>'
        else:
            out += f'<rect x="{x + dx}" y="{y}" width="{larg}" height="{alt}" rx="4" stroke="#000" stroke-width="2.5" stroke-dasharray="2 9" stroke-linecap="round"/>'
    return out


def inpulse_salto():
    corpo = (
        f'<circle cx="320" cy="350" r="250" fill="{VERDE}"/><circle cx="320" cy="350" r="250" fill="url(#pontos)" opacity=".12"/>'
        + pilha(92, 600, 8, PAPEL)
        + pilha(272, 600, 6, LIME, saiu=2)
        + pessoa_andando(500, 600, calca=PAPEL, tela=LIME)
        + icone("calendario-verde", 120, 130, 92)
        + chao(30, 610)
    )
    return f'<svg width="640" height="640" viewBox="0 0 640 640" fill="none" xmlns="http://www.w3.org/2000/svg" role="presentation">{DEFS}{corpo}</svg>'


def calendario(x, y, colunas=4, linhas=2, cel=64, vao=12, cheias=1):
    """Um calendário de parede, com as argolas em cima e uma célula por
    semana. As `cheias` primeiras ficam no lime e as outras tracejadas."""
    marg, cab = 24, 52
    larg = colunas * cel + (colunas - 1) * vao + 2 * marg
    alt = cab + linhas * cel + (linhas - 1) * vao + 2 * marg
    out = f'<rect x="{x}" y="{y}" width="{larg}" height="{alt}" rx="10" fill="{PAPEL}" {OBJ}/>'
    out += f'<path d="M{x} {y + cab}H{x + larg}" {OBJ}/>'
    for ax in (x + larg * 0.3, x + larg * 0.7):
        out += f'<rect x="{ax - 6}" y="{y - 18}" width="12" height="34" rx="6" fill="#000"/>'
    n = 0
    for l in range(linhas):
        for co in range(colunas):
            cx, cy = x + marg + co * (cel + vao), y + cab + marg + l * (cel + vao)
            if n < cheias:
                out += f'<rect x="{cx}" y="{cy}" width="{cel}" height="{cel}" rx="6" fill="{LIME}" {OBJ}/>'
            else:
                out += f'<rect x="{cx + 2}" y="{cy + 2}" width="{cel - 4}" height="{cel - 4}" rx="6" stroke="#000" stroke-width="2.5" stroke-dasharray="2 9" stroke-linecap="round"/>'
            n += 1
    return out


def processo_salto():
    corpo = (
        f'<circle cx="320" cy="350" r="250" fill="{LIME}"/><circle cx="320" cy="350" r="250" fill="url(#pontos)" opacity=".12"/>'
        + calendario(76, 250)
        + pessoa_andando(510, 600, calca=PAPEL)
        + icone("robo-lime", 440, 104, 92)
        + chao(30, 610)
    )
    return f'<svg width="640" height="640" viewBox="0 0 640 640" fill="none" xmlns="http://www.w3.org/2000/svg" role="presentation">{DEFS}{corpo}</svg>'


SAIDA.mkdir(parents=True, exist_ok=True)
(SAIDA / "omnichat-fronteira.svg").write_text(fronteira())
(SAIDA / "omnichat-salto.svg").write_text(salto())
(SAIDA / "mapa-salto.svg").write_text(mapa_salto())
(SAIDA / "inpulse-salto.svg").write_text(inpulse_salto())
(SAIDA / "processo-salto.svg").write_text(processo_salto())
print("ok")
