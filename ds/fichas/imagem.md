# Imagem

`Figure` · a tela, o percurso ou o ambiente do caso, em moldura, galeria ou sangria.

## Use quando

- **Uma tela ou um protótipo.** O leitor precisa ver o produto como objeto, pousado no papel. Use `moldura`, e `data-formato="retrato"` quando é uma tela de celular.
- **Uma tela de celular com o texto que leva até ela.** A tela é estreita, e sozinha na coluna deixaria metade da Seção vazia. Ponha o texto e a `moldura` `retrato` em `div.figure-ao-lado`.
- **Uma imagem com fundo vazio em volta do que importa.** Telas espalhadas na diagonal, por exemplo. Use `moldura` com `data-recorte`, e a imagem cresce por dentro do quadro até o fundo sair.
- **Várias telas na ordem do percurso.** O leitor precisa ver todas de uma vez, na ordem em que quem usa passa por elas. Use `galeria`, e `data-abertura` quando a primeira é o todo de que as outras são recorte.
- **Uma imagem que é ambiente, não objeto.** As telas do produto pronto, vistas como paisagem, cortadas na altura. Use `sangria`.

## Não use quando

- As telas são longas e o leitor vai ver uma ou duas. Use Abas, com uma tela por painel.
- A imagem só decora uma Seção que já se entende pelo texto. Texto corrido não leva imagem.
- É a ilustração do caso, presa ao indicador. Ela mora no Cartão do acento do Topo, com o Dado `salto`.
- É um número desenhado, de série ou proporção. Use Gráfico.
- A sangria entraria no mesmo caso que o Destaque na tinta. As duas são o peso forte da página, e entra só uma (regra 2 do `ds/RITMO.md`). Use `moldura`.

## Anatomia

**Moldura e sangria.**

1. Caixa, `figure.figure` com `data-variant`, obrigatória.
2. Quadro, `div.figure__quadro`, obrigatório. Dentro, um `img` com `width` e `height`, ou um `iframe` com `title`.
3. Legenda, `figcaption.figure__legenda`, opcional. Uma frase sobre o que se vê ou o que fazer com a tela.

**Galeria.**

1. Caixa, `div.figure` com `data-variant="galeria"`, obrigatória, e `data-abertura` opcional.
2. Lista, `ol.figure__lista`, obrigatória, porque a ordem é a do percurso.
3. Itens, um `li` por tela, cada um com uma `figure`, o quadro e a legenda. A legenda começa pelo número da figura num rótulo (`span.t-rotulo`, "Fig. 01").

Quando a tela tem uma versão completa fora da página, o Link `externo` vem logo depois da Imagem ("Abrir o protótipo completo", "Abrir o mapa completo").

## Variantes

| Atributo | Valor | Como fica | Quando |
| --- | --- | --- | --- |
| `data-variant` | `moldura` | O quadro com o contorno de tinta, o `radius` e o `muted` por baixo | Uma tela ou protótipo |
| | `galeria` | Os quadros abertos, duas por linha com 600px de Seção | Várias telas na ordem do percurso |
| | `sangria` | A faixa de beira a beira, sem contorno e sem raio, com fundo de tinta por baixo | A imagem que é ambiente |
| `data-formato` | `retrato` | A moldura para de crescer em 400px | Uma tela de celular |
| `data-abertura` | sem valor | A primeira tela da galeria ocupa a linha inteira | A primeira é o todo e as outras são recorte |
| `data-recorte` | sem valor, com `--zoom` no `style` | A moldura fica em 16:9 e a imagem cresce por dentro, centrada | A imagem tem fundo vazio em volta do que importa |
| `div.figure-ao-lado` | em volta do texto e da moldura | O texto à esquerda e a tela à direita, com o Link embaixo | Uma tela de celular com o texto que leva até ela |

A moldura é a caixa do sistema. O contorno de 2px em `border` e o `muted` por baixo impedem a imagem de flutuar solta no papel e dão onde terminar a uma tela clara como ele. O `iframe` dentro da moldura tem a altura entre 520px e 720px, conforme a tela.

