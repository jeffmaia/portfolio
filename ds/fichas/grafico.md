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
2. Grupo, `div.chart__grupo`, um por grandeza. O nome da grandeza em `h3.chart__nome`, opcional quando o título já diz qual é.
3. Linhas, `dl.chart__linhas`, com uma `div.chart__linha` por momento. O rótulo em `dt.chart__rotulo`, o valor escrito em `dd.chart__valor` e o trilho em `dd.chart__trilho`, com o `span.chart__preenche`.

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

**Os três tons.** A diferença entre os valores nunca fica só na cor, porque o azul e o mist quase se confundem. Cada tom tem forma própria, em `data-tom`.

| Tom | Como fica | Nas barras | Nas pilhas |
| --- | --- | --- | --- |
| `cheio` | o acento da página | o depois | o nível mais forte (Entusiasta) |
| `trama` | fios de tinta na diagonal, sobre o papel | o antes | o nível do meio (Receptivo) |
| `vazio` | o papel | | o nível mais fraco (Indiferente) |

O trilho vem das Barras dos posts. Papel, contorno de 2px em `border`, 20px de altura e o raio pela metade do `radius`, porque numa faixa de 20px o raio inteiro viraria pílula. O preenchimento das barras leva um fio de tinta na ponta, e as partes das pilhas, um fio entre uma e outra.

Nas `barras`, cada grandeza é um grupo, com o rótulo à esquerda e o valor à direita, sobre a ponta do trilho. Com 600px de Seção, dois grupos ficam lado a lado, e um grupo sozinho ocupa a linha inteira.

Nas `pilhas`, a faixa inteira é o total do grupo, e cada parte ocupa a proporção da contagem dela. A conta escrita vem embaixo, na mesma margem em todas, para o olho descer comparando. Com 600px de Seção o nome do grupo vai para a esquerda, num terço, e a faixa e a conta ficam nos outros dois. A legenda vem antes das faixas, em três colunas com 600px de Seção, separada por um fio.

Na `escala`, o eixo vai de `--min` a `--max` (−100 a +100, o do NPS). O zero é um fio de tinta que passa acima e abaixo do eixo, o percurso do antes ao depois é cheio, o antes é um ponto vazado e o depois um ponto de tinta. Os dois valores ficam acima do eixo, cada um na sua linha, para nunca se encostarem por perto que fiquem. Cada um se ancora na própria posição, à esquerda no começo do eixo, ao centro no meio e à direita no fim.

O Gráfico usa o acento da página. Na superfície tinta os papéis trocam por dentro e a forma continua de pé, mas ele não entra lá, porque a tinta é a do Resultado e mora no Destaque.

Pelo `ds/RITMO.md`, as três formas são médias.

## Limites

- Um Gráfico por Seção.
- `barras`, de um a dois grupos, com dois momentos cada. Rótulo de até quatro palavras e valor de até três.
- `pilhas`, de três a oito grupos e de dois a três níveis. Todos os grupos com o mesmo total. Nome do grupo de até três palavras.
- `escala`, dois pontos, antes e depois. Valores inteiros.
- O título em uma linha no desktop.
- Os valores do desenho são números de 0 a 100 nas barras (`--valor`), contagens nas pilhas (`--n`) e os pontos da escala (`--antes`, `--depois`). Quem escreve a página faz a conta das barras. "1 a 2 meses" é 100 e "~1 semana" é 12,5.

## Comportamento

1. **Mouse.** Não tem. O Gráfico mostra, não age.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** A figura leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. Depois de `dur-media`, nas barras e nas pilhas uma tampa de papel sobre o trilho encolhe para a direita em `dur-lenta`, e o preenchimento aparece da esquerda para a direita. O segundo grupo e a segunda linha esperam mais `dur-rapida`. Na escala, o percurso corre do antes ao depois em `dur-lenta`, e só então o ponto e o valor de depois aparecem, em `dur-media`.
5. **Sem JS.** Aparece pronto, com tudo desenhado.
6. **Movimento reduzido.** Aparece pronto. A tampa, o percurso e o depois não esperam.

