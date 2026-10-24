# Jeff DS no site

Plano para levar a identidade do Jeff DS, hoje feita para os posts do LinkedIn, para este portfólio. O plano completo, com inventário e fases, está publicado em https://claude.ai/artifact/GGthPLy5robgxFnJX69QQj. Este arquivo guarda o que foi decidido, para qualquer sessão continuar daqui.

O Jeff DS (tokens, cores, tipografia, componentes dos posts) está em https://claude.ai/artifact/YNnxB84kgyyzzUeY25XyeA.

## Estado

Fases 0 a 4 fechadas. Na Fase 5, as Ondas 1, 2 e 3 estão aprovadas e no artifact. A próxima é a Onda 4, o Gráfico, que vai primeiro para a vitrine.

Entregas da Fase 1, em `ds/`. `INVENTARIO.md` (matriz peça por página medida nas páginas reais), `capturas/index.html` (cada peça em 390, 768 e 1440px), `CONTRASTE.md`, `PORQUES.md` (os comentários do CSS e do HTML por peça) e `auditoria/` (os scripts que refazem tudo). A pasta do Industry foi para `arquivo/handoff/`.

Entregas da Fase 2.

- `ds/COMPONENTES.md`. A lista revisitada. As 54 peças da Fase 1 viram 15 componentes, porque boa parte delas só existia para sustentar a identidade antiga. Substitui as fusões do `INVENTARIO.md`.
- `ds/FUNDAMENTOS.md`. Cor, escala tipográfica fluida, espaço, grade, estados, movimento.
- `assets/ds/tokens.css`, `assets/ds/componentes.css` e `assets/ds/componentes.js`. O código, ainda usado só pela prova.
- `ds/prova/omnichat.html`. O caso do Omnichat montado só com o Jeff DS.

Segunda rodada da Fase 2, a pedido seu.

- `ds/REFERENCIAS.md`. Pesquisa de design editorial (grade suíça, medida de leitura, notas de margem, colunas, capítulos, grade quebrada) e o que cada variação tira dela.
- `ds/prova/variacoes/`. Seis variações da página do Omnichat, com índice em `index.html`. A 4 virou o modelo, as outras ficam como registro. Geradas por `ds/prova/variacoes.py`, que usa as partes comuns de `ds/prova/comum.py`.
- `assets/ds/icones/`. Ícones adesivo nos três acentos, 15 do kit do Jeff DS e 6 novos (camadas, fronteira, celular, megafone, verifica, rota). Gerados por `ds/icones/gerar.py`.
- `assets/ds/ilustracoes/`. Duas cenas do caso, fronteira e salto, presas ao indicador de 24% para 32%. Geradas por `ds/ilustracoes/gerar.py`.
- Menu com Home junto dos casos e o contato menor, abaixo. Rodapé sem "Fora daqui", com Voltar ao topo na linha de baixo.
- Carregamento que monta a tela em camadas (esboço, grade, componentes, textos, cores), o hero da Home ao contrário. Dura no mínimo 1,6s, mesmo com a página pronta.

Terceira rodada. A variação 4 (sumário e mosaico) foi escolhida como modelo de Caso.

- Movimento em toda troca de estado. Hover e toque com marca texto que corre só por trás das palavras, menu que desce com os itens chegando um a um, botão do menu que troca a palavra e vira xis, rolagem suave até a seção e até o topo, aba que entra subindo.
- Carregamento ao contrário quando se volta pelo histórico. A tela chega pronta e se desmonta até sobrar o esboço.
- Ficha do projeto e indicador lado a lado entre 720 e 1099px.
- Sumário vira um componente. Abaixo de 1100px ele é um trilho de marcas na borda direita, escolhido entre três formas testadas (faixa no cabeçalho, botão flutuante e trilho).

Ajustes que você fez na Fase 2. Uma página de exemplo só, a do Omnichat, que usa 13 dos 15 componentes. Revisitar a lista de componentes, que estava grande demais. E a regra do hover, que vale para o site todo (regra 5 abaixo). Toda interação que muda o estado de algo tem movimento.