No recorte, o quadro fica em 16:9 em qualquer largura e a imagem enche por cima, centrada, com a escala de `--zoom`. O quanto ela cresce é medido no arquivo, e é a página que escreve. Escolha o menor `--zoom` com que nenhum canto mostra fundo, conferido nos degraus da faixa, não só no centro. As telas do Inpulse, 3234 por 3260px numa faixa diagonal, pedem `--zoom: 2`, a imagem com o dobro da largura do quadro. Com 1,9 ainda escapa 1px.

Ao lado, a partir de 760px de Seção o texto corre à esquerda, numa coluna que ocupa o que sobra, e a moldura `retrato` fica à direita, em 400px, com o Link logo embaixo dela. O vão entre as duas é o `space-48`. Abaixo de 760px o texto vem antes e a tela depois, um debaixo do outro. O texto é prosa corrida, sem Destaque no meio, porque a nota no meio de dois parágrafos quebra a leitura ao lado da tela.

A galeria decide o arranjo pela largura da Seção, como o Passos. Com 600px de Seção são duas telas por linha, e abaixo disso uma debaixo da outra. Duas e não três, porque são telas densas.

A sangria é o contrário da moldura. O quadro sai da coluna e vai até a beira da tela, e o recuo é a distância da coluna à beira, que é a margem da página ou, na tela larga, a metade do que sobra além dos 1280px. No caso, a partir de 1100px a coluna da esquerda é do Sumário, e a faixa sangra só para a direita. A altura é fixa, entre 260px e 560px, e a imagem enche por cima.

Na superfície tinta o contorno da moldura vira papel, porque `border` troca por dentro. A Imagem não entra lá no caso, porque a tinta é a do Resultado.

Pelo `ds/RITMO.md`, a `moldura` e a `galeria` são médias, e a `sangria` é forte.

## Limites

- Uma `sangria` por caso, e só se o caso não tiver o Destaque na tinta.
- Uma `galeria` por caso, de três a seis telas. Mais que isso, as telas viram Abas ou duas Seções.
- Uma Imagem por Seção.
- Ao lado, só a `moldura` `retrato`. Uma tela larga ao lado do texto fica pequena demais para ler.
- No recorte, o `--zoom` não passa de 2,5. Mais que isso, a imagem perde nitidez e o que se vê já é outra imagem, que vale recortar no arquivo.
- Legenda de até duas linhas. O número da figura só na galeria.
- Toda `img` leva `width` e `height` com a proporção real, para a página não pular quando ela chega.

## Comportamento

1. **Mouse.** Não tem. A Imagem mostra, não age. O protótipo dentro do `iframe` tem o comportamento dele.
2. **Toque.** Não tem. O Link `externo` logo depois tem 44px.
3. **Foco.** A Imagem não recebe foco. O `iframe` recebe, com o anel do navegador em volta do quadro.
4. **Movimento.** A figura leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. A galeria entra inteira, para a leitura das telas não esperar.
5. **Sem JS.** Aparece pronta.
6. **Movimento reduzido.** Aparece pronta.

## Acessibilidade

- Toda `img` tem `alt` que diz o que a tela mostra ("O tabuleiro do mapa, com as 12 etapas da graduação distribuídas do START ao FINISH"). A legenda complementa, não repete.
- O `iframe` tem `title` ("Protótipo do aplicativo Inpulse").
- Na galeria a lista é ordenada, e quem ouve recebe a ordem do percurso.
- As imagens vêm com `loading="lazy"` e `decoding="async"`.
- O recorte esconde parte da imagem, então o `alt` descreve o que fica à vista no quadro.
- Ao lado, a ordem do HTML é a da leitura, o texto antes e a tela depois, igual no celular.
- A sangria não esconde texto. O que ela precisa dizer está no `alt` e no texto da Seção.

## Onde aparece

- Vitrine, na amostra e no palco da Imagem.
- Nas páginas publicadas, a `moldura` `retrato` ao lado do texto no Inpulse, Seção 03, depois de três parágrafos corridos. O protótipo navegável do aplicativo, com a legenda "Navegue pelo app aqui mesmo, ou abra o protótipo em tela cheia" e o Link "Abrir o protótipo completo".
- A `galeria` com abertura no Mapa de experiência, Seção 04. As cinco telas do mapa, da "Fig. 01 · O tabuleiro, do primeiro ao último semestre" à "Fig. 05 · O sentimento por eixo ao longo do curso", e o Link "Abrir o mapa completo".
- A `moldura` com `data-recorte` e `--zoom: 2` no Resultado do Inpulse, Seção 05. As telas do aplicativo, com o boletim por complexo temático, o calendário acadêmico e a situação atual do aluno. Elas estavam na `sangria`, que não pode ficar na mesma Seção que o Destaque na tinta (decisão 11 da Fase 6). A `sangria` fica na biblioteca, sem página que a use.

