"""Partes que toda página de prova divide: cabeça, carregamento, cabeçalho
com o menu, rodapé e scripts. E o texto do caso Omnichat, igual ao do site,
para as variações só mudarem a forma.

`pre` é o caminho da página até a raiz do repositório ("../../" ou
"../../../"), porque as provas moram em profundidades diferentes.
"""

FAVICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect x='3' y='3' width='94' height='94' rx='14' "
    "fill='%23edfe5e' stroke='%23000' stroke-width='6'/%3E%3Ctext x='50' y='74' font-family='Impact, Anton, sans-serif' font-size='62' "
    "text-anchor='middle' fill='%23000'%3EJ%3C/text%3E%3C/svg%3E"
)


def cabeca(pre, titulo, css="", corpo_classe="", descricao=""):
    """Com `descricao` a página é publicada: entra a descrição para a busca
    e o analytics, e sai o noindex das provas."""
    meta = (f'<meta name="description" content="{descricao}">\n<script src="{pre}assets/analytics.js"></script>'
            if descricao else '<meta name="robots" content="noindex">')
    return f"""<!DOCTYPE html>
<html lang="pt-BR" data-acento="azul">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add("js");try{{if(performance.getEntriesByType("navigation")[0].type==="back_forward")document.documentElement.classList.add("volta")}}catch(e){{}}</script>
<title>{titulo}</title>
{meta}
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{pre}assets/ds/tokens.css">
<link rel="stylesheet" href="{pre}assets/ds/componentes.css">
{f"<style>{css}</style>" if css else ""}
</head>
<body{f' class="{corpo_classe}"' if corpo_classe else ""}>
"""


# A tela que se monta no carregamento. Mesmas camadas do hero da Home,
# na ordem de chegada: esboço, grade, componentes, textos, cores.
CARGA = """<div class="carga" aria-hidden="true">
  <div class="carga__quadro">
    <svg class="carga__tela" viewBox="0 0 240 300" fill="none">
      <g class="carga__esboco" stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M8 10C70 6 160 12 232 8c4 82-2 202 2 284-74 4-164-2-228 2 4-84-2-204 2-284Z"/>
        <path d="M24 40c66-3 126 3 192-1 2 31-2 61 1 89-67 3-127-2-194 2 3-30-1-60 1-90Z"/>
        <path d="M26 42l188 84M214 41L25 128"/>
        <path d="M24 152c56-3 106 3 156-2M24 168c46-3 86 2 116-2"/>
        <path d="M24 192c36-3 66 2 88-1 2 29-2 54 1 77-33 3-63-2-91 2 3-26-1-54 2-78Z"/>
        <path d="M128 192c32-3 62 2 88-1 2 29-2 54 1 77-27 3-57-2-90 2 3-26-1-54 1-78Z"/>
      </g>
      <g class="carga__camada carga__camada--grade" stroke="#000" stroke-width="1.6" stroke-dasharray="1 6" stroke-linecap="round">
        <path d="M20 22v262M85 22v262M155 22v262M220 22v262M12 140h216"/>
      </g>
      <g class="carga__camada carga__camada--componentes" stroke="#000" stroke-width="2">
        <rect x="2" y="2" width="236" height="296" rx="12"/>
        <rect x="20" y="36" width="200" height="96" rx="8"/>
        <rect x="36" y="104" width="64" height="18" rx="9"/>
        <rect x="20" y="186" width="94" height="86" rx="8"/>
        <rect x="126" y="186" width="94" height="86" rx="8"/>
      </g>
      <g class="carga__camada carga__camada--textos" fill="#000">
        <rect x="36" y="50" width="122" height="10" rx="3"/>
        <rect x="36" y="66" width="84" height="10" rx="3"/>
        <rect x="36" y="84" width="104" height="5" rx="2.5"/>
        <rect x="48" y="110" width="40" height="5" rx="2.5"/>
        <rect x="20" y="148" width="148" height="6" rx="3"/>
        <rect x="20" y="162" width="102" height="6" rx="3"/>
        <rect x="32" y="204" width="56" height="6" rx="3"/>
        <rect x="32" y="216" width="44" height="5" rx="2.5"/>
        <rect x="138" y="204" width="56" height="6" rx="3"/>
        <rect x="138" y="216" width="66" height="5" rx="2.5"/>
      </g>
      <g class="carga__camada carga__camada--cores">
        <rect class="carga__cor" x="20" y="36" width="200" height="96" rx="8"/>
        <rect x="36" y="104" width="64" height="18" rx="9" fill="#edfe5e"/>
        <rect x="126" y="186" width="94" height="86" rx="8" fill="#dee5dd"/>
      </g>
    </svg>
    <div class="carga__barra"><i></i></div>
  </div>
</div>
"""


