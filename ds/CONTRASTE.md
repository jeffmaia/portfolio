# Contraste

Auditoria da paleta do Jeff DS aplicada ao site, e do que o site de hoje já erra. Os números vêm de `ds/auditoria/auditar.mjs` (texto medido nos elementos reais, em 390 e 1440px) e do cálculo WCAG 2,1 sobre os tokens.

## Paleta do Jeff DS, par a par

Razão de contraste. Texto normal pede 4,5 e texto grande (24px, ou 18,66px em negrito) ou controle pede 3.

| | paper | ink | lime | azul | verde | mist |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| **paper** `#f9f9f7` |  | **19,9** | _1,1_ | _1,4_ | _1,5_ | _1,2_ |
| **ink** `#000000` | **19,9** |  | **18,9** | **14,0** | **13,2** | **16,4** |
| **lime** `#edfe5e` | _1,1_ | **18,9** |  | _1,4_ | _1,4_ | _1,2_ |
| **azul** `#bed4fb` | _1,4_ | **14,0** | _1,4_ |  | _1,1_ | _1,2_ |
| **verde** `#31e992` | _1,5_ | **13,2** | _1,4_ | _1,1_ |  | _1,2_ |
| **mist** `#dee5dd` | _1,2_ | **16,4** | _1,2_ | _1,2_ | _1,2_ |  |

Em negrito, passa em texto normal (4,5 ou mais). Sem destaque, passa só em texto grande e controle (3 ou mais). Em itálico, não passa em nada.

### O que isso decide

- Tinta sobre qualquer acento passa com folga (18,9, 14,0 e 13,2 para 1). Por isso o acento é sempre fundo e a tinta é sempre texto.
- Acento sobre o papel não serve para nada além de preenchimento: lime 1,05, azul 1,42 e verde 1,51 para 1, abaixo até do mínimo de 3 para controles. Confirma a regra 1 do plano: lime, azul e verde nunca viram texto, nunca são a única borda de um controle e nunca são o anel de foco.
- Um acento ao lado de outro, como lime sobre azul, não separa por luminosidade (1,35 e 1,43). Duas áreas de acento vizinhas precisam de traço de tinta entre elas, que o 2px já dá.

## O site de hoje, par a par

| | bone-white | press-black | slate-verdant | newsprint-gray | muted-sage | highlighter-green | echo-green |
| --- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **bone-white** `#fafffa` |  | **18,0** | **14,7** | **6,4** | _1,5_ | _1,5_ | _1,4_ |
| **press-black** `#121613` | **18,0** |  | _1,2_ | _2,8_ | **11,7** | **11,7** | **13,3** |
| **slate-verdant** `#232924` | **14,7** | _1,2_ |  | _2,3_ | **9,6** | **9,5** | **10,8** |
| **newsprint-gray** `#516254` | **6,4** | _2,8_ | _2,3_ |  | 4,2 | 4,2 | **4,7** |
| **muted-sage** `#c8d2c8` | _1,5_ | **11,7** | **9,6** | 4,2 |  | _1,0_ | _1,1_ |
| **highlighter-green** `#2bee4b` | _1,5_ | **11,7** | **9,5** | 4,2 | _1,0_ |  | _1,1_ |
| **echo-green** `#c4e4c9` | _1,4_ | **13,3** | **10,8** | **4,7** | _1,1_ | _1,1_ |  |

## Texto que reprova hoje

Medido nos elementos visíveis, com a cor de fundo vinda do primeiro ancestral opaco. A barra do topo fica de fora, porque troca de fundo conforme a seção que passa por trás, e o texto escondido (opacidade zero) também.

### Home, 1440px

| Texto | Fundo | Razão | Mínimo | Quantos | Exemplos |
| --- | --- | :-: | :-: | :-: | --- |
| `#516254` | `#121613` (fundo com trama) | 2,8 | 4,5 | 1 | `span.micro` 11px "Voltar ao topo" |

### Processo com IA, 1440px

| Texto | Fundo | Razão | Mínimo | Quantos | Exemplos |
| --- | --- | :-: | :-: | :-: | --- |
| `#516254` | `#121613` (fundo com trama) | 2,8 | 4,5 | 3 | `span.micro` 11px "04 · Rituais"; `span.micro` 11px "05 · Liderança"; `span.micro` 11px "Voltar ao topo" |
| `#2bee4b` | `#fafffa` (fundo com trama) | 1,54 | 4,5 | 2 | `span.micro` 11px "01"; `span.micro` 11px "02" |

### Omnichat, 1440px

| Texto | Fundo | Razão | Mínimo | Quantos | Exemplos |
| --- | --- | :-: | :-: | :-: | --- |
| `#2bee4b` | `#fafffa` (fundo com trama) | 1,54 | 4,5 | 6 | `span.micro` 11px "01"; `span.micro` 11px "02"; `span.conversa__fim` 11px "Lead convertido" |
| `#516254` | `#121613` (fundo com trama) | 2,8 | 4,5 | 2 | `span.micro` 11px "03 · Processo"; `span.micro` 11px "Voltar ao topo" |

### Inpulse, 1440px

