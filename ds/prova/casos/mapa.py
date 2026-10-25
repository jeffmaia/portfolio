"""O caso do Mapa de experiência, com o texto da página publicada antes da
Fase 6. Os dois pontos viraram ponto final, e a terceira decisão do
Processo junta os dois parágrafos num só (decisões 3 e 6 da Fase 6)."""
import comum as c
import pecas as p

ARQUIVO = "case-mapa-experiencia.html"
ACENTO = "azul"
TITULO_PAGINA = "Como um mapa de experiência ajudou a deixar o NPS positivo · Jeff Maia"
DESCRICAO = (
    "Um relatório de pesquisa em formato de tabuleiro que fez 16 campus lerem a pesquisa e agirem sobre ela. "
    "O NPS geral saiu de 33 negativos para 15 positivos no mesmo ciclo, com o acesso ao relatório indo de 20 "
    "para 890 usuários únicos no primeiro mês."
)

SECOES = [
    ("contexto", "lupa", "Contexto"),
    ("nota", "alvo", "O que move a nota"),
    ("processo", "camadas", "Processo"),
    ("solucao", "rota", "Solução"),
    ("resultado", "grafico", "Resultado"),
]

BADGES = ["UX Research", "UX Strategy", "Pesquisa e NPS"]
TITULO = "Como um&nbsp;mapa de&nbsp;experiência ajudou a&nbsp;deixar o&nbsp;NPS positivo"
LEAD = "Um relatório de pesquisa que 16 campus liam e a&nbsp;partir do&nbsp;qual agiam, em&nbsp;vez de&nbsp;arquivar junto com&nbsp;os&nbsp;outros."
FICHA = [
    ("Duração", "3 meses, da análise do NPS à entrega para&nbsp;os&nbsp;16 campus"),
    ("Jeff", "Idealizador e mentor do&nbsp;formato e&nbsp;da&nbsp;estratégia de entrega"),
    ("Time", "Anna Marsillac na&nbsp;pesquisa, Lucas Dias e&nbsp;Natália Dantas no design"),
]
SALTO = ("−33", "+15", "A nota geral de NPS de um grupo educacional com 12 marcas e 16 campus, a&nbsp;partir das&nbsp;ações que cada campus construiu com o material. No mesmo ciclo, o acesso ao relatório saiu de 20 para 890 usuários únicos no&nbsp;primeiro mês.")
CENA = "mapa"

PERGUNTA = "Como ajudar cada campus a&nbsp;entender o&nbsp;motivo da&nbsp;nota negativa e&nbsp;a&nbsp;pensar em&nbsp;ações para&nbsp;melhorá-la?"
CONTEXTO = "Um grupo educacional com 12 marcas e 16 campus ao redor do Brasil convivia com um NPS negativo, e as ações dos últimos semestres não tinham mudado esse cenário. A pesquisa existia. O que faltava era um formato que fizesse cada campus percorrer a experiência do próprio aluno antes de propor&nbsp;qualquer coisa."

NOTA_TITULO = "Um&nbsp;mapa não move NPS sozinho"
NOTA = [
    "Quem move é a ação que cada campus toma, e o que&nbsp;estava travado era a leitura da pesquisa. Nos semestres anteriores o&nbsp;relatório chegava e não&nbsp;virava plano.",
    "Com o mapa, os&nbsp;16 campus construíram planos a&nbsp;partir do&nbsp;mesmo material, e a nota geral saiu de&nbsp;33 negativos para 15 positivos no&nbsp;ciclo seguinte.",
]

PROCESSO_TITULO = "Três decisões antes de&nbsp;desenhar qualquer&nbsp;tela"
DECISOES = [
    ("grafico", "Entender os&nbsp;dados do&nbsp;NPS",
     ["Clusterizamos os comentários do NPS em grandes eixos e subcategorias, com uma divisão entre semestres. Era preciso um relatório que ilustrasse a jornada do aluno do início ao fim da graduação, para que a ação surtisse efeito no período específico de cada problema."],
     "A insatisfação deixou de ser uma nota única e&nbsp;passou a ter lugar e momento na jornada."),
    ("pessoa", "Completar o&nbsp;que a&nbsp;reclamação não&nbsp;contava",
     ["As informações que tínhamos não bastavam, e fomos atrás dos alunos para preencher outros aspectos da vida deles. Um aluno que mora longe da instituição sofre muito mais com um cancelamento de aula em cima da hora do que um aluno que mora perto do campus, e nada disso aparece na nota."],
     "As ações passaram a considerar o contexto de&nbsp;vida do&nbsp;aluno, não só a&nbsp;reclamação registrada."),
    ("rota", "Achar um&nbsp;formato que&nbsp;obrigue a&nbsp;percorrer",
     ["Antes do tabuleiro testamos dois formatos mais óbvios, um dashboard de indicadores e um resumo executivo de duas páginas por campus. Os dois falharam pelo mesmo motivo. Entregavam a conclusão pronta, e ninguém precisava percorrer a jornada do aluno para chegar nela. O tabuleiro foi escolhido porque obriga quem lê a&nbsp;andar por semestre e&nbsp;por&nbsp;eixo, e&nbsp;é nesse trajeto que o time reconhece o próprio aluno e&nbsp;propõe ação."],
     "O formato virou parte da solução, não a&nbsp;embalagem da pesquisa."),
]

