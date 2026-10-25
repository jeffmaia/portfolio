"""O caso do Processo com IA, com o texto da página publicada antes da Fase 6.
São oito Seções, e o Design System, que era a sétima, entrou no fim do novo
funil (decisões 12 a 16 da Fase 6). Os dois pontos viraram ponto final e o
"30–40 min" virou "30 a 40 min" (decisão 3)."""
import comum as c
import pecas as p

ARQUIVO = "case-processo.html"
ACENTO = "lime"
TITULO_PAGINA = "Processo de produto e design com Claude no centro · Jeff Maia"
DESCRICAO = (
    "A maior mudança não foi trocar de ferramenta. Foi perceber quantas reuniões existiam só porque ninguém "
    "tinha um jeito melhor de transformar uma conversa em entregável. Discovery de até dois meses para cerca "
    "de uma semana, refinamento semanal de quatro a cinco horas para trinta a quarenta minutos."
)

SECOES = [
    ("contexto", "robo", "Contexto"),
    ("problema", "alerta", "O problema"),
    ("fluxo", "camadas", "O que a gente fez"),
    ("rituais", "calendario", "Rituais"),
    ("lideranca", "pessoa", "Liderança"),
    ("funil", "rota", "O novo funil"),
    ("antes-e-depois", "dialogo", "Antes e depois"),
    ("resultado", "grafico", "Resultado"),
]

BADGES = ["AX", "Processo de produto e design", "IA no fluxo de trabalho"]
# O "Reconstruindo o" saiu para o título caber em quatro linhas (aprovado por
# você em 25 de outubro de 2026).
TITULO = "Processo de&nbsp;produto e&nbsp;design com&nbsp;Claude no&nbsp;centro"
LEAD = "A maior mudança não foi trocar de ferramenta. Foi perceber quantas reuniões existiam só porque ninguém tinha um jeito melhor de&nbsp;transformar uma conversa em&nbsp;entregável."
FICHA = [
    ("Duração", "1 mês para validar o novo desenho, que segue evoluindo"),
    ("Jeff", "Liderei o processo de produto e design, conectando delivery, GA e GTM"),
    ("Time", "Produto, design, engenharia e dados"),
]
SALTO = ("2 meses", "1 semana", "O Discovery caiu de um a dois meses para cerca de uma semana. No mesmo desenho, o refinamento semanal saiu de quatro ou cinco horas para trinta ou quarenta minutos.")
CENA = "processo"

CONTEXTO = "A Omni vende agentes conversacionais para varejo. Configurar esses agentes exige muita tentativa até a conversa ficar boa em&nbsp;produção, e o nosso processo não acompanhava esse&nbsp;ritmo."

# O título da Seção é novo (decisão 13, aprovado), e os dois de hoje ficam nos Passos.
PROBLEMA_TITULO = "Dois gargalos ao&nbsp;mesmo tempo"
PROBLEMAS = [
    ("dialogo", "O&nbsp;trabalho vivia em&nbsp;reunião", "A gente discutia bem e decidia bem. Depois alguém tinha que transformar aquilo em PRD, story, relatório e protótipo. Esse alguém sempre demorava."),
    ("calendario", "A&nbsp;garantia prévia custava semanas", "Como construir era caro, quase toda validação acontecia antes do desenvolvimento. Fazia sentido, e consumia semanas."),
]

FLUXO_TITULO = "Da&nbsp;transcrição ao&nbsp;entregável"
ENTREGAS = [
    ("visao", "lampada", "Visão de produto", "Vira direção antes de virar backlog.", "A habilidade lê a transcrição do ritual e devolve o rascunho da visão. O time revisa e ajusta, em vez de escrever do zero depois da conversa."),
    ("prd", "lapis", "PRD", "Chega pronto para discussão, não para redação.", "Com o PRD já rascunhado, a Planning deixou de ser um rito semanal. Acontece sob demanda, e a maior parte dela é assíncrona."),
    ("us", "janela", "User stories", "Entram no Kanban já documentadas.", "O refinamento virou tirar dúvida sobre o que já está escrito na story e desenhado no protótipo. Foi o que derrubou o ritual de quatro horas para quarenta minutos."),
    ("usabilidade", "lupa", "Relatório de usabilidade", "Análise no lugar de rodada de teste.", "O Claude aponta problema de fluxo com consistência, usando heurística de Norman e Nielsen mais o que a gente já sabe do público da Omni."),
    ("prototipo", "celular", "Protótipo", "Nasce desenvolvido e segue direto para a&nbsp;engenharia.", "O protótipo sai do Claude Design e vai para o Claude Code, de onde a engenharia assume. Design usa o Claude Code para manter a biblioteca fiel à do código, que é a referência principal."),
]
# A saída se chama "Os rascunhos", a palavra que o próprio texto usa (decisão 14).
ESTAGIOS = [
    ("dialogo", "Transcrição dos rituais", "O que o time já falava em reunião, agora capturado como matéria&nbsp;prima.", "Entrada", None),
    ("robo", "Habilidades no&nbsp;Claude", "Habilidades que a gente criou leem a transcrição e devolvem os rascunhos.", "Camada", None),
    ("janela", "Os rascunhos", None, "Saída", [nome for _, _, nome, _, _ in ENTREGAS]),
]
TENTATIVA = ("A primeira tentativa não foi&nbsp;essa", [
    "Cada um usava o Claude do seu jeito, e a gente passou a gerar documento mais rápido e alinhar menos. Dois PRDs da mesma semana com estruturas diferentes, e a engenharia perguntando qual era o padrão. Não existia.",
    "A skill compartilhada nasceu como conserto disso, não como ideia de eficiência.",
])

