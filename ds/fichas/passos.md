# Passos

`Steps` · itens lidos em fila, cada um num Cartão com o ícone adesivo no canto. A forma diz como eles se ligam, em ordem, ao mesmo tempo, de uma entrada a uma saída, filtrando, num caminho ou lado a lado sem ordem.

## Use quando

- **Etapas em ordem, com texto em cada uma.** A sequência é o assunto, e o leitor precisa ver o caminho inteiro. Use a sequência, sem atributo.
- **Duas coisas que acontecem ao mesmo tempo.** Dois canais, dois públicos, duas frentes, sem uma vir depois da outra. Use `par`.
- **Entrada, o que acontece no meio e saída.** O meio é o que a Seção explica. Use `estagios`.
- **Etapas em que cada uma filtra a anterior.** O que entra na primeira é mais do que sai na última. Use `funil`.
- **Um caminho curto, de três marcos.** Cada marco é um nome e uma linha, e o que importa é a direção. Use `trilha`.
- **Ritos de time e o que mudou em cada um.** Três encontros sem ordem entre eles, cada um com o nome e a mudança numa linha. Use `ritos`.

## Não use quando

- O leitor precisa passar os olhos por vários itens e escolher um, sem ordem e sem ser rito. Use Cartões em mosaico.
- Cada item é longo e se lê um de cada vez. Use Abas. Elas também podem vir logo depois dos `estagios`, com o detalhe de cada entrega.
- São duas coisas para comparar ponto a ponto, ou a mesma coisa antes e depois. Use Antes e depois.
- A etapa é uma linha só e não há direção nem filtro. Use uma lista no texto corrido.
- São as categorias de uma legenda, como os níveis de reação de uma pesquisa. Use o Gráfico que elas explicam.

## Anatomia

1. Caixa, obrigatória. `ol.steps` quando a ordem é conteúdo (sequência, `estagios`, `funil`, `trilha`). `ul.steps` quando não há ordem (`par`, `ritos`).
2. Cartão, `li.step`, um por etapa. Contorno de 2px, raio e fundo `background`.
3. Ícone adesivo, `img.icone.step__icone`, obrigatório. Sobre o canto de cima, à esquerda, em 64px, com metade para fora do Cartão. Nos `ritos` ele desce para a faixa do topo, em 40px.
4. Número, `span.step__num` com `aria-hidden`, nas formas em ordem. Em Anton vazado, só o contorno, no canto de cima à direita. No `par` e nos `ritos` não entra, porque diria que um vem antes do outro.
5. Rótulo do estágio, `span.t-rotulo`, só nos `estagios` ("Entrada", "Camada", "Saída").
6. Nome, `h3.step__titulo`, obrigatório. No degrau `lead`, em negrito. Nos `ritos`, em Anton caixa alta, dentro da faixa do topo (`div.step__topo`).
7. Texto, `p`, obrigatório, menos na saída dos `estagios`. Um parágrafo, dois no máximo.
8. Lista, `ul.step__lista`, opcional. Itens separados por fios, como as entregas da saída dos `estagios`. Fios em vez de Etiquetas, porque um nome longo não cabe numa pílula de um terço.
9. Efeito, `p.step__efeito`, opcional. Um rótulo e uma frase no fundo `muted`, como o efeito do Cartão. Diz a consequência da etapa ou quem conduz. Não entra na `trilha` nem nos `ritos`.

## Variantes

| `data-layout` | Como fica | Quando |
| --- | --- | --- |
| sem atributo | Cartões com número. Três lado a lado com 900px de Seção, um embaixo do outro antes disso | Etapas em ordem |
| `par` | Dois Cartões sem número, lado a lado com 600px de Seção | Duas coisas ao mesmo tempo |
| `estagios` | Três Cartões com o rótulo do estágio e uma seta de tinta entre eles. O do meio é mais largo e fica no acento. Com 900px de Seção ficam em fila e a seta aponta para o lado. Antes disso descem em coluna e a seta aponta para baixo | Entrada, meio e saída |
| `funil` | Cartões centrados, um embaixo do outro, cada um 9% mais estreito que o anterior pelo índice `--i` | Cada etapa filtra a anterior |
| `trilha` | Cartões com número ligados por um fio tracejado, que aparece só entre eles. Em fila com 900px de Seção, fio na horizontal. Em coluna antes disso, fio na vertical passando pelos adesivos | Um caminho curto |
| `ritos` | Folhas de agenda. A faixa do topo no acento com o ícone e o nome em Anton, e a linha embaixo. Três lado a lado com 600px de Seção | Ritos de time |

