"""O caso do Inpulse, com o texto da página publicada antes da Fase 6. As
falas dos alunos ganharam uma Seção própria, a nota "O que a gente cortou"
virou o parágrafo que fecha o Experimento e as telas do Resultado foram
para a moldura (decisões 8 a 11 da Fase 6). Os dois pontos viraram ponto
final (decisão 3).

Na revisão do Jeff, a Descoberta virou três parágrafos corridos ao lado do
protótipo, e a nota "O aluno de medicina" é o do meio. As telas do
Resultado ganharam o recorte, que tira o fundo em volta delas."""
import comum as c
import pecas as p

ARQUIVO = "case-inpulse.html"
ACENTO = "verde"
TITULO_PAGINA = "Solução que ajudou a diminuir a recuperação dos alunos · Jeff Maia"
DESCRICAO = (
    "Boletim, calendário acadêmico e comunicação num app para alunos de medicina. A média de recuperação "
    "caiu de 8 para 6 a cada 10 avaliações por aluno, numa base de 420 alunos."
)

SECOES = [
    ("contexto", "celular", "Contexto"),
    ("aluno", "pessoa", "O aluno"),
    ("descoberta", "lupa", "Descoberta"),
    ("experimento", "lampada", "Experimento"),
    ("resultado", "grafico", "Resultado"),
]

BADGES = ["Inpulse", "Ideação e experimentação", "Graduação em medicina"]
TITULO = "Solução que&nbsp;ajudou a&nbsp;diminuir a&nbsp;recuperação dos&nbsp;alunos"
LEAD = "Uma prova de medicina vira cinco notas separadas e cinco recuperações independentes. Não existia lugar nenhum onde o&nbsp;aluno visse isso junto antes de&nbsp;já estar em&nbsp;recuperação."
FICHA = [
    ("Duração", "10 meses, do primeiro experimento ao&nbsp;primeiro semestre completo de&nbsp;uso"),
    ("Jeff", "Idealizador, mentor, designer UX e UI"),
    ("Time", "Pedro Anjos, designer UI, com&nbsp;a&nbsp;área acadêmica na&nbsp;cocriação"),
]
SALTO = ("8 em 10", "6 em 10", "A média de recuperação por aluno, comparando o semestre anterior ao&nbsp;lançamento com&nbsp;o&nbsp;primeiro semestre completo de&nbsp;uso, numa base de 420 alunos. O app não ensina conteúdo. O efeito veio de o aluno enxergar cedo qual eixo estava abaixo da&nbsp;média.")
CENA = "inpulse"

CONTEXTO_LEAD = "Por limitação técnica, a instituição não conseguia entregar ao&nbsp;aluno um&nbsp;boletim, um calendário acadêmico e&nbsp;uma&nbsp;comunicação que&nbsp;funcionasse."
CONTEXTO = "Antes do Inpulse, o aluno corria atrás da informação em grupo de WhatsApp ou indo até a coordenação, e anotava as próprias notas em algum lugar para conseguir ter uma visão geral do&nbsp;estudo. Cada avaliação da graduação gera cerca de cinco notas separadas, e ele fica de recuperação em cada nota abaixo da média de forma independente. Uma prova só vira vários eixos de estudo espalhados."

ALUNO_TITULO = "O que o&nbsp;aluno dizia"
FALAS = (
    ("“Precisamos correr atrás de&nbsp;nota, elas levam dias para&nbsp;sair, e quando saem a gente tem que&nbsp;anotar pra ver todas em&nbsp;um&nbsp;mesmo lugar. Difícil se preparar dessa maneira.”", "Nota 2 no NPS, de uma estudante no 3º semestre."),
    ("“Com o Inpulse eu não preciso ficar anotando as&nbsp;notas dos complexos temáticos, e isso facilitou pra eu achar o&nbsp;que devo estudar para&nbsp;as recuperações.”", "Aluna do 5º semestre de medicina."),
)

