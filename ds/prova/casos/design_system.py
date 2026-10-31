"""O caso do design system da Omnichat, escrito a partir de
Cases/case_omnichat_design_system.md. As imagens que o texto pedia viraram
peças do Jeff DS, a seu pedido. O antes e depois do sistema é o confronto da
Seção 02, e o MD do componente e a governança viraram os estágios e o funil.

As três versões legadas não foram unificadas. A decisão foi o sistema novo
receber toda tela nova e o legado migrar aos poucos, e é assim que a página
conta. O Dê Para de tokens saiu, porque não fazia parte dessa história."""
import comum as c
import pecas as p

ARQUIVO = "case-design-system.html"
ACENTO = "verde"
TITULO_PAGINA = "Um design system que pessoas e IA usam do mesmo jeito · Jeff Maia"
DESCRICAO = (
    "Na Omnichat, liderei a migração do design system do Figma para o código, com o Claude trabalhando junto "
    "com o time. Com 37 componentes documentados para a IA, as telas que voltavam da revisão de design caíram, "
    "em média, de 10 para 2, e documentar um componente caiu de dois dias para cinco minutos."
)

SECOES = [
    ("contexto", "lupa", "Contexto"),
    ("problema", "alerta", "O problema"),
    ("como-funciona", "camadas", "Como funciona"),
    ("governanca", "verifica", "Governança"),
    ("adocao", "pessoa", "Adoção"),
    ("o-que-deu-errado", "xis", "O que deu errado"),
    ("resultado", "grafico", "Resultado"),
]

BADGES = ["Omnichat", "Design system", "Documentação para IA"]
TITULO = "Um&nbsp;design system que&nbsp;pessoas e&nbsp;IA usam do&nbsp;mesmo jeito"
LEAD = "O sistema era grande e bem estruturado. O&nbsp;problema eram três versões dele em&nbsp;produção e&nbsp;uma documentação que só&nbsp;servia a&nbsp;quem abria o&nbsp;Figma."
FICHA = [
    ("Duração", "1 mês, do plano de migração à&nbsp;primeira versão no&nbsp;código"),
    ("Jeff", "Planejei a migração e negociei com produto, engenharia e&nbsp;as lideranças de&nbsp;desenvolvimento"),
    ("Time", "Os designers, junto comigo na reestruturação do sistema e&nbsp;nas skills do&nbsp;Claude"),
]
SALTO = ("2 dias", "5 minutos", "O tempo para documentar um componente depois de aprovado, com a skill de documentação escrevendo o arquivo que a IA lê e perguntando o que falta antes de&nbsp;fechar.")
CENA = "design-system"

CONTEXTO = "A Omnichat tinha um design system grande e bem estruturado, mas o produto rodava três versões dele ao&nbsp;mesmo tempo. Só a mais nova tinha documentação, e quase tudo sobre uso, anatomia e estilo morava no&nbsp;Figma."
APOIO = "Uma atualização no sistema não chegava nas telas antigas, e coisas começavam a ir para produção sem passar por&nbsp;design."

PROBLEMA_TITULO = "A&nbsp;documentação não&nbsp;servia para&nbsp;a&nbsp;IA"
PROBLEMA = "Quando passamos a pedir telas para o Claude, o problema ficou maior. Boa parte do que existia no Figma não existia na biblioteca do GitHub, e a IA não sabia qual componente usar em cada&nbsp;fluxo."
# Os quadros do sistema saem do arquivo de componentes no Figma, exportados
# por você em 31 de outubro de 2026.
CASOS_DE_USO = ('<img src="assets/casos/design-system/botao-casos-de-uso.jpg" alt="Os casos de uso do Botão, documentados no Figma. À esquerda, a conversa de atendimento no desktop, com um resumo das últimas mensagens e os botões terciários marcados em vermelho. À direita, a mesma conversa no celular, com a mensagem de um cliente pedindo um tênis vermelho." width="1240" height="906" loading="lazy" decoding="async">',
                "Os casos de uso do Botão, documentados no Figma. Uma documentação rica para quem abria o arquivo, e fora do alcance da&nbsp;IA")
