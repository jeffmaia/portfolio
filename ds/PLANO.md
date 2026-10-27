# Jeff DS no site

Plano para levar a identidade do Jeff DS, hoje feita para os posts do LinkedIn, para este portfólio. O plano completo, com inventário e fases, está publicado em https://claude.ai/artifact/GGthPLy5robgxFnJX69QQj. Este arquivo guarda o que foi decidido, para qualquer sessão continuar daqui.

O Jeff DS (tokens, cores, tipografia, componentes dos posts) está em https://claude.ai/artifact/YNnxB84kgyyzzUeY25XyeA.

## Estado

Fases 0 a 5 fechadas. As cinco ondas da Fase 5 foram aprovadas e estão no artifact, e as quinze peças da biblioteca estão no código. Na Fase 6 a Home e os quatro casos foram migrados e aprovados por você, o Manifesto saiu do ar e o site antigo foi para `arquivo/site-antigo/`. Os cinco passos estão feitos e falta o commit (ver Fase 6, mais abaixo).

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
- `assets/analytics.js` também não conta visita pela rede de casa (IP privado, `.local`) e tem a marca de aparelho interno: abrir o site publicado com `?interno=1` para a medição naquele navegador, `?interno=0` desfaz. Quem acessa de casa pelo site publicado só sai da conta assim, ou pelo filtro de tráfego interno por IP no painel do GA4.

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

Andamento da Onda 4.

- Em 24 de outubro de 2026 o Gráfico foi para a vitrine, antes da ficha. O código está em `assets/ds/componentes.css` (bloco Chart), sem JS novo. A amostra mostra as quatro formas, cada uma no acento do caso de onde vem o número, e o palco tem o Experimento do Inpulse, a nota do Mapa e o Resultado do Processo.
- O desenho vem das Barras dos posts. Trilho de papel com contorno de 2px e raio pela metade, e o preenchimento com o fio de tinta na ponta.
- Três tons com forma própria, em `data-tom`. `cheio` é o acento, `trama` são fios de tinta na diagonal e `vazio` é o papel. Nas barras o antes é trama e o depois é cheio. Nas pilhas entusiasta é cheio, receptivo é trama e indiferente é vazio. A trama entrou porque o azul e o mist quase se confundem, e a diferença não pode depender só da cor.
- `barras`. Uma grandeza por grupo, com o nome em cima, o rótulo à esquerda e o valor à direita. Dois grupos lado a lado com 600px de Seção.
- `pilhas`. Os três níveis de desejabilidade do Inpulse viraram a legenda, com o que cada um quer dizer. Uma faixa por funcionalidade, cada parte na proporção da contagem (`--n`), e a conta escrita embaixo. Com 600px de Seção o nome vai para a esquerda.
- `escala`. Eixo de −100 a +100 com o zero marcado, o percurso do antes ao depois no acento, o antes num ponto vazado e o depois num ponto de tinta. Os dois valores ficam acima do eixo, cada um na sua linha, para não se encostarem.
- Os valores vão no HTML como números em variáveis (`--valor`, `--n`, `--antes`, `--depois`), e o texto ao lado diz o mesmo número. O desenho fica escondido do leitor de tela, e cada Gráfico é uma figura com título.
- A entrada usa o revelar da página. Depois que o bloco sobe, uma tampa de papel descobre as faixas da esquerda para a direita, e na escala o percurso corre e só então aparece o depois. Sem JS e com movimento reduzido tudo nasce pronto.
- Conferido em 375, 768 e 1440 sem rolagem lateral, e sem erro no console. O Omnichat não muda, porque o bloco só acrescenta regras com `.chart` e nenhuma página publicada usa a classe. Movimento reduzido conferido só no código.
- A vitrine passou a aceitar peça sem ficha (`SEM_FICHA` em `ds/vitrine/gerar.py`). A página da ficha mostra só o palco e o que testar até a ficha existir.
- Aprovada por você em 24 de outubro de 2026, na vitrine, como estava. A ficha do Gráfico foi escrita (`ds/fichas/grafico.md`) e o Gráfico saiu de `SEM_FICHA`.
- O GUIA passou o Gráfico para "no código hoje", com os tons, e ganhou a regra de que o número do Gráfico não volta no Dado da mesma Seção. O RITMO ganhou um Gráfico por Seção na regra 10 e o número repetido no checklist. Os Fundamentos dizem que o Gráfico pinta só com o `acento` e que os `chart-1` a `chart-3` ficam reservados.
- No artifact, `SiteGrafico` entrou no grupo Site · Dados (versão 18), com a prévia feita da amostra por `ds/vitrine/artifact.py`, o CSS do site atualizado em `site/` e a Onda 4 no README. A prévia foi testada sozinha no navegador, sem nada de fora.
- Achado para a Fase 6. No Mapa, o 890 aparece nas barras do Resultado e de novo no Dado em grupo logo abaixo. A regra nova pede que saia de um dos dois.

