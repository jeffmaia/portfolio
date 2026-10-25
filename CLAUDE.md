# Portfólio Jeff Maia

Site estático em HTML, CSS e JS puros, servido pelo GitHub Pages. Sem servidor e sem build.

O site é montado com o Jeff DS. Antes de criar ou mudar qualquer página, leia `ds/PLANO.md`. Ele guarda as decisões aprovadas e a fase atual.

A pasta `arquivo/` guarda material que não vale mais, como o `handoff` do sistema Industry e o `site-antigo`, com o CSS, o JS e as fotos de antes do Jeff DS. Não use como referência.

## Roteiro antes de mexer numa página

1. `ds/PLANO.md`, para saber a fase e o que já foi decidido.
2. `ds/RECEITAS.md`, para a ordem da página e o que é fixo.
3. `ds/GUIA.md`, para escolher a peça de cada seção pelo que ela precisa mostrar.
4. A ficha do componente escolhido, em `ds/fichas/`. O Não use quando aponta o vizinho certo.
5. `ds/RITMO.md`, e o checklist do fim dele antes de dar por pronto.

Se nenhum componente serve, não crie a peça direto na página. Escreva a ficha nova em `ds/fichas/`, seguindo `ds/fichas/_modelo.md`, e traga para aprovar antes do código.

## Onde mora cada coisa

| O quê | Onde |
| --- | --- |
| Plano, decisões e fase atual | `ds/PLANO.md` |
| Os 15 componentes e o que cada um absorveu | `ds/COMPONENTES.md` |
| Cor, tipografia, espaço, grade, estados, movimento | `ds/FUNDAMENTOS.md` |
| Guia de decisão, receitas e ritmo | `ds/GUIA.md`, `ds/RECEITAS.md`, `ds/RITMO.md` |
| Fichas de componente | `ds/fichas/` |
| Tokens, componentes e comportamento | `assets/ds/tokens.css`, `assets/ds/componentes.css`, `assets/ds/componentes.js` |
| Ícones adesivo e cenas | `assets/ds/icones/`, `assets/ds/ilustracoes/`, gerados por `ds/icones/gerar.py` e `ds/ilustracoes/gerar.py` |
| Home | `index.html`, gerado por `ds/prova/home.py` com o hero e a Lista de casos de `ds/prova/comum.py` |
| Modelo de Caso e páginas de caso | `ds/prova/variacoes/v4.html` e os `case-*.html` já migrados, gerados por `ds/prova/caso.py` com `ds/prova/comum.py` (a v4 pelo `ds/prova/variacoes.py`). O texto e o miolo de cada caso moram em `ds/prova/casos/`, e o HTML das peças que levam conteúdo em `ds/prova/pecas.py`, que a vitrine também usa |
| Vitrine das peças ao vivo, onda a onda | `ds/vitrine/index.html`, com a peça sozinha em `ds/vitrine/amostra/`, a peça aplicada numa página em `ds/vitrine/palco/` (mostrada dentro da ficha) e as fichas em HTML em `ds/vitrine/fichas/`, tudo gerado por `ds/vitrine/gerar.py`. O quadro usa `ds/vitrine/vitrine.js`. Estudos de direção de uma peça ficam em `ds/vitrine/estudo/`, gerados por `ds/vitrine/estudo.py` (o do Passos), `ds/vitrine/estudo_barras.py` (o das barras do Gráfico) e `ds/vitrine/estudo_hero.py` (o do hero, com as imagens tiradas por `ds/vitrine/fotografar.mjs`). As prévias do grupo Site no artifact do Jeff DS saem das amostras, por `ds/vitrine/artifact.py` |
| Contraste e porquês do site antigo | `ds/CONTRASTE.md`, `ds/PORQUES.md` |

O que vem de um gerador se muda no gerador, nunca no HTML gerado.

## Regras que valem para o site inteiro

Textos do site e da documentação em português do Brasil, sem hífen, travessão ou dois pontos na escrita corrida. Palavra curta de ligação nunca termina linha de título, e se amarra à seguinte com espaço rígido.

Hover só existe onde há mouse. Toda regra de hover fica dentro de `@media (hover: hover) and (pointer: fine)`, e nada no site pode depender dele para ser descoberto. No toque, o retorno vem de `:active` e do foco, e todo alvo tem pelo menos 44px. A única exceção é o link no meio do texto, que tem a altura da linha da frase, como a WCAG aceita (critério 2.5.8). Vale para o site inteiro.

Toda interação que muda o estado de algo tem movimento, com os tokens de duração e curva de `assets/ds/tokens.css`. Nada troca seco. O realce de hover e de toque fica só atrás das palavras, nunca na largura toda da caixa.

Lime, azul e verde nunca viram texto, borda única ou anel de foco. Texto, borda e foco são sempre tinta (ou papel, na superfície tinta). Componente pede o papel da cor (`primary`, `acento`, `border`), nunca o valor da marca direto.

Tudo funciona sem JS e com movimento reduzido.

Toda página migrada leva na cabeça o script de uma linha que detecta a volta pelo histórico, antes das folhas de estilo (ver `ds/RECEITAS.md`).

## Conferir

Sirva a raiz do repositório na porta 4173 e confira em 390, 768 e 1440px. Nesta máquina existe `.claude/serve.js`, fora do git. Em outra, `python3 -m http.server 4173` resolve.

Commit só quando o Jeff pedir.
