# Antes e depois

`Compare` · a mesma coisa em dois momentos, lado a lado, para o leitor ver o que mudou sem precisar lembrar do primeiro lado enquanto lê o segundo.

## Use quando

- **A mesma coisa antes e depois, numa dimensão só.** Um fluxo, uma regra, um jeito de trabalhar, contado em dois parágrafos que se espelham. Use a forma de lados, sem atributo.
- **A mesma interação antes e depois da solução.** Uma conversa, com as falas na ordem em que aconteceram. Use lados com os turnos de fala dentro, a conversa.
- **A fala de quem usou, antes e depois.** Duas citações com autoria, uma de cada momento. Use `citacao`.
- **Uma mudança em várias dimensões ao mesmo tempo.** Três a seis aspectos, cada um com o antes e o depois numa linha. Use `confronto`.

## Não use quando

- O que mudou é um número. Use Dado `salto`, ou Gráfico `barras` quando a proporção importa.
- São duas coisas que acontecem ao mesmo tempo, sem uma substituir a outra. Use Passos `par`.
- É uma frase do caso, na voz do Jeff. Use Destaque, porque a `citacao` é a voz de quem usou.
- Só um dos lados tem conteúdo de verdade, e o outro existe para fazer par. Deixe no texto.
- São mais de dois momentos. Use Passos, que mostra a sequência inteira.

## Anatomia

**Lados, conversa e citação.**

1. Caixa, `div.compare`, obrigatória.
2. Lado, `div.card.compare__lado`, dois, obrigatórios. O antes com `data-variant="muted"` e o depois com `data-variant="acento"`.
3. Cabeça, `p.compare__cabeca`, obrigatória. Uma Etiqueta com o ícone e o nome do momento ("Antes" com o xis, "Depois" com o visto) e, opcional, uma Etiqueta `tinta` com o desfecho ("Conversa abandonada").
4. Conteúdo, obrigatório, um dos três.
   - Lados, um `p` ou uma `div.prosa`.
   - Conversa, `ol.turnos`, com um `li.turno` por fala, o rótulo de quem fala, a fala em `p.turno__fala` e, opcional, a nota da camada em `span.turno__nota`.
   - Citação, `figure.compare__citacao`, com a fala em `blockquote` e a autoria em `figcaption`.
5. Legenda, `p.t-apoio`, opcional, antes do Antes e depois. Diz se a conversa é ilustrativa ou de onde vieram as falas.

**Confronto.**

1. Caixa, `table.compare` com `data-variant="confronto"`, obrigatória, com uma `caption` que nomeia a tabela para o leitor de tela (pode ficar escondida da tela com `sr`).
2. Cabeça, `thead`, obrigatória. Três colunas, "Dimensão" em rótulo e "Antes" e "Depois" em Etiquetas sem atributo. A do depois já senta na faixa do acento, e por isso não leva a `acento`.
3. Linha, `tr`, uma por dimensão. A dimensão em `th scope="row"`, no degrau `lead` em negrito, e o antes e o depois em `td`.

## Variantes

| Forma | Como se escreve | Quando |
| --- | --- | --- |
| Lados | `.compare`, texto em cada lado | Uma dimensão, em dois parágrafos |
| Conversa | `.compare`, `ol.turnos` em cada lado | A mesma interação, fala a fala |
| `citacao` | `.compare` com `data-variant="citacao"` | A fala de quem usou, antes e depois |
| `confronto` | `table.compare` com `data-variant="confronto"` | Várias dimensões de uma vez |

Lados, conversa e citação são a mesma caixa com conteúdos diferentes. Lado a lado a partir de 720px, um debaixo do outro no celular, o antes no `muted` e o depois no acento. A diferença se lê pelo rótulo e pelo fundo, nunca só pelo fundo.

Na `citacao` a fala vem em Fraunces 300, no degrau `lead`, a voz de conversa do sistema. O Anton fica para a voz do caso, no Destaque. A autoria vem no degrau `apoio`, sem nome quando a pessoa não autorizou ("Aluna do 5º semestre de medicina"). As aspas são as do texto, sem aspa desenhada.

O `confronto` é uma tabela de verdade. A partir de 720px, três colunas, a dimensão num quarto e o antes e o depois dividindo o resto, com uma régua de 2px em `border` em cima e entre as linhas. A coluna do depois ganha o fundo do acento, de cima a baixo, e é o lado que a página defende. No celular cada linha vira um bloco, com a dimensão em cima e o antes e o depois embaixo, cada um com o seu rótulo (`span.compare__marca`). O depois vira uma caixa do acento com raio, e a cabeça sai da tela mas continua para o leitor de tela.

Pelo `ds/RITMO.md`, as quatro formas são médias.

Na superfície tinta não entra. A tinta da página é a do Resultado, e o Antes e depois mora no meio do caso.

## Limites

- Exatamente dois lados. Três momentos são Passos.
- Lados, até dois parágrafos de cada lado.
- Conversa, de três a oito falas de cada lado. Fala de até três linhas na largura do balão (`34ch`).
- `citacao`, uma fala de cada lado, de até quatro linhas no desktop, sempre com autoria.
- `confronto`, de três a seis dimensões. Dimensão de até três palavras. Antes e depois de até duas linhas cada no desktop.
- Um Antes e depois por Seção.

