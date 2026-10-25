# Seção

`Section` · a moldura de cada parte numerada do caso, com rótulo, título, texto e uma peça, numa coluna só ao lado do Sumário.

## Use quando

O caso tem uma parte que o Sumário lista. Cada parte numerada, do Contexto ao Resultado, é uma Seção, e o nome dela é o mesmo do Sumário.

## Não use quando

- É o Topo do caso. Ele é receita, com o mosaico próprio, e não entra no Sumário (ver `ds/RECEITAS.md`).
- É um trecho dentro de uma parte que pede subtítulo. Use o `h3` da peça (Cartão, Passos, Antes e depois). Seção não se aninha.
- A parte tem mais de três parágrafos antes da peça. São duas Seções (regra 5 do `ds/RITMO.md`).
- A página não tem Sumário, como a Home. O Hero e a Lista de casos são receitas, não Seções.
- É o convite e o Botão do fim. O fechamento mora dentro do Resultado e não vira uma Seção a mais.

## Anatomia

1. Caixa, `section.section`, obrigatória. Leva o `id` que o Sumário aponta e `aria-labelledby`.
2. Rótulo, obrigatório. `p.section__rotulo.t-rotulo`, com número e nome separados por ponto do meio ("02 · O problema") e a régua de 2px que corre até a borda.
3. Título, `h2.t-titulo`, obrigatório em toda Seção menos no Contexto. Diz o que a parte descobriu, não o nome da parte.
4. Texto, opcional. Uma `div.prosa` com até três parágrafos. No Contexto é um `p.t-lead.prosa` só, e é ele a Seção inteira.
5. Peça, opcional. Uma só, escolhida pelo `ds/GUIA.md`, sempre depois do texto.

As partes são filhas diretas da `section`, sem embrulho. O espaço entre elas é `space-24`, e entre uma Seção e a seguinte é `space-64`.

## Variantes

Uma forma só. A `lado` sai. Ela punha o rótulo e o título em quatro colunas à esquerda, e no caso essa coluna já é do Sumário. Nenhuma outra página tem Seção.

O Contexto não é variante. É a Seção sem título e sem peça, rotulada pelo próprio rótulo.

A Seção não vai para a superfície tinta. A parada de tinta da página é o Destaque do Resultado, que mora dentro da Seção.

## Limites

- De quatro a oito Seções por caso, contando Contexto e Resultado (regra 12 do `ds/RITMO.md`).
- Até três parágrafos antes da peça.
- Uma peça por Seção. A exceção é o Resultado, que leva o Dado em grupo, o Destaque na tinta e o fechamento, nessa ordem.
- Título de até três linhas em 390px.
- Texto corrido na medida de leitura (`leitura`, 66ch). A peça pode usar a largura inteira da coluna.

## Comportamento

1. **Mouse.** Não tem. A Seção não é alvo.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco. Quem chega pelo Sumário cai no começo da Seção, e o próximo Tab segue a ordem do conteúdo.
4. **Movimento.** Cada filho abaixo da dobra leva `data-revelar` e entra sozinho, subindo 16px em `dur-lenta` com `ease-saida`. Assim o rótulo, o título, o texto e a peça chegam na ordem em que a rolagem os encontra. A chegada pelo Sumário rola até a Seção com rolagem suave, e o `scroll-padding-top` deixa o rótulo abaixo do cabeçalho.
5. **Sem JS.** Tudo aparece pronto. O link do Sumário pula direto para a Seção.
6. **Movimento reduzido.** O revelar não existe e a rolagem até a Seção é instantânea.

## Acessibilidade

- `aria-labelledby` aponta para o `id` do `h2`. No Contexto, que não tem título, aponta para o rótulo.
- O rótulo é parágrafo, não título. Quem navega por títulos ouve o `h1` do Topo e um `h2` por Seção, e os `h3` ficam dentro das peças.
- O ponto do meio do rótulo é lido como pausa. O número e o nome chegam juntos ("zero dois, O problema").
- Tinta sobre papel em todo texto, com folga.

## Onde aparece

- Modelo de Caso, cinco Seções. "01 · Contexto", só o parágrafo em `t-lead`. "02 · O problema", com o título "Ninguém tinha desenhado a fronteira de entrada". "03 · Processo", "04 · Antes e depois" e "05 · Resultado".
- Nas páginas publicadas dos quatro casos, geradas com o modelo.
- Nas páginas publicadas, a Seção e o Cabeçalho de seção dos quatro casos (ver `ds/INVENTARIO.md`).

## Vizinhos

- **Topo do caso.** Abre a página, sem número e fora do Sumário.
- **Cartão.** Moldura de um bloco dentro da Seção, nunca da Seção inteira.
- **Destaque na tinta.** Fica dentro do Resultado. Não é uma Seção na tinta.

## Par nos posts

Sem par como peça. No carrossel a página inteira é a seção, e o campo `secao` do rodapé esquerdo faz o trabalho do rótulo, dizendo onde o leitor está.

## Código

```html
<!-- Seção do meio -->
<section class="section" id="problema" aria-labelledby="problema-titulo">
  <p class="section__rotulo t-rotulo" data-revelar>02 · O problema</p>
  <h2 class="t-titulo" id="problema-titulo" data-revelar>Ninguém tinha desenhado a&nbsp;fronteira de&nbsp;entrada</h2>
  <div class="prosa" data-revelar>
    <p>Não existia visão clara da jornada conversacional…</p>
  </div>
  <div class="cards" data-layout="mosaico" data-revelar>…</div>
</section>

<!-- Contexto -->
<section class="section" id="contexto" aria-labelledby="contexto-rotulo">
  <p class="section__rotulo t-rotulo" id="contexto-rotulo">01 · Contexto</p>
  <p class="t-lead prosa">…</p>
</section>
```

Estilo em `assets/ds/componentes.css`, seção Section. Não tem script além do revelar e do Sumário, que marca a Seção da vez pelo `id`.

**O que falta no código.**

- Nada para o uso atual. A `.section` já é a forma do modelo (a `.bloco-sec` da variação 4), e a `lado` saiu do CSS.
- A primeira prova, `ds/prova/omnichat.html`, foi escrita com a forma antiga e mudou de cara. Fica como registro.
