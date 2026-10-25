# Gráfico

`Chart` · o valor que só se entende ao lado de outros, numa série, numa proporção ou numa escala.

## Use quando

- **Uma grandeza antes e depois, em tempo ou quantidade, e a proporção importa.** O tamanho da barra mostra quanto encolheu ou cresceu, coisa que dois números soltos não mostram. Use `barras`.
- **A proporção de respostas em cada grupo.** Vários grupos com o mesmo total, e o que se compara é quanto de cada resposta coube em cada um. Use `pilhas`.
- **Uma posição numa escala com sinal, antes e depois.** O leitor precisa ver de que lado do zero o valor estava e para onde foi. Use `escala`.

## Não use quando

- É um número só, com o valor de antes, que prova o caso. Use Dado `salto`.
- São de dois a quatro números que fecham a conta, cada um com a sua frase. Use Dado em grupo, porque o Gráfico pede série ou proporção.
- O que mudou é uma regra, um fluxo ou um jeito de trabalhar, sem número. Use Antes e depois.
- A diferença entre os valores é pequena demais para o olho ver na barra (de 40 para 42). Use Dado e diga a diferença em texto.
- As pilhas teriam totais diferentes de um grupo para outro. A faixa inteira deixa de ser a mesma coisa. Use barras com a contagem, ou diga a proporção em texto.

## Anatomia

**Toda forma.**

1. Caixa, `figure.chart` com `data-variant`, obrigatória.
2. Título, `figcaption.t-rotulo`, obrigatório. Diz o que se mede e, quando precisa, de onde vem ("Reações de 10 participantes, em seis das dez funcionalidades testadas").
3. Trilho, `.chart__trilho`, a faixa de papel com contorno onde o valor se desenha. Escondido do leitor de tela.

**Barras.**

1. Grupos, `div.chart__grupos`, obrigatório.
2. Grupo, `div.chart__grupo`, um por grandeza. O nome da grandeza em `h3.chart__nome`, opcional quando o título já diz qual é. O grupo leva `--antes` e `--depois` no `style` e `data-sentido="queda"` quando o depois é menor.
3. Marcos, `dl.chart__marcos`, com uma `div.chart__marco` por momento (`data-ponto="antes"` e `data-ponto="depois"`). O momento em `dt.t-rotulo` e o valor escrito em `dd.chart__valor`.
4. Barra, `div.chart__barra`, escondida do leitor de tela. O trilho com o antes (`span.chart__antes`) e o depois (`span.chart__preenche`).
5. Chave, `p.chart__chave`, escondida do leitor de tela, com a amostra do antes e a do depois e os rótulos do primeiro grupo.

**Pilhas.**

1. Legenda, `dl.chart__legenda`, obrigatória. Um item por nível, com a amostra do tom (`span.chart__amostra`), o nome em `dt` e o que o nível quer dizer em `dd`.
2. Pilhas, `ol.chart__pilhas`, com um `li.chart__pilha` por grupo. O nome em `p.chart__nome`, o trilho com um `span.chart__parte` por nível e a conta escrita em `p.chart__conta`.

**Escala.**

1. Escala, `div.chart__escala`, obrigatória.
2. Marcos, `p.chart__marco` com `data-ponto="antes"` e `data-ponto="depois"`, o número em `span.chart__numero` (Anton) e o momento num rótulo.
3. Eixo, `div.chart__eixo`, escondido do leitor de tela, com o percurso (`.chart__percurso`), o zero (`.chart__zero`) e os dois pontos (`.chart__ponto`).
4. Régua, `p.chart__regua.t-rotulo`, com o mínimo, o zero e o máximo. Escondida do leitor de tela, que ouve a escala no título.

## Variantes

| Forma | Como se escreve | Quando |
| --- | --- | --- |
| `barras` | `figure.chart` com `data-variant="barras"` | Uma grandeza antes e depois |
| `pilhas` | `figure.chart` com `data-variant="pilhas"` | A proporção de respostas em cada grupo |
| `escala` | `figure.chart` com `data-variant="escala"` | A posição numa escala com sinal, antes e depois |