## Acessibilidade

- Cada Gráfico é uma `figure` com `figcaption`, e o leitor de tela ouve o título antes dos valores.
- O desenho fica escondido (`aria-hidden`). Todo valor que a barra mostra está escrito ao lado, e é isso que o leitor de tela ouve.
- Nas `barras`, cada momento é um par de `dt` e `dd` numa lista de definição. Quem ouve recebe "Antes, 1 a 2 meses".
- Nas `pilhas`, a legenda é uma lista de definição com o que cada nível quer dizer, e cada grupo é um item de lista com o nome e a conta escrita.
- Na `escala`, a faixa da régua vai no título só para o leitor de tela ("Nota geral de NPS, numa escala de −100 a +100").
- O til de aproximação é lido como "cerca de" (`<span aria-hidden="true">~</span><span class="sr">cerca de </span>`).
- Os tons não dependem da cor. Cheio, trama e vazio se distinguem também em tons de cinza.

## Onde aparece

- Vitrine, na amostra e no palco do Gráfico.
- Nas páginas publicadas, as `barras` no Processo, Seção 09. "Tempo antes e depois", com Discovery de "1 a 2 meses" para "~1 semana" e o refinamento semanal de "4 a 5 h" para "30 a 40 min".
- As `barras` no Mapa de experiência, Seção 05. "Usuários únicos no primeiro mês", de 20 sem o mapa para 890 com o mapa.
- As `pilhas` no Inpulse, Seção 03. "Reações de 10 participantes, em seis das dez funcionalidades testadas", com os três níveis de desejabilidade (Entusiasta, Receptivo e Indiferente) como a legenda. Antes eles eram ritos soltos, logo acima das faixas.
- A `escala` no Mapa de experiência, Seção 02. "Nota geral de NPS", de −33 para +15.

## Vizinhos

- **Dado `salto`.** Um número só, com o antes riscado.
- **Dado em grupo.** De dois a quatro números que fecham a conta, sem série.
- **Antes e depois.** A mudança sem número, em texto.
- **Passos `funil`.** Etapas que filtram, sem contagem.

## Par nos posts

Barras, o trilho com contorno e o preenchimento com o fio na ponta, para as `barras`. Waffle, os cem quadrados, faz o trabalho da proporção nos posts, e no site são as `pilhas`, porque o caso compara vários grupos e o waffle mostra um de cada vez. A `escala` não tem par.

## Código

```html
<!-- Barras -->
<figure class="chart" data-variant="barras" data-revelar>
  <figcaption class="t-rotulo">Tempo antes e depois</figcaption>
  <div class="chart__grupos">
    <div class="chart__grupo">
      <h3 class="chart__nome">Discovery</h3>
      <dl class="chart__linhas">
        <div class="chart__linha">
          <dt class="chart__rotulo">Antes</dt>
          <dd class="chart__valor">1 a 2 meses</dd>
          <dd class="chart__trilho" aria-hidden="true"><span class="chart__preenche" data-tom="trama" style="--valor: 100"></span></dd>
        </div>
        <div class="chart__linha">
          <dt class="chart__rotulo">Depois</dt>
          <dd class="chart__valor"><span aria-hidden="true">~</span><span class="sr">cerca de </span>1 semana</dd>
          <dd class="chart__trilho" aria-hidden="true"><span class="chart__preenche" data-tom="cheio" style="--valor: 12.5"></span></dd>
        </div>
      </dl>
    </div>
    <div class="chart__grupo">…</div>
  </div>
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

Entrou na Onda 4 e foi aprovado por você na vitrine, como está, em 24 de outubro de 2026. As páginas publicadas ainda usam o gráfico antigo, e passam para este na Fase 6.