def omnichat(pre, aqui):
    """O item do Omnichat no menu e no rodapé. Nas provas ele aponta para a
    própria página e é a atual. Sem `aqui` (a vitrine), é um link comum."""
    if aqui is None:
        return f'href="{pre}case-omnichat.html"'
    return f'href="{aqui}" aria-current="page"'


def cabecalho(pre, aqui, pular="Pular para o caso"):
    """Barra e menu. Home entra junto com os casos, porque é parte do site.
    O que leva para fora (LinkedIn, WhatsApp) fica abaixo, menor."""
    return f"""
<a class="pular" href="#conteudo">{pular}</a>

<header class="header">
  <div class="container header__inner">
    <a class="marca" href="{pre}index.html" aria-label="Jeff Maia, Product Design Manager">
      <b>Jeff Maia</b><span>Product Design Manager</span>
    </a>
    <button class="menu-botao" type="button" data-sheet-botao aria-expanded="false" aria-controls="menu">
      <span class="menu-botao__icone" aria-hidden="true"><i></i><i></i></span>
      <span class="menu-botao__rotulos"><span>Menu</span><span>Fechar</span></span>
    </button>
  </div>
</header>

<div class="sheet" id="menu">
  <nav class="container sheet__inner" aria-label="Principal">
    <ul class="sheet__lista">
      <li><a class="sheet__item" href="{pre}index.html"><span>Home</span></a></li>
      <li><a class="sheet__item" href="{pre}case-processo.html"><span>Processo com IA</span></a></li>
      <li><a class="sheet__item" {omnichat(pre, aqui)}><span>Omnichat</span></a></li>
      <li><a class="sheet__item" href="{pre}case-inpulse.html"><span>Inpulse</span></a></li>
      <li><a class="sheet__item" href="{pre}case-mapa-experiencia.html"><span>Mapa de experiência</span></a></li>
    </ul>
    <div class="sheet__contato">
      <p class="t-rotulo">Contato</p>
      <ul class="sheet__secundaria">
        <li><a class="link" data-variant="externo" href="https://www.linkedin.com/in/maiajeff/" target="_blank" rel="noopener">LinkedIn <i aria-hidden="true">↗</i></a></li>
        <li><a class="link" data-variant="externo" href="https://wa.me/5511977346175" target="_blank" rel="noopener">WhatsApp <i aria-hidden="true">↗</i></a></li>
      </ul>
    </div>
  </nav>
</div>
"""


def rodape(pre, aqui):
    """Sem a coluna "Fora daqui": WhatsApp e LinkedIn já estão na chamada,
    e voltar ao topo é desta página, então mora na linha de baixo."""
    return f"""
<footer class="footer superficie-tinta">
  <div class="container">
    <div class="footer__grade">
      <div class="footer__chamada">
        <h2 class="t-titulo">Quer conversar sobre&nbsp;um&nbsp;problema parecido?</h2>
        <a class="button" href="https://wa.me/5511977346175" target="_blank" rel="noopener">WhatsApp +55 11 97734-6175 <span aria-hidden="true">↗</span></a>
        <a class="link" data-variant="externo" href="https://www.linkedin.com/in/maiajeff/" target="_blank" rel="noopener">linkedin.com/in/maiajeff <i aria-hidden="true">↗</i></a>
      </div>
      <nav class="footer__col" aria-label="Páginas">
        <p class="t-rotulo">Páginas</p>
        <ul>
          <li><a class="link" href="{pre}index.html">Home</a></li>
          <li><a class="link" href="{pre}case-processo.html">Processo com IA</a></li>
          <li><a class="link" {omnichat(pre, aqui)}>Omnichat</a></li>
          <li><a class="link" href="{pre}case-inpulse.html">Inpulse</a></li>
          <li><a class="link" href="{pre}case-mapa-experiencia.html">Mapa de experiência</a></li>
        </ul>
      </nav>
    </div>
    <div class="footer__meta">
      <span class="t-rotulo">Jeff Maia · São Paulo, Brasil</span>
      <a class="link" data-variant="topo" href="#top">Voltar ao topo <i aria-hidden="true">↑</i></a>
    </div>
  </div>
</footer>

<script src="{pre}assets/ds/componentes.js"></script>
</body>
</html>
"""