**Os tons.** A diferença entre os valores nunca fica só na cor, porque o azul e o mist quase se confundem. Cada tom tem forma própria, em `data-tom`.

| Tom | Como fica | Nas barras | Nas pilhas |
| --- | --- | --- | --- |
| `cheio` | o acento da página | o depois | o nível mais forte (Entusiasta) |
| `muted` | o muted | o antes | |
| `trama` | fios de tinta na diagonal, sobre o papel | | o nível do meio (Receptivo) |
| `vazio` | o papel | | o nível mais fraco (Indiferente) |

O trilho vem das Barras dos posts. Papel, contorno de 2px em `border`, 20px de altura nas pilhas e 32px nas barras, e o raio pela metade do `radius`, porque numa faixa estreita o raio inteiro viraria pílula. Nas barras, o antes e o depois levam um fio de tinta na ponta, só dentro do trilho, e as partes das pilhas, um fio entre uma e outra.

Nas `barras`, cada grandeza é um grupo, com o antes e o depois no mesmo trilho, como na escala. O antes é a área de muted e o depois é o acento. Cada um termina num fio de tinta de 2px, o mesmo do contorno, que fica só dentro do trilho e some debaixo do contorno quando a barra chega a 100. Nenhum fio sai do trilho, porque o único fio que cruza o eixo é o zero da `escala`. A barra menor fica por cima, para as duas cores aparecerem sempre, da mesma cor da chave. Numa queda o acento cobre o começo do muted, e o muted que sobra é o que saiu. Num salto o muted cobre o começo do acento, e o acento que passa do antes é o que cresceu. O antes nunca fica com menos de 4px, para o 20 do Mapa ainda mostrar o muted. Os dois valores ficam numa linha só, acima do trilho, e cada um termina sobre a ponta da sua barra, na ordem das pontas. O menor termina na ponta dele e o maior na dele, então os dois nunca se cobrem. Quando o valor é mais largo que a barra, ele empurra o outro para a direita, mas continua do lado certo. O momento fica em cima e o valor embaixo, rente ao trilho. Cada marco se alinha ao lado da barra a que ele se liga. O da barra menor, que nasce na esquerda do trilho, se alinha pela esquerda, e o da maior se alinha pela direita, na ponta dela. Não há um lado só para os dois. Uma chave embaixo diz qual é o antes e qual é o depois. Com 600px de Seção, dois grupos ficam lado a lado, e um grupo sozinho ocupa a linha inteira.

As barras eram dois trilhos, um por momento, com o antes em trama e o valor na beira direita. O antes cheio parecia só marcar o espaço, e o valor ficava longe da ponta que media. O estudo das três direções está em `ds/vitrine/estudo/barras.html`.

Nas `pilhas`, a faixa inteira é o total do grupo, e cada parte ocupa a proporção da contagem dela. A conta escrita vem embaixo, na mesma margem em todas, para o olho descer comparando. Com 600px de Seção o nome do grupo vai para a esquerda, num terço, e a faixa e a conta ficam nos outros dois. A legenda vem antes das faixas, em três colunas com 600px de Seção, separada por um fio.

Na `escala`, o eixo vai de `--min` a `--max` (−100 a +100, o do NPS). O zero é um fio de tinta que passa acima e abaixo do eixo, o percurso do antes ao depois é cheio, o antes é um ponto vazado e o depois um ponto de tinta. Os dois valores ficam numa linha só, acima do eixo, cada um sobre o próprio ponto e na ordem dos pontos, para o olho ligar o número à bolinha sem esforço. O valor da esquerda termina no ponto dele e o da direita começa no dele, então os dois nunca se cobrem, por perto que os pontos fiquem. Perto da borda o valor não sai do eixo e passa por cima do ponto, mas continua do lado certo. O número fica embaixo, rente ao eixo, e o momento em cima. Numa queda o depois é o ponto da esquerda, e a figura leva `data-sentido="queda"` para os valores trocarem de lado com os pontos.