O arranjo segue a largura da Seção, não a da tela. A Seção é um container (`container-type: inline-size`), e as regras usam `@container`. A partir de 1100px o Sumário ocupa a coluna da esquerda, e a Seção volta a ter uns 750px, quase a largura do tablet. Com regra de tela, os três Cartões ficariam espremidos em 1100 e em 1280.

Pelo `ds/RITMO.md`, todas as formas são médias, caixa no papel com ícone.

O estágio do meio era tinta no site de hoje. A tinta da página é uma só (D4), a do Resultado, e por isso ele passa para o acento.

O acento só aparece no fundo do estágio do meio, na faixa dos `ritos` e no corpo dos adesivos, sempre com tinta por cima. Contorno, número, seta e fio são tinta. Na superfície tinta, contorno, número, seta e fio viram papel.

## Limites

- Sequência, três ou seis etapas, para a fila de três fechar sem Cartão sozinho na última linha. Quatro ou cinco pedem outra forma ou duas Seções.
- `par`, exatamente dois.
- `estagios`, exatamente três, e só o do meio leva o acento.
- `funil`, de três a seis etapas.
- `trilha` e `ritos`, exatamente três.
- Nome de até duas linhas no Cartão de um terço. Nos `ritos`, uma palavra ou duas.
- Texto de até seis linhas no Cartão de um terço. Passou disso, o item pede Abas.
- Efeito de até três linhas.
- Lista da saída de até seis itens.
- Um conjunto de Passos por Seção.

## Comportamento

1. **Mouse.** Não tem. Passos não é alvo. As Abas que vêm depois dos `estagios` seguem a ficha das Abas.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** O conjunto inteiro leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. Os Cartões entram juntos, sem cascata.
5. **Sem JS.** Aparece pronto. O arranjo é só CSS.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- O leitor de tela anuncia a lista e o número de itens. Nas formas em ordem a posição vem da `ol`, e por isso o número vazado fica escondido. No `par` e nos `ritos` a `ul` não sugere ordem.
- Cada item tem o seu `h3`, e quem navega por títulos acha cada um.
- O ícone adesivo tem `alt` vazio. O nome já diz o que é.
- A seta dos `estagios`, o fio da `trilha` e o estreitamento do `funil` são desenhados pelo CSS e não são lidos. A ordem vem da lista, e o filtro do funil precisa estar no texto de cada etapa.
- O rótulo dos `estagios` é texto de verdade, lido antes do nome.
- Tinta sobre papel, sobre `muted` e sobre o acento passam com folga.

## Onde aparece

- O modelo de Caso não usa Passos. As duas origens do Problema ficam em Cartões `meio`.
- Vitrine, na amostra e no palco do Passos, com o texto do Mapa e do Processo com IA.
- Sequência com efeito, nas Linhas indexadas do Mapa, Seção 03. "Entender os dados do NPS", com a consequência "A insatisfação deixou de ser uma nota única e passou a ter lugar e momento na jornada."
- `par`, nas Linhas do Problema do Processo, Seção 02. "O trabalho vivia em reunião" e "A garantia prévia custava semanas".
- `estagios`, no Processo, Seção 03. "Transcrição dos rituais" na entrada, "Habilidades no Claude" na camada e as cinco entregas na saída, com as Abas logo depois.
- `funil`, no Processo, Seção 06. As cinco fases, de "Identificação de oportunidades" a "Depois do lançamento", cada uma com o efeito "Quem conduz".
- `trilha`, no Processo, Seção 07. "Criação", "Comportamento e uso" e "Aprovação no código".
- `ritos`, no Processo, Seção 04. "Planning", "Daily" e "Refinamento".
- Os três níveis de desejabilidade do Inpulse ("Entusiasta", "Receptivo" e "Indiferente") usam a forma dos ritos no site de hoje, mas são a legenda das pilhas logo abaixo. Vão para o Gráfico `pilhas`, na Onda 4.
- A primeira prova (`ds/prova/omnichat.html`) e as variações 1 e 3 usam o `par` e aparecem com os Cartões. Ficam como registro.

