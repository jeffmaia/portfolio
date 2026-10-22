# Inventário fechado

Resultado da Fase 1. As páginas foram abertas em 390, 768 e 1440px, e cada peça foi procurada no HTML real pelo seletor de `ds/auditoria/pecas.json`. A matriz abaixo é medida, não copiada do plano. Para refazer tudo, rode `ds/auditoria/auditar.mjs` e depois `montar.py`.

São **54 peças** nas cinco páginas do site, contra as 53 do plano. 1 peça nova apareceu na varredura (Contêiner de página). As classes que o plano agrupava como peças já cobrem 100% do HTML: nenhum elemento das cinco páginas ficou sem peça.

## Matriz peça por página

| Peça | H | PR | OM | IN | MA | Seletor | Par no Jeff DS | Porquês |
| --- | :-: | :-: | :-: | :-: | :-: | --- | --- | :-: |
| **Casca, toda página divide** | | | | | | | | |
| Pular para o conteúdo | 1 | 1 | 1 | 1 | 1 | `.pular` | sem par | 0 |
| Barra com assinatura | 1 | 1 | 1 | 1 | 1 | `.nav` | Moldura, cabeçalho | 9 |
| Botão de menu | 1 | 1 | 1 | 1 | 1 | `.menu-btn` | sem par | 2 |
| Menu em painel | 2 | 2 | 2 | 2 | 2 | `.menu, .reticula` | sem par | 17 |
| Superfícies papel e tinta |  | 4 | 4 | 4 | 4 | `.tinta, .folha` | BlocoTinta | 9 |
| Onda | 5 | 6 | 6 | 6 | 6 | `.onda--clara, .onda--escura, .onda-defs` | sem par | 8 |
| Rodapé de contato | 1 | 1 | 1 | 1 | 1 | `.footer` | Fechamento | 8 |
| Voltar ao topo | 1 | 1 | 1 | 1 | 1 | `.subir` | sem par | 1 |
| Passagem entre páginas | 1 | 1 | 1 | 1 | 1 | `.transicao` | sem par | 11 |
| **Ação e navegação** | | | | | | | | |
| Botão principal | 5 | 1 | 1 | 1 | 1 | `.btn-green` | Tag preenchida | 0 |
| Link | 2 | 2 | 2 | 3 | 3 | `.link, .link-solto` | sem par | 1 |
| Voltar para os casos |  | 1 | 1 | 1 | 1 | `.voltar` | sem par | 0 |
| Próximo caso |  | 1 | 1 | 2 | 2 | `.proximo-link` | sem par | 0 |
| Seta de descer | 1 |  |  |  |  | `.descer` | sem par | 2 |
| Trilho de pontos | 1 |  |  |  |  | `.cena__trilho` | RitmoCarrossel | 0 |
| **Texto e rótulo** | | | | | | | | |
| Micro rótulo | 17 | 52 | 54 | 25 | 36 | `.micro` | rótulo da Moldura | 1 |
| Etiquetas de assunto |  | 1 | 1 | 1 | 2 | `.etiquetas` | TagCard | 1 |
| Cabeçalho de seção |  | 9 | 5 | 4 | 5 | `.secao__topo` | Moldura, cabeçalho | 0 |
| Abertura |  | 1 | 1 | 1 | 1 | `.abertura` | sem par | 2 |
| Corpo de texto |  | 5 | 3 | 5 | 5 | `.corpo-texto` | sem par | 0 |
| Grito |  | 1 |  | 1 |  | `.grito` | CenaPagina, BlocoTinta | 3 |
| Linha de nota |  | 1 |  | 2 | 1 | `.linha-nota` | sem par | 1 |
| Atrito |  | 3 |  |  |  | `.atrito` | BlocoTinta | 1 |
| Citação |  |  |  | 1 |  | `.citacoes` | Citacao, AntesDepois | 2 |
| Declaração final |  | 1 | 1 | 1 | 1 | `.fecho--unido` | Fechamento | 4 |
| **Abertura de página** | | | | | | | | |
| Hero editorial | 1 |  |  |  |  | `.hero` | Capa | 9 |
| Topo do caso |  | 1 | 1 | 1 | 1 | `.caso-topo` | CapaSangrada | 9 |
| Salto |  | 1 | 1 | 1 | 1 | `.salto` | Dado, NumeroSangrado | 2 |
| Convite ao manifesto | 1 |  |  |  |  | `.fecho:has(.fecho__link)` | sem par | 2 |
| **Organização** | | | | | | | | |
| Contêiner de página | 6 | 7 | 7 | 7 | 7 | `.wrap` | safe-side, canvas | 0 |
| Seção |  | 9 | 5 | 4 | 5 | `.secao` | sem par | 39 |
| Bloco com rótulo |  | 4 | 1 | 6 | 4 | `.bloco` | sem par | 2 |
| Ficha do projeto | 1 | 2 | 2 | 2 | 2 | `.ficha, .ficha-lateral, .faixa-ficha` | Cards | 2 |
| Cena dos casos | 1 |  |  |  |  | `.cena` | Cards | 10 |
| Orbe do número | 1 |  |  |  |  | `.cena__orbe` | Dado | 0 |
| Ações do fim |  | 1 | 1 | 1 | 1 | `.acoes` | Fechamento | 0 |
| **Sequência e processo** | | | | | | | | |
| Linhas indexadas |  | 1 | 1 |  | 1 | `.linhas` | Passos, Lista | 6 |
| Estágios |  | 1 |  |  |  | `.estagios` | Passos | 5 |
| Abas |  | 1 | 1 |  |  | `.abas` | sem par | 14 |
| Ritos |  | 1 |  | 1 |  | `.ritos` | Lista | 1 |
| Funil |  | 1 |  |  |  | `.funil` | Passos | 7 |
| Trilha |  | 1 |  |  |  | `.rail` | Passos | 3 |
| **Comparação** | | | | | | | | |
| Confronto |  | 1 |  |  |  | `.confronto` | AntesDepois | 4 |
| Conversa |  |  | 1 |  |  | `.conversas` | AntesDepois | 5 |
| **Dados** | | | | | | | | |
| Números do resultado |  | 1 | 1 | 1 | 1 | `.numeros` | Dado | 1 |
| Barras |  | 1 |  |  | 1 | `.barras` | Barras | 2 |
| Pilhas |  |  |  | 1 |  | `.pilhas` | Barras, Waffle | 4 |
| Escala de NPS |  |  |  |  | 1 | `.nps` | sem par | 1 |
| **Mídia** | | | | | | | | |
| Moldura |  |  |  | 1 |  | `.moldura` | sem par | 2 |
| Galeria |  |  |  |  | 1 | `.galeria` | sem par | 2 |
| Sangria |  |  |  | 1 |  | `.sangria` | FaixaDividida | 1 |
| **Comportamento** | | | | | | | | |
| Revelar na entrada | 12 | 38 | 22 | 27 | 28 | `[data-revelar]` | sem par | 0 |
| Régua de leitura |  | 1 | 1 | 1 | 1 | `.regua` | sem par | 5 |
| Carrossel de tela estreita |  | 2 | 1 |  |  | `.abas__lista, .rail` | sem par | 0 |