Andamento da Onda 5.

- Em 24 de outubro de 2026 as três peças foram para a vitrine, antes das fichas, e estão em `SEM_FICHA`. A especificação do hero estava fechada aqui, e a Imagem e o Cartão de caso seguem o site de hoje e a receita, então não houve estudo de direções.
- Imagem (`.figure`, bloco Figure de `componentes.css`). A `moldura` é a caixa do sistema com o `muted` por baixo, e com `data-formato="retrato"` para de crescer em 400px (o protótipo do Inpulse). A `galeria` abre as telas na ordem do percurso, duas por linha com 600px de Seção, e com `data-abertura` a primeira ocupa a linha inteira (as cinco telas do Mapa). A `sangria` vai até a beira da tela, e no caso a partir de 1100px sangra só para a direita, porque a coluna da esquerda é do Sumário (as telas do Inpulse). O `body` ganhou `overflow-x: clip`, para a sangria não abrir rolagem para o lado onde a barra de rolagem ocupa lugar.
- Hero (`.hero`, nas receitas de `componentes.css`, com o desenho em `ds/prova/comum.py`). É o Carregamento ao contrário, com as mesmas peças. Saem as cores, os textos, os componentes e a grade, cada uma na sua direção e com o seu giro, e sobra o esboço com o botão circulado, a seta e o "por quê?". O progresso vai do topo até o hero sair de baixo do cabeçalho, pela linha do tempo de rolagem do CSS (`view-timeline`, `exit-crossing`) e, onde ela não existe, pelo módulo 5 do `componentes.js`. Toda a desmontagem cabe no primeiro terço do progresso, para o esboço aparecer sozinho ainda inteiro na tela, no celular e no desktop. Sem JS ou com movimento reduzido, a vista explodida parada, com as camadas escapando pelas bordas do quadro e o esboço legível no meio. A tela cheia é só a partir de 1100px. No tablet ela deixava papel vazio em cima e embaixo.
- A especificação fala em cinco camadas saindo, mas lista quatro (cores, textos, componentes e grade) e diz que o esboço fica. Segui as quatro, que são as do Carregamento.
- Cartão de caso (`.card[data-variant="caso"]`, no mosaico com `meio`). O acento do caso entra só na base, com o Dado `salto` no tamanho de grupo, a ficha numa linha e o Link "Ver o caso", que diz ao leitor de tela qual caso abre. Sobre o acento o marca texto do Link corre em papel (`--marca`). O título, a frase e o rótulo com o número e o nome do caso ficam no papel. O rótulo não está na receita, e entrou porque o título do Omnichat não diz o nome do caso.
- O texto e os números vêm do Topo de cada caso publicado. O Omnichat usa o título novo da Onda 2, e o salto dele é 24% para 32%, como no caso, e não o +8% da Home de hoje.
- Conferido no navegador em 375, 390, 768 e 1440, sem rolagem lateral e sem erro no console. O Omnichat ficou idêntico ao do commit da Onda 4 nos 291 elementos da página, nas três larguras. O módulo 5 do JS não roda neste Chrome, que tem a linha do tempo de rolagem, e foi conferido só no código, assim como o movimento reduzido.
- Pontos para a Fase 6. O Inpulse tem a sangria e o Destaque na tinta no mesmo caso, e a regra 2 do ritmo pede um ou outro.
- Sua primeira revisão, em 24 de outubro de 2026. A Imagem e o Cartão de caso estão aprovados na forma. Lado a lado, as bases dos Cartões não se alinhavam. Agora os Cartões dividem as linhas da grade (subgrid), e o rótulo, o título, a frase, o Dado, a ficha e o Link de um ficam na mesma altura que os do vizinho, conferido em 768 e 1440. O hero vai ganhar motion, com três cenas que se constroem na chegada e a frase em duas linhas. O roteiro está em `ds/ROTEIRO-HERO.md`, para você colaborar antes de qualquer código.
- Segunda revisão, no mesmo dia. Você trocou a direção do hero. A frase passa a ser a própria cena, em três momentos (rascunho, cores, ilustrações e ícones), com só um deslocamento leve na rolagem. O roteiro foi reescrito, e os três momentos parados estão em `ds/vitrine/estudo/hero/`, gerados por `ds/vitrine/estudo_hero.py`, com as imagens em 1440 e 390 tiradas por `ds/vitrine/fotografar.mjs`.
- Os três momentos foram aprovados por você, e a chegada foi para o código. O hero novo substituiu o quadro em `componentes.css` e a função `hero` de `ds/prova/comum.py`. A chegada é toda de CSS, com os tempos dos tokens, e roda uma vez em uns 3,2s. O deslocamento da rolagem usa o mesmo progresso de antes (linha do tempo de rolagem ou o módulo 5 do JS). As cores das palavras pedem `primary`, `secondary` e `chart-3`. Conferido no navegador com a chegada parada em sete instantes em 1440 e 390, depois de rolar, sem JS e com movimento reduzido (a página chega pronta, sem animação). O Omnichat ficou idêntico nos 291 elementos, nas três larguras. Seguem abertos o degrau da frase na escala, a exceção da regra 7 para as cores e o Carregamento da Home.
- Aprovada por você em 24 de outubro de 2026, com a chegada e a rolagem do hero. As fichas novas são a da Imagem (`ds/fichas/imagem.md`) e a do hero (`ds/fichas/hero.md`), e o Cartão de caso entrou na ficha do Cartão como a variante `caso`. Na vitrine, a peça do Cartão de caso abre a ficha do Cartão, com o palco da Lista de casos dentro dela, e nenhuma peça ficou em `SEM_FICHA`.
- O GUIA passou a Imagem para "no código hoje" e ganhou a linha do Cartão `caso`. As RECEITAS descrevem o hero novo e a Lista de casos com o rótulo e o alinhamento. O RITMO pôs a moldura e a galeria nas peças médias, uma Imagem por Seção e uma galeria por caso, e a regra 7 ganhou a exceção da Home (a Lista de casos e o hero mostram os três acentos). Os Fundamentos dizem que a frase do hero é a única fora da escala, que o hero pede `primary`, `secondary` e `chart-3`, e que o Carregamento é o mesmo gesto do hero. Na seção Hero, mais abaixo, a especificação antiga fica como registro.
- No artifact, `SiteImagem`, `SiteHero` e `SiteCartaoCaso` entraram no grupo Site · Mídia e Home (versão 19). As doze prévias foram refeitas com o CSS de agora, o CSS e o JS do site foram atualizados em `site/`, os sete ícones do hero foram para `site/icones/`, e o README ganhou a Onda 5 e a exceção da Home. As três prévias novas foram testadas sozinhas no navegador. A da Imagem carrega as telas do Framer e o protótipo do Figma de fora, como o site, e não consegui ver no claude.ai se o card deixa.