## Vizinhos

- **Abas.** Telas longas, vistas uma de cada vez.
- **Gráfico.** O número desenhado, não a tela.
- **Cartão do acento com a ilustração.** A cena do caso, presa ao indicador do Topo.
- **Destaque na tinta.** O outro peso forte da página, que não entra junto com a sangria.

## Par nos posts

Mockup, a tela dentro de um aparelho, para a `moldura`. A `galeria` e a `sangria` não têm par, porque o carrossel mostra uma imagem por vez e nunca sai da margem.

## Código

```html
<!-- Moldura, retrato -->
<figure class="figure" data-variant="moldura" data-formato="retrato" data-revelar>
  <div class="figure__quadro"><iframe src="https://embed.figma.com/proto/…" title="Protótipo do aplicativo Inpulse" allowfullscreen loading="lazy"></iframe></div>
  <figcaption class="figure__legenda">Navegue pelo app aqui mesmo, ou abra o protótipo em tela cheia.</figcaption>
</figure>
<a class="link" data-variant="externo" href="https://www.figma.com/proto/…" target="_blank" rel="noopener">Abrir o protótipo completo <i aria-hidden="true">↗</i></a>

<!-- Moldura, retrato, ao lado do texto -->
<div class="figure-ao-lado" data-revelar>
  <div class="prosa"><p>…</p><p>…</p><p>…</p></div>
  <figure class="figure" data-variant="moldura" data-formato="retrato">
    <div class="figure__quadro"><iframe src="https://embed.figma.com/proto/…" title="Protótipo do aplicativo Inpulse" allowfullscreen loading="lazy"></iframe></div>
    <figcaption class="figure__legenda">Navegue pelo app aqui mesmo, ou abra o protótipo em tela cheia.</figcaption>
  </figure>
  <a class="link" data-variant="externo" href="https://www.figma.com/proto/…" target="_blank" rel="noopener">Abrir o protótipo completo <i aria-hidden="true">↗</i></a>
</div>

<!-- Moldura, recortada -->
<figure class="figure" data-variant="moldura" data-recorte style="--zoom: 2" data-revelar>
  <div class="figure__quadro"><img src="…" alt="Telas do aplicativo Inpulse, com o boletim por complexo temático, o calendário acadêmico e a situação atual do aluno." width="3234" height="3260" loading="lazy" decoding="async"></div>
</figure>

<!-- Galeria, com abertura -->
<div class="figure" data-variant="galeria" data-abertura data-revelar>
  <ol class="figure__lista">
    <li><figure>
      <div class="figure__quadro"><img src="…" alt="O tabuleiro do mapa, com as 12 etapas da graduação distribuídas do START ao FINISH." width="4320" height="3072" loading="lazy" decoding="async"></div>
      <figcaption class="figure__legenda"><span class="t-rotulo">Fig. 01</span>O tabuleiro, do primeiro ao último semestre</figcaption>
    </figure></li>
    <li>…</li>
  </ol>
</div>

<!-- Sangria -->
<figure class="figure" data-variant="sangria" data-revelar>
  <div class="figure__quadro"><img src="…" alt="Telas do aplicativo Inpulse, com o boletim por complexo temático, o calendário acadêmico e a situação atual do aluno." width="3234" height="3260" loading="lazy" decoding="async"></div>
</figure>
```

Estilo em `assets/ds/componentes.css`, seção Figure (`.figure` e as partes `figure__`, o recorte, o `.figure-ao-lado` e os arranjos da galeria e do ao lado em `@container`). Não tem script além do revelar. O `body` tem `overflow-x: clip`, para a sangria não abrir rolagem para o lado onde a barra de rolagem ocupa lugar.

Entrou na Onda 5 e foi aprovada por você na vitrine, como está, em 24 de outubro de 2026. O recorte e o ao lado entraram na Fase 6, no Inpulse, e foram aprovados por você na vitrine e na página em 25 de outubro de 2026.