Decidido na abertura da Fase 3, em 23 de outubro de 2026.

- Lista de 15 componentes aprovada como está.
- Da D3, o Carregamento em camadas fica no lugar da Passagem com o J, e a Cena dos casos sai. Na Home os casos viram uma lista de Cartões.
- Os tokens vão para o artifact do Jeff DS, no grupo Site, ao fim da Fase 3, junto com o README reorganizado em núcleo e superfícies.

## Fase 3

Tudo em Markdown dentro de `ds/`, sem tela nova. Uma etapa por vez, com parada para aprovar o formato depois da primeira.

1. Ficha padrão de dez campos em `ds/fichas/_modelo.md` e três amostras, Botão, Dado e Abas.
2. Guia de decisão em `ds/GUIA.md`, com os 15 componentes e as variantes.
3. Receitas de Caso e de Home em `ds/RECEITAS.md`.
4. Regras de ritmo em `ds/RITMO.md`.
5. CLAUDE.md completo, apontando para tudo.
6. Tokens e README no artifact do Jeff DS, e `PLANO.md` e `PROXIMA-SESSAO.md` atualizados.

Andamento.

- As seis etapas entregues e aprovadas por você em 23 de outubro de 2026.
- O plano publicado (https://claude.ai/artifact/GGthPLy5robgxFnJX69QQj) foi atualizado com o estado das fases, na seção Onde estamos.
- Tokens do Site e README reorganizado em núcleo, Posts e Site publicados no artifact do Jeff DS (versão 2 dos tokens). Os tokens dos posts não mudaram. Tamanho fluido aparece lá com o valor do desktop e a faixa no uso, porque o artifact não aceita `clamp`. A fonte dos valores continua sendo `assets/ds/tokens.css`.

Achados da Fase 3 que pesam na Fase 4.

- O modelo de Caso usa duas formas que só existem no CSS da variação 4, o mosaico e a seção ao lado do Sumário (`.bloco-sec`). Precisam virar componente antes do piloto.
- O modelo foi gerado sem `data-revelar`.
- As Abas mudam a altura da página a cada troca. O site de hoje evita isso.
- O grupo de Dados do modelo escreve o tamanho do número com `style` no HTML.

Decidido na abertura da Fase 4, em 23 de outubro de 2026.

- O piloto fica idêntico ao modelo aprovado, a variação 4 como estava no commit da Fase 3, com o revelar na entrada a mais. Por isso o Link de voltar não entra no Topo, o Problema continua em dois Cartões `meio` e o `terco` continua um terço no tablet. Essas três mudanças chegaram a ser aprovadas e foram desfeitas a seu pedido.
- O Botão é sempre lime, também em caso azul ou verde, como já diz a ficha.

## Fase 4

Entregas, aprovadas por você em 23 de outubro de 2026.

- Fichas novas da Seção, do Cartão (com o grupo em mosaico) e dos Passos, e a do Dado com o grupo em mosaico.
- Em `assets/ds/componentes.css`, a Seção com a forma do modelo e sem a `lado`, o mosaico como `.cards[data-layout="mosaico"]` com `data-tamanho`, o Dado em grupo sem `style` no HTML e sem o `.stats`, a página de caso (`.caso`) e o Topo (`.topo`).
- As Abas não mudam mais a altura da página a cada troca.
- `ds/prova/caso.py` gera `case-omnichat.html` e o miolo da variação 4. A página é idêntica à v4 do commit da Fase 3 nas três larguras, conferida elemento por elemento, com o revelar na entrada a mais e o "cerca de" para leitor de tela no "~40 mil".
- A página publicada leva a descrição, o analytics e o título de antes, sem o `noindex` das provas.
- `assets/analytics.js` não conta mais visita servida em localhost.

Achados que ficam para depois.

- O título do Omnichat ocupava cinco linhas em 390px, e a receita pede até quatro. Resolvido na Onda 2 da Fase 5, com o título mais curto.
- O menu do Jeff DS não tem o Manifesto. Ele segue no ar pelas outras páginas até a Fase 6 (D7).
- A primeira prova, `ds/prova/omnichat.html`, usava a Seção antiga e mudou de cara. Fica como registro.
- Sem JS e com movimento reduzido não foram conferidos no navegador, só no código.

## Fase 5

Plano aprovado por você em 23 de outubro de 2026. A biblioteca completa, em cinco ondas.

| Onda | O que entra |
| --- | --- |
| 1, casca | Fichas do Cabeçalho, do Rodapé e do Sumário, que já têm código. O pular para o conteúdo e o Carregamento passam pela mesma conferência |
| 2, ação e texto | Fichas do Link, da Etiqueta e do Destaque. O Destaque ganha `nota`, `atrito` e frase no papel. O título do Omnichat em cinco linhas se decide aqui |
| 3, sequência e comparação | Passos em `estagios`, `funil`, `trilha` e `ritos`. Ficha e código do Antes e depois em `confronto` e `citacao` |
| 4, dados | Ficha e código do Gráfico em `barras`, `pilhas` e `escala` |
| 5, mídia, hero e Home | Ficha e código da Imagem em `moldura`, `galeria` e `sangria`. O hero com a ilustração do esboço que sobra. O Cartão de caso da Lista de casos |

Como cada onda anda. A interface vem antes da documentação, pedido seu em 24 de outubro de 2026, a partir da Onda 3.

1. As peças da onda vão primeiro para a vitrine, em `ds/vitrine/`, já com o código em `tokens.css`, `componentes.css` e `componentes.js` e o texto real do caso onde cada forma aparece hoje.
2. Na vitrine cada peça aparece sozinha, numa amostra com todas as formas e o nome de cada uma, num quadro que se testa em 390, 768 e 1440px. A peça aplicada numa página, com outras peças em volta, fica no palco dentro da página da ficha.
3. A conferência em 390, 768 e 1440px, sem JS e com movimento reduzido, hover só com mouse e alvos de 44px. O Omnichat é comparado de novo, elemento por elemento, porque tudo o que muda em `componentes.css` chega nele.
4. Você olha, testa e aprova a interface e o comportamento.
5. Só depois vêm as fichas, os guias e o artifact do Jeff DS. As prévias do artifact saem das amostras, por `python3 ds/vitrine/artifact.py <pasta>`. Commit só quando você pedir.

Andamento da Onda 1.

- Fichas do Cabeçalho, do Rodapé e do Sumário aprovadas, com as três recomendações. Os tempos fora dos tokens passaram a `dur-media` e `dur-lenta`, o menu fecha quando o foco sai e o trilho leva o foco ao primeiro item, e a lista do Rodapé virou "Páginas".
- No código, o token `altura-cabecalho`, os links do Contato como Links `externo`, a página atual marcada no Rodapé, e o nome da Seção que não aparece mais sobre o Rodapé.
- A vitrine em `ds/vitrine/`. Cada peça roda ao vivo num palco, uma página de verdade num quadro que troca entre 390, 768 e 1440px e responde a mouse, toque e teclado, com a lista do que testar. A ficha abre como página, convertida do Markdown de `ds/fichas/` pelo mesmo gerador. Sem JS o quadro fica na largura da coluna. Pedido seu, depois da primeira versão, que só levava ao Markdown.
- Conferido no navegador. As três larguras sem rolagem lateral, o teclado no menu e no trilho, e sem JS (menu aberto no fluxo, lista do Sumário no topo, nada escondido). O Omnichat ficou idêntico ao do commit da Fase 4 nos 137 elementos do `main`, nas três larguras. Mudaram só o Contato do menu e a lista do Rodapé.
- Movimento reduzido conferido só no código. O navegador da sessão não simula a preferência.
- O Carregamento ainda usa tempos próprios (1,6s, 1,95s e outros), fora dos tokens. É fundamento e tem o mínimo de tempo como regra, então fica como está até você decidir.
- Aprovada por você em 23 de outubro de 2026, com a vitrine ao vivo. As três peças foram para o artifact do Jeff DS no grupo Site · Casca (`SiteCabecalho`, `SiteRodape` e `SiteSumario`), com prévias que rodam o CSS e o JS do site, copiados em `site/` do artifact, e o token `altura-cabecalho` no `tokens.json`.

Andamento da Onda 2.

- Fichas novas do Link, da Etiqueta e do Destaque, em `ds/fichas/`. O Botão já tinha ficha e não muda.
- O Destaque ganha a frase no papel (o Grito de hoje), a `nota` (a Linha de nota) e o `atrito`, que sai da tinta e vai para o `muted` com o ícone de alerta.
- Fichas aprovadas por você em 24 de outubro de 2026, com três decisões.
  - O ritmo dos Destaques. A regra 3 do `ds/RITMO.md` passou a ser uma frase na tinta, até uma frase no papel fora da Seção dela e no máximo um Destaque médio por Seção.
  - O link no meio do texto é a única exceção aos 44px, como a WCAG aceita. Está escrito no `CLAUDE.md`, nos Fundamentos e na ficha.
  - O título do Omnichat encurtou para "Verificação de intenção dos agentes conversacionais", e o `title` da página acompanha. A receita do Topo diz que, se passar de quatro linhas, encurta o título e não a régua do display.
- No código, o `.callout` ficou sem caixa, e o recuo e o raio foram para a `.callout.superficie-tinta`. Entraram a `.callout__legenda`, a `nota` (régua, rótulo e texto, em duas colunas a partir de 720px) e o `atrito` (fundo `muted`, contorno, alerta na margem a partir de 720px). As Etiquetas do Topo viraram lista, no gerador e na variação 5.
- Na vitrine, os palcos do Link, da Etiqueta e do Destaque. O do Destaque e o da Etiqueta são casos pequenos com Sumário, para a peça ter a largura que tem no caso. O Destaque usa o texto do Inpulse, do Processo e do Omnichat, um Destaque por Seção.
- Conferido no navegador em 390, 768 e 1440px, sem rolagem lateral, e os Links com seta com 44px no toque. O Omnichat foi comparado com o estado aprovado da Onda 1, elemento por elemento. Fora do Topo nada mudou. No Topo só o título encurtou (quatro linhas em 390 e em 1440, duas em 768) e o que vem abaixo dele subiu junto.
- A lista de Etiquetas esticava a linha em 1440 e descia o título 2px. Cada item virou caixa flex, e a diferença sumiu.
- Achado para a Fase 6. A Seção 05 do Processo tem a frase no papel e a nota juntas, e a regra nova pede uma das duas fora dali.
- Aprovada por você em 24 de outubro de 2026. As três peças foram para o artifact do Jeff DS no grupo Site · Ação e texto (`SiteLink`, `SiteEtiqueta` e `SiteDestaque`), com o CSS do site atualizado em `site/` e os ícones de alerta, xis e visto em `site/icones/`. O README do artifact ganhou a exceção dos 44px.

Andamento da Onda 3.

- Em 24 de outubro de 2026 você pediu para ver a interface antes de aprovar fichas. A vitrine passou a mostrar cada peça sozinha, com todas as formas, e o palco foi para a página da ficha. O Link com variante ficou na largura das palavras, porque numa grade ele esticava e o marca texto corria pelo vazio.
- As fichas abaixo foram escritas antes dessa mudança. Elas servem de rascunho para montar a Onda 3 na vitrine e só se fecham depois que você aprovar a interface.
- Na vitrine, com as três recomendações aplicadas. O Passos ganhou `estagios` (o meio na faixa do acento, a saída com as cinco entregas do Processo em Abas), `funil` (faixas que estreitam e desenham o funil, num quarto da largura a partir de 720px), `trilha`, `ritos` e o efeito opcional. O Antes e depois ganhou a `citacao` e o `confronto`, este como tabela de verdade. Os níveis de desejabilidade do Inpulse ficaram para o Gráfico `pilhas`.
- Os palcos mostram o Passos com o texto do Processo e o Antes e depois com o Inpulse, o Omnichat e o Processo.
- Conferido em 390, 768, 1000 e 1440px sem rolagem lateral. O Omnichat não mudou em nenhum elemento fora do Topo, do `main` ao Rodapé, nas três larguras.
- A linha 3 do Mapa tem dois parágrafos, e a ficha pede um. Fica para decidir com a ficha, depois da interface.
- Você aprovou o Antes e depois como está (a tabela e os Cartões) e recusou o Passos e o funil, pedindo um estudo como o das seis variações de página, com mais iconografia e alinhamento mais cuidadoso.
- O estudo está em `ds/vitrine/estudo/`, gerado por `ds/vitrine/estudo.py`. Seis direções, cada uma montando as seis formas com o texto real, numa página com o Sumário. Tabela suíça, Coluna e margem, Adesivos, Diagrama (a forma desenhada, com o funil de verdade, a escada e a estrada), Linha do tempo e Jornal. O CSS de cada direção mora no gerador do estudo e só vai para `componentes.css` depois da sua escolha, que pode misturar formas de direções diferentes.
- Você escolheu a direção 3, Adesivos. No tablet os três Cartões lado a lado apertavam o conteúdo, e a saída dos estágios vazava do Cartão. Agora o arranjo segue a largura da Seção (container query), e não a da tela, porque a partir de 1100px o Sumário ocupa a coluna da esquerda e a Seção volta a ter uns 750px. Três lado a lado só com 900px de Seção, dois no par e nos ritos com 600px, e um embaixo do outro no resto. A saída lista as entregas com fios, porque "Relatório de usabilidade" não cabe numa pílula de um terço. Conferido em 390, 768, 1024, 1100, 1280 e 1440, sem nada vazando dos Cartões.
- A D3 foi para o componente, a seu pedido. O bloco Steps de `componentes.css` foi trocado inteiro. Cada etapa é um Cartão com o adesivo no canto e o número vazado, e o arranjo segue a largura da Seção, que virou container (`.section { container-type: inline-size }`). As formas são a sequência (sem atributo), `par`, `estagios` (setas de tinta entre os Cartões), `funil`, `trilha` e `ritos` (com `.step__topo`). As entregas da saída usam `.step__lista`, e as Abas com o detalhe de cada entrega vêm logo depois dos estágios, no palco.
- A amostra e o palco do Passos na vitrine foram refeitos com a D3. Nada vaza dos Cartões em 390, 768, 1024, 1280 e 1440, e o Omnichat não mudou em nenhum elemento, do conteúdo ao Rodapé, nas três larguras.
- A ficha do Passos ainda descreve a primeira proposta. Ela se reescreve depois que você aprovar a D3 na vitrine. A primeira prova (`ds/prova/omnichat.html`) e as variações 1 e 3, que usavam o Passos `par`, agora aparecem com os Cartões. Ficam como registro.
- O nome "Cinco entregas" na saída não existe no Processo de hoje. Entrou para a amostra, e o nome de verdade se escreve na Fase 6.
- Aprovada por você em 24 de outubro de 2026, na vitrine. As fichas do Passos e do Antes e depois foram fechadas com o que está no código, o GUIA passou as formas para "no código hoje", o RITMO passou o Passos para médio, e os Fundamentos ganharam a regra do arranjo pela largura da Seção.
- No artifact, `SitePassos` e `SiteAntesDepois` entraram no grupo Site · Sequência. As prévias do Site apareciam só com o HTML, porque o card do artifact traz o próprio `<head>` e aproveita da prévia só o elemento raiz e um script, e assim perdia os `<link>` do CSS e o acento no `<body>`. Agora as oito prévias saem de `ds/vitrine/artifact.py`, feitas das amostras da vitrine, com o CSS, o JS, o acento e os ícones dentro do elemento raiz. Testadas sozinhas no navegador, sem nada de fora. Não consegui ver no claude.ai, que pede login no navegador da sessão.
- A ficha do Passos foi reescrita com as quatro formas, e o Antes e depois ganhou a ficha que faltava (`ds/fichas/antes-e-depois.md`).
- `estagios`. Três linhas com rótulo, e o estágio do meio no acento. Ele era tinta no site de hoje, e sai pela D4, como o atrito.
- `funil`. Um item debaixo do outro, com faixas do acento que estreitam de cima para baixo e desenham o funil. No celular ele desce na vertical, sem carrossel, pela mesma regra das Abas, e a `trilha` também.
- `trilha`. O fio com um ponto por marco, na horizontal a partir de 720px.
- `ritos`. Itens lado a lado com régua em cima, sem ordem.
- `citacao`. A mesma caixa da conversa, com a fala em Fraunces, a voz de conversa do sistema, e o Anton fica para a voz do caso.
- `confronto`. Uma tabela de verdade, com a coluna do depois no acento. No celular cada linha vira bloco, e os papéis de tabela vão escritos no HTML para o Safari não esquecer a tabela.
- Três pontos para você decidir.
  - O funil vertical. No site de hoje são cinco colunas na largura da página. Com o Sumário ao lado a coluna do caso tem 972px em 1440, e cinco colunas dariam uns 175px cada, com textos de dez linhas. Recomendo a forma vertical.
  - Os três níveis de desejabilidade do Inpulse usam a forma dos ritos hoje, mas são a legenda das pilhas logo abaixo. Recomendo levar para o Gráfico `pilhas`, na Onda 4.
  - O Passos ganha um efeito opcional, a mesma faixa `muted` do efeito do Cartão, para a "Consequência" do Mapa e o "Quem conduz" do funil. Recomendo, em vez de criar uma parte para cada caso.

## Decisões da Fase 0

| | Decisão | Status |
| --- | --- | --- |
| D1 | O site adota o Jeff DS inteiro. Saem o verde marca texto, a trama e a Instrument Serif. | Aprovada |
| D2 | Um Jeff DS só, com núcleo da marca e duas superfícies, Posts e Site, no mesmo artifact. | Aprovada |
| D3 | O hero fica, com formato novo (ver abaixo). O revelar fica repintado. A passagem com o J vira o Carregamento em camadas e a cena dos casos vira lista de Cartões. A onda e a trama saem. | Ajustada |
| D4 | A tinta vira superfície pontual, no rodapé e em no máximo uma parada por página. O topo do caso deixa de ser escuro. | Aprovada |
| D5 | Acento dominante por caso. Processo em lime, Omnichat em azul, Inpulse em verde, Mapa em azul. | Aprovada |
| D6 | Só HTML, CSS e JS, sem servidor e sem build. Usar a nomenclatura e os tokens do shadcn. | Ajustada |
| D7 | O manifesto sai desta versão e será repensado no futuro. Continua no ar até a Fase 6. | Ajustada |
| D8 | Arquivar a pasta `handoff/`, que descreve o sistema Industry, já obsoleto. | Aprovada |

## Regras que já valem

1. Lime, azul e verde nunca viram texto, nunca são a única borda de um controle e nunca são o anel de foco. Sobre o papel o contraste deles fica entre 1,1 e 1,5 para 1. Texto, borda e foco são sempre tinta.
2. Tokens com nomes do shadcn apontando para o Jeff DS. `background` paper, `foreground` ink, `primary` lime com texto em tinta, `secondary` azul, `muted` e `accent` mist, `border` e `ring` ink, `radius` 12px, gráficos em lime, azul e verde.
3. Componentes com nomes do shadcn (Button, Badge, Card, Tabs, Sheet, Dialog, Carousel, Table, Separator) e variantes por atributo de dados, sem React nem Tailwind.
4. Tudo funciona sem JS e com movimento reduzido.
5. Hover só existe onde há mouse. Toda regra de hover fica dentro de `@media (hover: hover) and (pointer: fine)`, e nada pode depender dele para ser descoberto. No toque, o retorno vem do pressionado (`:active`) e do foco, e todo alvo tem pelo menos 44px. A separação é por capacidade de entrada, nunca por largura de tela, e tablet com toque segue o celular.

## Fases

0. Decisões de base. Aprovada.
1. Inventário fechado e auditoria. Capturas em 390, 768 e 1440px, matriz peça por página, fusões, contraste, porquês extraídos dos comentários do CSS, pasta handoff arquivada.
2. Fundamentos do site. Escala tipográfica fluida, espaço, grade, estados, movimento, tokens no padrão shadcn e revisão da lista de componentes, provados numa página só, a do Omnichat.
3. Modelo de documentação. Ficha de dez campos, guia de decisão, receitas de Home e Caso, regras de ritmo, CLAUDE.md completo.
4. Piloto visual. A prova do Omnichat vira a página publicada, no lugar de `case-omnichat.html`.
5. Biblioteca completa, em cinco ondas.
6. Migração da Home e dos quatro casos. Manifesto sai do menu, do rodapé e da Home.
7. Governança.

## Hero

A frase continua a mesma e passa a ficar alinhada à esquerda. "O ofício continua o mesmo. O jeito de fazer, não." Ao lado, uma ilustração no estilo da marca que apoia a provocação, com movimento ligado à rolagem.

### O cuidado que muda tudo

A frase diz que uma coisa fica e outra vai embora. Se a ilustração inteira se desfaz na rolagem, ela contradiz a frase, porque diz que nada fica. O movimento precisa separar as duas metades. O jeito de fazer se desmonta e sai da tela. O ofício fica parado e termina sozinho no quadro.

### Ideias descartadas

1. Robô, cérebro com circuito ou o brilho de quatro pontas que virou símbolo de IA. São o lugar comum que a frase tenta evitar.
2. Mão humana e mão de robô, ou tela dividida em antes e depois. Contam uma disputa, e a frase fala de continuidade.
3. Partículas ou poeira se dissolvendo. É efeito genérico, pesa no celular e não diz o que fica.
4. Lápis que vira cursor. É literal demais e coloca a mudança na ferramenta, que é justamente o que o lead diz que não é o ponto.

### Recomendada. O esboço que sobra

Uma tela de produto pronta, desenhada no traço de 2px da marca, montada em camadas por cima de um esboço feito à mão. Na rolagem a tela se desmonta na ordem do que hoje a IA já produz. Primeiro saem as cores chapadas, depois os textos, depois os componentes, depois a grade. Cada camada desliza para fora do quadro com um leve giro, como adesivo descolando. No fim sobra só o esboço à mão, com uma anotação de quem decide, uma seta e um "por quê?".

O que fica é a decisão, que é o ofício. O que vai embora é a produção da tela, que é o jeito. Conversa direto com os casos, em que o protótipo já nasce desenvolvido e o design passa a decidir onde a atenção humana faz diferença.

### Alternativas

1. A mesa que esvazia. A cena "mesa" do Jeff DS com a pessoa cercada de ferramentas do jeito antigo, régua, post its, telas impressas. Na rolagem as ferramentas se soltam e saem, e ficam a pessoa e uma folha com a decisão. Tem gente na cena, o que aproxima, mas fica mais carregada ao lado de uma frase grande.
2. A pergunta que fica. A cena "pergunta" com a pessoa diante de uma parede de ícones adesivo. Os ícones se espalham e sobra um adesivo grande de interrogação. É a mais simples de produzir e a mais fraca de sentido, porque a pergunta não aparece na frase.

### Especificação do movimento

1. Ligado à rolagem, do topo da página até o hero sair da tela. Nada acontece sozinho com o tempo.
2. Cinco camadas saem em escada, cada uma com deslocamento e giro próprios, sempre para fora do quadro. O esboço não se move.
3. CSS com linha do tempo de rolagem onde o navegador suporta, e JS com `requestAnimationFrame` como reserva.
4. Sem JS ou com movimento reduzido aparece um quadro parado com as camadas levemente afastadas umas das outras, em vista explodida, que conta a mesma ideia sem movimento.
5. A ilustração é decorativa para leitor de tela. A frase carrega o sentido.
6. Desktop com a frase em 7 colunas e a ilustração em 5. No celular a frase vem primeiro e a ilustração entra abaixo, menor.