Os números são quantas vezes a peça aparece na página. H é Home, PR Processo com IA, OM Omnichat, IN Inpulse e MA Mapa de experiência.

## Colisões de nome

Classes que o site usa para duas coisas diferentes. O seletor das peças no `pecas.json` já as separa.

- `.fecho`: Convite ao manifesto (Home) e Declaração final (casos). Duas peças sem nada em comum dividem o mesmo nome de classe, cada uma com a sua regra em home.css e caso.css. A Fase 4 deve renomear uma delas.

## Peças de uma página só

Peça que aparece em uma única página pede uma pergunta antes de virar componente: ela é do sistema ou é da história daquele caso? As que ficam sozinhas:

- Seta de descer, só em H
- Trilho de pontos, só em H
- Atrito, só em PR
- Citação, só em IN
- Hero editorial, só em H
- Convite ao manifesto, só em H
- Cena dos casos, só em H
- Orbe do número, só em H
- Estágios, só em PR
- Funil, só em PR
- Trilha, só em PR
- Confronto, só em PR
- Conversa, só em OM
- Pilhas, só em IN
- Escala de NPS, só em MA
- Moldura, só em IN
- Galeria, só em MA
- Sangria, só em IN

## O que some em tela estreita

- **Trilho de pontos** não existe em 390, 768px. É a cena dos casos da Home: abaixo de certa largura ou altura ela não fica viva e os quatro casos empilham, sem trilho nem orbe. A ficha precisa dizer isso no campo Comportamento.
- **Orbe do número** não existe em 390, 768px. É a cena dos casos da Home: abaixo de certa largura ou altura ela não fica viva e os quatro casos empilham, sem trilho nem orbe. A ficha precisa dizer isso no campo Comportamento.

## Peças que são comportamento, não componente

Revelar na entrada, Régua de leitura e Carrossel de tela estreita não têm uma forma própria para fotografar. O revelar age em 38 elementos da Home e dos casos, a régua só existe nos quatro casos e o carrossel deita Abas e Trilha no celular. Entram no DS como regras de movimento e de layout (Fase 2), não como fichas.

## Fusões

