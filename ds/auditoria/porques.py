"""Extrai os porquês escritos nos comentários do CSS e do HTML e os
organiza por peça, a partir de pecas.json.

Cada comentário é ligado ao que vem logo depois dele: a primeira
regra de CSS ou a primeira tag de HTML. A classe dessa regra decide a
peça. O que não cai em nenhuma vai para "Fundação" (tokens, reset,
tipografia, movimento) ou para "Sem peça", para eu olhar à mão.

Uso: python3 ds/auditoria/porques.py
"""
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
pecas = json.loads((Path(__file__).parent / "pecas.json").read_text())

FONTES_CSS = ["assets/base.css", "assets/home.css", "assets/caso.css"]
FONTES_HTML = ["index.html", "case-processo.html", "case-omnichat.html", "case-inpulse.html", "case-mapa-experiencia.html"]
IGNORAR_HTML = ("Duas marcas postas antes do primeiro pixel",)  # script de arranque, igual em todas


def raiz(c):
    return re.split(r"__|--", c)[0]


# classe raiz -> índice da peça. A primeira peça que declara a classe fica com ela.
dono = {}
extra = {
    "wordmark": "Barra com assinatura", "nav": "Barra com assinatura",
    "menu": "Menu em painel", "reticula": "Menu em painel", "menu-btn": "Botão de menu",
    "onda": "Onda", "onda-defs": "Onda", "folha": "Superfícies papel e tinta", "tinta": "Superfícies papel e tinta",
    "footer": "Rodapé de contato", "fecho": "Convite ao manifesto",
    "orbe": "Orbe do número", "ato": "Cena dos casos", "cena": "Cena dos casos",
    "linha": "Linhas indexadas", "fase": "Funil", "estagio": "Estágios", "aba": "Abas", "aba-painel": "Abas",
    "rito": "Ritos", "turno": "Conversa", "conversa": "Conversa", "barra": "Barras", "pilha": "Pilhas", "cor": "Pilhas",
    "citacao": "Citação", "numero-caso": "Números do resultado", "ficha": "Ficha do projeto",
    "ficha-lateral": "Ficha do projeto", "faixa-ficha": "Ficha do projeto", "grito-par": "Grito",
    "btn-green": "Botão principal", "link": "Link", "link-solto": "Link", "etiqueta": "Etiquetas de assunto",
    "entregas": "Abas", "coluna-a": "Seção", "coluna-b": "Seção", "secao": "Seção", "transicao": "Passagem entre páginas",
    "descer": "Seta de descer", "subir": "Voltar ao topo", "hero": "Hero editorial", "foto": "Hero editorial",
    "nps": "Escala de NPS", "regua": "Régua de leitura", "rotulo": "Micro rótulo", "legenda": "Seção",
    "caso-topo": "Topo do caso", "caso": "Topo do caso", "acoes": "Ações do fim", "proximo-link": "Próximo caso",
    "grade": "Seção", "cores": "Pilhas", "turnos": "Conversa", "salto": "Salto", "numeros": "Números do resultado", "galeria": "Galeria", "moldura": "Moldura",
}
for p in pecas:
    for s in p["seletor"].split(","):
        for c in re.findall(r"\.([\w-]+)", s):
            dono.setdefault(raiz(c), p["nome"])
dono.update(extra)
for p in pecas:
    for s in p["seletor"].split(","):
        for c in re.findall(r"\.([\w-]+)", s):
            dono.setdefault(raiz(c), p["nome"])

FUNDACAO_CLASSES = {"wrap", "face-unica", "pular", "txt", "on-dark", "revelado", "crescido", "js", "js-mov"}


def limpa(t):
    t = t.strip()
    t = re.sub(r"^/\*+|\*+/$", "", t).strip()
    linhas = [re.sub(r"^\s*\*\s?", "", l.rstrip()) for l in t.splitlines()]
    # tira o recuo comum
    corpo = [l for l in linhas if l.strip()]
    if corpo:
        recuo = min(len(l) - len(l.lstrip()) for l in corpo[1:]) if len(corpo) > 1 else 0
        linhas = [linhas[0].strip()] + [l[recuo:] if l.strip() else "" for l in linhas[1:]]
    txt = "\n".join(linhas).strip()
    txt = re.sub(r"^=+\s*$", "", txt, flags=re.M).strip()
    return txt.replace("—", ",").replace("–", "a")


def classe_da_regra(css_depois):
    """Primeira classe do primeiro seletor depois do comentário."""
    m = re.match(r"\s*(?:@media[^{]*\{\s*)?([^{};]+)\{", css_depois)
    if not m:
        return None, css_depois[:60].strip()
    sel = m.group(1).strip()
    if sel.startswith(":root") or sel.startswith("html") or sel.startswith("body") or sel.startswith("*") or sel.startswith("@"):
        return None, sel
    cls = re.findall(r"\.([\w-]+)", sel.split(",")[0])
    return (cls[0] if cls else None), sel


