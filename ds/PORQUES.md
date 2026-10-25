# Os porquês do site

Tudo o que hoje está escrito nos comentários do CSS e do HTML e explica uma decisão de uso, organizado pela peça de que fala. Foi extraído por `ds/auditoria/porques.py`, que liga cada comentário à primeira regra ou tag que vem depois dele. O texto é o original, só sem travessão. É a matéria prima das fichas da Fase 3: o campo "Não use quando" e o campo "Limites" saem daqui.

São 271 comentários, 221 ligados a uma peça, 50 de fundação e 0 que o script não soube ligar.

## Índice

- [Barra com assinatura](#barra-com-assinatura) (9)
- [Botão de menu](#boto-de-menu) (2)
- [Menu em painel](#menu-em-painel) (17)
- [Superfícies papel e tinta](#superfcies-papel-e-tinta) (9)
- [Onda](#onda) (8)
- [Rodapé de contato](#rodap-de-contato) (8)
- [Voltar ao topo](#voltar-ao-topo) (1)
- [Passagem entre páginas](#passagem-entre-pginas) (11)
- [Link](#link) (1)
- [Seta de descer](#seta-de-descer) (2)
- [Micro rótulo](#micro-rtulo) (1)
- [Etiquetas de assunto](#etiquetas-de-assunto) (1)
- [Abertura](#abertura) (2)
- [Grito](#grito) (3)
- [Linha de nota](#linha-de-nota) (1)
- [Atrito](#atrito) (1)
- [Citação](#citao) (2)
- [Declaração final](#declarao-final) (4)
- [Hero editorial](#hero-editorial) (9)
- [Topo do caso](#topo-do-caso) (9)
- [Salto](#salto) (2)
- [Convite ao manifesto](#convite-ao-manifesto) (2)
- [Seção](#seo) (39)
- [Bloco com rótulo](#bloco-com-rtulo) (2)
- [Ficha do projeto](#ficha-do-projeto) (2)
- [Cena dos casos](#cena-dos-casos) (10)
- [Linhas indexadas](#linhas-indexadas) (6)
- [Estágios](#estgios) (5)
- [Abas](#abas) (14)
- [Ritos](#ritos) (1)
- [Funil](#funil) (7)
- [Trilha](#trilha) (3)
- [Confronto](#confronto) (4)
- [Conversa](#conversa) (5)
- [Números do resultado](#nmeros-do-resultado) (1)
- [Barras](#barras) (2)
- [Pilhas](#pilhas) (4)
- [Escala de NPS](#escala-de-nps) (1)
- [Moldura](#moldura) (2)
- [Galeria](#galeria) (2)
- [Sangria](#sangria) (1)
- [Régua de leitura](#rgua-de-leitura) (5)
- Fundação (50)
- Sem peça (0)


# Casca, toda página divide


## Barra com assinatura

**assets/base.css:261** `.nav::before`

> Uma névoa do papel atrás da barra, ligada só depois que a página
> anda: sem ela o texto grande do hero passa por baixo da marca e
> as duas se confundem. Parada no topo, a barra não tem fundo
> nenhum e a trama atravessa ela sem emenda.

**assets/base.css:276** `.nav--tinta`

> Sobre as seções escuras a barra inverte inteira. Quem decide é o
> JS, medindo qual fundo está passando debaixo dela.

**assets/base.css:280** `.nav--aberta::before`

> Com o menu aberto o fundo é o painel, que já é escuro.

**assets/base.css:283** `.nav--sem-travessia,
.nav--sem-travessia .wordmark__papel,
.nav--sem-t`

> A marca de um quadro só: na primeira pintura a barra assume a cor
> do fundo sem atravessar até ela. Quem põe e tira é o JS, no mesmo
> quadro em que decide a cor pela primeira vez.

**assets/base.css:290** `.wordmark`

> ── A marca que encolhe ─────────────────────────────────

**assets/base.css:304** `.wordmark__nome`

> O sublinhado verde é o logo inteiro: não existe ícone nem
> moldura. Ele fica neste bloco, que é o que encolhe.

**assets/base.css:311** `.wordmark__dobra`

> Tudo que some na rolagem: fecha a largura em vez de sumir de
> uma vez, para o "J" andar para a esquerda junto.

**assets/base.css:337** `.wordmark__papel`

> O cargo não cabe ao lado do botão num celular; some antes de
> qualquer rolagem.

**index.html:57** `<a class="wordmark">`

> A marca encolhe até a inicial na rolagem. O tracinho verde
> mora no bloco que segura o "J" e o "eff", então encolhe
> junto, sem precisar de uma segunda regra.


## Botão de menu

**assets/base.css:342** `.menu-btn`

> ── O botão de dois tracinhos ─────────────────────────────────

**assets/base.css:366** `.menu-btn:hover .menu-btn__traco:first-child`

> O hover junta os dois tracinhos; o clique cruza eles.


## Menu em painel

**assets/base.css:214** `.menu__item i,
.fecho__link i,
.footer__col i`

> A seta marca o que leva para fora desta página.

**assets/base.css:374** `.reticula`

> O menu
>
> Abre por cima de parte da tela, não da tela inteira: o que fica
> embaixo continua à vista e diz de onde se veio. A borda de baixo
> é a mesma onda das seções, virada de cabeça para baixo.
>
> Os itens são contorno; o preenchimento é a resposta do hover. A
> página em que se está já vem preenchida, em verde.

**assets/base.css:385** `.reticula`

> A retícula
>
> Com o painel aberto, a faixa de página que ainda se vê não fica
> crua: ela recebe um véu e uma trama de pontos por cima, como
> quem passa uma retícula de impressão sobre a foto. Serve a duas
> coisas ao mesmo tempo. Diz que aquilo ali está fora de foco
> agora, e diz que continua existindo, porque a página não some,
> ela só é vista através de alguma coisa.
>
> Três malhas quadradas de passo primo entre si, 3, 4 e 5: uma
> malha sozinha vira papel quadriculado; as três juntas só
> repetem a cada 60px, e a essa distância o olho já leu grão em
> vez de grade. Quadradas por obrigação: com passo diferente na
> horizontal e na vertical, os pontos se enfileiram em colunas e a
> trama vira listra.
>
> Fica abaixo da barra fixa: a marca e o botão de fechar são o que
> não se olha através de nada.

**assets/base.css:485** `.menu__inner`

> A rolagem, quando o painel não couber, é do miolo, não do
> painel: a onda fica pendurada abaixo dele, e um overflow no
> painel a cortaria fora.

**assets/base.css:505** `.menu__lista`

> Um vão entre os itens, para o contorno de uma linha nunca cruzar
> o da linha vizinha: só assim ele fecha só a borda externa da
> letra, sem risco por dentro.

**assets/base.css:578** `.menu__item[aria-current="page"]`

> A página em que se está já vem preenchida, em verde: com o
> traço embaixo e o preenchimento por cima, na mesma cor, a
> letra fecha sólida.

**assets/base.css:594** `.menu__lista--fora .menu__item`

> O segundo grupo sai daqui: corpo menor, cor mais baixa e a seta
> ao lado dizem isso antes do clique.

**index.html:73** `<div class="reticula">`

> Sem aria-hidden aqui: sem script o painel fica aberto no
> fluxo, e a marca fixa esconderia do leitor de tela um menu que
> está à vista. Quem escreve o estado é o JS, que já começa
> fechando o painel.

**index.html:77** `<div class="reticula">`

> A retícula: o véu de pontos que cai sobre a faixa de página que
> o painel não cobre. Fica fora do painel de propósito, porque o
> que ela cobre é a página, não o menu.

**case-processo.html:66** `<div class="reticula">`

> Sem aria-hidden aqui: sem script o painel fica aberto no
> fluxo, e a marca fixa esconderia do leitor de tela um menu que
> está à vista. Quem escreve o estado é o JS, que já começa
> fechando o painel.

**case-processo.html:70** `<div class="reticula">`

> A retícula: o véu de pontos que cai sobre a faixa de página que
> o painel não cobre. Fica fora do painel de propósito, porque o
> que ela cobre é a página, não o menu.

**case-omnichat.html:66** `<div class="reticula">`

> Sem aria-hidden aqui: sem script o painel fica aberto no
> fluxo, e a marca fixa esconderia do leitor de tela um menu que
> está à vista. Quem escreve o estado é o JS, que já começa
> fechando o painel.

**case-omnichat.html:70** `<div class="reticula">`

> A retícula: o véu de pontos que cai sobre a faixa de página que
> o painel não cobre. Fica fora do painel de propósito, porque o
> que ela cobre é a página, não o menu.

**case-inpulse.html:66** `<div class="reticula">`

> Sem aria-hidden aqui: sem script o painel fica aberto no
> fluxo, e a marca fixa esconderia do leitor de tela um menu que
> está à vista. Quem escreve o estado é o JS, que já começa
> fechando o painel.

**case-inpulse.html:70** `<div class="reticula">`

> A retícula: o véu de pontos que cai sobre a faixa de página que
> o painel não cobre. Fica fora do painel de propósito, porque o
> que ela cobre é a página, não o menu.

**case-mapa-experiencia.html:66** `<div class="reticula">`

> Sem aria-hidden aqui: sem script o painel fica aberto no
> fluxo, e a marca fixa esconderia do leitor de tela um menu que
> está à vista. Quem escreve o estado é o JS, que já começa
> fechando o painel.

**case-mapa-experiencia.html:70** `<div class="reticula">`

> A retícula: o véu de pontos que cai sobre a faixa de página que
> o painel não cobre. Fica fora do painel de propósito, porque o
> que ela cobre é a página, não o menu.


## Superfícies papel e tinta

**assets/caso.css:107** `.folha`

> Superfícies
>
> Papel e tinta, alternados. Cada uma carrega a própria trama, e a
> onda pendurada no topo leva o fundo da seção junto para a curva
> não cortar o padrão numa linha reta.

**assets/caso.css:127** `.folha__inner,
.tinta__inner`

> O recuo de baixo precisa caber a onda da seção seguinte, que
> fica pendurada por cima desta, e por isso soma a altura dela ao
> respiro.

**assets/caso.css:135** `main > .folha:last-child .folha__inner,
main > .tinta:last-child .tint`

> A seta de voltar ao topo mora no rodapé, mas sobe para dentro da
> última seção da página. Quem vem logo antes do rodapé abre o chão
> que ela ocupa, senão ela cai em cima do texto. É a mesma conta que
> o fecho da Home já faz.

**assets/caso.css:861** `.tinta .aba`

> Sobre o escuro as mesmas peças trocam de tom.

**assets/caso.css:895** `.tinta .atrito`

> Já estando no escuro, o bloco não precisa de fundo: o traço
> verde e o recuo bastam.

**case-processo.html:259** `<div class="tinta">`

> A parada escura: é aqui que o caso deixa de falar de processo
> e passa a falar de gente.

**case-omnichat.html:192** `<div class="tinta">`

> A parada escura: as cinco camadas do artefato. Elas ficavam
> atrás de uma aba, uma de cada vez. Agora são cinco linhas
> abertas, cada uma com a decisão e o efeito dela.

**case-inpulse.html:180** `<div class="tinta">`

> A parada escura: o que a descoberta encontrou de um lado e o
> protótipo que saiu dela do outro. O protótipo é uma tela de
> celular, vertical: ocupando a página inteira ele deixava duas
> faixas de fundo escuro do tamanho dele em volta. Numa coluna,
> a altura que ele pede passa a ser a altura da seção, e o texto
> corre ao lado em vez de empurrar o protótipo para longe.
>
> O escuro aqui existe para a tela do app ser a única coisa
> clara da seção.

**case-mapa-experiencia.html:203** `<div class="tinta">`

> A parada escura: como a pesquisa virou esse formato. As três
> etapas ficavam atrás de uma aba, uma por vez; agora são três
> linhas abertas, com a consequência de cada uma no fim.


## Onda

**assets/base.css:868** `.onda-defs`

> A onda entre as seções
>
> Fica pendurada acima da própria seção (bottom:100%) e leva o
> fundo dela inteiro (cor e trama) recortado pela curva. Pintar
> só a cor deixava a onda lisa e a trama começava numa linha reta
> logo abaixo dela. O caminho já vem desenhado no HTML, então
> funciona sem JS; com JS ele é redesenhado a cada quadro.

**assets/base.css:907** `.onda--pe`

> A mesma onda virada: pendurada abaixo do elemento em vez de
> acima dele. É a borda de baixo do painel do menu.

**assets/base.css:917** `.onda--bolha,
.onda--subir`

> ── A onda com bolha ────────────────────────────────
> Onde a página tem uma seta, a onda sobe num morro e a seta fica
> dentro dele. Não é um círculo colado por cima: é a mesma curva,
> que incha num ponto e volta a ser onda dos dois lados.
>
> O elemento tem o dobro da altura de uma onda comum, e o morro
> cabe nessa metade de cima. A linha de repouso é redesenhada na
> mesma altura absoluta de sempre (0.5167 de uma altura, que em
> duas viram 0.7583), então as ondas com e sem bolha continuam
> nascendo no mesmo lugar da página.
> ────────────────────────────────────────────────

**index.html:43** `<svg class="onda-defs">`

> Os recortes das ondas. O primeiro serve a todas as bordas
> comuns: elas são desenhadas no mesmo quadro e na mesma fase, e o
> clipPath em objectBoundingBox estica a forma até a largura de
> cada seção. Os outros dois são as ondas que carregam uma seta e
> incham num morro no meio da largura para recebê-la: uma para a
> cena, outra para o rodapé, porque o morro do rodapé cresce com a
> rolagem e o da cena não. Os três já vêm desenhados aqui, então
> as bordas existem sem JS.

**case-processo.html:40** `<svg class="onda-defs">`

> O recorte da onda é um só para todas: elas são desenhadas no
> mesmo quadro e na mesma fase, e o clipPath em objectBoundingBox
> estica a forma até a largura de cada seção. O caminho já vem
> desenhado aqui, então a borda ondulada existe sem JS.

**case-omnichat.html:40** `<svg class="onda-defs">`

> O recorte da onda é um só para todas: elas são desenhadas no
> mesmo quadro e na mesma fase, e o clipPath em objectBoundingBox
> estica a forma até a largura de cada seção. O caminho já vem
> desenhado aqui, então a borda ondulada existe sem JS.

**case-inpulse.html:40** `<svg class="onda-defs">`

> O recorte da onda é um só para todas: elas são desenhadas no
> mesmo quadro e na mesma fase, e o clipPath em objectBoundingBox
> estica a forma até a largura de cada seção. O caminho já vem
> desenhado aqui, então a borda ondulada existe sem JS.

**case-mapa-experiencia.html:40** `<svg class="onda-defs">`

> O recorte da onda é um só para todas: elas são desenhadas no
> mesmo quadro e na mesma fase, e o clipPath em objectBoundingBox
> estica a forma até a largura de cada seção. O caminho já vem
> desenhado aqui, então a borda ondulada existe sem JS.


## Rodapé de contato

**assets/base.css:947** `.footer__grid`

> O rodapé também mora na grade de doze colunas: seis para o
> contato, três para cada lista. Antes ele corria em frações
> próprias (1.6fr, 1fr, 1fr), que é justamente o tipo de medida
> que não se alinha a nada no resto da página.

**assets/base.css:1010** `.footer__subir`

> Voltar ao topo
>
> A seta mora dentro da onda preta do rodapé, no morro que a
> própria onda faz para recebê-la. Conforme a página chega ao fim,
> o morro cresce e a seta sobe junto com ele: são os dois dizendo,
> sem escrever, que dali em diante só se anda para cima.
>
> A seta não sobe por conta própria: ela senta a uma distância
> fixa do alto do morro, e é o morro que cresce. O JS mede esse
> alto no mesmo quadro em que redesenha a curva e escreve o
> número aqui. Sem JS o número cai no padrão, e a seta aparece no
> alto do morro já desenhado no HTML.

**assets/base.css:1025** `.footer__subir`

> A seta pendura pelo alto do morro: desce a altura dela mais um
> pouco mais de meia altura de folga, e é aí que ela senta. A conta
> é na altura da seta, não numa fração da onda, porque a seta para
> de encolher antes da onda: no celular uma fração fixa dava cinco
> pixels de preto acima da ponta e a seta encostava no contorno.
>
> Quem escreve --pico-subir é o JS, no mesmo quadro em que redesenha
> a curva: a seta não sobe por conta, ela sobe porque o morro subiu.
> Sem JS o número cai no padrão, que é o alto do morro já desenhado
> no HTML.

**index.html:301** `<div class="footer__subir">`

> A seta de voltar ao topo mora dentro da onda preta, no morro
> que a onda faz para recebê-la. Conforme a página chega ao
> fim, o morro cresce e a seta sobe junto com ele: são os dois
> dizendo, sem escrever, que dali em diante só se anda para
> cima. É o par exato da seta de descer, lá no alto.
>
> #top e não um id nosso: a barra é fixa, e uma âncora para um
> elemento fixo não faz o navegador rolar nada. "#top" sem
> elemento correspondente é o fragmento que o HTML define como
> "o começo do documento".

**case-processo.html:577** `<div class="footer__subir">`

> A seta de voltar ao topo mora dentro da onda preta, no morro
> que a onda faz para recebê-la. Conforme a página chega ao
> fim, o morro cresce e a seta sobe junto com ele: são os dois
> dizendo, sem escrever, que dali em diante só se anda para
> cima.
>
> #top e não um id nosso: a barra é fixa, e uma âncora para um
> elemento fixo não faz o navegador rolar nada. "#top" sem
> elemento correspondente é o fragmento que o HTML define como
> "o começo do documento".

**case-omnichat.html:402** `<div class="footer__subir">`

> A seta de voltar ao topo mora dentro da onda preta, no morro
> que a onda faz para recebê-la. Conforme a página chega ao
> fim, o morro cresce e a seta sobe junto com ele: são os dois
> dizendo, sem escrever, que dali em diante só se anda para
> cima.
>
> #top e não um id nosso: a barra é fixa, e uma âncora para um
> elemento fixo não faz o navegador rolar nada. "#top" sem
> elemento correspondente é o fragmento que o HTML define como
> "o começo do documento".

**case-inpulse.html:413** `<div class="footer__subir">`

> A seta de voltar ao topo mora dentro da onda preta, no morro
> que a onda faz para recebê-la. Conforme a página chega ao
> fim, o morro cresce e a seta sobe junto com ele: são os dois
> dizendo, sem escrever, que dali em diante só se anda para
> cima.
>
> #top e não um id nosso: a barra é fixa, e uma âncora para um
> elemento fixo não faz o navegador rolar nada. "#top" sem
> elemento correspondente é o fragmento que o HTML define como
> "o começo do documento".

**case-mapa-experiencia.html:420** `<div class="footer__subir">`

> A seta de voltar ao topo mora dentro da onda preta, no morro
> que a onda faz para recebê-la. Conforme a página chega ao
> fim, o morro cresce e a seta sobe junto com ele: são os dois
> dizendo, sem escrever, que dali em diante só se anda para
> cima.
>
> #top e não um id nosso: a barra é fixa, e uma âncora para um
> elemento fixo não faz o navegador rolar nada. "#top" sem
> elemento correspondente é o fragmento que o HTML define como
> "o começo do documento".


## Voltar ao topo

**assets/base.css:1061** `.subir::after,
.descer::after`

> O alvo do dedo é a região, não a letra e o traço dentro dela. O
> rótulo tem a largura da frase, a seta tem dezesseis pixels, e
> entre os dois havia um vão de meia onda que não pertencia a
> ninguém: um toque no meio, que é onde o olho mira, caía fora do
> link. Agora o alvo começa acima do rótulo, desce uma altura de
> seta abaixo da ponta e sobra quase cem pixels para cada lado, com
> duzentos e quarenta de piso para a seta sozinha nunca ficar mais
> estreita que um dedo.
>
> Embaixo ele entra um pouco no preto da onda, que é onde o dedo
> sobra quando mira a seta. Não há nada clicável ali: o pé do rodapé
> começa bem abaixo. Nada disso aparece no desenho.


## Passagem entre páginas

**assets/base.css:636** `.transicao`

> A passagem de uma página para outra
>
> Quatro tempos, em fila, e nenhum deles se move: a passagem
> inteira é feita de opacidade e de uma largura.
>
> 1. A tela fecha. O que estava escrito se apaga e o preto sobe ao
>    mesmo tempo, um cruzando o outro. Já foi em duas etapas, o
>    apagamento primeiro e a cortina depois, e do rodapé aquilo era
>    um defeito à vista: a tela inteira ali é o rodapé preto, então
>    apagá-lo devolvia o fundo claro do corpo, e sobrava um quadro
>    de tela vazia e clara antes de escurecer. Uma coisa saindo
>    enquanto a outra entra não tem esse buraco.
>
>    De dentro do menu quem se apaga é o miolo do painel, e quem
>    cobre é o próprio painel crescendo até a tela toda; ali a
>    cortina só precisa estar acesa a tempo do J.
> 2. Com a tela já fechada e parada, o J entra, e só depois de ele
>    estar inteiro a barra começa a encher. A barra é o que se veio
>    ver: dividir o começo dela com a entrada do J era gastar um
>    terço do percurso por baixo de uma letra que ainda chegava.
> 3. A barra atravessa a troca de página. Ela vai até uma fração de
>    si mesma deste lado, a navegação acontece com ela em
>    movimento, e ela termina de encher já na página nova. Antes ela
>    fechava inteira antes da navegação, e o que a pessoa via era
>    uma animação terminando de contar o carregamento antes de o
>    carregamento começar: o tempo de espera de verdade ficava com
>    uma barra cheia e parada por cima.
> 4. Quando a barra fecha, o J sai, a cortina sai atrás dele e a
>    página nova aparece por baixo.
>
> Fade e não deslize, porque o que está sendo dito aqui não é
> direção, é troca: uma coisa acaba e outra começa no mesmo lugar.
> Onda e biquinho continuam sendo a borda entre as seções e a
> borda do painel; a passagem deixou de disputar isso com elas.
>
> A cortina que chega é animação de CSS puro, disparada por uma
> classe posta no <html> ainda no <head>. Se o script de baixo
> falhar, ela sai sozinha: página coberta é falha grave demais
> para depender de um caminho só.

**assets/base.css:694** `.transicao__marca`

> O traço verde debaixo do J é a barra. Eram duas coisas, o traço
> parado que é a marca e uma barra à parte mais abaixo, dizendo a
> mesma coisa duas vezes em dois lugares. Agora o traço nasce sem
> largura nenhuma e enche até a largura da letra: quando ele
> fecha, a marca está inteira e a página está pedida.
>
> O trilho apagado atrás diz onde o traço vai chegar. Sem ele, um
> traço crescendo é um enfeite se mexendo; com ele, é uma barra.

**assets/base.css:725** `.transicao__marca i`

> O traço enche em dois pedaços, um de cada lado da navegação, e a
> fração onde ele para é a costura entre os dois. Fica num nome só
> para os dois lados não poderem discordar: qualquer diferença aqui
> apareceria como um salto da barra no instante da troca.

**assets/base.css:753** `.transicao.saindo`

> Sem atraso: a cortina sobe no mesmo instante em que a página se
> apaga, e uma cruza a outra. Qualquer folga aqui aparece do rodapé
> como um quadro de tela clara e vazia. As duas são o mesmo tempo,
> o apagamento; o que vem depois é outro.

**assets/base.css:773** `.transicao.saindo .transicao__marca`

> O J entra com a tela já fechada, nos dois caminhos, e não em cima
> do apagamento: entre um tempo e outro há 140ms de preto parado,
> que é o que faz os dois serem lidos como duas coisas em fila e não
> como uma coisa só acontecendo ao mesmo tempo.

**assets/base.css:778** `.transicao.saindo .transicao__marca i`

> Linear, e não com a curva de saída: uma barra que acelera e
> desacelera está contando uma história sobre o carregamento que
> ela não tem como saber. Passo constante é a única coisa honesta
> que uma barra de tempo fixo pode dizer.
>
> Ela termina este pedaço no instante exato da navegação, e não
> antes. Enchendo até o fim deste lado, a barra acabava enquanto a
> página velha ainda estava lá, e o carregamento de verdade, que é
> o que ela existe para cobrir, começava com ela já cheia. O resto
> dela está do outro lado.

**index.html:358** `<div class="transicao">`

> A cortina da passagem entre páginas. Fica fora da tela até que
> um link interno seja clicado, ou até que a página anterior peça
> a entrada.

**case-processo.html:634** `<div class="transicao">`

> A cortina da passagem entre páginas. Fica fora da tela até que
> um link interno seja clicado, ou até que a página anterior peça
> a entrada.

**case-omnichat.html:459** `<div class="transicao">`

> A cortina da passagem entre páginas. Fica fora da tela até que
> um link interno seja clicado, ou até que a página anterior peça
> a entrada.

**case-inpulse.html:470** `<div class="transicao">`

> A cortina da passagem entre páginas. Fica fora da tela até que
> um link interno seja clicado, ou até que a página anterior peça
> a entrada.

**case-mapa-experiencia.html:477** `<div class="transicao">`

> A cortina da passagem entre páginas. Fica fora da tela até que
> um link interno seja clicado, ou até que a página anterior peça
> a entrada.


# Ação e navegação


## Link

**assets/base.css:205** `.link`

> O sublinhado é o tratamento inteiro do link: nada de mudar peso
> ou cor no hover.


## Seta de descer

**assets/base.css:1088** `.descer`

> O par da seta de cima, na onda que abre a seção dos casos. Mesmo
> morro, mesma distância, sentido contrário.

**index.html:176** `<a class="descer">`

> A seta desceu para dentro da onda preta da cena, no morro
> que a própria onda faz para recebê-la. O rótulo fica acima
> do morro, ainda no fundo escuro do hero. É o par exato da
> seta de voltar ao topo, no morro do rodapé.


# Texto e rótulo


## Micro rótulo

**assets/caso.css:367** `.rotulo`

> O rótulo miúdo que abre um bloco. Sem margem própria: quem dá o
> respiro é a linha do grupo.


## Etiquetas de assunto

**assets/caso.css:230** `.etiquetas`

> As etiquetas de assunto, sem fundo e sem moldura. A última é a
> que muda de cor.


## Abertura

**assets/caso.css:384** `.abertura`

> Abertura
>
> O parágrafo de entrada da seção, em corpo grande, na margem
> esquerda e no mesmo prumo do rótulo que abre a seção.

**assets/caso.css:391** `.abertura`

> Sete colunas a partir da primeira: a linha de leitura de um corpo
> grande fica em pouco mais de sessenta caracteres, e a margem que
> sobra à direita é o que mantém o parágrafo com cara de entrada e
> não de bloco de texto. Ele começa na margem, no mesmo prumo do
> rótulo da seção: um recuo aqui só faria a leitura procurar onde
> começa.


## Grito

**assets/caso.css:950** `.grito`

> Grito: a frase que a seção existe para carregar

**assets/caso.css:973** `.grito-par`

> O grito e a nota dele descem numa coluna só, na mesma margem.
> Lado a lado, com a nota alinhada pela base da frase, o leitor
> tinha que adivinhar se começava pela manchete ou pela letra miúda
> ao lado dela. E o mesmo par aparecia em duas páginas com duas
> formas diferentes, sem que nada no conteúdo justificasse a
> diferença. Uma forma só: a frase, e embaixo de onde ela veio.

**assets/caso.css:981** `.grito-par .grito`

> Duas linhas de manchete, não uma linha e meia atravessando a
> página: o grito perde um pouco de corpo para caber na coluna de
> leitura e ficar no mesmo prumo de tudo que vem depois.


## Linha de nota

**assets/caso.css:990** `.linha-nota`

> A linha final da seção: rótulo na margem, texto do lado.


## Atrito

**assets/caso.css:877** `.atrito`

> Atrito
>
> Onde a coisa deu errado. Bloco escuro dentro do papel: é o que
> um leitor apressado mais precisa achar, e é também o que quebra
> a página sem custar uma troca de fundo inteira.


## Citação

**assets/caso.css:1322** `.citacoes`

> Citação
>
> A fala de quem usou. Sem aspas desenhadas e sem cartão: o traço
> verde na margem já diz que a voz mudou, e é o mesmo traço do
> bloco de atrito. Duas falas, seis colunas cada.

**assets/caso.css:1345** `.citacao p`

> A fala tem medida de leitura própria. Nas doze colunas do celular
> largo ela chegava a mais de oitenta caracteres por linha, que já é
> muito para texto corrido e é demais para uma citação em corpo
> grande: são três linhas em que o olho tem de voltar do fim ao
> começo sem nenhuma marca no caminho.


## Declaração final

**assets/caso.css:1256** `.fecho`

> Fecho: o que fica do caso e para onde ir

**assets/caso.css:1271** `.fecho--unido`

> O que fecha o caso não se parte em duas colunas: partir aqui obrigava
> a ler metade de um lado e a outra metade do outro, sem nada explicar
> por quê. A frase e o que a explica descem na mesma coluna, um sob o
> outro, na mesma margem.

**assets/caso.css:1280** `.fecho--unido .corpo-texto`

> Junto, o texto do fecho ocupa oito colunas, e nessa largura a linha
> passa dos noventa caracteres. Quem manda aqui é a medida, não a
> grade. Vem depois da regra de cima de propósito: as duas têm o mesmo
> peso, e a última é a que vale.

**assets/caso.css:1764** `.fecho .corpo-texto`

> Empilhado, o texto do fecho ocupa as doze colunas, e nessa
> largura a linha passa dos noventa caracteres. A medida volta a
> ser a do texto, não a da grade.


# Abertura de página


## Hero editorial

**assets/home.css:29** `.hero`

> Hero
>
> A grade editorial: cada palavra e cada fotografia pesam o
> mesmo, em fileiras que se alternam lado a lado até fechar um
> retângulo só, sem vão entre elas. O fundo continua claro, como
> sempre foi: quem muda de cor é só a onda que abre a cena logo
> abaixo, escurecendo para receber a seta, igual a onda que abre
> o rodapé.
>
> A seta de descer mora dentro da onda preta da cena, no morro
> que ela faz para recebê-la; ver .descer, em base.css.

**assets/home.css:43** `.hero`

> O hero é o berço da seta, e a onda da cena passa por cima dele:
> sem o z-index, o preto da onda cobriria a seta.
>
> E ele abre uma tela inteira, nem mais nem menos. Antes tinha a
> altura do que havia dentro dele e mais nada, que numa janela de
> notebook dava oitocentos pixels de conteúdo dentro de seiscentos e
> poucos de tela: a onda e a seta caíam abaixo da dobra, e quem
> chegava não via que a página continuava.
>
> svh, e não vh: no celular vh é a tela sem as barras do navegador,
> que só somem depois de rolar. A promessa aqui é justamente a de
> antes de rolar, então a medida tem que ser a da tela com as barras
> à vista.

**assets/home.css:111** `.hero__linha`

> A frase mais longa ("continua o mesmo.") é quem decide o teto:
> num corpo maior ela sozinha já enche a coluna de 920px e a foto
> desaparece. O tamanho aqui é o maior que ainda deixa uma faixa
> de foto visível nessa fileira, mesmo com uma só tipografia para
> as quatro.

**assets/home.css:137** `.hero__titulo`

> Cada foto guarda duas imagens sobrepostas, e a troca não
> acontece uma vez só: ela roda em looping. As duas imagens sobem
> juntas, como um filme vertical de dois quadros. A de baixo entra
> e a de cima sai no mesmo movimento, sempre a exatamente uma
> altura de distância, então nunca abre um vão entre elas.
>
> As quatro trocas são uma sequência, não um acorde: a de cima
> termina antes de a de baixo começar. Por isso o intervalo entre
> fileiras (--foto-passo) é maior que a subida em si.
>
> A conta não pode sair de --atraso: aquele é o escalonamento
> curto do texto, de 90ms, e ele existe para as frases entrarem
> quase juntas. A foto quer o contrário.
>
> Sem movimento (JS desligado, ou movimento reduzido) nada roda e
> só a primeira imagem aparece.

**assets/home.css:202** `.hero`

> Empilhada, a fileira muda de forma e a conta muda junto: não são
> mais quatro fileiras iguais, são quatro frases mais quatro
> faixas. A frase é a parte que não se aperta, porque ela é o que
> se lê; quem paga a conta da tela baixa é a faixa.
>
> E a frase de baixo deixa de ser uma linha: na coluna estreita ela
> ocupa três, e o orçamento precisa saber disso, senão reserva um
> terço do que ela vai pedir.

**assets/home.css:216** `.hero__titulo`

> Empilhado, o vão entre fileiras tem que ser maior que o vão
> entre a frase e a foto dela: senão cada frase parece legenda
> da foto de cima, e não título da foto de baixo.

**assets/home.css:234** `.hero__foot`

> A linha de baixo mora na mesma coluna estreita da grade, numa
> linha só enquanto couber.

**index.html:108** `<section class="hero">`

> O hero virou a mesma trama escura da cena logo abaixo: as
> duas dividem cor e textura de propósito, para a onda entre
> elas sumir e a rolagem começar como um bloco só. Palavra e
> fotografia agora pesam igual, cada par numa fileira própria
> em vez de dentro da frase corrida; por isso o par de fotos
> que trocava sozinho no scroll virou duas fotos fixas, uma em
> cada fileira.
>
> As fotos vão com alt vazio de propósito: aqui elas são ritmo
> de leitura, não conteúdo. O que o leitor de tela ouve é a
> frase inteira, sem interrupção.

**index.html:121** `<h1 class="hero__titulo">`

> As quatro fileiras têm foto, e as trocas acontecem uma
> depois da outra, de cima para baixo, em looping.
>
> O lado da foto alterna: texto e foto, foto e texto,
> texto e foto, foto e texto. Quem manda é a ordem do
> HTML, e ela vale só no desktop; em tela estreita a
> fileira empilha e o texto vem sempre primeiro, para a
> leitura não trocar de perna no meio da frase.
>
> São 6 fotos reais para 8 posições, então duas aparecem
> duas vezes. O emparelhamento acima não é aleatório: as
> quatro primeiras imagens são diferentes entre si, as
> quatro finais também, e as duas repetidas entram como
> foto de baixo numa fileira que já trocou antes de
> reaparecerem como foto de cima mais abaixo. Assim a
> mesma imagem nunca está em duas fileiras ao mesmo tempo.
> Quando houver duas fotos novas, elas entram no lugar de
> jeito-teclado (base) e jeito-wireframe (base) e a
> repetição some.


## Topo do caso

**assets/caso.css:1** `.caso`

> Caso: a página de um caso, por dentro
>
> Continua de onde o cartão da Home parou: quem clica no caso em
> destaque, que lá é o bloco escuro, chega num topo escuro igual.
> Daí em diante a página alterna papel e tinta, e cada troca é uma
> onda, o mesmo recorte da Home.
>
> Só o que é da página de caso mora aqui. Tokens, barra do topo,
> ficha, onda, rodapé e movimento vêm de base.css.
>
> ── A grade ──────────────────────────────────────────────
>
> Esta folha foi refeita sobre uma grade de 12 colunas. Ela nunca
> aparece, mas tudo se apoia nela: não existe mais bloco que
> invente o próprio arranjo de colunas, e nenhuma margem nasce de
> um número escolhido no olho.
>
> Doze porque divide bem: 2, 3, 4 e 6 colunas iguais saem da mesma
> grade, e é isso que faz três ritos, quatro números, cinco fases
> e duas conversas caberem no mesmo desenho sem cada seção virar
> uma exceção.
>
> Três regras seguram a coisa toda:
>
> 1. A calha é uma só na página inteira (--calha), e a margem
>    externa também (--gutter, de base.css).
>
> 2. Todo elemento começa e termina numa coluna. Nada de largura
>    solta: onde antes havia max-width em ch ou uma fração
>    inventada (1.35fr, .62fr), agora há um intervalo de colunas.
>
> 3. As larguras mudam por faixa de tela trocando o intervalo de
>    colunas, nunca a grade. São três faixas: larga (1100 para
>    cima), média (720 a 1099) e estreita (abaixo de 720), e na
>    estreita quase tudo ocupa as doze.
>
> ── O respiro ────────────────────────────────────────────
>
> Três níveis, e cada um pelo menos o dobro do de dentro, que é o
> que faz o olho agrupar sem precisar de moldura nem de fio:
>
>   dentro de um grupo   16   rótulo e o que ele nomeia
>   entre blocos         48   linha da seção
>   entre seções         96   e a troca de papel para tinta soma
>                             o recuo da superfície a isso
>
> As medidas saem todas da régua de base.css. Nesta folha não
> existe valor de espaço escrito à mão.

**assets/caso.css:52** `.caso`

> Quebra de linha
>
> Duas regras para a página inteira, porque quebra de linha é
> decisão de leitura, não sobra de largura:
>
> - título quebra equilibrado, nunca deixando uma palavra sozinha
>   na última linha;
> - parágrafo nunca termina com uma palavra órfã.
>
> O resto é o &nbsp; escrito no texto, que amarra artigo e
> preposição na palavra que eles regem.

**assets/caso.css:192** `.caso-topo`

> Topo do caso
>
> O título grande à esquerda, o texto de apoio e o número
> dividindo a linha de baixo. O número é o salto: de quanto era
> para quanto passou a ser.

**assets/caso.css:200** `.caso-topo`

> A barra é fixa e o corpo abre o vão dela lá em base.css. Num caso
> o topo é escuro, e esse vão claro deixava uma tira de papel na
> altura da barra, com a marca clara em cima dela. O topo sobe para
> debaixo da barra e devolve a altura dela como respiro de dentro.

**assets/caso.css:251** `.caso-topo h1::after`

> O traço verde no fim do título é o gesto de marca-texto da
> referência: ela põe um risco depois da última palavra de cada
> linha. Aqui basta um, no fim da frase.

**assets/caso.css:1678** `.caso-topo h1`

> Tela média: de 720 a 1099
>
> A grade continua de doze colunas. O que muda é o intervalo que
> cada bloco ocupa: o que era metade passa a ser quase tudo, e o
> que corria em quatro por fileira passa a correr em dois.

**assets/caso.css:1776** `.caso-topo__lead,
  .salto,
  .secao > .corpo-texto,
  .secao > .legen`

> Tela estreita: abaixo de 720
>
> Uma coluna de leitura. A grade não some, mas quase tudo passa a
> ocupar as doze colunas, e o que era lado a lado empilha na ordem
> em que se lê.

**case-processo.html:101** `<header class="caso-topo">`

> O topo repete o escuro do cartão da Home de propósito: quem
> clicou no caso em destaque chega no mesmo lugar de onde saiu.
> O título fica sozinho na largura toda; o salto e o texto de
> apoio dividem a linha de baixo.

**case-omnichat.html:102** `<header class="caso-topo">`

> O topo escuro é o mesmo de todos os casos: quem clicou no
> cartão da Home chega no fundo de onde saiu. O salto aqui é a
> conversão por origem, de quanto era para quanto passou a
> ser.


## Salto

**assets/caso.css:283** `.salto`

> O salto: o número velho riscado em verde, o novo em corpo grande
> logo abaixo.

**assets/caso.css:286** `.salto__de`

> O número riscado é a metade de cima do salto: se ele não se lê, o
> número grande embaixo perde a comparação e vira só um número. Por
> isso ele sai do corpo miúdo e sobe para perto do corpo de texto.


## Convite ao manifesto

**assets/home.css:463** `.fecho`

> Fecho
>
> Um respiro claro entre a cena e o rodapé, e o lugar próprio do
> manifesto, que antes disputava espaço com o lead do hero.

**index.html:286** `<section class="fecho">`

> Um respiro claro entre a cena e o rodapé, e o lugar próprio
> do manifesto, que antes disputava espaço com o lead do hero.


# Organização


## Seção

**assets/base.css:826** `.secao__head`

> Cabeçalho de seção
>
> Um rótulo curto e uma régua que atravessa o resto da largura.
> É o que numera as seções em qualquer página.

**assets/caso.css:144** `.grade,
.secao`

> A grade
>
> Doze colunas, uma calha só. Quem quiser participar da grade
> herda esta classe, e é ela que faz o miolo de um componente
> cair exatamente nas mesmas colunas do resto da página.
>
> Um contêiner que ocupa as doze colunas pode redesenhar as doze
> por dentro sem sair do prumo: as pistas são iguais e a calha é a
> mesma, então a coluna 7 de dentro cai em cima da coluna 7 de
> fora. É o que .linhas, .estagios e .confronto fazem.

**assets/caso.css:164** `.secao`

> Entre blocos de uma seção, sempre a mesma linha de respiro.

**assets/caso.css:167** `.secao > *`

> O padrão é ocupar a largura toda. Quem for mais estreito diz
> abaixo em quais colunas cabe, e assim nenhum bloco fica com uma
> largura que não veio da grade.

**assets/caso.css:188** `.secao__topo .secao__head`

> O cabeçalho de seção vem de base.css; aqui ele perde a margem
> própria, porque quem dá o respiro é a linha da grade.

**assets/caso.css:315** `.secao__titulo`

> Peças de texto
>
> A medida de leitura também sai da grade: seis colunas na tela
> larga dão a linha de texto que se lê sem cansar, e é por isso
> que o corpo não ocupa a largura toda.

**assets/caso.css:347** `.secao > .colunas`

> Duas colunas de texto corrido, do jeito que um jornal resolve um
> bloco largo. A calha entre elas é a mesma da grade, então as
> duas caem exatamente nas colunas 1 a 6 e 7 a 12.

**assets/caso.css:358** `.secao > p,
.bloco > p`

> Nenhum parágrafo solto na grade carrega margem própria: quem dá
> o ritmo vertical é a linha da grade, e uma margem de navegador
> somada a ela seria um respiro que não veio da régua.

**assets/caso.css:372** `.secao > .legenda,
.secao__topo > .legenda`

> A linha de apoio embaixo de uma frase: explica de onde ela veio.

**assets/caso.css:407** `.secao--par > .coluna-a`

> Duas colunas de leitura dentro de uma seção
>
> Quando dois assuntos da mesma seção não dependem um do outro, eles
> correm lado a lado em vez de virar uma fila. Cada coluna tem a
> própria sequência de cima para baixo, e o olho escolhe por onde
> começar sem perder nenhuma das duas.

**assets/caso.css:418** `.secao--par > .coluna-a > *`

> Dentro de uma coluna nada corre lado a lado: o que estava em
> fileira desce em fila.

**assets/caso.css:421** `.coluna-b .corpo-texto`

> A coluna tem pouco mais de meia página, e a medida de leitura dela
> sai daí, não do que caberia na página inteira.

**assets/caso.css:425** `.coluna-b > .atrito,
.coluna-a > .linha-nota,
.coluna-b > .linha-nota`

> O atrito abre um grupo novo dentro da coluna, então ganha o
> respiro de fora, não o de dentro. O mesmo vale para a linha de
> nota que fecha uma coluna.

**assets/caso.css:432** `.coluna-a .linha-nota,
.coluna-b .linha-nota`

> A linha de nota nasceu para a página inteira: rótulo em três
> colunas, texto em seis ao lado. Dentro de meia página essas três
> colunas viram uma tira de duas palavras por linha. Na coluna ela
> se lê como se lê na sequência, o rótulo em cima do que ele
> nomeia.

**assets/caso.css:445** `.secao--ficha > .secao__topo,
.secao--ficha > .abertura`

> Ficha do projeto
>
> Três campos, quatro colunas cada. Corre embaixo da abertura, em
> faixa, como o crédito de uma matéria.
>
> Na abertura do caso ela sai da faixa e vira coluna: os três campos
> empilhados na margem direita, começando na mesma linha do rótulo
> da seção. Assim a ficha se lê de uma vez, e o texto de entrada
> fica com a página inteira à esquerda dele.

**assets/caso.css:1006** `.secao--sequencia > .corpo-texto,
.secao--sequencia > .linha-nota`

> Sequência: uma seção que só se lê de cima para baixo
>
> Há seção em que a ordem é o conteúdo. Se a frase grande está de um
> lado, de onde ela veio está do outro e a resposta volta para o
> primeiro, o leitor tem que adivinhar por onde continuar, e o corpo
> de letra mudando a cada bloco não ajuda a decidir.
>
> Aqui tudo assenta na mesma margem esquerda e desce numa coluna só,
> em corpo que vai diminuindo: a pergunta, de onde ela veio, o que eu
> respondi, o que destravou. Não há segunda coluna para onde o olho
> possa escapar.

**assets/caso.css:1706** `.secao--par--largo > .coluna-a,
  .secao--par--largo > .coluna-b`

> Há par que só existe onde cabem duas leituras. Quando um dos
> lados é um objeto de altura fixa, o outro fica com o que sobra,
> e o que sobra numa página de 900 são trinta e poucos caracteres
> por linha: metade de uma medida de leitura. Aqui o par desmancha
> e as duas peças voltam para a fila, cada uma com a página
> inteira. A linha de nota volta junto para a forma larga, rótulo
> na margem e texto ao lado, que é a forma dela em toda a página
> que não é coluna.

**assets/caso.css:1801** `.secao > .atrito,
  .secao--ficha > .secao__topo,
  .secao--ficha > .a`

> Empilhado, o bloco de atrito não tem motivo para parar antes da
> margem: a coluna estreita já é a medida de leitura, e o corte em
> oito colunas só deixava o texto caindo em três palavras por
> linha dentro de uma caixa com espaço de sobra ao lado.

**assets/caso.css:1820** `.secao > .colunas`

> Texto em duas colunas não sobrevive a uma tela estreita: vira
> duas colunas de três palavras.

**case-processo.html:133** `<section class="secao">`

> 01. O parágrafo de abertura abre na margem e a ficha corre
> ao lado dele, na coluna da direita, começando na mesma
> linha do rótulo da seção.

**case-processo.html:158** `<section class="secao">`

> 02. Os dois problemas são simultâneos, não uma sequência:
> correm lado a lado, uma coluna cada.

**case-processo.html:182** `<section class="secao">`

> 03. Os três estágios viram tabela: rótulo na margem, o
> que acontece no meio, o texto na direita. A saída abre em
> cinco entregas, cada uma com o destino do lado.

**case-processo.html:265** `<section class="secao">`

> 04. Duas colunas: os três ritos descem em fila de um lado,
> a usabilidade corre do outro. Os dois assuntos não dependem
> um do outro, então não fazem fila.

**case-processo.html:305** `<section class="secao">`

> 05. A seção que só existe pela ordem: a pergunta, de onde
> ela veio, o que eu respondi e o que destravou. Tudo na
> mesma margem, numa coluna só, sem nada correndo ao lado
> para o olho escapar no meio do caminho.

**case-processo.html:341** `<section class="secao">`

> 06. As cinco fases são cinco colunas que estreitam: a
> forma do funil é a própria grade.

**case-processo.html:401** `<section class="secao">`

> 07. Texto de um lado, a trilha do componente correndo na
> horizontal embaixo, porque ela é um caminho.

**case-processo.html:436** `<section class="secao">`

> 08. Os dois estados lado a lado, separados por um fio.
> Antes ficava metade escondida atrás de um botão.

**case-processo.html:476** `<section class="secao">`

> 09. O resultado: o gráfico ocupa a largura, o atrito
> entra escuro e os quatro números fecham a conta.

**case-omnichat.html:134** `<section class="secao">`

> 01. A abertura começa na margem e a ficha corre ao lado
> dela, na coluna da direita, na mesma linha do rótulo.

**case-omnichat.html:158** `<section class="secao">`

> 02. O problema em texto corrido e as duas origens lado a
> lado: elas chegam ao mesmo tempo, por canais diferentes.
> Em fila, a segunda pareceria consequência da primeira.

**case-omnichat.html:259** `<section class="secao">`

> 04. As duas conversas ficam abertas, lado a lado. Antes
> elas eram digitadas por um temporizador, uma mensagem de
> cada vez; agora estão inteiras no HTML, e o que separa os
> dois estados é o fio verde da coluna da direita.

**case-omnichat.html:342** `<section class="secao">`

> 05. O resultado, o que ficou e para onde ir.

**case-inpulse.html:130** `<section class="secao">`

> 01. A entrada de um lado e a ficha correndo na coluna da
> direita, começando na mesma linha de "01 · Contexto".
> Embaixo, as duas falas de aluno: a de antes e a de depois.
> Elas eram dois cartões iguais lado a lado; agora o que
> separa as duas é o traço na margem, verde só no depois.

**case-inpulse.html:231** `<section class="secao">`

> 03. O experimento. Os três níveis de desejabilidade usam
> o mesmo arranjo dos rituais da página de processo.
>
> A contagem é uma barra por funcionalidade: são sempre dez
> participantes, então a barra inteira é a mesma em todas e
> o que se lê é a proporção. Antes havia um número solto à
> direita do nome, "8 de 10", que não dizia de que dos três
> grupos estava falando. Agora as três contagens vêm
> escritas embaixo da barra, na mesma ordem das cores e
> começando sempre na mesma margem: assim dá para correr o
> olho pela coluna e ver quem teve mais entusiasta, que é a
> pergunta que a seção faz.

**case-inpulse.html:346** `<section class="secao">`

> 04. O resultado. As telas do app atravessam a página de
> beira a beira, sem moldura e sem margem: é a única imagem
> do caso que mostra o produto pronto, e cortada na altura
> ela vira uma faixa, não um retrato pendurado no papel.

**case-mapa-experiencia.html:130** `<section class="secao">`

> 01. A pergunta que o caso persegue de um lado, e a ficha
> correndo na coluna da direita, começando na mesma linha de
> "01 · A pergunta". Em faixa, embaixo do texto, ela era um
> metadado atravessando a página inteira antes de o caso ter
> começado.

**case-mapa-experiencia.html:161** `<section class="secao">`

> 02. A nota geral numa escala com sinal: é o único gráfico
> do site que precisa mostrar de que lado do zero a coisa
> está.

**case-mapa-experiencia.html:257** `<section class="secao">`

> 04. O mapa. As cinco telas ficavam num carrossel, uma de
> cada vez, com seta e ponto; agora estão abertas na
> galeria, na ordem em que o campus percorria.
>
> A primeira abre com as doze colunas. Ela é o tabuleiro
> inteiro, e é dela que as outras quatro são recortes: em
> meia página o caminho de doze etapas virava um desenho
> bonito e ilegível. Não vai de beira a beira como a imagem
> do Inpulse porque é clara como o papel: sem a margem em
> volta, ela não teria onde terminar.

**case-mapa-experiencia.html:338** `<section class="secao">`

> 05. O resultado: quem leu, e o que isso fez com a nota.


## Bloco com rótulo

**assets/caso.css:174** `.bloco,
.secao__topo`

> Um grupo: o rótulo e aquilo que ele nomeia. O respiro aqui
> dentro é a metade do respiro que existe em volta, e é esse
> contraste que faz o olho ler os dois como uma coisa só.

**assets/caso.css:363** `.bloco > .link-solto`

> Um link que fecha um bloco abre um degrau a mais que o respiro
> de dentro dele: ele é ação, não continuação do texto.


## Ficha do projeto

**assets/base.css:842** `.ficha`

> Ficha do projeto
>
> Papel, ritmo e duração. Aparece no caso em destaque da Home e no
> alto da página do próprio caso, nos dois sobre o fundo escuro,
> que é onde ela nasceu.

**assets/caso.css:1816** `.ficha-lateral`

> A ficha já está empilhada; na coluna única ela volta a ser um
> bloco atrás do outro, e não uma faixa presa à linha do topo.


## Cena dos casos

**assets/home.css:250** `.cena`

> A cena dos casos
>
> A segunda seção não é uma lista: é uma cena que abre. O palco
> gruda no alto da tela e a rolagem passa a mover o que está
> dentro dele: um caso de cada vez, do destaque para os outros
> três. O orbe desce ao longo do percurso e encolhe no meio de
> cada passagem, como quem toma fôlego antes da próxima cena.
>
> Nada disso é obrigatório. Sem script, com movimento reduzido ou
> em tela curta, .cena--viva nunca é posta: os quatro casos ficam
> empilhados no fluxo normal, cada um com o seu número à vista, e
> a página inteira continua legível rolando de cima a baixo.

**assets/home.css:284** `.cena--viva`

> A altura é o que dá curso à rolagem: uma tela para ler o
> primeiro caso, mais um passo para cada passagem.

**assets/home.css:309** `.cena:not(.cena--viva) .cena__contador`

> Fora da cena o contador não conta nada: os quatro estão à vista.

**assets/home.css:315** `.cena__atos`

> Empilhados: no modo cena os quatro ocupam a mesma célula da
> grade, então a altura é a do mais alto e ninguém salta na
> passagem. Fora dele, viram uma coluna comum.

**assets/home.css:346** `.ato__stat`

> O número do caso mora no orbe enquanto a cena está viva; fora
> dela, ele volta para dentro do próprio caso.

**assets/home.css:358** `.cena--viva .ato__num`

> Dentro do palco a altura é fixa (uma tela), e o caso mais
> cheio é o que decide. Os respiros passam a ser medidos em vh
> para o ato inteiro caber de pé em qualquer tela funda o
> bastante, em vez de estourar por baixo.

**assets/home.css:369** `.cena__orbe`

> ── O orbe ────────────────────────────────
> Desce ao longo da cena e pulsa: cheio quando um caso está
> parado à frente, encolhido no meio do caminho entre dois. É o
> relógio da cena: quem olha para ele sabe que ainda está
> andando.
> ────────────────────────────────────────────────

**assets/home.css:414** `.cena__trilho`

> ── O trilho ────────────────────────────────
> Quatro traços dizendo quantos atos existem e em qual se está.
> Numa cena que prende a rolagem, saber que há fim é metade do
> conforto, e cada traço leva direto ao seu ato.
> ────────────────────────────────────────────────

**index.html:186** `<section class="cena">`

> A cena. O palco gruda no alto da tela e a rolagem passa a
> trocar o que está dentro dele: o caso em destaque primeiro,
> os outros três depois. O orbe desce e encolhe nas passagens.
>
> Sem script, em movimento reduzido ou em tela curta, .cena--viva
> nunca é posta e os quatro casos ficam empilhados no fluxo
> normal, cada um inteiro e com o seu número à vista.

**index.html:256** `<div class="cena__orbe">`

> O orbe repete o número do caso que está à frente. Ele
> é decoração com dado dentro: o mesmo número já está
> no texto do caso, então aqui vai escondido do leitor
> de tela para não ser lido duas vezes.


# Sequência e processo


## Linhas indexadas

**assets/caso.css:492** `.linhas`

> Linhas indexadas
>
> Número na primeira coluna, título nas quatro seguintes, texto da
> sexta em diante. É o arranjo que resolve uma lista de itens
> longos sem virar uma fileira de cartões iguais, e as três
> colunas dele são colunas da própria página.

**assets/caso.css:504** `.linhas--par`

> Quando são só dois itens, empilhar um debaixo do outro faz parecer
> que o segundo vem depois do primeiro. Eles são simultâneos, então
> correm lado a lado, seis colunas cada, cada um abrindo no próprio
> fio verde.

**assets/caso.css:527** `.linhas--par .linha > p`

> Cinco das seis colunas do bloco: na sexta a linha de texto passava
> de oitenta caracteres, e nessa largura o olho perde o começo da
> linha seguinte.

**assets/caso.css:552** `.linha > p,
.linha__par`

> Cinco colunas, não sete: a linha de texto que vai até a margem
> direita passa de cem caracteres, e nessa largura o olho perde o
> começo da linha seguinte.

**assets/caso.css:1824** `.linha__num,
  .linha__titulo,
  .linha > p,
  .linha__par,
  .estagio`

> Na linha indexada o número passa a abrir a linha, e título e
> texto correm embaixo dele, nas mesmas colunas.

**assets/caso.css:1841** `.linha p`

> Na página larga o texto da linha para na quinta coluna, e é esse
> corte que segura a medida de leitura. Empilhado ele ia até a
> margem, e numa tela de 719 isso dá quase noventa caracteres por
> linha: a largura em que o olho perde o começo da linha seguinte,
> que é justamente o que o corte de cinco colunas evita lá em
> cima.


## Estágios

**assets/caso.css:572** `.estagios`

> Estágios
>
> Uma tabela de três estágios em vez de três caixas com setas: o
> rótulo nas duas primeiras colunas, o que acontece nas quatro
> seguintes, o texto no resto. O estágio do meio é o que a seção
> explica, e é o único que ganha fundo.

**assets/caso.css:611** `.estagio--nucleo`

> O estágio do meio: a camada que faz o trabalho. O fundo sangra
> uma calha para cada lado, e só isso, para o texto de dentro
> continuar nas mesmas colunas dos estágios de cima e de baixo.

**assets/caso.css:625** `.estagio--saida`

> A saída abre em cinco entregas. A lista ocupa da terceira coluna
> em diante, que é onde o título dos outros estágios começa, e por
> dentro ela redesenha essas dez colunas: o nome da entrega cai
> nas mesmas quatro do título, e o destino nas mesmas seis do
> texto.

**assets/caso.css:671** `.estagio--saida > .abas`

> Abas
>
> Cinco saídas da mesma camada. Empilhadas, elas viravam uma lista
> de cinco itens quase iguais, lida na diagonal e esquecida. Em
> abas, os cinco nomes ficam à vista de uma vez, na horizontal, e
> quem escolhe o que ler é o leitor.
>
> Sem script nenhum painel se esconde: as cinco saídas aparecem
> uma debaixo da outra, com o nome de cada uma em cima do texto
> dela. É o mesmo conteúdo, sem a escolha.

**assets/caso.css:684** `.estagio--saida > .abas`

> As abas caem nas mesmas dez colunas que a lista ocupava: da
> terceira em diante, que é onde o título dos outros estágios
> começa.


## Abas

**assets/caso.css:722** `.abas:not(.abas--js) .abas__lista`

> Sem script a lista de nomes não tem função: quem nomeia cada
> saída é o título dentro do painel.

**assets/caso.css:731** `.abas--js .abas__paineis`

> Com script os cinco painéis dividem a mesma célula, então a altura
> do bloco é a do maior deles e a página não pula de tamanho a cada
> troca de aba. Quem está fora de cena sai da árvore de acessibilidade
> pela visibilidade, não pelo display: se saísse pelo display, a
> célula encolheria e o pulo voltaria.

**assets/caso.css:751** `.aba-painel`

> Dentro do painel, o mesmo arranjo que a lista tinha: o destino nas
> quatro primeiras colunas das dez, o texto nas seis seguintes. Em
> uma coluna só, o painel ficava com metade da largura vazia à
> direita e o dobro de altura reservada para o maior deles.

**assets/caso.css:784** `.abas--lado`

> Abas na vertical
>
> O mesmo componente, com os nomes descendo em índice na coluna da
> esquerda e o painel abrindo na direita. É o arranjo de quando os
> nomes são frases: numa fileira horizontal eles só caberiam
> encurtados, e encurtar aqui seria reescrever o conteúdo para
> acomodar o formato.
>
> A altura é a mesma nas cinco abas, e quem tem texto mais longo
> rola por dentro. Duas coisas dependem disso: a página nunca dá um
> salto quando alguém troca de aba, e a aba curta não deixa um vão
> do tamanho da aba mais longa embaixo dela.

**assets/caso.css:817** `.abas--lado .abas__paineis`

> A janela de leitura do painel. A altura não é um número escrito
> aqui: as duas colunas dividem a mesma fileira da grade, e a fileira
> fica do tamanho da mais alta das duas. Como os cinco painéis se
> empilham na mesma célula, a fileira é a mesma para as cinco abas, e
> a página nunca dá um salto quando alguém troca de camada.
>
> A rolagem por dentro é a válvula: se um dia o texto de uma camada
> passar da janela, ele rola ali e não empurra a seção seguinte. O
> min-height é o que deixa o painel encolher dentro da célula; sem
> ele o painel cresce e leva a fileira junto.

**assets/caso.css:841** `.abas--lado .aba-painel::-webkit-scrollbar`

> A barra fica fina e no tom do fio da página: ela avisa que há mais
> texto embaixo, e não vira um objeto de interface no meio da
> leitura.

**assets/caso.css:852** `.aba__num`

> O número da camada abre o nome dela. Ele não é enfeite: a seção do
> antes e depois aponta para "camada 02" e "camada 03", e sem o número
> aqui essa referência não teria para onde apontar.

**assets/caso.css:1849** `.abas__lista`

> Na coluna estreita os cinco nomes não cabem numa fileira: em vez
> de quebrar em duas linhas e meia, com um item sozinho no meio,
> eles descem em lista. Cada nome ganha a largura toda, que é
> também o alvo de toque que um dedo pede.

**assets/caso.css:1865** `.abas--lado .abas__lista,
  .abas--lado .abas__paineis`

> Numa coluna só, o índice volta a ser uma lista e o painel volta
> a ter a altura do texto: rolagem dentro de rolagem, num celular,
> é o leitor perdendo o controle da página.

**assets/caso.css:1965** `.abas--carrossel .abas__lista`

> Os painéis eram abas e viram cartões. Sem o índice, quem nomeia
> cada um é o título dentro dele, que é o mesmo elemento que
> aparece quando não há script.

**assets/caso.css:1973** `.abas.abas--carrossel .aba-painel + .aba-painel,
  .tinta .abas.abas--`

> O empilhado sem script separava um painel do outro com fio e
> respiro. Deitados, quem separa é o vão entre os cartões.

**assets/caso.css:1981** `.abas--carrossel .aba-painel__nome`

> O nome da entrega é rótulo, e o título embaixo dele é a frase.
> Dentro do estágio ele estava herdando o corpo de letra dos
> títulos do estágio e saía do mesmo tamanho e da mesma serifa da
> frase, com as duas disputando quem abre o cartão.

**assets/caso.css:1994** `.abas--carrossel .entregas__cabeca`

> "Destino" nomeava a coluna da direita do painel aberto. Sem
> colunas e sem índice ele fica sobrando logo abaixo de "saída",
> dois rótulos empilhados sem nada entre eles, e o que ele nomeava
> já é a frase que abre cada cartão.

**case-omnichat.html:208** `<div class="abas">`

> As cinco camadas em abas na vertical. Na horizontal os
> nomes não cabem numa fileira sem serem encurtados, e
> encurtar aqui seria reescrever o conteúdo para acomodar o
> formato. Então a fila vira índice. Sem script os cinco
> painéis aparecem abertos, um debaixo do outro.


## Ritos

**assets/caso.css:916** `.ritos`

> Ritos
>
> Três itens, quatro colunas cada. Sem moldura e sem fio em cima:
> o traço verde curto embaixo do nome é o que separa.


## Funil

**assets/caso.css:1030** `.funil`

> Funil
>
> Cinco fases, cinco colunas de mesma largura. Colunas que estreitam
> desenhavam a forma do funil e cobravam por isso: a última fase
> ficava com metade da linha da primeira, e o mesmo parágrafo passava
> a custar o dobro de linhas para ser lido. Comparar cinco coisas
> pede cinco lugares iguais.

**assets/caso.css:1066** `.fase > p`

> O texto estica até o fim do espaço livre e o rodapé encosta
> embaixo dele. Isso alinha o pé das cinco colunas, e não o fio de
> "quem conduz": onde o texto de baixo tem três linhas em vez de
> uma, o fio sobe. É o arranjo de reserva.

**assets/caso.css:1738** `.funil`

> Cinco colunas não cabem aqui sem virar cinco tiras de duas
> palavras por linha. Duas por fileira, e o pé de cada fase volta
> a se alinhar por dentro dela.

**assets/caso.css:1900** `.funil,
  .abas--carrossel .abas__paineis`

> Carrossel de tela estreita
>
> Cinco coisas da mesma natureza, numa coluna de trezentos pixels,
> viram cinco telas de rolagem. Quem chega na quinta já não tem a
> primeira na cabeça, e comparar, que é a razão de as cinco estarem
> juntas, deixa de ser possível. Deitadas, cada uma ocupa uma tela
> inteira e a troca é o gesto que o polegar já faz.
>
> Três lugares usam isto, e a forma é a mesma nos três: as cinco
> fases do funil, as cinco entregas da transcrição e as cinco
> camadas do artefato. A forma também é a do resto do site, fio
> verde em cima e texto embaixo, sem caixa em volta: quem faz o
> cartão parecer cartão é o corte na beirada da tela, não uma
> moldura desenhada.
>
> O cartão para antes da margem direita de propósito. A beirada do
> próximo é o que conta que existe um próximo; alinhado com a
> margem, o carrossel fica igual a um bloco só.

**assets/caso.css:1946** `.funil > .fase,
  .abas--carrossel .aba-painel`

> A largura do cartão é a que sobra depois de guardar a beirada do
> próximo. Os trezentos pixels são o teto: numa tela grande de
> celular o cartão para de crescer e a beirada aparece maior, o
> que é o mesmo recado.

**assets/caso.css:1956** `.funil > .fase`

> align-items: stretch dá a mesma altura aos cinco cartões, e é o
> mesmo arranjo de reserva do desktop: o texto estica até o fim do
> espaço livre e "quem conduz" encosta embaixo dele, então o que
> alinha entre as fases é o pé, não o fio. Aqui isso ganha uma
> segunda função, que no desktop não fazia falta: a trilha tem a
> altura do cartão mais alto de uma vez por todas, e a página não
> muda de tamanho a cada gesto do polegar.

**assets/caso.css:2005** `.funil:focus-visible,
  .abas--carrossel .abas__paineis:focus-visible`

> A trilha ganha foco de teclado no JS, então ela precisa mostrar
> que está com o foco. O anel fica do lado de fora do sangramento,
> onde não corta em nada.


## Trilha

**assets/caso.css:1095** `.rail`

> Rail: a trilha do componente
>
> Três marcos numa linha só, quatro colunas cada, com o fio
> passando por trás dos pontos. Horizontal porque é um caminho,
> não uma lista.

**assets/caso.css:1732** `.rail__marco`

> A trilha continua sendo uma trilha: os três marcos ficam na
> mesma fileira. Quebrada em duas, o fio que os liga só cobre a
> primeira, e o terceiro fica com um ponto verde solto no meio
> do nada.

**assets/caso.css:1885** `.rail`

> Empilhada, a trilha deixa de ser um caminho horizontal. O fio
> que ligava os três marcos sai, e cada um passa a abrir com o
> mesmo fio de topo das fases, com o ponto verde acima do nome.
> Um recuo à esquerda para caber a linha jogaria os três para
> fora da coluna, e não vale furar a grade por um enfeite.


# Comparação


## Confronto

**assets/caso.css:1132** `.confronto`

> Confronto: antes e depois
>
> Três colunas de conteúdo em cima das doze: a dimensão nas três
> primeiras, o antes nas quatro seguintes, o depois no resto. As
> duas ficam à vista ao mesmo tempo, separadas por um fio, e o
> depois é o lado que a página defende.

**assets/caso.css:1151** `.confronto__cabeca`

> As três etiquetas nascem logo abaixo do fio que abre a tabela, e
> sem respiro elas encostam nele. O respiro de cima é o que faz o
> fio ler como abertura da tabela e não como sublinhado do título.

**assets/caso.css:1158** `.confronto__cabeca .micro:nth-child(3)`

> A terceira etiqueta acompanha o recuo que o fio vertical cria na
> coluna do depois, senão o cabeçalho fica fora do prumo.

**assets/caso.css:1171** `.confronto__depois`

> O fio entre as colunas divide os dois estados; ele nasce no
> texto do depois para não precisar de um elemento só para isso.


## Conversa

**assets/caso.css:1573** `.conversas`

> Conversa
>
> Os dois estados de um mesmo atendimento. A conversa aconteceu num
> celular, então ela se lê dentro de um: cada estado ganha o
> contorno de uma tela, e as duas telas ficam no meio da página,
> com respiro nas laterais e entre elas.
>
> O contorno é estreito de propósito. Uma tela de celular que ocupa
> meia página deixa de ser uma tela de celular, e era isso que as
> duas colunas faziam antes: a conversa tinha a largura de um
> texto, não a de um aparelho.
>
> O aparelho é o mesmo nos dois lados, então o contorno também é.
> Quem separa os dois estados continua sendo o fio em cima do
> rótulo, cinza de um lado e verde do outro.

**assets/caso.css:1614** `.turnos`

> A lista de turnos é a tela. Fio de 2px com o raio de um aparelho,
> o mesmo fio de qualquer moldura da página: o celular aqui é
> desenho de contorno, não fotografia. O alto-falante em cima e a
> barra em baixo são o que basta para o olho ler aparelho, e são
> dois riscos, não um desenho.
>
> Dentro do contorno o papel perde a trama. É a única superfície do
> site que não é papel, e tem que ser: é uma tela.

**assets/caso.css:1646** `.turno__fala`

> Dentro da tela a fala não se mede em caracteres e sim na largura
> do aparelho: ela para antes da borda oposta, e é essa sobra que
> diz de que lado da conversa cada bolha está. Bolha curta encolhe
> até o texto, que é como uma conversa se parece; uma bolha de duas
> palavras com a largura da tela pareceria um campo vazio.

**assets/caso.css:1662** `.turno--agente .turno__quem`

> A fala do agente encosta na margem direita e troca de tom: é o
> suficiente para separar os dois lados sem pintar cada um de uma
> cor.

**assets/caso.css:1667** `.turno__nota`

> A nota embaixo da fala diz o que aquele turno custou, ou qual
> camada o consertou. Ela é a única coisa ali dentro que não é da
> conversa, então ocupa a largura toda da tela e não a da bolha.


# Dados


## Números do resultado

**assets/caso.css:1227** `.numeros`

> Números do resultado
>
> Quatro números, três colunas cada. As doze colunas divididas em
> quatro partes iguais, e não uma fileira que se acomoda sozinha.


## Barras

**assets/caso.css:1182** `.barras`

> Barras: o tempo antes e depois
>
> A barra do "antes" é a régua; a do "depois" é a mesma medida em
> verde. A largura é escrita pelo JS quando o bloco entra na tela;
> sem JS ela já nasce no valor final.

**assets/caso.css:1207** `.barra__valor`

> O valor fica encostado na direita, junto do fim do trilho: é
> assim que dois números viram comparação em vez de duas frases.


## Pilhas

**assets/caso.css:1453** `.pilhas`

> Pilhas
>
> Dez participantes por funcionalidade, e a barra inteira são os
> dez. O que muda de uma para outra é quanto de cada reação ocupa:
> entusiasmo em verde, receptividade em cinza de jornal, a
> indiferença quase apagada. Uma barra por funcionalidade, não
> três, porque a soma é sempre a mesma e é a proporção que se quer
> ler.
>
> Três reações são três quantidades, e um número só no lugar delas
> não diz de qual está falando. Elas vêm escritas embaixo da barra,
> na ordem das cores, e embaixo é de propósito: à direita do nome,
> cada linha começaria num lugar diferente, e a comparação que
> interessa, quem teve mais entusiasta, é justamente a que se faz
> descendo o olho pela mesma margem.

**assets/caso.css:1478** `.pilha__conta`

> A contagem é letra miúda: quem compara é a barra, e o número está
> ali para quem quiser a conta exata.

**assets/caso.css:1500** `.cores`

> A legenda das cores, que serve a qualquer gráfico desta folha.

**assets/caso.css:1513** `.cores span b`

> O texto da legenda não herda a cor da bolinha: só a bolinha
> muda, senão a palavra "indiferente" sumiria junto com ela.


## Escala de NPS

**assets/caso.css:1517** `.nps__eixo`

> Escala de NPS
>
> Um eixo que vai de cem negativos a cem positivos, com o zero
> marcado no meio e o trecho percorrido pintado por cima. É o
> único gráfico do site que precisa mostrar sinal, e por isso ele
> não é uma barra que cresce da esquerda.


# Mídia


## Moldura

**assets/caso.css:1366** `.moldura`

> Moldura e galeria
>
> Onde entra pixel de produto. A moldura ocupa a largura da grade
> e não tem borda: o canto arredondado e o fundo escuro por baixo
> bastam para a imagem não flutuar solta no papel.

**assets/caso.css:1388** `.moldura--retrato`

> Quando o que está dentro é uma tela de celular, a moldura para de
> crescer antes de virar paisagem. Passando disso, o que ganha
> largura é o fundo em volta do aparelho, não o aparelho: o
> protótipo fica do mesmo tamanho e mais longe do texto.


## Galeria

**assets/caso.css:1424** `.galeria`

> A galeria: figuras abertas lado a lado, seis colunas cada, com a
> legenda embaixo. Sem seta e sem ponto, porque estão todas à
> vista. Seis e não quatro porque são telas densas, e três por
> fileira deixaria cada uma pequena demais para se ler.

**assets/caso.css:1438** `.galeria--abertura > li:first-child`

> A primeira figura de uma galeria pode ser o todo de que as outras
> são recorte. Quando for, ela abre com as doze colunas: um desenho
> denso em meia página fica bonito e ilegível, e a diferença de
> largura é o que diz, sem escrever, que as quatro seguintes são
> pedaços dela.


## Sangria

**assets/caso.css:1394** `.sangria`

> A sangria: a imagem sai da grade e atravessa a página de beira a
> beira. Não é moldura sem borda, é o contrário da moldura: aqui a
> imagem não é um objeto pousado no papel, é uma faixa que o papel
> atravessa.
>
> A conta do recuo negativo sai da própria caixa: metade da largura
> da coluna menos metade da largura da tela põe a beirada esquerda
> no zero da viewport, qualquer que seja a margem da página. O corpo
> já esconde o que passar da largura, então a barra de rolagem, que
> entra em vw e não na tela, não abre estouro horizontal.
>
> A altura é fixa e a imagem enche por cima, porque o que interessa
> é a faixa ter sempre a mesma proporção de página. No celular a
> faixa fica mais alta em relação à largura: as telas do app são
> pequenas ali, e um corte baixo demais não mostraria nenhuma.


# Comportamento


## Régua de leitura

**assets/caso.css:88** `.regua`

> Régua de leitura
>
> A única peça de cromo que uma página longa ganha: uma linha
> verde no topo da tela dizendo quanto falta. Sem JS ela fica em
> zero e some, que é o mesmo que não existir.

**case-processo.html:48** `<div class="regua">`

> Quanto falta para o fim da página. Sem JS fica em zero e some.

**case-omnichat.html:48** `<div class="regua">`

> Quanto falta para o fim da página. Sem JS fica em zero e some.

**case-inpulse.html:48** `<div class="regua">`

> Quanto falta para o fim da página. Sem JS fica em zero e some.

**case-mapa-experiencia.html:48** `<div class="regua">`

> Quanto falta para o fim da página. Sem JS fica em zero e some.


# Fora das peças


## Fundação

**assets/base.css:1** `@import url('https://fonts.googleapis.com/css2?family=Inter`

> Base: "editorial broadsheet in a green room"
>
> O que toda página do site divide: os tokens do DESIGN.md, o
> papel com a trama, a barra do topo, a onda entre as seções, o
> rodapé e o movimento de entrada. O que é de uma página só mora
> na folha dela (home.css, caso.css), carregada depois desta.
>
> Tokens do DESIGN.md (referência: newformcap.com). As três faces
> originais são licenciadas (TWK Lausanne, PP Mondwest e
> Editorial New). Aqui entram os substitutos livres que o próprio
> DESIGN.md indica:
>   TWK Lausanne  → Inter (variável, cobre o peso 550)
>   PP Mondwest   → Instrument Serif
>   Editorial New → Instrument Serif italic
>
> Uma correção ao DESIGN.md: ele manda passar toda fotografia por
> uma cadeia de filtro que a joga para o verde. O site real não faz
> isso: as fotos dele são preto e branco de contraste cheio, e o
> filtro verde fica em outros elementos. Seguimos o site.

**assets/base.css:44** `--space-4: 4px;
  --space-8: 8px;
  --space-12: 12px;
  -`

> A régua de espaço do site. Unidade base de 8, com 4 para o
> ajuste fino, e cada degrau pelo menos 25% maior que o
> anterior: abaixo disso o olho não vê diferença e a hierarquia
> de espaço se perde. Nenhuma medida de respiro do site nasce
> fora daqui.

**assets/base.css:64** `--onda-bolha-h: clamp(58px, 5.2vw, 88px);
  /* A seta tem`

> A onda que carrega uma seta é mais alta que as outras: ela
> precisa de corpo para a bolha subir sem virar um espeto, e o
> mínimo dela é maior porque a seta não encolhe junto.

**assets/base.css:68** `--seta-h: max(28px, calc(var(--onda-bolha-h) * 0.38));`

> A seta tem altura própria porque ela para de encolher antes da
> onda: abaixo de certo tamanho deixaria de se ler como seta. Ter
> o número aqui é o que permite sentá-la no morro pela altura
> dela, e não por uma fração da onda que só bate no desktop.

**assets/base.css:78** `--shadow-green: rgba(16, 94, 29, 0.45) 1px 8px 20px 0px;`

> Existe uma só elevação, e ela pertence ao verde.

**assets/base.css:96** `background-color: var(--bone-white);
  background-image:`

> A trama é quase invisível de perto: linhas onduladas a 2,5px uma
> da outra que, à distância, só dão ao papel um leve tom verde.
> Reproduzida a partir da tile da referência: mesmas cores, mesmo
> espaçamento, mesma deriva diagonal de fase.

**assets/base.css:150** `.js-mov [data-revelar]`

> Movimento
>
> O site de referência não usa parallax: usa reveal na entrada
> (opacidade + subida), um float em laço e um marquee. O reveal é
> o que faz a página parecer viva ao rolar, então é o efeito
> principal aqui, com o parallax das fotos por cima.
>
> O estado inicial escondido é posto pelo JS (.js-mov no html).
> Sem JS, nada nunca fica invisível.

**assets/base.css:224** `body`

> Navegação
>
> A barra é fixa e vive fechada: só a marca e o botão, em qualquer
> largura de tela. Não existe mais uma versão de desktop com os
> links soltos e outra de celular escondida. O menu inteiro mora
> atrás do botão nas duas.
>
> Ao rolar, a marca encolhe até a inicial. O tracinho verde não
> precisa de uma segunda regra para isso: ele mora no bloco que
> segura o "J" e o "eff", então encolhe junto com ele.

**assets/base.css:237** `body`

> A barra saiu do fluxo; o corpo abre o vão dela. O scroll-padding
> é para as âncoras não pararem debaixo da barra. Num nome, porque
> há seção que precisa desfazer exatamente esta folga e um número
> repetido ali viraria uma discordância silenciosa.

**assets/base.css:433** `height: auto;
  min-height: min(78vh, 680px);
  max-heigh`

> O piso é o painel de sempre; daí para cima ele cresce só o
> quanto o conteúdo pedir, e nunca passa de 88vh, para a onda do
> pé nunca sair da tela. Numa janela baixa é isso que segura os
> sete itens dentro do painel em vez de mandá-los para a rolagem.

**assets/base.css:451** `html.saindo--menu .menu`

> ── A saída de dentro do menu ──────────────────────────
> O painel não sai: ele termina de chegar. Cresce até cobrir a
> tela inteira, mais uma altura de onda, para a onda do pé passar
> da borda de baixo em vez de parar em cima dela.
>
> A altura de partida é escrita no elemento pelo script, porque
> height:auto não transiciona: sem um número dos dois lados o
> painel pularia para a tela cheia em um quadro.
>
> O miolo, enquanto isso, se apaga. E se apaga parado: o painel
> alinha o conteúdo pela borda de baixo, então crescendo ele
> arrastaria os sete itens para baixo junto. O script mede onde o
> miolo está e o prende ali antes de a altura começar a andar.
> ────────────────────────────────────────────────

**assets/base.css:475** `html.saindo--menu .menu__lista li`

> Os itens somem com o miolo inteiro, de uma vez. A escadinha de
> atrasos é da entrada, e na saída ela só atrapalharia: são sete
> coisas sumindo em fila dentro de uma superfície que já está
> indo embora.

**assets/base.css:493** `scrollbar-width: none;
  -ms-overflow-style: none;
  padd`

> A barra de rolagem não aparece: o painel é uma superfície
> inteira, e um trilho cinza no canto direito quebra isso. A
> rolagem continua existindo, para o caso de a tela ser baixa
> demais; ela só não se anuncia.

**assets/base.css:524** `font-size: clamp(28px, min(9vw, 6.4vh), 52px);
  font-wei`

> O corpo cresce com a largura, e o piso do celular é alto de
> propósito: numa tela estreita o menu é a tela inteira, e um
> item de 26px ali é um link de rodapé, não a porta da página.
> O coeficiente 9vw é o maior que ainda deixa "Mapa de
> experiência", o item mais longo, numa linha só em 320.
>
> O segundo termo é a altura, e existe por causa da janela baixa
> de notebook: lá a largura pediria o corpo máximo e os sete
> itens não caberiam no painel. Quem manda é o menor dos dois.

**assets/base.css:535** `line-height: 1.22;
  /* Tracking zero por obrigação, não`

> Folga de sobra: se um item futuro for longo o bastante para
> quebrar em duas linhas dentro do mesmo link, o contorno de uma
> linha não pode cruzar o da outra.

**assets/base.css:539** `letter-spacing: 0;
  color: var(--bone-white);
  text-dec`

> Tracking zero por obrigação, não por gosto. O contorno é
> desenhado letra a letra: com tracking negativo as letras
> encostam, e os contornos de duas letras vizinhas se cruzam.

**assets/base.css:548** `@supports (-webkit-text-stroke: 1px currentColor) and (paint-order: st`

> ── O contorno vazado ───────────────────────────────
> O desenho que se quer é o da referência: a letra fechada só na
> borda de fora, o miolo inteiro vazado, sem nenhum risco por
> dentro.
>
> Contorno puro não dá isso. Uma fonte variável guarda a letra
> como partes que se sobrepõem: o "A" são duas diagonais e um
> travessão, o "P" é a haste mais a barriga, o "x" são dois
> riscos cruzados. Preenchida, a sobreposição some. Contornada,
> cada parte é contornada por inteiro, e as costuras internas
> aparecem, que é o X no meio do "x" e o risco no encontro da
> haste com a barriga.
>
> A saída é pintar na ordem inversa: primeiro o traço, depois o
> preenchimento na cor do painel por cima. O preenchimento usa a
> regra de dentro-e-fora, então cobre a união das partes de uma
> vez e apaga com ela todas as costuras. Sobra a metade de fora
> do traço, que é o contorno.
>
> Por isso o traço vai com o dobro da espessura: metade dele fica
> debaixo do preenchimento.
> ────────────────────────────────────────────────

**assets/base.css:587** `@supports not (paint-order: stroke)`

> Onde o navegador não sabe inverter a ordem de pintura, o
> contorno sairia riscado por dentro. Item preenchido é melhor
> desenho que item riscado, então é esse o estado.

**assets/base.css:611** `html:not(.js) .menu`

> Sem script não há painel que abra: o menu fica aberto no fluxo,
> no alto da página, e o botão some. Nada de link inalcançável.

**assets/base.css:623** `html:not(.js) .menu__inner`

> No fluxo, o vão da barra fixa já é o padding do corpo.

**assets/base.css:704** `padding-bottom: .1em;
  font-family: var(--font-ui);
  fo`

> O par de medidas embaixo é o vão entre a perna do J e o traço.
> Com line-height 1 sobra a altura do descendente dentro da
> caixa, e um traço encostado na borda de baixo dela cairia
> longe demais da letra. O padding dá lugar ao traço dentro da
> caixa; o bottom o traz de volta para perto da perna.

**assets/base.css:731** `html.saindo--pagina .nav,
html.saindo--pagina .menu,
html.saindo--pagi`

> ── Saída ───────────────────────────────────────────

**assets/base.css:733** `html.saindo--pagina .nav,
html.saindo--pagina .menu,
html.saindo--pagi`

> Saindo de um link da página, a página se apaga primeiro, sobre o
> fundo dela mesma, e só depois o preto entra. Antes o preto entrava
> por cima de tudo de uma vez, e a diferença entre esta saída e a do
> menu era grande demais para duas coisas que são a mesma coisa.
>
> Nomeados um a um, e não `body > *`: o que se apaga é o que a
> pessoa está vendo. Os desenhos das ondas também moram no corpo, e
> apagá-los junto seria apagar a definição de um recorte que ainda
> está em uso.

**assets/base.css:747** `animation: pagina-apaga .30s var(--ease-saida) forwards;`

> Animação e não transição, como todo o resto da passagem: a barra
> e o painel já têm transições próprias de outras coisas, e um
> `transition` aqui entraria numa disputa que a animação não tem.

**assets/base.css:759** `html.saindo--pagina,
html.saindo--menu,
html.chegando`

> A cortina é fixa e cobre a área de rolagem, não a barra de rolagem:
> onde o navegador desenha barra clássica em vez de barra flutuante,
> sobrava uma tira clara na direita durante a passagem inteira. Pintar
> a barra não desloca nada, que é a diferença entre isto e escondê-la.
> Onde a propriedade não existe, a tira volta e nada mais muda.

**assets/base.css:768** `html.saindo--menu .transicao.saindo`

> Saindo de dentro do menu a cortina não cobre nada: o painel já
> cobriu. Ela só precisa estar acesa quando o J entrar, e por isso
> troca de tempo em vez de trocar de papel.

**assets/base.css:790** `html.chegando .transicao`

> ── Chegada ─────────────────────────────────────────

**assets/base.css:792** `html.chegando .transicao`

> Do lado de cá o J chega com o traço no ponto em que a outra
> página o deixou, e o resto da barra enche aqui. É a única parte
> da passagem que acontece de fato durante o carregamento: o que
> está atrás dela é a página nova sendo montada, e não uma página
> velha esperando a hora de sair. Só quando a barra fecha o J sai.
>
> A animação começa quando a página é lida, não quando ela é
> pintada, e por isso a barra não parte do primeiro quadro: os
> 120ms de folga são o que sobra para ela ser vista mesmo num
> carregamento rápido.
>
> `both` e não `forwards`: com um atraso e sem o preenchimento
> para trás, a cortina ficaria transparente durante esses 580ms e
> a página nova apareceria por um instante antes de ser coberta;
> e a barra piscaria vazia antes de reaparecer onde parou.

**assets/base.css:883** `bottom: calc(100% - 1px);
  display: block;
  width: 100%`

> 1px a menos que 100%: a onda pisa 1px dentro da própria seção
> em vez de só encostar nela. Sem esse afogamento, o
> antialiasing da curva deixa um traço claro exatamente na
> emenda, por cima de uma cor idêntica dos dois lados.

**assets/base.css:892** `background-position: left bottom;
  clip-path: url(#onda-`

> A trama tem que atravessar a curva sem emenda. Ancorada embaixo,
> a tile fecha um ciclo exatamente na borda de baixo da onda, que
> é onde a seção começa a desenhar a dela, no começo do ciclo.

**assets/home.css:1** `.face-unica`

> Home
>
> Só o que é da página inicial. O resto (tokens, barra do topo,
> menu, onda, rodapé, movimento) vem de base.css, carregada antes
> desta.
>
> Uma tipografia só
>
> A referência tem uma face e nada mais: a hierarquia inteira sai
> de corpo, peso e cor. A Home fazia diferente, misturando a
> grotesca com a serifada, e a mistura era o que mais destoava.
> Aqui a serifada é desligada no ponto em que ela é escolhida
> (--font-display passa a apontar para a mesma face da
> interface), então tudo que já pedia display continua pedindo, e recebe Inter.

**assets/home.css:20** `.face-unica .footer h2`

> Inter no corpo de display precisa de peso e de aperto para
> segurar o que a serifada segurava com a forma da letra. As peças
> desta folha já pedem os dois; a única que vem de fora e não sabe
> disso é a chamada do rodapé.

**assets/home.css:63** `--hero-topo: clamp(24px, 4vw, 56px);
  --hero-vao: clamp(`

> O orçamento vertical, parcela por parcela. Tudo que não é fileira
> é dado: o respiro de cima, a frase de baixo com a margem dela, e
> o pé, que é a altura da onda com o morro mais o ar entre ela e a
> frase. O que sobra é --hero-sobra, e é dele que sai a fileira.
>
> As parcelas ficam declaradas aqui, e não escritas de novo lá
> embaixo, porque a conta só fecha enquanto as duas pontas disserem
> o mesmo número.

**assets/home.css:82** `--hero-linha: clamp(40px, min(11.5cqi, var(--hero-sobra)`

> A largura ainda manda enquanto couber. Quando não couber, quem
> manda é a altura da tela, e a fileira fica com um quarto do que
> sobrou. O piso de 40px é o ponto em que a frase deixa de ser
> legível: daí para baixo a tela é curta demais e a seta volta a
> ficar abaixo da dobra, o que é honesto.

**assets/home.css:92** `flex: 1 0 auto;
  display: flex;
  flex-direction: column`

> Numa tela alta sobra altura depois de as fileiras baterem no teto
> delas. A sobra se reparte igual em cima e embaixo, e o bloco de
> título e frase fica no meio do vão entre a barra e a onda, em vez
> de encostar no alto e deixar um buraco antes da seta.

**assets/home.css:127** `font-size: calc(var(--hero-linha) * .87);
  line-height:`

> O corpo sai da altura da fileira, e não da largura por conta
> própria: a fileira agora encolhe quando a tela é baixa, e uma
> letra dimensionada por outro caminho transbordaria dela. 0.87 é
> exatamente a proporção que as duas medidas já tinham quando cada
> uma vinha do seu lado.

**assets/home.css:158** `@keyframes hero-foto-nova`

> Os dois quadros do filme. A subida ocupa os últimos 8,33% de
> cada meia volta, que em 12s dá 1s de movimento e 5s de imagem
> parada. Entre 50% e 91,67% a nova cobre o quadro inteiro, e é
> nessa janela que a base atravessa escondida de volta para
> baixo: em nenhum instante as duas deixam de somar uma altura,
> então nunca se abre um vão entre elas.

**assets/home.css:175** `.js-mov .hero__linha.revelado .foto img`

> Em longhand de propósito: o atalho `animation` zera o nome, e
> aqui o nome vem de outra regra.

**assets/home.css:195** `@media (max-width: 720px)`

> Empilhada, a fileira lê de cima para baixo, e a ordem do HTML
> deixa de valer: o texto vem sempre primeiro e a foto embaixo
> dele, nas quatro. Alternar aqui só faria a frase pular de lado
> sem que houvesse lados. E a foto vira uma faixa: metade da
> altura de antes, para a frase continuar sendo o que se lê e não
> uma legenda entre duas imagens.

**assets/home.css:225** `max-height: max(30px, calc((var(--hero-sobra) - (var(--`

> A faixa fica com o que sobrar depois das quatro frases e dos
> quatro vãos entre frase e faixa. O piso de 36px é onde ela para
> de encolher: mais fina que isso não é mais fotografia, é um
> risco atravessado, e aí prefiro que a seta fique um dedo abaixo
> da dobra a entregar quatro riscos.

**assets/home.css:273** `scroll-margin-top: calc(-1 * var(--ancora-topo));
}
/* A`

> A seta e o link de pular apontam para cá, e aqui a folga que
> protege as âncoras da barra fixa trabalha contra: parando 108px
> abaixo do começo da seção, sobrava no alto da tela uma tira do
> hero claro com o morro da onda no meio dela. A folga existe para
> texto não parar debaixo da barra, e o que começa aqui não é
> texto, é o fundo: o primeiro rótulo está a mais de 400px daqui.
> Desfazendo a folga, a seção encosta no topo e a tela inteira é
> preta, que é o que a seta prometeu ao apontar para dentro do
> morro.

**assets/home.css:422** `right: max(8px, calc(var(--gutter) - 26px));
  top: 50%;`

> Fica na calha, encostado por fora da coluna de texto: o traço
> tem 26px, então a borda esquerda dele cai exatamente na borda
> do conteúdo em qualquer largura.

**assets/home.css:485** `text-wrap: balance;
}
.fecho__link { color: var(--press-b`

> balance, não pretty: aqui são quatro linhas de título, e o que
> se quer é o rio parelho dos quatro. Os espaços rígidos da frase
> já impedem que uma linha comece ou termine em "o", "que" ou
> "e"; o balance escolhe entre as quebras que sobraram.

**assets/caso.css:67** `--calha: clamp(var(--space-16), 2vw, var(--space-32));`

> A calha cresce com a tela, mas sai da mesma régua: 16 no
> celular, 32 no desktop. É a mesma distância entre duas colunas
> em qualquer ponto da página.

**assets/caso.css:71** `--section-gap: clamp(var(--space-48), 7vw, var(--space-96`

> Uma página de caso é longa: o intervalo entre seções fica um
> pouco menor que o do resto do site, para o vazio continuar
> sendo pausa e não interrupção.

**assets/caso.css:461** `grid-row: 1 / span var(--ficha-faixas, 2);
}
.ficha-later`

> Quantas faixas da esquerda a ficha acompanha. O padrão é duas, o
> rótulo da seção e a abertura. Onde a entrada tem um parágrafo a
> mais antes do próximo bloco largo, a página pede três, e a ficha
> desce junto em vez de deixar um vão embaixo da abertura.

**assets/caso.css:1074** `@supports (grid-template-rows: subgrid)`

> Onde o subgrid existe, as cinco fases assinam as mesmas quatro
> faixas da lista: número, nome, texto e quem conduz. O fio de "quem
> conduz" passa a cair na mesma altura nas cinco, com texto de
> qualquer tamanho dos dois lados dele, porque quem decide a altura
> da faixa é a lista inteira e não cada fase por si.

**assets/caso.css:1928** `margin-inline: calc(var(--gutter) * -1);
    padding-in`

> A trilha sangra até a beirada da tela e devolve a margem por
> dentro. Assim o primeiro cartão nasce na margem da página,
> como todo o resto, e o último sai por baixo da beirada em vez
> de parar num degrau no meio do nada.

**assets/caso.css:1938** `scrollbar-width: none;
  }
  .funil::-webkit-scrollbar,`

> A barra de rolagem sai: o corte do cartão já diz que há mais
> coisa, e uma barra horizontal dentro de uma página que rola na
> vertical vira um segundo controle disputando o mesmo dedo.

**index.html:32** ``

> O favicon é o mesmo desenho da marca encolhida: o "J" com o
> sublinhado verde, sem ícone nem moldura à parte.


## Sem peça