def icone(pre, nome, tam=56, classe="icone"):
    return f'<img class="{classe}" src="{pre}assets/ds/icones/{nome}-azul.svg" alt="" width="{tam}" height="{tam}">'


def ilustracao(pre, nome, classe="ilustracao", eager=True):
    larg, alt = (900, 640) if nome == "fronteira" else (640, 640)
    return f'<img class="{classe}" src="{pre}assets/ds/ilustracoes/omnichat-{nome}.svg" alt="" width="{larg}" height="{alt}" {"" if eager else "loading=lazy"}>'


# ---------------------------------------------------------------- texto do caso
BADGES = ["Omnichat", "Agentic Experience", "Agentes conversacionais"]
TITULO = "Verificação de&nbsp;intenção dos&nbsp;agentes conversacionais"
LEAD = "A maior perda de conversão não estava na&nbsp;interface. Estava na&nbsp;camada onde a&nbsp;intenção do&nbsp;lead entra no&nbsp;sistema."
SALTO_FRASE = "A conversão de leads qualificados nas origens redesenhadas, medida em&nbsp;produção ao longo de 8 semanas sobre cerca de 40 mil conversas, comparando com&nbsp;o&nbsp;fluxo anterior no&nbsp;mesmo período."
CONTEXTO = "A Omnichat opera agentes de vendas conversacionais que atendem leads em escala, vindos de origens diferentes. Cada origem carrega um tipo de intenção, e o agente tratava todo lead do mesmo jeito, como se toda conversa começasse do&nbsp;zero."
FICHA = [
    ("Duração", "4 meses, com 8 semanas de medição em produção"),
    ("Jeff", "Product Design Manager, responsável pelo desenho da&nbsp;camada de decisão e&nbsp;pelo recorte do experimento"),
    ("Time", "2 engenheiros de IA e 1 analista de dados"),
]
PROBLEMA_TITULO = "Ninguém tinha desenhado a&nbsp;fronteira de&nbsp;entrada"
PROBLEMA = [
    "Não existia visão clara da jornada conversacional. O time via o&nbsp;resultado final, lead convertido ou lead perdido, mas não enxergava o caminho entre a mensagem de entrada e a decisão do&nbsp;agente.",
    "O erro não era de capacidade do modelo, era de design. A&nbsp;fronteira onde a intenção do lead entra no sistema ficava por&nbsp;conta do&nbsp;acaso de cada canal de&nbsp;origem.",
]
ORIGENS = [
    ("celular", "Instagram", "Chegavam com um objetivo implícito, moldado pelo anúncio que&nbsp;clicaram. O agente não tinha acesso a esse contexto e&nbsp;tratava a primeira mensagem como uma pergunta genérica."),
    ("megafone", "Disparos de&nbsp;WhatsApp", "Chegavam ainda mais comprimidos, muitas vezes respondendo a&nbsp;um&nbsp;gatilho automático sem nunca ter formulado a própria intenção com clareza."),
]
CAMADAS_TITULO = "Cinco camadas de&nbsp;um&nbsp;artefato de&nbsp;design"
CAMADAS = [
    ("prompt", "lapis", "A&nbsp;arquitetura de&nbsp;prompt como superfície de&nbsp;design",
     "Parar de tratar o prompt como configuração técnica. Cada ponto em que o agente decide algo, seguir a conversa, pedir mais contexto ou escalar para um vendedor, virou um ponto de decisão desenhado com intenção, no mesmo nível de uma interface visual.",
     "Tornou a conversa um objeto de design, com pontos de falha localizáveis em vez de um resultado opaco."),
    ("jornada", "rota", "Jornada mapeada por&nbsp;origem do&nbsp;lead",
     "Em vez de um fluxo único, a entrada da conversa virou uma fronteira distinta por canal. Leads de Instagram passaram a receber uma pergunta inicial que resgata o contexto do anúncio. Leads de disparos de WhatsApp ganharam uma etapa extra de verificação de intenção.",
     "Recuperou contexto que antes se perdia no primeiro turno, justamente nas duas origens de maior perda."),
    ("limites", "verifica", "Limites de&nbsp;decisão do&nbsp;agente redesenhados",
     "A primeira ideia do time era fazer o agente sempre pedir confirmação antes de ofertar. Descartamos porque isso adicionava um turno em toda conversa e derrubava a conversão de quem já chegava com intenção clara. Optamos por um limite condicionado à origem: com a intenção confirmada o agente segue com a oferta sozinho, e havendo sinal de ambiguidade ele para e verifica antes de agir.",
     "Reduziu ofertas erradas apresentadas cedo demais, um&nbsp;dos&nbsp;principais pontos de abandono."),
    ("desvio", "lupa", "Leitura de&nbsp;desvio no&nbsp;lugar de&nbsp;leitura completa",
     "O time passou a revisar apenas os pontos em&nbsp;que&nbsp;a&nbsp;conversa fugiu do padrão esperado para&nbsp;aquela origem, em vez de&nbsp;ler transcrições inteiras.",
     "Permitiu revisar volume alto de conversas em pouco tempo e ajustar a fronteira de entrada com base em dado real."),
    ("teste", "alvo", "Teste controlado em&nbsp;produção",
     "Rodar o redesenho em produção com testes controlados, comparando taxa de conversão por origem antes e depois, em vez de validar a mudança isolada em ambiente de teste.",
     "Isolou o ganho de 8 pontos na conversão de&nbsp;leads qualificados por origem de lead."),
]
CONVERSA_TITULO = "O&nbsp;mesmo lead de&nbsp;Instagram, nas&nbsp;duas versões da&nbsp;fronteira de&nbsp;entrada"
CONVERSA_LEGENDA = "Conversa ilustrativa. As notas de&nbsp;camada ligam cada correção ao&nbsp;ponto correspondente da&nbsp;lista acima."
LEAD_Q = "Lead · Instagram"
ANTES = [
    ("lead", "Oi, vi aqui no Instagram e queria saber mais", None),
    ("agente", "Olá! Tudo bem? Posso te ajudar com&nbsp;informações sobre nossos produtos. Qual o seu nome?", "Trata a primeira mensagem como pergunta genérica"),
    ("lead", "É sobre aquilo que&nbsp;apareceu no&nbsp;anúncio", None),
    ("agente", "Temos várias opções disponíveis. Quer fechar o&nbsp;plano anual em 12x sem juros?", "Oferta apresentada antes de&nbsp;a&nbsp;intenção existir"),
    ("lead", "…", "Conversa abandonada no quarto turno"),
]
DEPOIS = [
    ("lead", "Oi, vi aqui no Instagram e queria saber mais", None),
    ("agente", "Oi! Você chegou pelo anúncio da&nbsp;campanha de inverno. É sobre isso que quer falar, ou é outro assunto?", "Camada 02, jornada por origem"),
    ("lead", "É sobre isso mesmo", None),
    ("agente", "Fechado. Antes de te passar valores, só confirmando: é para&nbsp;uso próprio ou para revenda?", "Camada 03, verifica antes de ofertar"),
    ("lead", "Uso próprio", None),
    ("agente", "Então a opção que faz sentido é a&nbsp;que&nbsp;estava no anúncio, com entrega para&nbsp;a&nbsp;sua região. Quero já reservar para você?", "Camada 03, segue sozinho com&nbsp;a&nbsp;intenção confirmada"),
    ("lead", "Pode reservar sim", None),
]
RESULTADO_TITULO = "O&nbsp;agente parou de&nbsp;responder à&nbsp;mensagem e&nbsp;passou a&nbsp;responder à&nbsp;intenção"
RESULTADO = [
    "A conversão de leads qualificados subiu 8 pontos, medida pela taxa dos&nbsp;agentes de vendas conversacionais. O ganho não veio de uma&nbsp;oferta melhor nem de um texto mais persuasivo.",
    "Veio das duas origens que mais perdiam conversão antes da mudança, Instagram e&nbsp;disparos de&nbsp;WhatsApp.",
]
STATS = [
    ("grafico", "+8%", "de conversão de leads qualificados, de&nbsp;24% para&nbsp;32%"),
    ("dialogo", "~40 mil", "conversas comparadas em&nbsp;produção"),
    ("calendario", "8 semanas", "de medição contra o fluxo anterior no&nbsp;mesmo período"),
    ("fronteira", "2 origens", "redesenhadas, Instagram e&nbsp;disparos de&nbsp;WhatsApp"),
]
LEVO_ROTULO = "O que eu levo daqui"
DECLARACAO = "A&nbsp;interface não é&nbsp;mais o&nbsp;objeto principal do&nbsp;trabalho. O&nbsp;objeto é&nbsp;a&nbsp;decisão."
DECL_CORPO = "O que o agente pode decidir sozinho, o que ele precisa verificar antes de agir e como mostra isso para quem precisa confiar no resultado. Desenhar bem essa camada foi o que gerou o ganho de&nbsp;conversão."
FECHO = 'Trabalho com design de decisão em produtos conversacionais. Se&nbsp;esse tipo de&nbsp;camada é um problema no seu produto, <a class="link" href="https://wa.me/5511977346175" target="_blank" rel="noopener">me&nbsp;chama no&nbsp;WhatsApp</a> ou veja o próximo caso.'