RITUAIS_TITULO = "Saímos de&nbsp;Scrum para&nbsp;Kanban"
RITUAIS = "Com o rascunho já pronto antes do encontro, o que sobrou para a agenda foi&nbsp;dúvida, não&nbsp;redação."
RITOS = [
    ("calendario", "Planning", "Virou assíncrona e sob&nbsp;demanda, não&nbsp;mais um rito&nbsp;semanal."),
    ("pessoa", "Daily", "Ficou só com engenharia. Produto entra quando&nbsp;precisa."),
    ("lupa", "Refinamento", "De 4 horas para 40&nbsp;minutos, porque virou tirar dúvida sobre o&nbsp;que já&nbsp;está escrito."),
]
USABILIDADE = "Reduzimos bastante teste de usabilidade, porque o Claude passou a apontar problema de fluxo com consistência, usando heurística de Norman e Nielsen mais o que a gente já sabe do&nbsp;nosso público."
CORTE = ("Aqui eu cortei rápido&nbsp;demais", [
    "A análise pegava tudo que é padrão de interface e não pegou a única coisa que travava um fluxo de configuração de agente, que era o nome de um campo no vocabulário de quem trabalha dentro de um varejista. Heurística não pega linguagem de domínio.",
    "Hoje a regra é que teste com gente continua obrigatório quando a entrega traz vocabulário novo ou muda modelo mental.",
])

LIDERANCA_TITULO = "A&nbsp;conversa mais difícil não&nbsp;foi sobre&nbsp;ferramenta"
FRASE = ("O que sobra pra&nbsp;gente?", "A pergunta que o time fez quando ficou claro que o rascunho do documento e da primeira tela sairia automático.")
# "O que destravou" vira o último parágrafo (decisão 15).
LIDERANCA = [
    "Eu respondi com produtividade, mostrando o tempo que aquilo liberava na semana, e foi a resposta errada. Ninguém se acalma ouvindo que vai produzir mais rápido quando a dúvida é se ainda precisa existir.",
    "Por algumas semanas o time usou as skills no mínimo, entregando o suficiente e sem melhorar nada.",
    "O que destravou foi mudar o critério antes da rotina. Parei de avaliar entregável e passei a avaliar decisão. Qual oportunidade entra, onde vale manter atrito, quando o campo está certo e o&nbsp;nome está errado.",
]

FUNIL_TITULO = "Cinco fases, do&nbsp;sinal ao&nbsp;pós&#8209;lançamento"
FASES = [
    ("Identificação de oportunidades", "Dado de produto, pesquisa e canais de feedback alimentam uma árvore de oportunidades que facilita escolher o que entra em pauta.", "Produto e design, com&nbsp;dados alimentando a&nbsp;árvore."),
    ("Validação de desejabilidade e diferencial", "Confirmamos se a aposta faz sentido antes de o time gastar tempo desenhando a solução.", "Produto e design."),
    ("Definição e prototipagem", "É aqui que nasce a maior parte da solução. O&nbsp;protótipo já sai desenvolvido e segue para a&nbsp;engenharia sem etapa de tradução no&nbsp;meio.", "Produto, design e engenharia, com&nbsp;prototipação distribuída entre os&nbsp;três."),
    ("Delivery", "Alfa na engenharia, que garante o funcionamento do que foi construído. Beta, aberto ou fechado, validando o experimento antes de abrir para todos.", "Engenharia no alfa, time inteiro no beta."),
    ("Depois do lançamento", "O foco vira satisfação e adoção. A&nbsp;validação qualitativa entra quando o&nbsp;dado quantitativo mostra desvio do&nbsp;esperado.", "Produto, design e dados, junto de GA e GTM."),
]
FASE_ICONES = ["lupa", "alvo", "lapis", "celular", "grafico"]
# O Design System era a Seção 07. O título dele abre o trecho em t-lead,
# porque a Seção tem um h2 só (decisão 12).
DS_TITULO = "O&nbsp;Design System corre por&nbsp;fora do&nbsp;funil."
DS = [
    "Em paralelo ao funil roda o fluxo do Design System, com componente aprovado direto no código antes de subir para o&nbsp;GitHub.",
    "Hoje áreas fora de design também prototipam, CS inclusive, o que abriu uma discussão interna sobre controle. Resolvi separando o que cada protótipo pode prometer, não restringindo quem&nbsp;cria.",
]
TRILHA = [
    ("lampada", "Criação", "Novo componente nasce a partir de uma&nbsp;necessidade do&nbsp;produto."),
    ("olho", "Comportamento e&nbsp;uso", "Definição escrita pensando também na&nbsp;leitura do&nbsp;Claude."),
    ("verifica", "Aprovação no&nbsp;código", "Validação direto no&nbsp;código, antes de subir para o repositório no&nbsp;GitHub."),
]