PROBLEMA_2 = "O sistema tinha sido feito para designers consultarem. Para servir também à IA, ele precisava mudar de lugar, de dono e de&nbsp;formato."
DIMENSOES = [
    ("Onde mora", "No Figma, com a biblioteca do GitHub atrás", "No código, no repositório do design&nbsp;system"),
    ("Quem cuida", "A engenharia de front&#8209;end", "Design"),
    ("Como nasce", "Desenhado no Figma e depois&nbsp;codado", "Descrito e criado direto no&nbsp;código"),
    ("Documentação", "Só na versão mais nova, escrita para&nbsp;designers", "Um MD por componente, escrito para&nbsp;a&nbsp;IA"),
    ("Telas antigas", "Não recebiam as atualizações do&nbsp;sistema", "Migram aos poucos para o sistema&nbsp;novo"),
]

COMO_TITULO = "Os&nbsp;componentes passaram a&nbsp;nascer no&nbsp;código"
COMO = [
    "Propus que design assumisse o repositório do design system, que até então era da engenharia de front&#8209;end. Os componentes passaram a nascer direto no código, criados com o Claude a partir de descrição e seguindo atomic&nbsp;design.",
    "Não migramos as três versões de uma vez. Toda tela nova passou a nascer no sistema novo, e as antigas migram conforme são refeitas. O legado parou de crescer sem que o produto precisasse&nbsp;parar.",
    "Um conjunto de título e subtítulo vira componente e entra dentro de qualquer outro, se ajustando ao que o componente pai precisa. No Modal, ele aparece duas vezes. E cada componente ganhou um arquivo MD escrito para a IA, com quando usar, comportamento e responsividade por&nbsp;dispositivo.",
]
# O Modal foi exportado do arquivo de componentes no Figma (Playground, nó
# 4634:13448). O MD é uma reconstituição, porque o original ficou no
# repositório da Omnichat. O formato é o que o time usava, e o que está
# no Figma (a largura de 680px, o backdrop, o botão de fechar e as cores
# fixas) entra como está.
MODAL = '<img src="assets/casos/design-system/modal-claro-escuro.png" alt="O Modal do design system no tema claro e no escuro, com o título primário na faixa de cima, o título secundário, o texto e dois botões, um secundário e um primário em amarelo." width="1198" height="451" loading="lazy" decoding="async">'
MODAL_MD = """
    # Modal

    Sobreposição que interrompe o fluxo principal para mostrar uma informação ou pedir uma ação importante, como uma confirmação ou um formulário curto.

    ## Quando usar
    - A pessoa precisa decidir ou preencher algo antes de seguir.
    - O conteúdo extra é curto e não pede rolar a página de trás.

    ## Não use quando
    - A ação é destrutiva e só pede sim ou não. Use Confirmation Dialog.
    - É um aviso que não interrompe nada. Use Toast.

    ## Anatomia
    1. Título primário, na faixa de cima, com o botão de fechar.
    2. Título secundário e texto, o componente Título e subtítulo.
    3. Ações, um botão secundário e um primário, nessa ordem.
    4. Backdrop com 70% de transparência, sempre.

    ## Comportamento
    - A altura acompanha o conteúdo. A largura vai até 680px.
    - O botão de fechar é sempre o Tertiary em color‑fixed‑white.
    - Esc e o clique no backdrop fecham, e o foco volta para quem abriu.
    - As cores vêm do componente e não mudam.

    ## Responsividade
    - Mobile. Largura da tela com 16px de margem, ações empilhadas.
    - Tablet. Centralizado, na largura do conteúdo.
    - Desktop. Centralizado, até 680px.
"""
MODAL_LEGENDA = "O Modal, exportado do Figma, e o MD dele reconstituído no formato que o time usava. O arquivo original ficou no repositório da&nbsp;Omnichat"
COMO_MD = "O MD sai de uma skill de documentação, depois que o componente é aprovado, e o caminho é sempre o&nbsp;mesmo."
ESTAGIOS = [
    ("lapis", "Descrição do&nbsp;componente", "O designer descreve o que o componente faz, em vez de desenhar no&nbsp;Figma.", "Entrada", None),
    ("robo", "Claude e&nbsp;a&nbsp;skill de&nbsp;documentação", "O Claude cria o componente no código, e a skill escreve o MD e pergunta o que está faltando antes de&nbsp;fechar.", "Camada", None),
    ("janela", "O&nbsp;MD do&nbsp;componente", None, "Saída", ["Quando usar", "Comportamento", "Responsividade no mobile, no tablet e no desktop"]),
]