## Fase 6

Plano aprovado por você em 25 de outubro de 2026, com todas as recomendações.

| Passo | O quê |
| --- | --- |
| 0 | Gerador e casca. O `comum.py` aceita qualquer acento e qualquer página atual, e o `caso.py` monta qualquer caso. O Omnichat sai idêntico |
| 1 | Mapa de experiência |
| 2 | Inpulse |
| 3 | Processo com IA |
| 4 | Home, e o Manifesto sai do ar |
| 5 | Limpeza dos arquivos antigos e dos documentos |

Cada página para numa conferência sua no navegador, em 390, 768 e 1440, sem JS e com movimento reduzido.

Decisões que valem para os três casos.

1. Uma cena por caso no Topo, presa ao indicador, desenhada em `ds/ilustracoes/gerar.py`. A cena é mostrada sozinha antes de você aprovar a página.
2. O Contexto aceita o `t-lead` e mais um parágrafo de apoio, para o texto de hoje ficar inteiro.
3. Os dois pontos do texto viram ponto final, e "30–40 min" vira "30 a 40 min".
4. As seções que estavam na tinta passam para o papel (D4), o Link "Todos os casos" sai do Topo e a ficha do projeto sobe para o Topo.

Mapa (azul, cinco seções). 01 Contexto, 02 O que move a nota, 03 Processo, 04 Solução, 05 Resultado.