## Comportamento

1. **Mouse.** Não tem. O Antes e depois não é alvo.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** A caixa inteira leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. Os dois lados entram juntos, para nenhum parecer mais importante pela ordem.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- Cada lado começa pelo nome do momento, em texto. Quem ouve sabe qual lado é antes de ouvir o conteúdo.
- Os turnos da conversa são uma lista numerada, e cada fala diz quem fala.
- A `citacao` usa `figure`, `blockquote` e `figcaption`, e o leitor de tela liga a fala à autoria.
- O `confronto` é uma `table` com `caption`, `th` de coluna e `th scope="row"`. No celular, onde as linhas viram blocos, os papéis de tabela vão escritos no HTML (`role="table"`, `row`, `columnheader`, `rowheader`, `cell`), porque o Safari esquece a tabela quando o CSS troca a forma dela. Os rótulos "Antes" e "Depois" de cada célula no celular ficam escondidos do leitor de tela, que já ouve a coluna.
- Os ícones das Etiquetas têm `alt` vazio. O texto diz o momento.
- Tinta sobre o `muted` e tinta sobre o acento passam com folga.

## Onde aparece

- Modelo de Caso, Seção 04, a conversa. "O mesmo lead de Instagram, nas duas versões da fronteira de entrada", com "Conversa abandonada" de um lado e "Lead convertido" do outro, e a legenda "Conversa ilustrativa."
- Vitrine, na amostra e no palco do Antes e depois, com a citação do Inpulse, a conversa do Omnichat e o confronto do Processo.
- Nas páginas publicadas, o Confronto do Processo, Seção 08. "O mesmo time, com o eixo do trabalho deslocado", em quatro dimensões, "Prototipação", "Validação qualitativa", "Rituais" e "Testes A/B".
- A Citação do Inpulse, na Seção 01. "O que o aluno dizia", com a nota 2 no NPS de uma estudante do 3º semestre antes e a aluna do 5º semestre depois.

## Vizinhos

- **Dado `salto`.** Quando o que mudou é um número, com o valor de antes.
- **Passos `par`.** Duas coisas ao mesmo tempo, sem substituição.
- **Destaque.** A frase do caso, na voz do Jeff.
- **Gráfico `barras`.** Uma grandeza antes e depois, em que a proporção importa.

## Par nos posts

AntesDepois, os dois cards lado a lado com o antes no mist e o depois no acento, para os lados e a conversa. Citacao, a fala grande com autoria, para a `citacao`. O `confronto` não tem par, porque a tabela não cabe no canvas com texto legível.

## Código

```html
<!-- Conversa -->
<div class="compare" data-revelar>
  <div class="card compare__lado" data-variant="muted">
    <p class="compare__cabeca"><span class="badge"><img class="icone-inline" src="assets/ds/icones/xis-azul.svg" alt="" width="20" height="20">Antes</span><span class="badge" data-variant="tinta">Conversa abandonada</span></p>
    <ol class="turnos">…</ol>
  </div>
  <div class="card compare__lado" data-variant="acento">
    <p class="compare__cabeca"><span class="badge"><img class="icone-inline" src="assets/ds/icones/check-azul.svg" alt="" width="20" height="20">Depois</span><span class="badge" data-variant="tinta">Lead convertido</span></p>
    <ol class="turnos">…</ol>
  </div>
</div>

<!-- Citação -->
<div class="compare" data-variant="citacao" data-revelar>
  <div class="card compare__lado" data-variant="muted">
    <p class="compare__cabeca"><span class="badge"><img class="icone-inline" src="assets/ds/icones/xis-verde.svg" alt="" width="20" height="20">Antes</span></p>
    <figure class="compare__citacao">
      <blockquote><p>“Precisamos correr atrás de&nbsp;nota, elas levam dias para&nbsp;sair…”</p></blockquote>
      <figcaption>Nota 2 no NPS, de uma estudante no 3º semestre.</figcaption>
    </figure>
  </div>
  <div class="card compare__lado" data-variant="acento">…</div>
</div>

<!-- Confronto -->
<table class="compare" data-variant="confronto" role="table" data-revelar>
  <caption class="sr">O trabalho do time antes e depois, em quatro dimensões</caption>
  <thead>
    <tr role="row">
      <th role="columnheader" scope="col"><span class="t-rotulo">Dimensão</span></th>
      <th role="columnheader" scope="col"><span class="badge">Antes</span></th>
      <th role="columnheader" scope="col"><span class="badge">Depois</span></th>
    </tr>
  </thead>
  <tbody>
    <tr role="row">
      <th role="rowheader" scope="row">Prototipação</th>
      <td role="cell"><span class="t-rotulo compare__marca" aria-hidden="true">Antes</span>Concentrada em design</td>
      <td role="cell"><span class="t-rotulo compare__marca" aria-hidden="true">Depois</span>Distribuída entre produto, design e engenharia</td>
    </tr>
  </tbody>
</table>
```

Estilo em `assets/ds/componentes.css`, seção Antes e depois (`.compare`, `.turnos`, `.compare__citacao` e o bloco do `confronto`). Não tem script além do revelar.

A `citacao` e o `confronto` entraram na Onda 3 e foram aprovados por você na vitrine, como estão.