GOVERNANCA_TITULO = "Qualquer área propõe e&nbsp;design aprova"
GOVERNANCA = "Desenvolvedores, QAs e PMs podem propor componentes. Nenhuma proposta chega à base sem passar por design, e o caminho até lá é o&nbsp;mesmo para&nbsp;todas."
FASES = [
    ("Proposta", "Um componente novo, proposto por quem está construindo a&nbsp;tela.", "Dev, QA ou PM"),
    ("Branch de aprovação", "A proposta cai numa branch só de componentes novos, fora da raiz do&nbsp;repositório.", "O repositório"),
    ("Aviso automático", "Design é avisado automaticamente de cada proposta que&nbsp;chega.", "Automação"),
    ("Aprovar ou negociar", "Das 10 propostas que chegaram, 4 viraram evolução de um componente que já existia, em vez de outro com a mesma&nbsp;função.", "Design"),
    ("Raiz do repositório", "As outras 6 entraram como componentes novos, e só aí ganham o MD para&nbsp;a&nbsp;IA.", "Design"),
]
ICONES_FASES = ["lampada", "rota", "megafone", "dialogo", "check"]
VOTACAO_TEXTO = "Quando a dúvida era o nome, a decisão ia para votação. Na Sidebar, quatro nomes foram para a mesa, e cada pessoa do time marcava a opção com a sua bolinha e uma justificativa. SideBar ficou com quatro dos cinco&nbsp;votos."
VOTACAO = ('<img src="assets/casos/design-system/votacao-sidebar.jpg" alt="A votação do nome da Sidebar no Figma. Quatro opções, Drawer, SideNav, SideBar e SlideOut, cada uma numa linha, com um quadro por pessoa do time para o voto e a justificativa. SideBar tem quatro votos e SlideOut tem um." width="1545" height="470" loading="lazy" decoding="async">',
           "A votação do nome da Sidebar, no arquivo de componentes do&nbsp;Figma")

ADOCAO_TITULO = "O&nbsp;sistema saiu do&nbsp;time de&nbsp;design"
ADOCAO = "Deixamos o design system disponível dentro do Claude para qualquer pessoa da empresa. Pessoas de CS, PMM e vendas passaram a prototipar para conversar com clientes, e engenharia, PMs, QAs e designers passaram a consumir a mesma&nbsp;base."
VIRADA = ("Passaram a&nbsp;usar o&nbsp;nosso sistema em&nbsp;vez de&nbsp;improvisar o&nbsp;seu.",
          "Quase todas as áreas já usavam o Claude por conta própria antes da&nbsp;formalização.")

ERRADO_TITULO = "O&nbsp;apego ao&nbsp;jeito antigo pesou mais que&nbsp;a&nbsp;ferramenta"
ERRADO = [
    "A resistência maior veio das pessoas. Designers passaram a descrever em vez de desenhar, e alguns desenhavam no Figma antes de pedir e se frustravam quando o resultado vinha&nbsp;diferente.",
    "O front&#8209;end perguntou o que faria sem a biblioteca. Respondi que eu também não sabia, mas que parte do trabalho dos dois times ia se&nbsp;fundir.",
]
FIGMA = ("Comecei achando que a&nbsp;migração passaria pelo&nbsp;Figma", [
    "Pedíamos para o Claude desenhar no Figma e depois para ele ler o Figma e escrever o código. Um dia paramos e admitimos que era trabalho em dobro, por apego ao jeito&nbsp;antigo.",
])
DE_NOVO = "Se fizesse de novo, amadureceria a primeira versão só entre os designers antes de levar para outras áreas. Vendi o projeto antes de ele existir, sem números, e isso deixou a adoção mais lenta do que&nbsp;precisava."