Conta honesta: **54 peças medidas, 41 componentes com as cinco fusões do plano, 29 com as que a varredura sugere a mais.** O plano falava em cerca de 30; esse número só se alcança com a segunda lista, que são propostas minhas e dependem do seu sim.

### Do plano

- **Sequência** (5 para 1): Linhas indexadas, Estágios, Ritos, Funil, Trilha. A pergunta que escolhe a variante: a ordem importa, afunila, tem entrada e saída, é um caminho curto.
- **Antes e depois** (4 para 1): Salto, Confronto, Conversa, Citação. A forma do que muda: um número, várias dimensões, uma conversa ou a fala de quem usa.
- **Gráfico** (3 para 1): Barras, Pilhas, Escala de NPS. Três formas e uma regra de entrada só, com a mesma rede de segurança para movimento reduzido.
- **Botão e link** (4 para 2): Botão principal, Link, Voltar para os casos, Próximo caso. Botão para a ação principal, Link com variantes para voltar, seguir, sair do site e fechar bloco.
- **Imagem** (3 para 1): Moldura, Galeria, Sangria. Variantes de enquadramento, com crédito e texto alternativo num lugar só.

### Propostas desta fase

- **Comportamento fora da lista** (3 para 0): Revelar na entrada, Régua de leitura, Carrossel de tela estreita. São regras de movimento e de layout. Saem da lista de componentes e vão para a Fase 2.
- **Navegação** (3 para 1): Barra com assinatura, Botão de menu, Menu em painel. Os três são uma máquina só: o botão abre o painel, e a barra muda de cor com o que passa por trás. Hoje as três folhas de regra se referenciam.
- **Seção** (3 para 1): Seção, Cabeçalho de seção, Bloco com rótulo. Cabeçalho e bloco nunca aparecem fora da seção. Viram partes da ficha da Seção.
- **Cena dos casos** (3 para 1): Cena dos casos, Orbe do número, Trilho de pontos. Orbe e trilho só existem dentro da cena e somem junto com ela em tela estreita.
- **Superfície** (2 para 1): Superfícies papel e tinta, Onda. A onda é a borda da superfície: leva o fundo da seção junto para a curva não cortar a trama.
- **Seta de rolagem** (2 para 1): Seta de descer, Voltar ao topo. Mesmo morro, mesma distância, sentido contrário. O CSS já descreve uma como par da outra.
- **Texto corrido** (2 para 1): Abertura, Corpo de texto. Diferem só no corpo da letra. É uma variante.

### Lista final se tudo for aceito

São 29 componentes (Botão e link conta duas vezes: Botão e Link).

- Abas
- Antes e depois (Salto, Confronto, Conversa, Citação)
- Atrito
- Ações do fim
- Botão e link (Botão principal, Link, Voltar para os casos, Próximo caso)
- Cena dos casos (Cena dos casos, Orbe do número, Trilho de pontos)
- Contêiner de página
- Convite ao manifesto
- Declaração final
- Etiquetas de assunto
- Ficha do projeto
- Grito
- Gráfico (Barras, Pilhas, Escala de NPS)
- Hero editorial
- Imagem (Moldura, Galeria, Sangria)
- Linha de nota
- Micro rótulo
- Navegação (Barra com assinatura, Botão de menu, Menu em painel)
- Números do resultado
- Passagem entre páginas
- Pular para o conteúdo
- Rodapé de contato
- Sequência (Linhas indexadas, Estágios, Ritos, Funil, Trilha)
- Seta de rolagem (Seta de descer, Voltar ao topo)
- Seção (Seção, Cabeçalho de seção, Bloco com rótulo)
- Superfície (Superfícies papel e tinta, Onda)
- Texto corrido (Abertura, Corpo de texto)
- Topo do caso

## Manifesto, fora desta versão

A decisão D7 tira o manifesto desta versão do site. A página `manifesto/index.html` foi fotografada para registro, mas nenhuma das suas peças entra no inventário. Elas ficam marcadas aqui para que ninguém as migre sem querer:

- Palco com quadros que trocam na rolagem
- Rótulo da etapa
- Contador
- Trilho de progresso
- Dica de rolagem com mouse animado
- Assinatura com duas ações
- Versão em texto corrido para quem chega sem JS

O manifesto também é a única página que usa outra identidade (papel creme e laranja, cores escritas no JS), e o único lugar com `--om-accent`, `--om-paper` e companhia. Continua no ar até a Fase 6.

## Capturas

`ds/capturas/index.html` reúne, para cada peça, a fotografia em 390, 768 e 1440px, e as páginas inteiras. As imagens estão em `ds/capturas/<largura>/<peça>.jpg` e `ds/capturas/paginas/`.

