# Fundamentos do site

Fase 2. O núcleo do Jeff DS traduzido para a tela. Os valores moram em `assets/ds/tokens.css`, os componentes em `assets/ds/componentes.css` e `assets/ds/componentes.js`, e a prova é `ds/prova/omnichat.html`. A lista de componentes está em `ds/COMPONENTES.md`.

Ajuste combinado para esta fase. Uma página de exemplo só, a do Omnichat, porque ela sozinha usa 13 dos 15 componentes. O resto do site não muda até a migração.

## Cor

Os nomes são os do shadcn (D6), e cada um aponta para um token da marca. Componente nenhum pede `--lime` ou `--ink` direto, pede o papel da cor.

| Nome | Papel | Valor |
| --- | --- | --- |
| `background` / `foreground` | fundo e texto | paper e ink |
| `primary` / `primary-foreground` | botão principal | lime, com texto em tinta |
| `secondary` | segundo acento | azul |
| `muted` / `accent` | apoio, ficha, efeito | mist |
| `border` / `input` / `ring` | contorno e foco | ink |
| `chart-1` a `chart-3` | gráficos | lime, azul, verde |
| `acento` | acento dominante da página (D5) | o caso declara com `data-acento` |

**Gráfico.** O Gráfico pinta só com o `acento` da página, pela regra de um acento por página. O que separa um valor do outro é a forma do tom, `cheio` (o acento), `trama` (fios de tinta na diagonal) e `vazio` (o papel), e não a cor. Os `chart-1` a `chart-3` ficam reservados nos gráficos.

**Hero da Home.** É o único lugar além da Lista de casos em que os três acentos aparecem juntos, sempre como fundo atrás das palavras (regra 7 do `ds/RITMO.md`). Ele pede o `primary` (lime), o `secondary` (azul) e o `chart-3` (verde), pelos papéis, nunca pelo valor da marca.

**Superfície tinta.** A classe `superficie-tinta` troca os valores por dentro. `foreground`, `border` e `ring` viram papel, e o mesmo componente funciona no escuro sem regra própria. No Omnichat ela aparece duas vezes, no fechamento e no rodapé (D4).

Os acentos sobre o papel ficam entre 1,05 e 1,51 para 1 (ver `ds/CONTRASTE.md`). Por isso são sempre fundo, e quem escreve, contorna e marca foco é a tinta.

## Tipografia

Três famílias com papel fixo, como nos posts. A escala é fluida, uma reta entre 390 e 1440px que para de crescer fora dessa faixa.

| Degrau | Família | 390px | 1440px | Uso |
| --- | --- | --- | --- | --- |
| `numero` | Anton | 56 | 120 | o número do Dado |
| `display` | Anton, caixa alta | 40 | 72 | título do caso, frase do Destaque |
| `titulo` | Fraunces 300 | 30 | 52 | título de seção, chamada do rodapé, valor dos Dados em grupo |
| `sub` | Fraunces 300 | 22 | 32 | frase de apoio do topo, itens do menu |
| `lead` | Inter 400 | 18 | 22 | abertura, títulos de passo e de aba |
| `corpo` | Inter 400 | 16 | 18 | texto corrido |
| `apoio` | Inter 400 | 15 | 15 | ficha, legenda, falas da conversa |
| `rotulo` | Inter 700, caixa alta | 12 | 12 | rótulos, etiquetas, números de seção |

**De onde saíram.** Os posts são desenhados num canvas de 1080 que o celular mostra a uns 36%. O título de capa de 118px vira cerca de 42px na tela do celular, e é daí que vem o `display` de 40. O mesmo vale para os outros degraus. No desktop a tela é maior e a escala sobe.

**A frase do hero.** É a única fora da escala, com degraus próprios em `tokens.css`, `text-hero` (115px em 1440 e 63px em 768) e `text-hero-estreito` (82px em 390). O tamanho sai da largura do hero (`cqi`), para cada linha caber sem quebrar, e nunca passa da altura que a tela mostra ao abrir (`svh`), para a frase caber inteira com um pedaço da linha de apoio embaixo (ver `ds/fichas/hero.md`). A entrelinha é a do `display`.