5. A 01 deixa de se chamar "A pergunta". A pergunta é o `t-lead` e o parágrafo sobre o grupo é o apoio.
6. A linha 3 do Processo junta os dois parágrafos num só, com o mesmo texto.
7. O 890 sai do Dado em grupo, porque já está nas barras. Ficam +48, 16 campus e 12 etapas, em terços.

Inpulse (verde, cinco seções). 01 Contexto, 02 O aluno, 03 Descoberta, 04 Experimento, 05 Resultado.

8. As falas dos alunos saem do Contexto e vão para a Seção "02 · O aluno", com o título "O que o aluno dizia" e o Antes e depois `citacao`.
9. A Descoberta fica com o primeiro parágrafo, a nota "O aluno de medicina", o segundo parágrafo e o protótipo em `moldura` `retrato` com o Link. Mudou na sua revisão de 25 de outubro. Os três viram parágrafos corridos à esquerda, a nota no meio, e o protótipo fica à direita com o Link.
10. No Experimento fica a frase no papel "O calendário doía mais que o boletim", e a nota "O que a gente cortou" vira o parágrafo que fecha a Seção. Os níveis de desejabilidade são a legenda das `pilhas`.
11. A imagem do Resultado vai para a `moldura`, porque são telas do app e a `sangria` não pode ficar com o Destaque na tinta. A `sangria` fica na biblioteca sem página que a use.

Processo (lime, oito seções). 01 Contexto, 02 O problema, 03 O que a gente fez, 04 Rituais, 05 Liderança, 06 O novo funil, 07 Antes e depois, 08 Resultado.

12. A regra 12 do `ds/RITMO.md` passa a "de quatro a oito seções". Oito marcas do trilho somam uns 300px e cabem no celular.
13. Os dois títulos de hoje ficam nos Passos `par`, e a Seção 02 ganha um título curto novo, que vem para você aprovar.
14. Na 03 a ordem é estágios, o atrito "A primeira tentativa não foi essa" e as Abas, para a 03 e a 04 não fecharem com a mesma peça. A saída dos estágios se chama "Os rascunhos".
15. Na Liderança fica a frase "O que sobra pra gente?", e "O que destravou" vira o último parágrafo.
16. No Resultado o "~1 sem" e o "30 a 40 min" saem do Dado em grupo, porque estão nas barras. Ficam o Kanban e os 100%.

Home e Manifesto.

17. Na Home a cortina do Carregamento não monta a tela, porque o hero faz esse papel. A frase do hero ganha um degrau próprio em `tokens.css`, fora da escala de texto. As notas do rascunho ficam como estão. A descrição para a busca é a linha de apoio do hero.
18. A página do Manifesto sai do ar. O git guarda a página para ela ser repensada depois.
19. Na limpeza, os CSS e JS antigos, as fotos, a trama e a cortina do J vão para `arquivo/site-antigo/`, depois de conferir que nada aponta para eles.

Andamento.