O Gráfico usa o acento da página. Na superfície tinta os papéis trocam por dentro e a forma continua de pé, mas ele não entra lá, porque a tinta é a do Resultado e mora no Destaque.

Pelo `ds/RITMO.md`, as três formas são médias.

## Limites

- Um Gráfico por Seção.
- `barras`, de um a dois grupos, com dois momentos cada. Rótulo de até três palavras e valor de até três, porque os dois dividem uma linha sobre o trilho.
- `pilhas`, de três a oito grupos e de dois a três níveis. Todos os grupos com o mesmo total. Nome do grupo de até três palavras.
- `escala`, dois pontos, antes e depois. Valores inteiros.
- O título em uma linha no desktop.
- Os valores do desenho são números de 0 a 100 nas barras (`--antes`, `--depois`), contagens nas pilhas (`--n`) e os pontos da escala (`--antes`, `--depois`). Quem escreve a página faz a conta das barras. "1 a 2 meses" é 100 e "~1 semana" é 12,5.

## Comportamento

1. **Mouse.** Não tem. O Gráfico mostra, não age.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** A figura leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. Depois de `dur-media`, nas barras e nas pilhas uma tampa de papel sobre o trilho encolhe para a direita em `dur-lenta`, e o preenchimento aparece da esquerda para a direita. O segundo grupo espera mais `dur-rapida`. Na escala, o percurso corre do antes ao depois em `dur-lenta`, e só então o ponto e o valor de depois aparecem, em `dur-media`.
5. **Sem JS.** Aparece pronto, com tudo desenhado.
6. **Movimento reduzido.** Aparece pronto. A tampa, o percurso e o depois não esperam.

## Acessibilidade

- Cada Gráfico é uma `figure` com `figcaption`, e o leitor de tela ouve o título antes dos valores.
- O desenho fica escondido (`aria-hidden`). Todo valor que a barra mostra está escrito ao lado, e é isso que o leitor de tela ouve.
- Nas `barras`, cada momento é um par de `dt` e `dd` numa lista de definição, sempre o antes primeiro, mesmo quando o depois aparece à esquerda. Quem ouve recebe "Antes, 1 a 2 meses". A chave fica escondida, porque repete os rótulos.
- Nas `pilhas`, a legenda é uma lista de definição com o que cada nível quer dizer, e cada grupo é um item de lista com o nome e a conta escrita.
- Na `escala`, a faixa da régua vai no título só para o leitor de tela ("Nota geral de NPS, numa escala de −100 a +100").
- O til de aproximação é lido como "cerca de" (`<span aria-hidden="true">~</span><span class="sr">cerca de </span>`).
- Os tons não dependem da cor. Cheio, muted, trama e vazio se distinguem também em tons de cinza, e nas barras o fio de tinta marca a ponta de cada barra.

## Onde aparece

- Vitrine, na amostra e no palco do Gráfico.
- Nas páginas publicadas, as `barras` no Processo, Seção 08. "Tempo antes e depois", com Discovery de "1 a 2 meses" para "~1 semana" e o refinamento semanal de "4 a 5 h" para "30 a 40 min".
- As `barras` no Mapa de experiência, Seção 05. "Usuários únicos no primeiro mês", de 20 "Sem o mapa" para 890 "Com o mapa".
- As `pilhas` no Inpulse, Seção 04. "Reações de 10 participantes, em seis das dez funcionalidades testadas", com os três níveis de desejabilidade (Entusiasta, Receptivo e Indiferente) como a legenda. Antes eles eram ritos soltos, logo acima das faixas.
- A `escala` no Mapa de experiência, Seção 02. "Nota geral de NPS", de −33 para +15.

## Vizinhos

- **Dado `salto`.** Um número só, com o antes riscado.
- **Dado em grupo.** De dois a quatro números que fecham a conta, sem série.
- **Antes e depois.** A mudança sem número, em texto.
- **Passos `funil`.** Etapas que filtram, sem contagem.

## Par nos posts

Barras, o trilho com contorno e o preenchimento com o fio na ponta, para as `barras`, que dão o mesmo fio à ponta do antes. Waffle, os cem quadrados, faz o trabalho da proporção nos posts, e no site são as `pilhas`, porque o caso compara vários grupos e o waffle mostra um de cada vez. A `escala` não tem par.

