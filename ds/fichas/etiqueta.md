# Etiqueta

`Badge` · uma palavra ou um nome curto numa pílula com contorno de tinta. Nomeia, não age.

## Use quando

- **O assunto do caso.** No Topo, duas a quatro Etiquetas dizem de que o caso trata. A última leva o acento.
- **O estado de um lado.** No Antes e depois, uma Etiqueta na tinta diz como aquela versão terminou ("Conversa abandonada", "Lead convertido").
- **O rótulo de um bloco na tinta.** No Destaque do Resultado, uma Etiqueta do acento diz o que a frase é ("O que eu levo daqui").

## Não use quando

- Leva a algum lugar. Use Link, ou Botão se for a ação principal.
- São os dados do projeto, como duração e time. Use o Cartão `muted` com a ficha.
- É o número ou o nome de uma Seção. Use o rótulo da Seção, que já é `t-rotulo` com a régua.
- É um filtro que liga e desliga. A Etiqueta não tem estado. Um filtro pede uma ficha nova antes do código.
- É uma frase. Etiqueta é nome, e frase é Destaque ou texto.

## Anatomia

1. Grupo, `ul.badges` com `role="list"`, quando há mais de uma. Uma fileira que quebra linha, com `space-8` entre elas, e um `li` por Etiqueta.
2. Etiqueta, `span.badge`, obrigatória. Texto em caixa alta no degrau `rotulo`, numa pílula com contorno de 2px.
3. Ícone, opcional. Um ícone adesivo pequeno (`icone-inline`) antes do texto, quando ele ajuda a ler o estado. No Antes e depois, o xis no Antes e o visto no Depois (ícones `xis` e `check`).

## Variantes

| `data-variant` | Como fica | Quando |
| --- | --- | --- |
| sem atributo | Fundo `background`, texto e contorno em `foreground` | O padrão. Assuntos e nomes de lado |
| `acento` | Fundo `acento`, texto em tinta | Uma por grupo, a que mais importa. A última do Topo, o rótulo do Destaque |
| `tinta` | Fundo tinta, texto em papel | Um estado que encerra algo, sobre o papel ou sobre o acento |

Na superfície tinta a Etiqueta sem atributo fica com fundo tinta, texto e contorno em papel, porque troca por dentro. A `tinta` some sobre a tinta e não entra ali. Use a `acento`.

## Limites

- De duas a quatro Etiquetas no Topo. Uma só não é grupo, e cinco viram uma lista.
- Uma `acento` por grupo.
- Texto de até três palavras e uma linha em 390px. A Etiqueta não quebra linha por dentro.
- Sem Etiqueta solta no meio do texto corrido.

## Comportamento

1. **Mouse.** Não tem. A Etiqueta não é alvo.
2. **Toque.** Não tem, pelo mesmo motivo.
3. **Foco.** Não recebe foco.
4. **Movimento.** Entra com o bloco em que mora, pelo revelar da página. Nenhum movimento próprio.
5. **Sem JS.** Aparece pronta.
6. **Movimento reduzido.** Aparece pronta.

## Acessibilidade

- O grupo é uma lista, e o leitor de tela anuncia quantas Etiquetas há e lê uma de cada vez.
- A caixa alta vem do CSS. No HTML o texto é escrito normal ("Agentes conversacionais"), para o leitor de tela não soletrar.
- O ícone dentro da Etiqueta tem `alt` vazio. O texto já diz o estado.
- Tinta sobre papel, tinta sobre o acento e papel sobre tinta passam com folga.
- A cor da `acento` não carrega sentido sozinha. O que ela marca também está no texto.

## Onde aparece

- Modelo de Caso, Topo. "Omnichat", "Agentic Experience" e "Agentes conversacionais", a última no acento.
- Modelo de Caso, Antes e depois. "Antes" com o xis e "Conversa abandonada" na tinta. "Depois" com o visto e "Lead convertido" na tinta.
- Modelo de Caso, Destaque do Resultado. "O que eu levo daqui" no acento, sobre a tinta.
- Nas páginas publicadas, as Etiquetas de assunto (`.etiquetas`) dos quatro casos. "AX", "Processo de produto e design" e "IA no fluxo de trabalho" no Processo. "UX Research", "UX Strategy" e "Pesquisa e NPS" no Mapa.

## Vizinhos

- **Botão.** A mesma pílula, mas age.
- **Rótulo da Seção.** Nomeia a parte da página, com número e régua, sem pílula.
- **Cartão `muted` com a ficha.** Os dados do projeto, que são valores e não assuntos.

## Par nos posts

TagCard, a tag em pílula com o acento. No post a tag tem 19px de canvas, abaixo do mínimo de rótulo, e a proposta é subir para 23px. No site o degrau `rotulo` já é o mínimo (12px).

## Código

```html
<!-- Assuntos, no Topo -->
<ul class="badges" role="list">
  <li><span class="badge">Omnichat</span></li>
  <li><span class="badge">Agentic Experience</span></li>
  <li><span class="badge" data-variant="acento">Agentes conversacionais</span></li>
</ul>

<!-- Estado de um lado, com ícone -->
<p class="compare__cabeca">
  <span class="badge"><img class="icone-inline" src="assets/ds/icones/check-azul.svg" alt="" width="20" height="20">Depois</span>
  <span class="badge" data-variant="tinta">Lead convertido</span>
</p>
```

Estilo em `assets/ds/componentes.css`, seção Badge (`.badges`, `.badge`). Não tem script.

O grupo era um parágrafo, e o leitor de tela lia as três Etiquetas emendadas, sem pausa. Na Onda 2 virou lista, lida item a item. O `role="list"` devolve a lista ao Safari, que a esquece quando os marcadores somem, e cada `li` é uma caixa flex para a linha do texto em volta não esticar a Etiqueta. A tela não mudou.