- Passo 0, em 25 de outubro de 2026. O `comum.py` aceita o acento (`cabeca`) e qualquer página atual no menu e no rodapé (`PAGINAS`, `atual`), e os blocos do Topo e do fechamento recebem o texto do caso. O miolo de cada caso mora em `ds/prova/casos/`, um módulo por caso, e o `caso.py` gera todos os casos de `CASOS`. As peças que levam conteúdo (Passos, Gráfico, galeria, Dado em grupo, Seção) saíram da vitrine para `ds/prova/pecas.py`, e a vitrine e as páginas usam o mesmo código. O Omnichat, as variações e a vitrine saíram idênticos, byte a byte. Na vitrine mudou só a amostra do Passos, com a terceira decisão do Mapa num parágrafo (decisão 6).
- Passo 1, Mapa. A cena `mapa-salto.svg` desenha o chão como o zero, o antes como um poço de 33 pontos e o depois como um degrau de 15 no lime, com a pessoa em cima e o percurso tracejado de um para o outro. A página é gerada por `ds/prova/casos/mapa.py`, com todo o texto da página antiga.
- Ajustes que a página pediu. A ficha da Etiqueta não tem rótulo sobre o grupo, então os eixos são uma lista de Etiquetas com o nome "Eixos do mapa" para leitor de tela, logo depois do parágrafo que fala dos eixos. O "12 etapas" quebrava em duas linhas no Cartão de um terço, então o valor é "12" e a frase começa com "etapas", como no "16 campus" ao lado. O "palavras‑chave" usa o hífen que não quebra.
- Conferido em 1440, 768 e 390 sem rolagem lateral. O título tem quatro linhas em 1440 e em 390 e duas em 768. Os `id` não se repetem e todo `aria-labelledby` aponta para um elemento que existe. O revelar só esconde com `.js-mov`, então sem JS e com movimento reduzido a página nasce pronta (conferido no código).
- Revisão sua do Mapa, em 25 de outubro de 2026. No Gráfico `escala`, os dois valores passaram para uma linha só, cada um sobre o próprio ponto e na ordem dos pontos. O da esquerda termina no ponto dele e o da direita começa no dele, então os dois não se cobrem, por perto que fiquem. Numa queda a figura leva `data-sentido="queda"`, que o `pecas.escala` põe sozinho. Testado com os pontos colados (10 e 12), nas duas bordas e numa queda. A ficha do Gráfico foi atualizada. Na cena, o tracejado agora sai do vértice da seta e entra pelo meio da abertura, e a seta aponta para onde a linha chega, para baixo, no rumo do degrau.
- Passo 2, Inpulse, em 25 de outubro de 2026. A cena `inpulse-salto.svg` desenha as recuperações como folhas de prova empilhadas, oito no papel para o antes e seis no lime para o depois, com o contorno tracejado das duas que saíram. A aluna ao lado olha o app no celular, com a tela no lime. A página é gerada por `ds/prova/casos/inpulse.py`, com as decisões 8 a 11. A citação, as pilhas, a moldura, a frase no papel e o Link `externo` passaram para `ds/prova/pecas.py`, e a vitrine saiu idêntica.
- Saíram três rótulos que eram texto de apoio. "Protótipo navegável" (o `iframe` tem o título "Protótipo do aplicativo Inpulse"), "Três níveis de desejabilidade" (os níveis viraram a legenda das pilhas) e "O que a gente cortou" (a nota virou o parágrafo final, decisão 10). As fichas da Imagem, do Gráfico e do Antes e depois apontam para as Seções novas.
- Conferido em 1440, 768 e 390 sem rolagem lateral. O título tem quatro linhas em 1440 e em 390 e duas em 768, e o "6 em 10" do Salto cabe numa linha em 390. Os `id` não se repetem e todo `aria-labelledby` aponta para um elemento que existe. Sem JS e com movimento reduzido conferido só no código.
- Revisão sua do Inpulse, em 25 de outubro de 2026. Duas formas novas da Imagem, montadas na vitrine e aplicadas na página, à espera da sua aprovação para irem à ficha.
  - Ao lado (`div.figure-ao-lado`). Com 760px de Seção o texto corre à esquerda e a moldura `retrato` fica à direita, com o Link embaixo. Abaixo disso, o texto vem antes e a tela depois. Usada na Descoberta.
  - Recorte (`data-recorte`, com `--zoom`). A moldura fica em 16:9 e a imagem cresce por dentro, centrada. A imagem das telas do app tem 3234 por 3260px, com as telas numa faixa diagonal e fundo vazio nos cantos. Medido no arquivo, o recorte só fica sem fundo com `--zoom: 2`, a imagem com o dobro da largura do quadro. Com 1,9 ainda escapa 1px nos degraus da faixa. Usada no Resultado. O `width` e o `height` da imagem passaram aos valores reais (antes 1600 por 900), o que mudou também o palco da Imagem na vitrine.
