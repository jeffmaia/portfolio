# Hero da Home

`Hero` · a frase que abre a Home e é a própria cena, do rascunho à página pronta.

## Use quando

- **A abertura da Home.** É a única página que tem hero. A frase é "O ofício continua o mesmo. O jeito de fazer, não.", e a linha de apoio diz o que o Jeff faz.

## Não use quando

- É o começo de um caso. Use o Topo do caso, com as Etiquetas, o título, a frase de apoio, a ficha e o Dado `salto` (ver `ds/RECEITAS.md`).
- É uma frase que o leitor precisa levar embora no meio de uma página. Use Destaque.
- É o número que prova o caso. Use Dado `salto`.
- É a chegada de qualquer página. Ela é do Carregamento, que é fundamento e não peça.

## Anatomia

1. Caixa, `section.hero`, obrigatória, rotulada pela frase com `aria-labelledby`.
2. Filtro do tremor, `svg.hero__filtro` com o `filter#hero-tremor`, obrigatório no hero que se move. Escondido do leitor de tela.
3. Grade do rascunho, `span.hero__grade`, decorativa.
4. Frase, `h1.hero__frase`, obrigatória. Duas linhas (`span.hero__linha`), cada uma com três pedaços (`span.hero__q`) e um número de ordem (`--i`), e as palavras marcadas com cor (`span.hero__p`).
5. Notas do rascunho, `span.hero__nota`, decorativas, dentro do `h1` e escondidas do leitor de tela.
6. Adesivos, os sete ícones do acento (`img.hero__adesivo`) e a folha de esboço solta, dentro do `h1`, decorativos.
7. Apoio, `div.hero__apoio`, obrigatório. A linha de apoio em `p.t-sub` e, no mesmo lugar, os três traços do rascunho em `svg.hero__rascunho`.

## Variantes

| Atributo | Valor | Como fica | Quando |
| --- | --- | --- | --- |
| sem atributo | | Com movimento, a chegada do rascunho à página pronta e o deslocamento na rolagem | A Home |
| `data-parado` | sem valor | A página pronta, sem chegada e sem deslocamento | A amostra da vitrine, para ver o fim parado |

**A frase.** O tamanho sai da largura do hero, e não da escala de texto. Do tablet para cima são duas linhas, uma por frase, e a primeira ocupa 10,8 vezes o tamanho da fonte em Anton (115px em 1440, 63px em 768). No celular cada frase quebra em três linhas, "O ofício / continua / o mesmo." e "O jeito / de fazer, / não.", para ganhar o peso que tem no desktop (82px em 390). A entrelinha é a do `leading-display`, que dá espaço ao til do NÃO.

**As cores.** Ficam sempre atrás das palavras, como adesivos com contorno de tinta. O `primary` (lime) marca OFÍCIO, o `secondary` (azul) é um círculo no fim de MESMO, o `chart-3` (verde) sublinha JEITO DE FAZER, e o NÃO fica numa caixa de tinta, com o texto em papel. A faixa verde é feita de dois pedaços, porque no celular quebra depois de "jeito". No desktop os dois emendam numa faixa só.

**Os adesivos.** Os do ofício, o que continua, sentam na primeira linha (lápis, lupa e pessoa). Os do jeito de fazer, o que mudou, sentam embaixo da segunda (tela, conversa, celular e camadas), com a folha de esboço ao lado do NÃO. No celular eles descem pelo vão que as linhas curtas deixam à direita. O robô fica de fora, lugar comum de IA.

**A dobra.** No desktop o hero deixa 9rem da primeira tela, onde aparecem o rótulo Quatro casos e o alto dos primeiros Cartões, para ficar claro que a página continua. Abaixo de 720px o hero tem a altura do conteúdo.

## Limites

- Um hero por site, na Home.
- A frase não muda e não quebra de outro jeito. Se um dia mudar, o tamanho se mede de novo pela linha mais larga.
- Sete adesivos e a folha de esboço. Mais que isso, a frase perde para os ícones.
- A linha de apoio em até três linhas no celular e duas no desktop.

## Comportamento

1. **Mouse.** Não tem.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** A chegada roda uma vez, em uns 3,2s, e para pronta. Todos os tempos saem dos tokens.
   - Rascunho. A grade aparece em `dur-media`. A partir de `dur-media`, cada linha é escrita da esquerda para a direita em `dur-lenta` com `ease-troca`, a segunda uma `dur-media` depois. No celular cada pedaço vem uma `dur-rapida` depois do anterior. As guias tracejadas vêm junto com a linha. A hachura corre por OFÍCIO, os traços da linha de apoio se desenham, entram as notas e o NÃO é circulado, cada um em `dur-media`.
   - Cores. Em duas `dur-lenta` e meia (1,6s), o contorno se enche de tinta, o tremor some e o rascunho se apaga, em `dur-media`. As cores colam atrás das palavras com `ease-saida`, uma `dur-rapida` depois da outra, e o NÃO vira papel quando a caixa chega. A linha de apoio aparece.
   - Adesivos. Em 3,9 `dur-lenta` (2,5s) os adesivos chegam, meia `dur-rapida` um depois do outro, de um tamanho maior e girados até assentar.
   - Rolagem. O progresso vai do topo da página até o hero sair de baixo do cabeçalho, pela linha do tempo de rolagem do CSS e, onde ela não existe, pelo módulo 5 do `componentes.js`. A primeira linha sobe 8px, a segunda 40px e os adesivos de 60 a 120px. No celular é a metade. Nada gira nem muda de cor.