DESCOBERTA_TITULO = "Qual a&nbsp;melhor maneira de&nbsp;entregar um&nbsp;boletim que&nbsp;o&nbsp;aluno use"
DESCOBERTA = [
    "Depois de analisar o NPS, as pesquisas que o time já tinha feito e um dia na vida conduzido por um dos designers, ficou claro que esse aluno está sempre em movimento e precisava de algo de fácil acesso, que estivesse com ele o&nbsp;tempo todo.",
    "O curso é integral e exige muito. Devolver tempo para&nbsp;o&nbsp;que&nbsp;importa, o&nbsp;estudo e&nbsp;o&nbsp;descanso, era o&nbsp;critério que&nbsp;separava uma boa solução de&nbsp;uma&nbsp;solução bonita.",
    "Depois de várias sessões de cocriação com&nbsp;a&nbsp;área acadêmica e&nbsp;com&nbsp;todo o&nbsp;time de produto e desenvolvimento, saímos com&nbsp;um&nbsp;protótipo navegável de alta fidelidade, pronto para&nbsp;validação.",
]
PROTOTIPO = ("https://embed.figma.com/proto/w5TixfaNOqjwjYoY8hZ0cg/Painel-Longitudinal---Aluno?page-id=2891%3A23975&amp;node-id=2891-27267&amp;starting-point-node-id=2891%3A27267&amp;scaling=scale-down&amp;content-scaling=fixed&amp;embed-host=share",
             "Protótipo do aplicativo Inpulse")
PROTOTIPO_LEGENDA = "Navegue pelo app aqui mesmo, ou abra o protótipo em&nbsp;tela&nbsp;cheia."
FIGMA = ("https://www.figma.com/proto/w5TixfaNOqjwjYoY8hZ0cg/Painel-Longitudinal---Aluno?page-id=2891%3A23975&amp;node-id=2891-27267&amp;p=f&amp;viewport=521%2C589%2C0.07&amp;t=N9ol2L7UQFaCxwX8-1&amp;scaling=scale-down&amp;content-scaling=fixed&amp;starting-point-node-id=2891%3A27267",
         "Abrir o protótipo completo")

EXPERIMENTO_TITULO = "Qual funcionalidade o&nbsp;aluno quer primeiro"
EXPERIMENTO = [
    "Estruturamos um experimento para medir a desejabilidade de&nbsp;cada funcionalidade, e assim priorizar o que já sabíamos ser dor do&nbsp;aluno e da&nbsp;empresa.",
    "Usamos a estrutura de um teste de usabilidade, com tarefas oferecidas aos participantes, mas não para medir facilidade. Era para registrar a reação espontânea a cada&nbsp;funcionalidade.",
]
# Os três níveis de desejabilidade são a legenda das pilhas (decisão 10).
NIVEIS = [
    ("cheio", "Entusiasta", "entusiasta", "entusiastas", "Demonstra interesse de maneira espontânea."),
    ("trama", "Receptivo", "receptivo", "receptivos", "Demonstra interesse a partir de uma interação ou pergunta do&nbsp;facilitador."),
    ("vazio", "Indiferente", "indiferente", "indiferentes", "Verbaliza a falta de interesse, ou ignora que a funcionalidade&nbsp;existe."),
]
# Reações de 10 participantes por funcionalidade: entusiasta, receptivo e
# indiferente.
REACOES = ("Reações de 10 participantes, em seis das dez funcionalidades testadas", NIVEIS, [
    ("Próximas avaliações", (0, 8, 2)),
    ("Faltas", (0, 10, 0)),
    ("Situação atual", (1, 9, 0)),
    ("Últimas avaliações", (1, 8, 1)),
    ("Calendário", (3, 7, 0)),
    ("Planejar estudos", (1, 8, 1)),
])
FRASE = ("O calendário doía mais que&nbsp;o&nbsp;boletim.", "De 10 funcionalidades testadas, 4 tiveram entusiasta espontâneo, e&nbsp;o&nbsp;boletim completo, que era a&nbsp;aposta inicial do&nbsp;time, ficou atrás delas.")
CORTE = "Quatro funcionalidades saíram da primeira versão, e no lugar delas priorizamos o acompanhamento por complexo temático, que era o mais caro de construir. Era também o único que respondia à recuperação fragmentada, que é a dor que o caso&nbsp;inteiro persegue."