SOLUCAO_TITULO = "Um&nbsp;tabuleiro com&nbsp;as&nbsp;12 etapas da&nbsp;graduação"
SOLUCAO = [
    "Cada instituição recebeu um mapa interativo para transitar por&nbsp;toda a jornada do estudante, com visualização por&nbsp;semestre e por&nbsp;eixo da vida do&nbsp;aluno.",
    "O mesmo material resume a variação de sentimento entre semestres e&nbsp;as&nbsp;palavras&#8209;chave que aparecem em cada cruzamento de&nbsp;eixo e&nbsp;etapa.",
]
EIXOS = ["Saúde mental", "Saúde física", "Vida financeira", "Expectativa de futuro", "Dores",
         "Experiência com a instituição", "Sugestões", "Aplicativos", "Oportunidades"]
FIGMA = "https://www.figma.com/proto/8fvE9ztg50OQFqWIqGfH3y/Mapa-de-Experie%CC%82ncia-Estudante-Medicina?page-id=221%3A2&amp;node-id=288-1762&amp;starting-point-node-id=288%3A1762&amp;t=rEOOuyzD3vuwNv1m-1"
TELAS = [
    ("jB0FYWxzKTWaMHwYRuFkT0OR8", "O tabuleiro do mapa, com as 12 etapas da graduação distribuídas do START ao FINISH.", "O tabuleiro, do primeiro ao último&nbsp;semestre"),
    ("2u2l4cvOcOdO1jQGPl637PRYmWI", "Uma etapa aberta sobre o tabuleiro, com o achado da pesquisa e a régua de sentimento na base da tela.", "Uma etapa aberta, com a régua de&nbsp;sentimento"),
    ("Gt20MHEWr6seNOXMahLIqb4plQ", "Visão ampla institucional, com experiência, sugestões, apps e oportunidades cruzados com os pares de etapas.", "Visão ampla, lado&nbsp;institucional"),
    ("3IY6aXgfkDIxVCej0xa2DWhplw", "Visão ampla pessoal, com mental, físico, financeiro, futuro e dores cruzados com os pares de etapas.", "Visão ampla, lado&nbsp;pessoal"),
    ("D6BfM2dEe92QhBtCV7Q9lTCTu0", "Gráfico de sentimento com três linhas, financeiro, físico e mental, ao longo dos seis pares de etapas.", "O sentimento por eixo ao longo do&nbsp;curso"),
]
RELATORIOS = ("Relatórios por eixo", "Além do mapa, os principais eixos ganharam relatórios em profundidade, com recortes das entrevistas e as reclamações na íntegra. Os achados foram cruzados com informação de mercado, e cada um veio com uma lista curta de indicadores para acompanhar depois da&nbsp;ação.")

RESULTADO_TITULO = "O&nbsp;relatório passou a&nbsp;ser lido"
RESULTADO = [
    "Com um trabalho de várias mãos, o engajamento com&nbsp;os&nbsp;relatórios mudou de&nbsp;patamar. A média de usuários únicos no primeiro mês era de 20 sem o&nbsp;mapa.",
    "Com o mapa, foram 890 no mesmo período, e são esses acessos que&nbsp;viraram os planos de ação de cada&nbsp;campus.",
]
# Os rótulos ficam curtos porque se alinham à ponta de cada barra.
ACESSOS = ("Usuários únicos no primeiro mês", [
    (None, ("Sem o mapa", "20", 2.2), ("Com o mapa", "890", 100)),
])
# O 890 está nas barras e não volta aqui (decisão 7 da Fase 6). Num terço
# o valor cabe numa linha só, então a unidade vai para a frase.
DADOS = [
    ("seta", "+48", "pontos de NPS, de 33 negativos para 15&nbsp;positivos"),
    ("lapis", "16", "campus construindo plano a&nbsp;partir do mesmo&nbsp;material"),
    ("calendario", "12", "etapas da graduação, cada uma com o&nbsp;próprio recorte de&nbsp;sentimento"),
]
LEVO = "Pesquisa que&nbsp;entrega a&nbsp;conclusão pronta não&nbsp;vira ação."
LEVO_CORPO = "O formato não é embalagem. Quando ele obriga o&nbsp;time a percorrer a jornada, o plano de ação nasce de quem vai executar, e é por&nbsp;isso que&nbsp;ele acontece."
FECHO = 'Precisa transformar pesquisa em&nbsp;ação dentro do&nbsp;time? <a class="link" href="https://wa.me/5511977346175" target="_blank" rel="noopener">Me&nbsp;chama no&nbsp;WhatsApp</a> ou&nbsp;veja o&nbsp;próximo caso.'
PROXIMO = ("case-processo.html", "Processo com IA")


def corpo(pre):
    s = SECOES
    return "\n\n    ".join([
        p.secao(s, 1, f'<p class="t-lead prosa">{PERGUNTA}</p>', p.prosa(CONTEXTO)),
        p.secao(s, 2, p.prosa(*NOTA), p.escala("Nota geral de NPS", -33, 15), titulo=NOTA_TITULO),
        p.secao(s, 3, p.sequencia(pre, DECISOES, cor=ACENTO), titulo=PROCESSO_TITULO),
        p.secao(s, 4, p.prosa(*SOLUCAO), p.etiquetas(EIXOS, "Eixos do mapa"),
                p.galeria(TELAS, (FIGMA, "Abrir o mapa completo")), p.nota(*RELATORIOS), titulo=SOLUCAO_TITULO),
        p.secao(s, 5, p.prosa(*RESULTADO), p.barras(*ACESSOS), p.dados(pre, DADOS, "terco", ACENTO),
                c.callout(LEVO, LEVO_CORPO), c.fechamento(pre, FECHO, PROXIMO), titulo=RESULTADO_TITULO),
    ])
