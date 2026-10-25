# Roteiro do hero

Os três momentos foram aprovados por você em 24 de outubro de 2026, e a chegada e a rolagem já estão no código, em `assets/ds/componentes.css` (bloco do hero, nas receitas) e em `ds/prova/comum.py` (função `hero`). O hero antigo, o quadro com a tela que se desmontava, saiu. A vitrine mostra o hero novo ao vivo, na amostra e no palco da Home.

**A ideia.** A frase é a própria cena. O motion acontece em cima dela, em três momentos, do rascunho à página pronta. Na rolagem quase nada se move, só um deslocamento leve da frase e dos adesivos.

**As prévias.** Os três momentos parados, em 1440 e 390, estão em `ds/vitrine/estudo/hero/index.html`, com cada cena ao vivo ao lado. Saem de `ds/vitrine/estudo_hero.py`, e as imagens de `node ds/vitrine/fotografar.mjs`. O CSS mora no gerador do estudo e só vai para `componentes.css` depois da sua escolha.

## A frase

É o maior texto da tela, e o tamanho sai da largura da coluna.

- **Do tablet para cima,** duas linhas, "O ofício continua o mesmo." numa e "O jeito de fazer, não." na outra. A primeira ocupa 10,8 vezes o tamanho da fonte em Anton.
- **No celular,** seis linhas, três por frase ("O ofício / continua / o mesmo." e "O jeito / de fazer, / não."), com um respiro a mais entre as duas frases. Em duas linhas ela ficava com 32px e perdia o peso que tem no desktop. A linha mais larga, "O MESMO.", ocupa 3,8 vezes o tamanho da fonte.

| Largura | Linhas | Tamanho da frase |
| --- | --- | --- |
| 390 | seis | 82px |
| 768 | duas | 63px |
| 1440 | duas | 115px |

A faixa verde de "jeito de fazer," é feita de dois pedaços. No desktop eles emendam numa faixa só, e no celular cada um fecha na sua linha.

**A dobra.** No desktop o hero não ocupa a primeira tela inteira. Sobram uns 144px, onde aparecem o rótulo Quatro casos e o alto dos dois primeiros Cartões, para ficar claro que a página continua. No celular a frase enche a primeira tela e a linha de apoio começa na beirada de baixo.

A entrelinha é a do token `leading-display` (1,22). Com menos, o til do NÃO encosta na primeira linha, o mesmo motivo que levou o token a esse valor.

## Momento 1 · Rascunho

A página chega e a frase começa a ser desenhada, como desenho de tipo.

1. As colunas da grade aparecem em fios claros, de cima para baixo.
2. As guias de altura e de base correm da esquerda para a direita em cada linha, tracejadas.
3. O contorno das letras é traçado à mão, com o tremor do lápis, primeiro a primeira linha e depois a segunda.
4. A hachura preenche OFÍCIO, a palavra que já está decidida.
5. Entram as notas de quem desenha, em Fraunces, "Anton, duas linhas, sempre" e "o não fica". Por último, o NÃO é circulado.
6. No lugar da linha de apoio, três traços à mão.

## Momento 2 · Cores

O rascunho vira tipo de verdade, e as cores do Jeff DS desenham a tipografia.

1. O tremor some, o contorno se enche de tinta letra a letra, e as guias e a grade se apagam.
2. As cores entram por trás das palavras como adesivos que assentam, cada um com contorno de tinta. O lime marca OFÍCIO, o círculo azul abraça o fim de MESMO, a faixa verde sublinha JEITO DE FAZER, e o NÃO ganha uma caixa de tinta, com o texto passando a papel.
3. Os traços da linha de apoio viram o texto, em Fraunces.

O texto nunca muda para lime, azul ou verde. A cor fica sempre atrás.

## Momento 3 · Ilustrações e ícones

Os adesivos completam a frase e chegam como adesivo sendo colado, um pouco maiores e girados, assentando no lugar.

1. Os do ofício, na primeira linha, chegam primeiro e ficam calmos. Lápis, lupa e pessoa, o que continua igual.
2. Os do jeito de fazer, embaixo da segunda linha, chegam depois. Tela, conversa, celular e camadas, o que mudou.
3. Por último, uma folha de esboço solta ao lado do NÃO, que liga o hero ao Carregamento.