5. **Sem JS.** A página chega pronta, sem chegada e sem deslocamento.
6. **Movimento reduzido.** A página chega pronta, sem chegada e sem deslocamento. O rascunho não existe.

## Acessibilidade

- O `h1` é a frase inteira, lida uma vez. As notas, os adesivos e a folha de esboço ficam escondidos do leitor de tela, e o texto fica em minúsculas no HTML, com a caixa alta só no CSS.
- A grade, o filtro e os traços do rascunho são decorativos.
- A chegada dura menos de 5s, então não pede botão de pausa (WCAG, critério 2.2.2).
- Tinta sobre papel, tinta sobre o lime, o azul e o verde, e papel sobre a tinta passam com folga. Ver `ds/CONTRASTE.md`.

## Onde aparece

- Vitrine, na amostra e no palco da Home, com a Lista de casos logo abaixo.
- O estudo dos três momentos parados, em `ds/vitrine/estudo/hero/`.
- A Home publicada, desde o passo 4 da Fase 6. As fotos do hero antigo foram para `arquivo/site-antigo/`.

## Vizinhos

- **Topo do caso.** A abertura de cada caso, com título, ficha e número.
- **Destaque.** A frase que fica, no meio de uma página.
- **Carregamento.** O mesmo gesto, do esboço à página pronta, na chegada de toda página.

## Par nos posts

A capa do carrossel, com a tese curta em Anton e os ícones adesivo em volta. Lá a capa é parada, e aqui ela se escreve na chegada.

## Código

```html
<section class="hero" aria-labelledby="hero-frase">
  <svg class="hero__filtro" aria-hidden="true" focusable="false"><filter id="hero-tremor">…</filter></svg>
  <span class="hero__grade" aria-hidden="true"></span>
  <h1 class="hero__frase" id="hero-frase">
    <span class="hero__linha" style="--i: 0">
      <span class="hero__q" style="--i: 0">o&nbsp;<span class="hero__p hero__p--oficio">ofício</span></span>
      <span class="hero__q" style="--i: 1">continua</span>
      <span class="hero__q" style="--i: 2">o&nbsp;<span class="hero__p hero__p--mesmo">mesmo.</span></span>
    </span>
    <span class="hero__linha" style="--i: 1">
      <span class="hero__q" style="--i: 3">o&nbsp;<span class="hero__p hero__p--jeito hero__p--emenda">jeito</span></span>
      <span class="hero__q" style="--i: 4"><span class="hero__p hero__p--jeito">de&nbsp;fazer,</span></span>
      <span class="hero__q" style="--i: 5"><span class="hero__p hero__p--nao">não.</span></span>
    </span>
    <span class="hero__nota hero__nota--topo" aria-hidden="true">Anton, o maior da tela</span>
    <span class="hero__nota hero__nota--pe" aria-hidden="true">o não fica</span>
    <img class="hero__adesivo hero__a--lapis" src="assets/ds/icones/lapis-lime.svg" alt="" width="96" height="96">
    …
  </h1>
  <div class="hero__apoio">
    <p class="t-sub">Ajudo times de produto e design a integrar IA no processo real de trabalho, não só na ferramenta.</p>
    <svg class="hero__rascunho" viewBox="0 0 520 90" aria-hidden="true" focusable="false">…</svg>
  </div>
</section>
```

O HTML sai da função `hero` de `ds/prova/comum.py`, que escreve os pedaços, os adesivos e a folha de esboço. Estilo e chegada em `assets/ds/componentes.css`, nas receitas (`.hero` e as partes `hero__`). A chegada é toda de CSS, com os tempos dos tokens. O deslocamento usa o progresso `--p`, da linha do tempo de rolagem ou do módulo 5 do `componentes.js`.

**Decidido na Fase 6.** O tamanho da frase ganhou degraus próprios em `tokens.css`, `text-hero` e `text-hero-estreito`, fora da escala de texto. As notas do rascunho ficam como estão. Na Home a cortina do Carregamento não monta a tela, porque o hero já é a chegada (`data-sem-chegada`, ver `ds/FUNDAMENTOS.md`).

Entrou na Onda 5, com a direção trocada por você no meio da onda, e a chegada e a rolagem foram aprovadas na vitrine em 24 de outubro de 2026. O roteiro está em `ds/ROTEIRO-HERO.md`.