# ---------------------------------------------------------------- blocos prontos
def badges(variante_ultima="acento"):
    # Lista, para o leitor de tela ler uma Etiqueta de cada vez. O
    # role devolve a lista ao Safari, que a esquece sem os marcadores.
    itens = [f'<li><span class="badge">{b}</span></li>' for b in BADGES[:-1]]
    itens.append(f'<li><span class="badge" data-variant="{variante_ultima}">{BADGES[-1]}</span></li>')
    return '<ul class="badges" role="list">' + "".join(itens) + "</ul>"


def salto(classe=""):
    return f"""<div class="stat {classe}" data-variant="salto">
  <span class="stat__antes"><span class="sr">De </span>24%</span>
  <span class="stat__valor"><span class="sr">para </span>32%</span>
  <p class="stat__frase">{SALTO_FRASE}</p>
</div>"""


def ficha():
    return '<dl class="ficha">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in FICHA) + "</dl>"


def turnos(lista):
    out = []
    for quem, fala, nota in lista:
        cls = "turno turno--agente" if quem == "agente" else "turno"
        rot = "Agente" if quem == "agente" else LEAD_Q
        n = f'<span class="turno__nota">{nota}</span>' if nota else ""
        out.append(f'<li class="{cls}"><span class="t-rotulo">{rot}</span><p class="turno__fala">{fala}</p>{n}</li>')
    return '<ol class="turnos">' + "".join(out) + "</ol>"