RESULTADO_TITULO = "Uma base que&nbsp;pessoas e&nbsp;IA leem do&nbsp;mesmo jeito"
RESULTADO = [
    "Com o MD de cada componente, a IA passou a saber qual usar em cada fluxo. As telas que o Claude gerava e voltavam da revisão de design caíram, em média, de 10 para&nbsp;2.",
    "O design system deixou de ser uma biblioteca que só designers consultavam e virou a base que qualquer área da empresa usa para prototipar. Toda tela nova nasce nele, e o legado só&nbsp;diminui.",
]
# Os rótulos ficam curtos porque se alinham à ponta de cada barra.
REVISAO = ("Telas voltando da revisão de design, em média", [
    (None, ("Antes dos MDs", "10", 100), ("Com os MDs", "2", 20)),
])
# O 2 dias e os 5 minutos estão no Salto do Topo, e o 10 e o 2 nas barras.
# Nenhum volta aqui.
DADOS = [
    ("olho", "37", "componentes com documentação escrita para a IA, do&nbsp;mobile ao&nbsp;desktop"),
    ("celular", "15", "pessoas de CS, PMM e vendas prototipando com o sistema para conversar com&nbsp;clientes"),
]
LEVO = "Quem executa não faz igual a&nbsp;você, e&nbsp;funciona."
LEVO_CORPO = "É a mesma lição de quando virei gestor. Ela voltou quando os designers passaram a descrever em vez de desenhar, e o resultado vinha diferente do que eles imaginavam e servia do&nbsp;mesmo&nbsp;jeito."
FECHO = 'Precisa que o design system do seu time sirva para pessoas e para a IA? <a class="link" href="https://wa.me/5511977346175" target="_blank" rel="noopener">Me&nbsp;chama no&nbsp;WhatsApp</a> ou&nbsp;veja o&nbsp;próximo caso.'
PROXIMO = ("case-omnichat.html", "Omnichat")


def corpo(pre):
    s = SECOES
    return "\n\n    ".join([
        p.secao(s, 1, f'<p class="t-lead prosa">{CONTEXTO}</p>', p.prosa(APOIO)),
        p.secao(s, 2, p.prosa(PROBLEMA), p.moldura(*CASOS_DE_USO), p.prosa(PROBLEMA_2),
                p.confronto(DIMENSOES, "O design system antes e depois, em cinco dimensões"), titulo=PROBLEMA_TITULO),
        p.secao(s, 3, p.prosa(*COMO), p.arquivo("modal.md", MODAL_MD, "Reconstituição", MODAL, MODAL_LEGENDA),
                p.prosa(COMO_MD), p.estagios(pre, ESTAGIOS, cor=ACENTO), titulo=COMO_TITULO),
        p.secao(s, 4, p.prosa(GOVERNANCA), p.funil(pre, FASES, ICONES_FASES, cor=ACENTO), p.prosa(VOTACAO_TEXTO),
                p.moldura(*VOTACAO), titulo=GOVERNANCA_TITULO),
        p.secao(s, 5, p.prosa(ADOCAO), p.frase(*VIRADA), titulo=ADOCAO_TITULO),
        p.secao(s, 6, p.prosa(*ERRADO), p.atrito(pre, *FIGMA, cor=ACENTO), p.prosa(DE_NOVO), titulo=ERRADO_TITULO),
        p.secao(s, 7, p.prosa(*RESULTADO), p.barras(*REVISAO), p.dados(pre, DADOS, "meio", ACENTO),
                c.callout(LEVO, LEVO_CORPO), c.fechamento(pre, FECHO, PROXIMO), titulo=RESULTADO_TITULO),
    ])