## Código

```html
<!-- Barras -->
<figure class="chart" data-variant="barras" data-revelar>
  <figcaption class="t-rotulo">Tempo antes e depois</figcaption>
  <div class="chart__grupos">
    <div class="chart__grupo" data-sentido="queda" style="--antes: 100; --depois: 12.5">
      <h3 class="chart__nome">Discovery</h3>
      <dl class="chart__marcos">
        <div class="chart__marco" data-ponto="antes"><dt class="t-rotulo">Antes</dt><dd class="chart__valor">1 a 2 meses</dd></div>
        <div class="chart__marco" data-ponto="depois"><dt class="t-rotulo">Depois</dt><dd class="chart__valor"><span aria-hidden="true">~</span><span class="sr">cerca de </span>1 semana</dd></div>
      </dl>
      <div class="chart__barra" aria-hidden="true">
        <div class="chart__trilho"><span class="chart__antes"></span><span class="chart__preenche"></span></div>
      </div>
    </div>
    <div class="chart__grupo">…</div>
  </div>
  <p class="chart__chave" aria-hidden="true"><span><span class="chart__amostra" data-tom="muted"></span>Antes</span><span><span class="chart__amostra" data-tom="cheio"></span>Depois</span></p>
</figure>

<!-- Pilhas -->
<figure class="chart" data-variant="pilhas" data-revelar>
  <figcaption class="t-rotulo">Reações de 10 participantes, em seis das dez funcionalidades testadas</figcaption>
  <dl class="chart__legenda">
    <div><dt><span class="chart__amostra" data-tom="cheio" aria-hidden="true"></span>Entusiasta</dt><dd>Demonstra interesse de maneira espontânea.</dd></div>
    <div><dt><span class="chart__amostra" data-tom="trama" aria-hidden="true"></span>Receptivo</dt><dd>…</dd></div>
    <div><dt><span class="chart__amostra" data-tom="vazio" aria-hidden="true"></span>Indiferente</dt><dd>…</dd></div>
  </dl>
  <ol class="chart__pilhas">
    <li class="chart__pilha">
      <p class="chart__nome">Calendário</p>
      <div class="chart__trilho" aria-hidden="true"><span class="chart__parte" data-tom="cheio" style="--n: 3"></span><span class="chart__parte" data-tom="trama" style="--n: 7"></span></div>
      <p class="chart__conta">3 entusiastas · 7 receptivos</p>
    </li>
  </ol>
</figure>

<!-- Escala -->
<figure class="chart" data-variant="escala" style="--antes: -33; --depois: 15" data-revelar>
  <figcaption class="t-rotulo">Nota geral de NPS<span class="sr">, numa escala de −100 a +100</span></figcaption>
  <div class="chart__escala">
    <p class="chart__marco" data-ponto="antes"><span class="chart__numero">−33</span><span class="t-rotulo">Antes</span></p>
    <p class="chart__marco" data-ponto="depois"><span class="chart__numero">+15</span><span class="t-rotulo">Depois</span></p>
    <div class="chart__eixo" aria-hidden="true"><span class="chart__percurso"></span><span class="chart__zero"></span><span class="chart__ponto" data-ponto="antes"></span><span class="chart__ponto" data-ponto="depois"></span></div>
    <p class="chart__regua t-rotulo" aria-hidden="true"><span>−100</span><span>0</span><span>+100</span></p>
  </div>
</figure>
```

Estilo em `assets/ds/componentes.css`, seção Chart (`.chart` e as partes `chart__`, os tons em `data-tom` e o arranjo em `@container`). Não tem script além do revelar. Uma parte que nenhuma pilha tem, como o indiferente do Calendário, sai do HTML em vez de entrar com `--n: 0`.

Entrou na Onda 4 e foi aprovado por você na vitrine, como está, em 24 de outubro de 2026. Os casos publicados usam este desde a Fase 6, com as barras de um trilho só que você escolheu no estudo.