def conversa(pre):
    return f"""<div class="compare">
  <div class="card compare__lado" data-variant="muted">
    <p class="compare__cabeca"><span class="badge">{icone(pre, "xis", 20, "icone-inline")}Antes</span><span class="badge" data-variant="tinta">Conversa abandonada</span></p>
    {turnos(ANTES)}
  </div>
  <div class="card compare__lado" data-variant="acento">
    <p class="compare__cabeca"><span class="badge">{icone(pre, "check", 20, "icone-inline")}Depois</span><span class="badge" data-variant="tinta">Lead convertido</span></p>
    {turnos(DEPOIS)}
  </div>
</div>"""


def tabs(pre, prefixo="aba"):
    abas = []
    paineis = []
    for i, (cid, ic, tit, txt, ef) in enumerate(CAMADAS, 1):
        abas.append(f'<button class="tab" type="button" role="tab" id="{prefixo}-{cid}" aria-controls="{prefixo}-painel-{cid}">{icone(pre, ic, 32, "icone-inline")}<span class="t-rotulo">0{i}</span>{tit}</button>')
        paineis.append(f"""<div class="tabs__painel" id="{prefixo}-painel-{cid}" tabindex="0">
  <h3 class="tabs__painel-titulo">{icone(pre, ic, 32, "icone-inline")}<span class="t-rotulo">0{i}</span>{tit}</h3>
  <p>{txt}</p>
  <p class="tabs__efeito"><span class="t-rotulo">Efeito</span> {ef}</p>
</div>""")
    return f"""<div class="tabs" data-tabs>
  <div class="tabs__lista" aria-label="Camadas do artefato" aria-orientation="vertical">{"".join(abas)}</div>
  <div class="tabs__paineis">{"".join(paineis)}</div>
</div>"""


def callout():
    return f"""<div class="callout superficie-tinta">
  <span class="badge" data-variant="acento">{LEVO_ROTULO}</span>
  <p class="callout__frase">{DECLARACAO}</p>
  <p class="prosa">{DECL_CORPO}</p>
</div>"""


def fechamento(pre):
    return f"""<div class="fechamento">
  <p class="prosa">{FECHO}</p>
  <a class="button" href="{pre}case-inpulse.html">Próximo caso, Inpulse <span aria-hidden="true">→</span></a>
</div>"""