No celular os adesivos descem pela tela no vão que as linhas curtas deixam à direita. Lápis e pessoa ao lado de "O OFÍCIO", a lupa ao lado de "CONTINUA", tela e conversa ao lado de "O JEITO", o celular ao lado de "DE FAZER,", e as camadas e a folha de esboço ao lado do NÃO.

O robô ficou de fora de propósito. O PLANO já tinha descartado o robô e o cérebro com circuito como lugar comum de IA.

## Na rolagem

Um deslocamento só, ligado à rolagem, do topo até o hero sair da tela.

- A primeira linha quase não se move. É o ofício, que fica.
- A segunda linha sobe um pouco mais rápido que a página.
- Os adesivos se deslocam mais que a frase, cada um no seu ritmo, como camadas mais próximas de quem olha.
- Nada sai da tela antes do hero, e nada gira ou muda de cor.

O deslocamento máximo fica em torno de 40px no desktop e metade disso no celular.

## Tempo

A sequência roda uma vez, na chegada, e para no Momento 3.

Todos os tempos saem dos tokens (`dur-lenta` 640ms, `dur-media` 240ms e `dur-rapida` 120ms).

| Quando | O que acontece |
| --- | --- |
| 0s | A grade aparece em fios claros |
| 0,24s | A primeira linha começa a ser escrita, com as guias. A segunda vem uma `dur-media` depois. No celular cada pedaço vem uma `dur-rapida` depois do anterior |
| 0,9s | A hachura corre por OFÍCIO, e os três traços da linha de apoio se desenham |
| 1,12s | Entram as duas notas |
| 1,36s | O NÃO é circulado |
| 1,6s | O contorno se enche de tinta, o tremor some, e a grade, as guias, as notas, o círculo e os traços se apagam |
| 1,72s a 2,08s | As cores colam por trás das palavras, uma `dur-rapida` depois da outra (OFÍCIO, MESMO, JEITO DE FAZER e a caixa do NÃO) |
| 2,2s | O NÃO vira papel, e a linha de apoio aparece |
| 2,5s a 3,16s | Os adesivos chegam, meia `dur-rapida` um depois do outro |

São uns 3,2s no total. Por ficar abaixo de 5s, a WCAG não pede botão de pausa (critério 2.2.2). O deslocamento da rolagem é de 8px na primeira linha, 40px na segunda e de 60 a 120px nos adesivos, e no celular é a metade.

## O que não pode cair

- **Sem JS ou com movimento reduzido.** Aparece direto o Momento 3, parado, sem deslocamento na rolagem.
- **Leitor de tela.** O `h1` é a frase, inteira e lida uma vez. As notas do rascunho, os adesivos e as cores ficam escondidos dele.
- **Celular.** Só deslocamento, giro, escala e opacidade. O tremor do rascunho é um filtro de SVG, e sai assim que o Momento 2 começa, para não pesar.
- **Hover.** Não existe no hero.

## O Carregamento da Home

O Momento 1 já é a página se construindo. Recomendo que na Home a cortina do Carregamento não monte a tela, e o hero faça esse papel. A cortina continua no clique para sair da Home e nas outras páginas.

## Para você decidir

1. **O tamanho da frase.** Ela tem 82px no celular e 115px em 1440, acima do `display` (40 a 72px) e perto do `numero` (56 a 120px), que é do Dado. Ou o hero ganha um degrau próprio na escala, ou a frase usa o `numero`.
2. **As cores.** A regra 7 do `ds/RITMO.md` diz um acento por página, e a Home é lime. O Momento 2 usa lime, azul e verde. A Lista de casos logo abaixo já mostra os três acentos, um por caso. Ou o hero vira a exceção da regra, ou ele fica só com lime, mist e tinta.
3. **As notas do rascunho.** "Anton, o maior da tela" e "o não fica" são texto provisório.
4. **Os adesivos.** Lápis, lupa e pessoa para o ofício, e tela, conversa, celular e camadas para o jeito de fazer, mais a folha de esboço.