| Texto | Fundo | Razão | Mínimo | Quantos | Exemplos |
| --- | --- | :-: | :-: | :-: | --- |
| `#516254` | `#121613` (fundo com trama) | 2,8 | 4,5 | 2 | `span.micro` 11px "02 · Descoberta"; `span.micro` 11px "Voltar ao topo" |
| `#2bee4b` | `#fafffa` (fundo com trama) | 1,54 | 4,5 | 1 | `span.micro` 11px "Depois" |

### Mapa de experiência, 1440px

| Texto | Fundo | Razão | Mínimo | Quantos | Exemplos |
| --- | --- | :-: | :-: | :-: | --- |
| `#516254` | `#121613` (fundo com trama) | 2,8 | 4,5 | 2 | `span.micro` 11px "03 · Processo"; `span.micro` 11px "Voltar ao topo" |

## Onde o verde marca texto está hoje

A regra 1 proíbe lime, azul e verde como texto, como única borda de controle e como anel de foco. Estes são os usos do `#2bee4b` e do `#c4e4c9` nas páginas, medidos nos estilos computados (1440px):

| Uso | Elemento | Páginas | Veredito |
| --- | --- | --- | --- |
| borda | `button.aba` | omnichat, processo | Reprova se for a única borda. Passa para tinta de 2px. |
| borda | `div.conversa.conversa--depois` | omnichat | Reprova se for a única borda. Passa para tinta de 2px. |
| borda | `div.fecho.fecho--unido` | inpulse, mapa, omnichat, processo | Reprova se for a única borda. Passa para tinta de 2px. |
| borda | `div.linha` | omnichat | Reprova se for a única borda. Passa para tinta de 2px. |
| borda | `div.linha.revelado` | processo | Reprova se for a única borda. Passa para tinta de 2px. |
| borda | `div.orbe__disco` | home | Reprova se for a única borda. Passa para tinta de 2px. |
| borda | `li.fase` | processo | Reprova se for a única borda. Passa para tinta de 2px. |
| texto | `a.menu__item` | inpulse, mapa, omnichat, processo | Reprova a regra 1. Passa para tinta. |
| texto | `b` | home, omnichat | Reprova a regra 1. Passa para tinta. |
| texto | `span.conversa__fim` | omnichat | Reprova a regra 1. Passa para tinta. |
| texto | `span.etiqueta--verde` | inpulse, mapa, omnichat, processo | Reprova a regra 1. Passa para tinta. |
| texto | `span.micro` | home, mapa, omnichat, processo | Reprova a regra 1. Passa para tinta. |
| texto | `span.micro.aba__num` | omnichat | Reprova a regra 1. Passa para tinta. |
| texto | `span.micro.citacao__quando` | inpulse | Reprova a regra 1. Passa para tinta. |
| texto | `span.micro.linha__num` | mapa, omnichat, processo | Reprova a regra 1. Passa para tinta. |
| preenchimento | `a.btn-green` | home, inpulse, mapa, omnichat, processo | Permitido, é o papel do acento. |
| preenchimento | `a.pular` | home, inpulse, mapa, omnichat, processo | Permitido, é o papel do acento. |
| preenchimento | `div.barra__preenche` | mapa, processo | Permitido, é o papel do acento. |
| preenchimento | `div.regua` | inpulse, mapa, omnichat, processo | Permitido, é o papel do acento. |
| preenchimento | `i` | home, inpulse, mapa, omnichat, processo | Permitido, é o papel do acento. |
| preenchimento | `i.cor--entusiasta` | inpulse | Permitido, é o papel do acento. |
| preenchimento | `img` | mapa | Permitido, é o papel do acento. |
| preenchimento | `p.turno__fala` | omnichat | Permitido, é o papel do acento. |
| preenchimento | `span.menu-btn__traco` | home, inpulse, mapa, omnichat, processo | Permitido, é o papel do acento. |
| preenchimento | `span.nps__faixa` | mapa | Permitido, é o papel do acento. |
| preenchimento | `span.pilha__parte.pilha__parte--entusiasta` | inpulse | Permitido, é o papel do acento. |

### No CSS

49 declarações usam o verde marca texto ou o verde claro. 7 são cor de texto, traço ou preenchimento de SVG, 9 são borda e 2 são anel de foco.

**Anel de foco**, o mais grave, porque é o que o teclado usa para achar onde está. O foco hoje é verde sobre papel, razão 1,54 para 1:

- `assets/base.css:116` `outline: 2px solid var(--highlighter-green);`
- `assets/caso.css:2010` `outline: 2px solid var(--highlighter-green);`

O manifesto usa `--om-accent` (laranja) no foco, o que também sai com ele.

## Resumo do que a Fase 2 herda

1. O foco muda de verde para tinta em todo o site, no `:where(a):focus-visible`, no `:where(button):focus-visible` e nos dois focos de `caso.css`.
2. Todo texto, link e borda de controle que hoje usa verde passa para tinta. O verde fica como fundo de botão, de etiqueta e de barra.
3. Os pares de cinza que reprovam saem do cinza verdoso (`newsprint-gray`, `muted-sage`) e vão para tinta pura, porque o Jeff DS não tem cinza de texto, só a linha de fonte a 75% de opacidade. A hierarquia de leitura passa a depender de tamanho e peso, e não de tom.
4. O texto de apoio sobre a tinta (rótulos, descrições) precisa de papel e não de cinza claro.