CONFRONTO_TITULO = "O&nbsp;mesmo time, com&nbsp;o&nbsp;eixo do&nbsp;trabalho deslocado"
DIMENSOES = [
    ("Prototipação", "Concentrada em design", "Distribuída entre produto, design e engenharia"),
    ("Validação qualitativa", "Quase sempre antes do desenvolvimento", "Depois do lançamento, quando o dado mostra desvio do esperado"),
    ("Rituais", "Longos e na agenda", "Curtos e assíncronos"),
    ("Testes A/B", "Poucas variações, porque cada uma custava caro para construir", "Muitas variações, porque desenvolver ficou ágil e barato"),
]

RESULTADO_TITULO = "Sobrou tempo justamente onde o&nbsp;produto precisa de&nbsp;experimentação"
RESULTADO = [
    "E muito mais experimento rodando, que é o que decide a qualidade da conversa em produção.",
    "Design segue revisando tudo que vira PR.",
]
TEMPOS = ("Tempo antes e depois", [
    ("Discovery", ("Antes", "1 a 2 meses", 100), ("Depois", "~1 semana", 12.5)),
    ("Refinamento semanal", ("Antes", "4 a 5 h", 100), ("Depois", "30 a 40 min", 13)),
])
CONTA = ("A conta estava sendo lida ao&nbsp;contrário", [
    "Um número desses também gera a pergunta que eu não queria receber, se dá para fazer com menos gente. O gargalo nunca foi produzir documento, era decidir com informação suficiente.",
    "O que ganhamos não foi vaga a menos, foi aposta a mais no mesmo trimestre. E mais aposta exige mais gente sabendo julgar resultado.",
])
# O "~1 sem" e o "30 a 40 min" estão nas barras e saem daqui (decisão 16).
DADOS = [
    ("calendario", "Kanban", "no lugar do&nbsp;Scrum, com&nbsp;Planning só&nbsp;quando&nbsp;necessário"),
    ("verifica", "100%", "dos PRs passam por revisão de&nbsp;design"),
]
# A declaração de hoje passa de quatro linhas na tinta. A primeira frase fica
# no Destaque e a segunda vira o corpo, com as mesmas palavras.
LEVO = "O trabalho de design não é mais desenhar a&nbsp;tela primeiro."
LEVO_CORPO = "É decidir, entre tantas coisas que a IA já gera sozinha, onde a atenção humana ainda faz&nbsp;diferença."
FECHO = 'Esse desenho segue em construção na Omni. Se quiser entender como aplicar algo parecido no seu time, <a class="link" href="https://wa.me/5511977346175" target="_blank" rel="noopener">me&nbsp;chama no&nbsp;WhatsApp</a> ou veja o próximo caso.'
PROXIMO = ("case-omnichat.html", "Omnichat")


def corpo(pre):
    s, a = SECOES, ACENTO
    return "\n\n    ".join([
        p.secao(s, 1, f'<p class="t-lead prosa">{CONTEXTO}</p>'),
        p.secao(s, 2, p.par(pre, PROBLEMAS, a), titulo=PROBLEMA_TITULO),
        p.secao(s, 3, p.estagios(pre, ESTAGIOS, a), p.atrito(pre, *TENTATIVA, cor=a),
                p.abas(pre, ENTREGAS, "rascunho", "Os rascunhos", a), titulo=FLUXO_TITULO),
        p.secao(s, 4, p.prosa(RITUAIS), p.ritos(pre, RITOS, a), p.prosa(USABILIDADE), p.atrito(pre, *CORTE, cor=a), titulo=RITUAIS_TITULO),
        p.secao(s, 5, p.frase(*FRASE), p.prosa(*LIDERANCA), titulo=LIDERANCA_TITULO),
        p.secao(s, 6, p.funil(pre, FASES, FASE_ICONES, cor=a), f'<p class="t-lead prosa">{DS_TITULO}</p>', p.prosa(*DS),
                p.trilha(pre, TRILHA, a), titulo=FUNIL_TITULO),
        p.secao(s, 7, p.confronto(DIMENSOES, "O trabalho do time antes e depois, em quatro dimensões"), titulo=CONFRONTO_TITULO),
        p.secao(s, 8, p.prosa(*RESULTADO), p.barras(*TEMPOS), p.atrito(pre, *CONTA, cor=a), p.dados(pre, DADOS, "meio", a),
                c.callout(LEVO, LEVO_CORPO), c.fechamento(pre, FECHO, PROXIMO), titulo=RESULTADO_TITULO),
    ])