**Duas diferenças dos posts.** O rótulo dos posts tem no mínimo 23px de canvas, que dão uns 8px na tela. No site o mínimo é 12px. E a entrelinha do Anton fica em 1,22, a mesma dos posts. Testei 1,1 e 1,16, e nas duas a cedilha do Ç bate no til da linha de baixo ("VERIFICAÇÃO" sobre "INTENÇÃO" no título do Omnichat).

## Espaço e grade

- A régua de espaço do site atual fica. Base 8, ajuste fino de 4, degraus de 4 a 96.
- Entre seções, `space-secao`, de 64 a 128px.
- Doze colunas, largura máxima de 1280px, margem lateral de 16px no celular a 48px no desktop.
- Quebras em 720 (tablet) e 1100 (desktop). No caso, a partir de 1100 o Sumário ocupa uma coluna de 260px e o conteúdo usa um mosaico de seis colunas.
- **Arranjo pela largura da Seção.** Com o Sumário ao lado, a Seção tem uns 750px em 1100 e em 1280, quase a largura do tablet. Por isso a Seção é um container (`container-type: inline-size`), e uma peça que põe itens lado a lado decide pela largura dela, com `@container`, e não pela da tela. O Passos é o primeiro a usar. Três itens lado a lado pedem 900px de Seção, e dois pedem 600px.
- Texto corrido com no máximo 66 caracteres por linha.
- A barra do Cabeçalho tem `altura-cabecalho` (66px, com o traço). O menu, o fundo escurecido e o trilho do Sumário começam logo abaixo dela.

## Estados

**A regra que vale para o site inteiro.** Hover só existe onde há mouse. Celular e tablet com toque nunca têm hover, então nada no site pode depender dele para ser descoberto ou entendido. A separação é por capacidade de entrada, nunca por largura de tela, porque um tablet largo continua sendo toque.

| Estado | Onde existe | Como se escreve | O que acontece |
| --- | --- | --- | --- |
| hover | só com mouse | dentro de `@media (hover: hover) and (pointer: fine)` | Botão inverte para tinta e a seta anda. Link e item de menu ganham o acento como marca texto, que corre da esquerda para a direita só por trás das palavras. Item do sumário ganha a mesma marca em mist e o ícone inclina. Aba ganha mist. |
| pressionado | em todo lugar | `:active` | Botão desce 2px. Link, item de menu e item do sumário ganham a marca texto no acento. No toque é o único retorno de que o dedo acertou. |
| foco | em todo lugar | `:focus-visible` | Anel de 2px na cor `ring`, afastado 3px. Tinta no papel, papel na tinta. Nunca um acento. |
| selecionado | abas, menu | `aria-selected`, `aria-current`, `aria-expanded` | Acento no fundo e também contorno de 2px e peso 700, para não depender só da cor. |
| desabilitado | botão | `:disabled`, `aria-disabled` | Contorno tracejado e opacidade de 60%. A forma muda, não só o tom. |

**Toque.** Onde o ponteiro é o dedo (`pointer: coarse`), todo alvo tem pelo menos 44px de altura. Na prova, em 390 e 768px, nenhum link ou botão ficou abaixo disso. A única exceção é o link no meio do texto, que tem a altura da linha da frase, com mouse ou com toque. A WCAG aceita essa exceção para links dentro de texto (critério 2.5.8), e esticar a linha quebraria a medida de leitura.

**O link é sempre sublinhado.** Sem hover não há outro jeito de saber que um trecho de texto é clicável.

## Movimento

| Token | Valor | Uso |
| --- | --- | --- |
| `dur-rapida` | 120ms | pressionado, troca de cor |
| `dur-media` | 240ms | abrir e fechar, trocar de aba |
| `dur-lenta` | 640ms | conteúdo entrando na tela |
| `ease-saida` | `cubic-bezier(.22, .61, .36, 1)` | tudo que entra ou responde |
| `ease-troca` | `cubic-bezier(.65, 0, .35, 1)` | o que sai e outro entra no lugar |

**A regra.** Toda interação que muda o estado de alguma coisa tem movimento. Nada troca seco.

Nenhum tempo fica fora dos três tokens. O que entra de longe (o painel do menu, a lista do trilho) usa `dur-lenta`, e os itens que chegam um depois do outro usam `dur-media`, com o intervalo tirado do `dur-rapida` (um terço dele por item). Até o script espera pelos tokens, lidos de `tokens.css`.