achados = []  # (peça, origem, linha, texto, seletor)
for f in FONTES_CSS:
    s = (RAIZ / f).read_text()
    for m in re.finditer(r"/\*.*?\*/", s, re.S):
        txt = limpa(m.group(0))
        if len(txt) < 25:
            continue
        linha = s.count("\n", 0, m.start()) + 1
        resto = s[m.end():]
        # pula comentários seguidos
        while re.match(r"\s*/\*", resto):
            resto = resto[resto.index("*/") + 2:]
        cls, sel = classe_da_regra(resto)
        # comentário de cabeçalho de seção ("=====") nomeia a peça pelo título
        peca = None
        if cls:
            r = raiz(cls)
            if r in FUNDACAO_CLASSES:
                peca = "Fundação"
            elif r == "fecho" and f.endswith("caso.css"):
                # Mesmo nome, duas peças: na Home .fecho é o convite ao
                # manifesto, nos casos é a declaração final.
                peca = "Declaração final"
            else:
                peca = dono.get(r)
        if peca is None:
            peca = "Fundação" if (sel.startswith((":root", "html", "body", "*", "@")) or cls is None) else "Sem peça"
        achados.append((peca, f, linha, txt, sel[:70]))

for f in FONTES_HTML:
    s = (RAIZ / f).read_text()
    for m in re.finditer(r"<!--(.*?)-->", s, re.S):
        txt = limpa(m.group(1))
        if len(txt) < 25 or any(i in txt for i in IGNORAR_HTML):
            continue
        linha = s.count("\n", 0, m.start()) + 1
        resto = s[m.end():]
        t = re.search(r"<(\w+)[^>]*?class=\"([^\"]+)\"", resto[:600])
        cls = t.group(2).split()[0] if t else None
        peca = None
        if cls:
            r = raiz(cls)
            peca = "Fundação" if r in FUNDACAO_CLASSES else dono.get(r)
        if peca is None:
            peca = "Fundação" if cls is None else "Sem peça"
        achados.append((peca, f, linha, txt, f"<{t.group(1)} class=\"{cls}\">" if t else ""))

ordem = [p["nome"] for p in pecas]
por_peca = {}
for a in achados:
    por_peca.setdefault(a[0], []).append(a)

fam_de = {p["nome"]: p["familia"] for p in pecas}
out = []
out.append("# Os porquês do site\n")
out.append(
    "Tudo o que hoje está escrito nos comentários do CSS e do HTML e explica uma decisão de uso, organizado pela peça de que fala. "
    "Foi extraído por `ds/auditoria/porques.py`, que liga cada comentário à primeira regra ou tag que vem depois dele. "
    "O texto é o original, só sem travessão. É a matéria prima das fichas da Fase 3: o campo \"Não use quando\" e o campo \"Limites\" saem daqui.\n"
)
out.append(f"São {len(achados)} comentários, {sum(1 for a in achados if a[0] not in ('Fundação','Sem peça'))} ligados a uma peça, {len(por_peca.get('Fundação', []))} de fundação e {len(por_peca.get('Sem peça', []))} que o script não soube ligar.\n")
out.append("## Índice\n")
fam_atual = None
for n in ordem:
    if n in por_peca:
        out.append(f"- [{n}](#{re.sub(r'[^a-z0-9]+','-',n.lower().encode('ascii','ignore').decode() or n.lower()).strip('-')}) ({len(por_peca[n])})")
out.append("- Fundação (%d)" % len(por_peca.get("Fundação", [])))
out.append("- Sem peça (%d)\n" % len(por_peca.get("Sem peça", [])))


def bloco(nome, itens):
    out.append(f"\n## {nome}\n")
    for _, f, linha, txt, sel in itens:
        out.append(f"**{f}:{linha}** `{sel}`\n")
        out.append("\n".join("> " + l if l else ">" for l in txt.splitlines()))
        out.append("")


fam_atual = None
for n in ordem:
    if n in por_peca:
        if fam_de[n] != fam_atual:
            fam_atual = fam_de[n]
            out.append(f"\n# {fam_atual}\n")
        bloco(n, por_peca[n])
out.append("\n# Fora das peças\n")
bloco("Fundação", por_peca.get("Fundação", []))
bloco("Sem peça", por_peca.get("Sem peça", []))

(RAIZ / "ds/PORQUES.md").write_text("\n".join(out) + "\n")
json.dump({k: len(v) for k, v in por_peca.items()}, open(Path(__file__).parent / "porques-contagem.json", "w"), ensure_ascii=False, indent=1)
print(len(achados), "comentários;", {k: len(v) for k, v in por_peca.items() if k in ("Fundação", "Sem peça")})
print("sem peça:", [(a[1], a[2], a[4]) for a in por_peca.get("Sem peça", [])][:30])