- Aprovadas por você em 25 de outubro de 2026, o recorte, o ao lado e a página do Inpulse. A ficha da Imagem ganhou as duas formas (Use quando, Variantes, Limites, Acessibilidade e Código), e o GUIA e o COMPONENTES citam as duas.
- Passo 3, Processo com IA, em 25 de outubro de 2026. A cena `processo-salto.svg` é um calendário de parede com oito semanas, os dois meses do antes. Uma semana fica no lime e as outras sete só com o contorno tracejado, e o robô é o Claude que fez o rascunho. A página é gerada por `ds/prova/casos/processo.py`, com oito Seções e as decisões 12 a 16. O par, os estágios, o funil, a trilha, os ritos, as Abas numeradas, o confronto e o atrito passaram para `ds/prova/pecas.py`, e a vitrine saiu idêntica.
- Ajustes que a página pediu. O título do Design System abre o fim da Seção 06 em `t-lead`, porque a Seção tem um `h2` só. A declaração do fechamento passava de sete linhas na tinta em 1440, e a ficha do Destaque aceita quatro. A primeira frase ficou no Destaque e a segunda virou o corpo, com as mesmas palavras. "O que destravou" virou o começo do último parágrafo ("O que destravou foi mudar o critério antes da rotina"). Saíram os rótulos "destino", "Usabilidade" e "A trilha do componente", e "User stories (US)" ficou "User stories", como na vitrine.
- Decidido por você em 25 de outubro de 2026. A Seção 02 se chama "Dois gargalos ao mesmo tempo" (decisão 13). O título do caso tinha cinco linhas em 390 e em 1440, porque "COM CLAUDE NO CENTRO" passava 1px da coluna em 390 e 6px em 1440. Ele perdeu o "Reconstruindo o" e virou "Processo de produto e design com Claude no centro". Ficou com três linhas em 390 e em 1440, e duas em 768.
- Conferido em 1440, 768 e 390 sem rolagem lateral. As oito marcas do trilho somam 242px em 390. Os `id` não se repetem e todo `aria-labelledby` aponta para um elemento que existe.
- Revisão sua do Processo, em 25 de outubro de 2026. Nas Abas, o ícone, o número e o nome agora se alinham pelo centro, como no Sumário (antes pela linha de base, e o ícone descia). Vale para o Omnichat também, e a ficha das Abas diz isso.
- As barras do Gráfico não contavam a história. O antes em trama enchia o trilho e parecia só marcar o espaço, e o valor ficava na beira direita, longe da ponta. Estudo com três direções em `ds/vitrine/estudo/barras.html`, gerado por `ds/vitrine/estudo_barras.py`, cada uma com o tempo do Processo e os acessos do Mapa. Um trilho só (antes e depois no mesmo trilho, o valor sobre a ponta, como a escala), barras soltas (cada barra do tamanho do valor, e o tracejado do que saiu) e unidades (um quadrado por semana ou por dez minutos, com a trama na faixa). Você escolheu a direção 1, um trilho só, em 25 de outubro de 2026.
- As barras viraram um trilho só no componente. O antes é a área de muted com o fio de tinta na ponta, o depois é o acento por cima, e cada valor termina sobre a ponta da sua barra, como na escala. Numa queda o grupo leva `data-sentido="queda"`, que o `pecas.barras` põe sozinho. A chave embaixo usa os rótulos do primeiro grupo. No Mapa os rótulos ficaram "Sem o mapa" e "Com o mapa", para caberem sobre a ponta. A regra da escala usava a mesma classe `.chart__marco` sem escopo e passava por cima das barras. As duas agora ficam presas à própria figura, e a escala continua certa na subida e na queda. A ficha do Gráfico foi reescrita na parte das barras.
- Conferido em 1440, 768 e 390 sem rolagem lateral. Em 390 cada valor cabe numa linha, e nenhum se cobre.
- Revisão sua do Mapa. Num salto o acento cobria o antes, e o 20 virava só o fio, sem o muted que a chave mostra. Agora a barra menor fica por cima, nas duas direções, e o antes tem no mínimo 4px. A tampa da entrada passou para cima das duas, para nada aparecer antes da hora.
- O fio do antes passou a só subir do trilho, rumo ao valor, como você pediu.
- Revisão sua das barras, em 25 de outubro de 2026. O fio do antes saía do trilho e, no Processo, ficava sobrando na ponta de uma barra cheia. Ele saiu. O antes agora termina num fio de tinta de 2px só dentro do trilho, como o depois, e o fio some debaixo do contorno quando a barra chega a 100. O único fio que cruza o eixo é o zero da escala, a do NPS.
- Nas barras, cada marco se alinha ao lado da barra a que ele se liga, como você explicou. O da barra menor, que nasce na esquerda do trilho, vai pela esquerda, e o da maior vai pela direita, na ponta dela. Antes os dois iam pela direita, e o 20 do Mapa ficava solto debaixo do fim de “Sem o mapa”.
- Passo 4, Home e Manifesto, em 25 de outubro de 2026. A Home é gerada por `ds/prova/home.py`, com o hero e a Lista de casos de `ds/prova/comum.py`, no lime, e a descrição para a busca é a linha de apoio do hero. O título do Processo na Lista de casos acompanhou o título novo. A cortina da Home leva `data-sem-chegada` e não monta a tela na chegada nem na volta, só desce ao sair (módulo 0 do `componentes.js`). A frase do hero ganhou `--text-hero` e `--text-hero-estreito` em `tokens.css`, com os mesmos tamanhos de antes. A página do Manifesto saiu (`manifesto/index.html` apagado, o git guarda). O `manifesto.css` e o `manifesto.js` ficam para a limpeza do passo 5.
- Conferido em 1440, 768 e 390 sem rolagem lateral. A frase tem 115px, 62px e 82px. Um `h1` só, os `id` não se repetem e todo `aria-labelledby` aponta para um elemento que existe. A cortina nasce escondida, desce ao clicar num caso e volta escondida pelo voltar do navegador.
- Passo 5, limpeza, em 25 de outubro de 2026, depois da sua aprovação das barras e da Home. Conferido antes que nenhuma página, gerador ou estilo do site aponta para o que saiu. Foram para `arquivo/site-antigo/assets/` o `base`, o `home`, o `caso` e o `manifesto` (CSS e JS), a trama `bg-weave` e `bg-weave-dark`, as fotos do hero antigo e a cortina do J, que morava no `base.css` e no `base.js`. O `CREDITOS.md`, que era só das fotos, foi junto. O `assets/analytics.js` fica, porque as páginas novas usam. Os scripts de `ds/auditoria/` passaram a ler o CSS do arquivo e dizem que são registro da Fase 1. O `arquivo/LEIAME.md` ganhou a seção do site antigo.
- Documentos. As RECEITAS dão a Home como publicada, com a cortina escondida na chegada e o tamanho próprio da frase, o Contexto com o parágrafo de apoio e o meio do Caso de duas a seis Seções. A regra 12 do RITMO passou a "de quatro a oito", e as fichas do Sumário e da Seção acompanharam. As fichas do Cabeçalho, do Cartão, do Gráfico, do Hero e do Rodapé deixaram de dizer que a página publicada ainda é a antiga. O `ds/PROXIMA-SESSAO.md` foi reescrito para depois da Fase 6.
- O Sumário escalonava a chegada só até o sexto item, e no Processo o sétimo e o oitavo chegavam junto com o primeiro. Agora escalona até o oitavo.
- Revisão sua do hero no celular, em 25 de outubro de 2026, depois de publicada a Home. No iPhone, no Safari e no Chrome, a chegada andava aos trancos e a primeira cena não aparecia. Medido no Chrome com pintura por CPU e fotografado no WebKit do Mac com a chegada parada instante a instante. Três causas. O filtro de SVG do tremor refazia a frase inteira a cada quadro e saiu. O Safari ignora `-webkit-text-stroke` dentro de `@keyframes`, então o rascunho em contorno não existia, e o contorno passou a ler a variável registrada `--contorno`. A escrita do celular recortava com `clip-path` e a rolagem passava por uma variável herdada, os dois na thread principal, e viraram `translate`. Na Home a chegada espera a Anton e o primeiro quadro (`HERO_ESPERA`). Você testou no celular por páginas de teste servidas pela rede e aprovou.
- A frase do hero passou a caber na altura visível da tela ao abrir (`--hero-altura` em `tokens.css`), com só 2rem da linha de apoio embaixo. Conferido em 1440, 768 e 390 com a tela alta, idêntico pixel a pixel ao teste aprovado, inclusive rolado, sem JS e com movimento reduzido. Nas telas baixas a frase diminui e cabe, de 375 por 560 a 430 por 740.
