"""Ícones adesivo do Jeff DS para o site.

Duas fontes. `kit/` guarda uma cópia dos ícones do Jeff DS (grupo Icones do
artifact), desenhados em lime. `NOVOS`, abaixo, são ícones que o site pediu e
o kit não tinha, desenhados na mesma gramática:

- grid de 48, viewBox -2 -2 54 54;
- sombra sólida preta, as mesmas formas deslocadas 2,6;
- corpo no acento, detalhes em papel, contorno de 2,6 em tinta;
- traços soltos (linhas internas, brilho) por cima de tudo.

Gera `assets/ds/icones/<nome>-<acento>.svg` para os três acentos, porque um SVG
servido por <img> não enxerga variável de CSS e cada caso tem o seu acento.

Uso: python3 ds/icones/gerar.py
"""
from pathlib import Path

AQUI = Path(__file__).parent
SAIDA = AQUI.parents[1] / "assets/ds/icones"
ACENTOS = {"lime": "#edfe5e", "azul": "#bed4fb", "verde": "#31e992"}
PAPEL = "#f9f9f7"
TRACO = 'stroke="#000" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"'

# nome: (formas no acento, formas em papel, traços soltos)
NOVOS = {
    # Três camadas empilhadas, a de cima no acento.
    "camadas": (
        ['<path d="M5 17.5 24 8l19 9.5L24 27Z"/>'],
        ['<path d="M5 31.5 24 22l19 9.5L24 41Z"/>', '<path d="M5 24.5 24 15l19 9.5L24 34Z"/>'],
        [],
    ),
    # A fronteira de entrada: um arco com a porta aberta.
    "fronteira": (
        ['<path d="M10 42V21a14 14 0 0 1 28 0v21Z"/>'],
        ['<path d="M17 42V22a7 7 0 0 1 14 0v20Z"/>'],
        ['<path d="M5 42h38M27 32h.5"/>'],
    ),
    # Celular com uma conversa na tela: a origem Instagram, sem a marca.
    "celular": (
        ['<rect x="13" y="4" width="22" height="40" rx="5"/>'],
        ['<rect x="17" y="10" width="14" height="24" rx="2"/>'],
        ['<path d="M21 39h6M20.5 16h7M20.5 21h4.5M23 27h5"/>'],
    ),
    # Megafone: o disparo automático.
    "megafone": (
        ['<path d="M7 19h7l17-9v28l-17-9H7a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2Z"/>'],
        ['<path d="M13 29l3 11h6l-2.5-11Z"/>'],
        ['<path d="M36 18c2.5 3 2.5 9 0 12M40.5 14c4.5 5 4.5 15 0 20"/>'],
    ),
    # Escudo com verificação: o agente para e confere antes de agir.
    "verifica": (
        ['<path d="M24 5l15 6v11c0 10-6.5 17-15 21-8.5-4-15-11-15-21V11Z"/>'],
        [],
        ['<path d="M16.5 24l5.5 5.5 10-11"/>'],
    ),
    # Rota com dois pontos: a jornada mapeada por origem.
    "rota": (
        ['<path d="M14 5a8 8 0 0 1 8 8c0 7-8 14-8 14S6 20 6 13a8 8 0 0 1 8-8Z"/>'],
        ['<path d="M34 19a7 7 0 0 1 7 7c0 6-7 12-7 12s-7-6-7-12a7 7 0 0 1 7-7Z"/>'],
        ['<path d="M14 31c0 7 6 11 13 11" stroke-dasharray="1 5"/>', '<circle cx="14" cy="13" r="2.5"/>', '<circle cx="34" cy="26" r="2"/>'],
    ),
}


def montar(corpo, papel, linhas, acento):
    sombra = "".join(corpo + papel)
    return (
        '<svg width="192" height="192" viewBox="-2 -2 54 54" fill="none" xmlns="http://www.w3.org/2000/svg">'
        f'<g transform="translate(2.6 2.6)" fill="#000" {TRACO}>{sombra}</g>'
        f'<g fill="{acento}" {TRACO}>{"".join(corpo)}</g>'
        f'<g fill="{PAPEL}" {TRACO}>{"".join(papel)}</g>'
        f'<g {TRACO}>{"".join(linhas)}</g>'
        "</svg>"
    )


SAIDA.mkdir(parents=True, exist_ok=True)
n = 0
for arq in sorted((AQUI / "kit").glob("*.svg")):
    base = arq.read_text()
    for nome, cor in ACENTOS.items():
        (SAIDA / f"{arq.stem}-{nome}.svg").write_text(base.replace("#edfe5e", cor))
        n += 1
for icone, (corpo, papel, linhas) in NOVOS.items():
    for nome, cor in ACENTOS.items():
        (SAIDA / f"{icone}-{nome}.svg").write_text(montar(corpo, papel, linhas, cor))
        n += 1
print(n, "ícones em", SAIDA)