## Vizinhos

- **Cartões em mosaico.** Vários itens sem ordem, para escolher qual ler.
- **Abas.** Itens longos, um de cada vez. Também detalham as entregas depois dos `estagios`.
- **Antes e depois.** Dois lados que se comparam, não que acontecem juntos.
- **Gráfico `barras`.** Quando o que estreita é um número, e não uma etapa.

## Par nos posts

Passos, a proposta de sequência numerada com o número em Anton num disco de acento. Lá os discos alternam lime, azul e verde. Aqui todos os adesivos levam o acento do caso, porque a página usa um acento só (regra 7 do `ds/RITMO.md`). O `par` conversa com a Lista dos posts, em que cada item tem o seu ícone adesivo. As outras formas não têm par, porque o post não tem espaço para cinco etapas com texto.

## Código

```html
<!-- Sequência, com efeito -->
<ol class="steps" data-revelar>
  <li class="step">
    <img class="icone step__icone" src="assets/ds/icones/grafico-azul.svg" alt="" width="64" height="64">
    <span class="step__num" aria-hidden="true">01</span>
    <h3 class="step__titulo">Entender os&nbsp;dados do&nbsp;NPS</h3>
    <p>Clusterizamos os comentários do NPS em grandes eixos e subcategorias…</p>
    <p class="step__efeito"><span class="t-rotulo">Consequência</span> A insatisfação deixou de ser uma nota única…</p>
  </li>
</ol>

<!-- Par: sem número -->
<ul class="steps" data-layout="par" data-revelar>
  <li class="step">
    <img class="icone step__icone" src="assets/ds/icones/dialogo-lime.svg" alt="" width="64" height="64">
    <h3 class="step__titulo">O&nbsp;trabalho vivia em&nbsp;reunião</h3>
    <p>A gente discutia bem e decidia bem…</p>
  </li>
  <li class="step">…</li>
</ul>

<!-- Estágios: o rótulo antes do nome, e a lista na saída -->
<ol class="steps" data-layout="estagios" data-revelar>
  <li class="step">
    <img class="icone step__icone" src="assets/ds/icones/dialogo-lime.svg" alt="" width="64" height="64">
    <span class="t-rotulo">Entrada</span>
    <h3 class="step__titulo">Transcrição dos rituais</h3>
    <p>O que o time já falava em reunião…</p>
  </li>
  <li class="step">…</li>
  <li class="step">
    <img class="icone step__icone" src="assets/ds/icones/janela-lime.svg" alt="" width="64" height="64">
    <span class="t-rotulo">Saída</span>
    <h3 class="step__titulo">…</h3>
    <ul class="step__lista"><li>Visão de produto</li><li>PRD</li>…</ul>
  </li>
</ol>

<!-- Funil: o índice --i estreita cada Cartão -->
<ol class="steps" data-layout="funil" data-revelar>
  <li class="step" style="--i: 0">…</li>
  <li class="step" style="--i: 1">…</li>
</ol>

<!-- Ritos: a faixa do topo com o ícone e o nome -->
<ul class="steps" data-layout="ritos" data-revelar>
  <li class="step">
    <div class="step__topo">
      <img class="icone step__icone" src="assets/ds/icones/calendario-lime.svg" alt="" width="40" height="40">
      <h3 class="step__titulo">Planning</h3>
    </div>
    <p>Virou assíncrona e sob&nbsp;demanda, não&nbsp;mais um rito&nbsp;semanal.</p>
  </li>
</ul>
```

Estilo em `assets/ds/componentes.css`, seção Steps. A seta dos `estagios` é uma máscara SVG pintada com `foreground`, e o fio da `trilha` é um tracejado em `border`. Não tem script além do revelar.

A forma saiu da direção 3, Adesivos, do estudo em `ds/vitrine/estudo/`, escolhida por você na Onda 3.
