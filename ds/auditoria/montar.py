"""Escreve os documentos da Fase 1 a partir de resultado.json (feito por
auditar.mjs) e de pecas.json.

Saídas, todas em ds/:
  INVENTARIO.md        matriz peça por página, fusões, o que não aparece em toda largura
  CONTRASTE.md         a paleta do Jeff DS e o que ela muda nas páginas de hoje
  capturas/index.html  folha de revisão com as capturas das peças em 390, 768 e 1440

Uso: python3 ds/auditoria/montar.py [plano.html]
O plano.html é opcional: é o artifact do plano salvo em disco, e serve para
conferir a matriz medida contra a que o plano tinha.
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).parent
RAIZ = AQUI.parents[1]
pecas = json.loads((AQUI / "pecas.json").read_text())
r = json.loads((AQUI / "resultado.json").read_text())
PG = [("home", "H"), ("processo", "PR"), ("omnichat", "OM"), ("inpulse", "IN"), ("mapa", "MA")]
NOMES = {"home": "Home", "processo": "Processo com IA", "omnichat": "Omnichat", "inpulse": "Inpulse", "mapa": "Mapa de experiência"}


def slug(s):
    import unicodedata
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


# ---------------------------------------------------------------- matriz
def paginas_de(p):
    m = r["matriz"][p["nome"]]
    return [sig for pid, sig in PG if m.get(pid, 0) > 0]


# O plano tinha uma matriz escrita à mão. Confere contra a medida.
plano = {}
if len(sys.argv) > 1 and Path(sys.argv[1]).exists():
    html = Path(sys.argv[1]).read_text()
    for m in re.finditer(r'\["([^"]+)","[^"]*","([A-Z ]+)",\[', html):
        plano[m.group(1)] = set(m.group(2).split())

porques = json.loads((AQUI / "porques-contagem.json").read_text())

L = []
L.append("# Inventário fechado\n")
L.append(
    "Resultado da Fase 1. As páginas foram abertas em 390, 768 e 1440px, e cada peça foi procurada no HTML real pelo seletor de `ds/auditoria/pecas.json`. "
    "A matriz abaixo é medida, não copiada do plano. Para refazer tudo, rode `ds/auditoria/auditar.mjs` e depois `montar.py`.\n"
)
n_pecas = len(pecas)
n_nova = sum(1 for p in pecas if p.get("nova"))
L.append(f"São **{n_pecas} peças** nas cinco páginas do site, contra as 53 do plano. {n_nova} peça nova apareceu na varredura (Contêiner de página). "
         "As classes que o plano agrupava como peças já cobrem 100% do HTML: nenhum elemento das cinco páginas ficou sem peça.\n")

L.append("## Matriz peça por página\n")
L.append("| Peça | H | PR | OM | IN | MA | Seletor | Par no Jeff DS | Porquês |")
L.append("| --- | :-: | :-: | :-: | :-: | :-: | --- | --- | :-: |")
fam = None
for p in pecas:
    if p["familia"] != fam:
        fam = p["familia"]
        L.append(f"| **{fam}** | | | | | | | | |")
    m = r["matriz"][p["nome"]]
    cel = [("%d" % m[pid]) if m.get(pid) else "" for pid, _ in PG]
    par = ", ".join(p["par"]) if p["par"] else "sem par"
    L.append(f"| {p['nome']} | " + " | ".join(cel) + f" | `{p['seletor']}` | {par} | {porques.get(p['nome'], 0)} |")
L.append("\nOs números são quantas vezes a peça aparece na página. H é Home, PR Processo com IA, OM Omnichat, IN Inpulse e MA Mapa de experiência.\n")

# diferenças contra o plano
dif = []
for p in pecas:
    if p["nome"] in plano:
        real = set(paginas_de(p))
        antes = plano[p["nome"]]
        if real != antes:
            dif.append((p["nome"], sorted(antes - real), sorted(real - antes)))
if plano:
    L.append("## Onde o plano errou a matriz\n")
    if dif:
        L.append("| Peça | O plano dizia que aparece, mas não aparece | Aparece e o plano não dizia |")
        L.append("| --- | --- | --- |")
        for n, a, b in dif:
            L.append(f"| {n} | {', '.join(a) or ''} | {', '.join(b) or ''} |")
    else:
        L.append("Nenhuma diferença.")
    L.append("")

# colisões de nome
colisoes = [
    ("`.fecho`", "Convite ao manifesto (Home) e Declaração final (casos)", "Duas peças sem nada em comum dividem o mesmo nome de classe, cada uma com a sua regra em home.css e caso.css. A Fase 4 deve renomear uma delas."),
]
L.append("## Colisões de nome\n")
L.append("Classes que o site usa para duas coisas diferentes. O seletor das peças no `pecas.json` já as separa.\n")
for c, quem, why in colisoes:
    L.append(f"- {c}: {quem}. {why}")
L.append("")

# nunca ou uma vez
uma = [(p["nome"], paginas_de(p)) for p in pecas if len(paginas_de(p)) == 1]
L.append("## Peças de uma página só\n")
L.append("Peça que aparece em uma única página pede uma pergunta antes de virar componente: ela é do sistema ou é da história daquele caso? As que ficam sozinhas:\n")
for n, pgs in uma:
    L.append(f"- {n}, só em {pgs[0]}")
L.append("")

# ocultas
if r.get("ocultas"):
    L.append("## O que some em tela estreita\n")
    for n, ls in r["ocultas"].items():
        L.append(f"- **{n}** não existe em {', '.join(str(x) for x in ls)}px. É a cena dos casos da Home: abaixo de certa largura ou altura ela não fica viva e os quatro casos empilham, sem trilho nem orbe. A ficha precisa dizer isso no campo Comportamento.")
    L.append("")

# comportamento
L.append("## Peças que são comportamento, não componente\n")
L.append("Revelar na entrada, Régua de leitura e Carrossel de tela estreita não têm uma forma própria para fotografar. O revelar age em %d elementos da Home e dos casos, a régua só existe nos quatro casos e o carrossel deita Abas e Trilha no celular. Entram no DS como regras de movimento e de layout (Fase 2), não como fichas.\n" % max(r["matriz"]["Revelar na entrada"].values()))

# --------------------------------------------------------------- fusões
fusoes_plano = [
    ("Sequência", ["Linhas indexadas", "Estágios", "Ritos", "Funil", "Trilha"], 5, 1,
     "A pergunta que escolhe a variante: a ordem importa, afunila, tem entrada e saída, é um caminho curto."),
    ("Antes e depois", ["Salto", "Confronto", "Conversa", "Citação"], 4, 1,
     "A forma do que muda: um número, várias dimensões, uma conversa ou a fala de quem usa."),
    ("Gráfico", ["Barras", "Pilhas", "Escala de NPS"], 3, 1,
     "Três formas e uma regra de entrada só, com a mesma rede de segurança para movimento reduzido."),
    ("Botão e link", ["Botão principal", "Link", "Voltar para os casos", "Próximo caso"], 4, 2,
     "Botão para a ação principal, Link com variantes para voltar, seguir, sair do site e fechar bloco."),
    ("Imagem", ["Moldura", "Galeria", "Sangria"], 3, 1,
     "Variantes de enquadramento, com crédito e texto alternativo num lugar só."),
]
fusoes_extra = [
    ("Comportamento fora da lista", ["Revelar na entrada", "Régua de leitura", "Carrossel de tela estreita"], 3, 0,
     "São regras de movimento e de layout. Saem da lista de componentes e vão para a Fase 2."),
    ("Navegação", ["Barra com assinatura", "Botão de menu", "Menu em painel"], 3, 1,
     "Os três são uma máquina só: o botão abre o painel, e a barra muda de cor com o que passa por trás. Hoje as três folhas de regra se referenciam."),
    ("Seção", ["Seção", "Cabeçalho de seção", "Bloco com rótulo"], 3, 1,
     "Cabeçalho e bloco nunca aparecem fora da seção. Viram partes da ficha da Seção."),
    ("Cena dos casos", ["Cena dos casos", "Orbe do número", "Trilho de pontos"], 3, 1,
     "Orbe e trilho só existem dentro da cena e somem junto com ela em tela estreita."),
    ("Superfície", ["Superfícies papel e tinta", "Onda"], 2, 1,
     "A onda é a borda da superfície: leva o fundo da seção junto para a curva não cortar a trama."),
    ("Seta de rolagem", ["Seta de descer", "Voltar ao topo"], 2, 1,
     "Mesmo morro, mesma distância, sentido contrário. O CSS já descreve uma como par da outra."),
    ("Texto corrido", ["Abertura", "Corpo de texto"], 2, 1,
     "Diferem só no corpo da letra. É uma variante."),
]


def soma(lst):
    return sum(a - b for _, _, a, b, _ in lst)


L.append("## Fusões\n")
base = n_pecas
com_plano = base - soma(fusoes_plano)
com_tudo = com_plano - soma(fusoes_extra)
L.append(
    f"Conta honesta: **{base} peças medidas, {com_plano} componentes com as cinco fusões do plano, {com_tudo} com as que a varredura sugere a mais.** "
    "O plano falava em cerca de 30; esse número só se alcança com a segunda lista, que são propostas minhas e dependem do seu sim.\n"
)
L.append("### Do plano\n")
for t, itens, a, b, why in fusoes_plano:
    L.append(f"- **{t}** ({a} para {b}): {', '.join(itens)}. {why}")
L.append("\n### Propostas desta fase\n")
for t, itens, a, b, why in fusoes_extra:
    L.append(f"- **{t}** ({a} para {b}): {', '.join(itens)}. {why}")
L.append("")
L.append("### Lista final se tudo for aceito\n")
usado = {n for _, itens, *_ in fusoes_plano + fusoes_extra for n in itens}
final = []
for t, itens, a, b, _ in fusoes_plano + fusoes_extra:
    if t != "Comportamento fora da lista":
        final.append((t, ", ".join(itens)))
for p in pecas:
    if p["nome"] not in usado:
        final.append((p["nome"], ""))
final.sort(key=lambda x: x[0])
# o botão e link vira dois
L.append(f"São {len(final) + 1} componentes (Botão e link conta duas vezes: Botão e Link).\n")
for t, itens in final:
    L.append(f"- {t}" + (f" ({itens})" if itens else ""))
L.append("")

# ------------------------------------------------------------- manifesto
L.append("## Manifesto, fora desta versão\n")
L.append(
    "A decisão D7 tira o manifesto desta versão do site. A página `manifesto/index.html` foi fotografada para registro, mas nenhuma das suas peças entra no inventário. "
    "Elas ficam marcadas aqui para que ninguém as migre sem querer:\n"
)
for x in ["Palco com quadros que trocam na rolagem", "Rótulo da etapa", "Contador", "Trilho de progresso", "Dica de rolagem com mouse animado", "Assinatura com duas ações", "Versão em texto corrido para quem chega sem JS"]:
    L.append(f"- {x}")
L.append("\nO manifesto também é a única página que usa outra identidade (papel creme e laranja, cores escritas no JS), e o único lugar com `--om-accent`, `--om-paper` e companhia. Continua no ar até a Fase 6.\n")

L.append("## Capturas\n")
L.append("`ds/capturas/index.html` reúne, para cada peça, a fotografia em 390, 768 e 1440px, e as páginas inteiras. As imagens estão em `ds/capturas/<largura>/<peça>.jpg` e `ds/capturas/paginas/`.\n")
if r.get("falhas"):
    L.append("### Fotografias que falharam\n")
    for f in r["falhas"]:
        L.append(f"- {f}")
    L.append("")
(RAIZ / "ds/INVENTARIO.md").write_text("\n".join(L) + "\n")

# ---------------------------------------------------------------- contraste
def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def razao(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


DS = [("paper", "#f9f9f7"), ("ink", "#000000"), ("lime", "#edfe5e"), ("azul", "#bed4fb"), ("verde", "#31e992"), ("mist", "#dee5dd")]
SITE = [("bone-white", "#fafffa"), ("press-black", "#121613"), ("slate-verdant", "#232924"), ("newsprint-gray", "#516254"), ("muted-sage", "#c8d2c8"), ("highlighter-green", "#2bee4b"), ("echo-green", "#c4e4c9")]

C = []
C.append("# Contraste\n")
C.append("Auditoria da paleta do Jeff DS aplicada ao site, e do que o site de hoje já erra. Os números vêm de `ds/auditoria/auditar.mjs` (texto medido nos elementos reais, em 390 e 1440px) e do cálculo WCAG 2.1 sobre os tokens.\n")
C.append("## Paleta do Jeff DS, par a par\n")
C.append("Razão de contraste. Texto normal pede 4,5 e texto grande (24px, ou 18,66px em negrito) ou controle pede 3.\n")
C.append("| | " + " | ".join(n for n, _ in DS) + " |")
C.append("| --- | " + " | ".join(":-:" for _ in DS) + " |")
for n, h in DS:
    cel = []
    for n2, h2 in DS:
        v = razao(h, h2)
        cel.append("" if n == n2 else (f"**{v:.1f}**" if v >= 4.5 else (f"{v:.1f}" if v >= 3 else f"_{v:.1f}_")))
    C.append(f"| **{n}** `{h}` | " + " | ".join(cel) + " |")
C.append("\nEm negrito, passa em texto normal (4,5 ou mais). Sem destaque, passa só em texto grande e controle (3 ou mais). Em itálico, não passa em nada.\n")
C.append("### O que isso decide\n")
ink_lime, ink_azul, ink_verde = razao("#000000", "#edfe5e"), razao("#000000", "#bed4fb"), razao("#000000", "#31e992")
pl, pa, pv = razao("#f9f9f7", "#edfe5e"), razao("#f9f9f7", "#bed4fb"), razao("#f9f9f7", "#31e992")
C.append(f"- Tinta sobre qualquer acento passa com folga ({ink_lime:.1f}, {ink_azul:.1f} e {ink_verde:.1f} para 1). Por isso o acento é sempre fundo e a tinta é sempre texto.")
C.append(f"- Acento sobre o papel não serve para nada além de preenchimento: lime {pl:.2f}, azul {pa:.2f} e verde {pv:.2f} para 1, abaixo até do mínimo de 3 para controles. Confirma a regra 1 do plano: lime, azul e verde nunca viram texto, nunca são a única borda de um controle e nunca são o anel de foco.")
C.append(f"- Um acento ao lado de outro, como lime sobre azul, não separa por luminosidade ({razao('#edfe5e','#bed4fb'):.2f} e {razao('#edfe5e','#31e992'):.2f}). Duas áreas de acento vizinhas precisam de traço de tinta entre elas, que o 2px já dá.\n")

C.append("## O site de hoje, par a par\n")
C.append("| | " + " | ".join(n for n, _ in SITE) + " |")
C.append("| --- | " + " | ".join(":-:" for _ in SITE) + " |")
for n, h in SITE:
    cel = []
    for n2, h2 in SITE:
        v = razao(h, h2)
        cel.append("" if n == n2 else (f"**{v:.1f}**" if v >= 4.5 else (f"{v:.1f}" if v >= 3 else f"_{v:.1f}_")))
    C.append(f"| **{n}** `{h}` | " + " | ".join(cel) + " |")
C.append("")

C.append("## Texto que reprova hoje\n")
C.append("Medido nos elementos visíveis, com a cor de fundo vinda do primeiro ancestral opaco. A barra do topo fica de fora, porque troca de fundo conforme a seção que passa por trás, e o texto escondido (opacidade zero) também.\n")
tot = 0
for pid, nome in NOMES.items():
    for larg in (1440, 390):
        lst = r["contraste"].get(f"{pid}-{larg}", [])
        if larg == 390 and lst == r["contraste"].get(f"{pid}-1440"):
            continue
        if not lst:
            continue
        C.append(f"### {nome}, {larg}px" + (" (fora desta versão)" if pid == "manifesto" else "") + "\n")
        C.append("| Texto | Fundo | Razão | Mínimo | Quantos | Exemplos |")
        C.append("| --- | --- | :-: | :-: | :-: | --- |")
        for g in lst:
            ex = "; ".join(f"`{e['el']}` {e['px']:g}px \"{e['texto']}\"" for e in g["exemplos"][:3])
            nota = " (fundo com trama)" if g.get("sobreImagem") else ""
            C.append(f"| `{g['texto']}` | `{g['fundo']}`{nota} | {g['razao']} | {g['meta']} | {g['n']} | {ex} |")
            if pid != "manifesto":
                tot += g["n"]
        C.append("")
if not tot:
    C.append("Nenhum texto reprovou nas páginas do site.\n")

C.append("## Onde o verde marca texto está hoje\n")
C.append("A regra 1 proíbe lime, azul e verde como texto, como única borda de controle e como anel de foco. Estes são os usos do `#2bee4b` e do `#c4e4c9` nas páginas, medidos nos estilos computados (1440px):\n")
agr = {}
for k, v in r["verde"].items():
    if not k.endswith("1440"):
        continue
    for x in v:
        agr.setdefault((x["uso"], x["el"]), set()).add(k.split("-")[0])
C.append("| Uso | Elemento | Páginas | Veredito |")
C.append("| --- | --- | --- | --- |")
ver = {"texto": "Reprova a regra 1. Passa para tinta.", "borda": "Reprova se for a única borda. Passa para tinta de 2px.", "anel de foco ou contorno": "Reprova. O foco passa a ser tinta.", "preenchimento": "Permitido, é o papel do acento."}
for (uso, el), pgs in sorted(agr.items(), key=lambda x: (x[0][0] == "preenchimento", x[0])):
    C.append(f"| {uso} | `{el}` | {', '.join(sorted(pgs))} | {ver[uso]} |")
C.append("")

css_uso = []
for f in ("assets/base.css", "assets/home.css", "assets/caso.css"):
    for i, l in enumerate((RAIZ / f).read_text().splitlines(), 1):
        if re.search(r"highlighter-green|echo-green|#2bee4b|#c4e4c9", l) and not l.strip().startswith(("/*", "*", "--")):
            prop = l.split(":")[0].strip()
            css_uso.append((f, i, prop, l.strip()))
foco = [x for x in css_uso if "outline" in x[2]]
txt = [x for x in css_uso if x[2] in ("color", "text-decoration-color", "fill", "stroke")]
bor = [x for x in css_uso if x[2].startswith("border")]
C.append("### No CSS\n")
C.append(f"{len(css_uso)} declarações usam o verde marca texto ou o verde claro. {len(txt)} são cor de texto, traço ou preenchimento de SVG, {len(bor)} são borda e {len(foco)} são anel de foco.\n")
C.append("**Anel de foco**, o mais grave, porque é o que o teclado usa para achar onde está. O foco hoje é verde sobre papel, razão %.2f para 1:\n" % razao("#2bee4b", "#fafffa"))
for f, i, p, l in foco:
    C.append(f"- `{f}:{i}` `{l}`")
C.append("\nO manifesto usa `--om-accent` (laranja) no foco, o que também sai com ele.\n")

C.append("## Resumo do que a Fase 2 herda\n")
C.append("1. O foco muda de verde para tinta em todo o site, no `:where(a):focus-visible`, no `:where(button):focus-visible` e nos dois focos de `caso.css`.")
C.append("2. Todo texto, link e borda de controle que hoje usa verde passa para tinta. O verde fica como fundo de botão, de etiqueta e de barra.")
C.append("3. Os pares de cinza que reprovam saem do cinza verdoso (`newsprint-gray`, `muted-sage`) e vão para tinta pura, porque o Jeff DS não tem cinza de texto, só a linha de fonte a 75% de opacidade. A hierarquia de leitura passa a depender de tamanho e peso, e não de tom.")
C.append("4. O texto de apoio sobre a tinta (rótulos, descrições) precisa de papel e não de cinza claro.\n")
(RAIZ / "ds/CONTRASTE.md").write_text(re.sub(r"(\d)\.(\d)", r"\1,\2", "\n".join(C)) + "\n")

# ---------------------------------------------------------------- folha de revisão
H = ["""<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Capturas das peças</title>
<style>
body{font:14px/1.5 system-ui,sans-serif;margin:0;padding:24px;background:#f9f9f7;color:#000}
h1{font-size:28px;margin:0 0 4px}h2{font-size:18px;margin:40px 0 8px;border-top:2px solid #000;padding-top:12px}
p{margin:0 0 12px;max-width:70ch}code{background:#dee5dd;padding:1px 5px;border-radius:4px}
.linha{display:grid;grid-template-columns:minmax(0,1fr);gap:12px;margin:0 0 28px}
@media(min-width:1100px){.linha{grid-template-columns:240px 360px 520px minmax(0,1fr);align-items:start}}
.linha figure{margin:0;border:2px solid #000;border-radius:12px;overflow:hidden;background:#dee5dd}
.linha figcaption{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.07em;padding:6px 10px;border-bottom:2px solid #000;background:#fff}
.linha img{display:block;width:100%;height:auto;max-height:640px;object-fit:contain;object-position:top}
.nome{font-weight:700;font-size:16px}.nome small{display:block;font-weight:400;color:#000;opacity:.75;margin-top:4px}
.ausente{padding:14px;font-size:13px}
</style>
<h1>Capturas das peças</h1>
<p>Cada peça na primeira página em que aparece, em 390, 768 e 1440px. Gerado por <code>ds/auditoria/auditar.mjs</code>. No fim, as páginas inteiras.</p>"""]
cap = r["capturas"]
fam = None
for p in pecas:
    if not p["captura"]:
        continue
    if p["familia"] != fam:
        fam = p["familia"]
        H.append(f"<h2>{fam}</h2>")
    pid = cap.get(p["nome"])
    sl = slug(p["nome"])
    figs = []
    for larg in (390, 768, 1440):
        f = RAIZ / f"ds/capturas/{larg}/{sl}.jpg"
        oculta = larg in r.get("ocultas", {}).get(p["nome"], [])
        if f.exists() and not oculta:
            figs.append(f'<figure><figcaption>{larg}px</figcaption><img loading="lazy" src="{larg}/{sl}.jpg" alt="{p["nome"]} em {larg}px"></figure>')
        else:
            figs.append(f'<figure><figcaption>{larg}px</figcaption><p class="ausente">{"Não existe nesta largura." if oculta else "Sem captura."}</p></figure>')
    H.append(f'<div class="linha"><div class="nome">{p["nome"]}<small>{p["faz"]}<br>Fotografada em {NOMES.get(pid, pid)}</small></div>{"".join(figs)}</div>')
H.append("<h2>Páginas inteiras</h2>")
for pid, nome in list(NOMES.items()) + [("manifesto", "Manifesto (fora desta versão)")]:
    figs = "".join(f'<figure><figcaption>{l}px</figcaption><img loading="lazy" src="paginas/{pid}-{l}.jpg" alt="{nome} em {l}px"></figure>' for l in (390, 768, 1440))
    H.append(f'<div class="linha"><div class="nome">{nome}</div>{figs}</div>')
(RAIZ / "ds/capturas/index.html").write_text("\n".join(H) + "\n")
print("ok", n_pecas, com_plano, com_tudo)