- Marca texto do hover e do toque. O acento corre por trás das palavras em 240ms, na largura do texto e não da caixa.
- Menu. O painel desce do cabeçalho, os itens chegam um depois do outro e a página por trás escurece. Fechando, sobe mais rápido do que desceu.
- Botão do menu. A palavra Menu sobe e sai, Fechar sobe e entra, e as duas linhas do ícone giram até virar um xis. O botão não muda de largura.
- Rolagem. Pular para uma seção ou voltar ao topo rola até lá. O pulo para abaixo das barras fixas.
- Abas. O painel que chega sobe 8px e aparece.
- Sumário. A seção da vez ganha a marca no acento e o ícone gira. No celular, as marcas do trilho crescem e mudam de cor, o nome da seção desliza para o lado e a lista entra de lado.
- Hero da Home. Na chegada, a frase vai do rascunho à página pronta uma vez só, em uns 3,2s, com os tempos em múltiplos dos tokens. Na rolagem só se desloca um pouco, a segunda linha e os adesivos mais que a primeira.
- Revelar na entrada sobe 16px e aparece. O estado escondido só existe quando o script confirma que há JS e que o movimento não está reduzido.

Com movimento reduzido, toda transição e animação vai a zero e a rolagem pula direto.

## Componentes com comportamento

- **Tabs** só viram abas a partir de 720px. Abaixo disso, e sem JS, cada painel aparece aberto com o seu título, um debaixo do outro. O teclado segue o padrão de abas (setas, Home, End).
- **Sheet**, o menu, abre por cima da página e fecha com Esc. Sem JS fica aberto no fluxo, logo abaixo da barra.

## Carregamento

A página chega montando uma tela por cima de um esboço, na ordem esboço, grade, componentes, textos e cores, e a barra avança uma vez por camada. É o mesmo gesto do hero da Home, do esboço à página pronta, para o site ter um gesto só. A animação manda no tempo, não a rede. São no mínimo 1,6s, e se a rede demorar mais a barra espera perto do fim. Ao clicar num link interno a cortina desce antes da troca. Sem JS ou com movimento reduzido, não existe.

**Na Home.** O hero já é a chegada, do rascunho à página pronta, e a cortina não monta a tela por cima dele. Ela leva `data-sem-chegada`, nasce escondida, não roda na chegada nem na volta e só desce ao sair por um link interno.

**A volta.** Chegando pelo voltar do navegador, a animação roda de trás para a frente. A tela começa pronta e perde as cores, os textos, os componentes e a grade, nessa ordem, até o traço do esboço se recolher, com a barra recuando junto. São no mínimo 1,95s. Quem avisa é uma linha no script da cabeça de cada página, que lê o tipo de navegação antes da primeira pintura. Toda página migrada precisa dela.

## Sumário abaixo de 1100px

A partir de 1100px o sumário senta fixo na coluna da esquerda. Abaixo disso a página tem uma coluna só, e o sumário vira um trilho na borda direita. São cinco marcas finas dentro da margem, que não cobrem o texto. As seções lidas ficam em tinta e a da vez cresce no acento. Enquanto a página rola, o nome da seção aparece ao lado das marcas e some quando a rolagem para. Um toque abre a lista de lado, e escolher uma seção rola até ela e fecha a lista. Perto do rodapé o trilho sai de cena. Sem JS, a lista fica aberta no topo da página.

Foram testadas três formas, e o trilho ganhou. A faixa grudada no cabeçalho roubava altura da leitura, e o botão flutuante cobria o fim de cada tela.

## O que foi conferido na prova

- Em 390, 768 e 1440px, sem rolagem lateral e sem erro de script.
- Hover ligado só em 1440 com mouse. Em 768 e 390 com toque, desligado.
- Abas em 768 e 1440, lista aberta em 390.
- Menu abrindo e fechando no celular.

## O que ainda falta

- Publicar estes tokens no artifact do Jeff DS, no grupo Site. Fica para depois da sua aprovação, porque mexe no artifact que também serve os posts.
- A Imagem e o Gráfico, que o Omnichat não usa, entraram nas Ondas 4 e 5 e estão provados na vitrine.