RESULTADO_TITULO = "Agora o&nbsp;aluno tem mais tempo para&nbsp;estudar"
RESULTADO = [
    "O aluno passou a ter acesso rápido e&nbsp;real à&nbsp;informação de&nbsp;aula, com&nbsp;as&nbsp;notas centralizadas num lugar&nbsp;só.",
    "A primeira versão já mostrou números de&nbsp;engajamento altos no&nbsp;primeiro semestre de&nbsp;lançamento.",
]
TELAS_APP = ("aV4KtUaueCwZ17TJ4mz299XAw", "Telas do aplicativo Inpulse, com o boletim por complexo temático, o calendário acadêmico e a situação atual do aluno.", 3234, 3260)
# As telas ocupam uma faixa diagonal da imagem, com fundo vazio nos cantos.
# Medido no arquivo, o recorte 16:9 centrado só fica sem fundo com a
# imagem em 2 vezes a largura do quadro (com 1,9 ainda escapa 1px).
ZOOM_APP = 2
DADOS = [
    ("celular", "93%", "dos alunos acessando o&nbsp;app"),
    ("calendario", "45%", "acessando ao menos uma&nbsp;vez por&nbsp;dia"),
    ("check", "4,8", "de CSAT na&nbsp;primeira versão"),
    ("grafico", "−25%", "de recuperação por&nbsp;semestre por&nbsp;aluno"),
]
LEVO = "Desejo do&nbsp;usuário e&nbsp;aposta do&nbsp;time raramente são a&nbsp;mesma coisa."
LEVO_CORPO = "O experimento não serviu para confirmar o que a gente queria construir. Serviu para mudar a ordem. O que&nbsp;doía mais entrou antes, mesmo sendo o&nbsp;mais caro."
FECHO = 'Quer conversar sobre produto em educação, ou&nbsp;sobre&nbsp;como medir desejo antes de&nbsp;construir? <a class="link" href="https://wa.me/5511977346175" target="_blank" rel="noopener">Me&nbsp;chama no&nbsp;WhatsApp</a> ou&nbsp;veja o&nbsp;próximo caso.'
PROXIMO = ("case-mapa-experiencia.html", "Mapa de experiência")


def corpo(pre):
    s = SECOES
    return "\n\n    ".join([
        p.secao(s, 1, f'<p class="t-lead prosa">{CONTEXTO_LEAD}</p>', p.prosa(CONTEXTO)),
        p.secao(s, 2, p.citacao(pre, *FALAS, cor=ACENTO), titulo=ALUNO_TITULO),
        p.secao(s, 3, p.ao_lado(p.prosa(*DESCOBERTA), p.moldura(p.prototipo(*PROTOTIPO), PROTOTIPO_LEGENDA, retrato=True, link=FIGMA)),
                titulo=DESCOBERTA_TITULO),
        p.secao(s, 4, p.prosa(*EXPERIMENTO), p.pilhas(*REACOES), p.frase(*FRASE), p.prosa(CORTE), titulo=EXPERIMENTO_TITULO),
        p.secao(s, 5, p.prosa(*RESULTADO), p.moldura(p.tela(*TELAS_APP), zoom=ZOOM_APP), p.dados(pre, DADOS, "meio", ACENTO),
                c.callout(LEVO, LEVO_CORPO), c.fechamento(pre, FECHO, PROXIMO), titulo=RESULTADO_TITULO),
    ])
