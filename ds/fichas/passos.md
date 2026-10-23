# Passos

`Steps` · itens lidos em fila, cada um com uma marca, um nome e um parágrafo. Em ordem quando a ordem importa, lado a lado quando acontecem juntos.

## Use quando

- **Etapas em ordem, com texto em cada uma.** A sequência é o assunto, e o leitor precisa ver o caminho inteiro. Use o padrão.
- **Duas coisas que acontecem ao mesmo tempo.** Dois canais, dois públicos, duas frentes, sem uma vir depois da outra. Use `par`.

## Não use quando

- O leitor precisa passar os olhos por vários itens e escolher um, sem ordem. Use Cartões em mosaico.
- Cada item é longo e se lê um de cada vez. Use Abas.
- São duas coisas para comparar ponto a ponto, ou a mesma coisa antes e depois. Use Antes e depois.
- A etapa é uma linha só. Use uma lista no texto corrido.
- Há entrada, meio e saída, e o meio é o que importa. Espere a variante `estagios`, que dá peso ao meio, em vez de forçar o padrão.

## Anatomia

1. Caixa, obrigatória. `ol.steps` no padrão, porque a ordem é conteúdo. `ul.steps` no `par`, porque não há ordem.
2. Item, `li.step`, um por etapa.
3. Marca, obrigatória. No padrão é o número num círculo de traço com fundo do acento, `span.step__num` com `aria-hidden`, já que a lista numerada diz a posição. No `par` é o ícone adesivo do item, `img.step__icone`, porque um número diria que um vem antes do outro.
4. Nome, `h3.step__titulo`, obrigatório. No degrau `lead`, em negrito.
5. Texto, um `p`, obrigatório. Um parágrafo por item.

## Variantes

| `data-layout` | Como fica | Quando |
| --- | --- | --- |
| sem atributo | Um item debaixo do outro, com o número à esquerda | Etapas em ordem |
| `par` | Dois itens lado a lado a partir de 720px, com o ícone à esquerda. No celular, um debaixo do outro | Duas coisas ao mesmo tempo |

Previstas para a Fase 5, escritas aqui antes de existir no código.

| `data-layout` | Quando |
| --- | --- |
| `estagios` | Entrada, o que acontece no meio e saída, com o meio maior |
| `funil` | Cada etapa filtra a anterior, e a largura mostra o estreitamento |
| `trilha` | Um caminho curto de três marcos |
| `ritos` | Ritos de time e o que mudou em cada um |

O acento só aparece no fundo do número e no ícone. Na superfície tinta o traço do círculo e o texto viram papel, e o fundo do acento continua com o número em tinta.

## Limites

- No padrão, de três a seis passos. Dois são `par` ou Antes e depois, e sete ou mais pedem duas Seções.
- No `par`, exatamente dois itens. Três coisas ao mesmo tempo são Cartões em mosaico.
- Nome de até duas linhas no `par` em 720px.
- Texto de até cinco linhas por item no desktop. Passou disso, o item pede Abas.
- Um conjunto de Passos por Seção.

## Comportamento

1. **Mouse.** Não tem. Passos não é alvo.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** O conjunto inteiro leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- O leitor de tela anuncia a lista e o número de itens. No padrão a posição vem da `ol`, e por isso o círculo é escondido. No `par` a `ul` não sugere ordem.
- Cada item tem o seu `h3`, e quem navega por títulos acha cada um.
- O ícone é decorativo. O nome já diz o que é.
- Tinta sobre o acento no número passa com folga em qualquer acento.

## Onde aparece

- O modelo de Caso não usa Passos. As duas origens do Problema ficam em Cartões `meio`.
- Primeira prova, `ds/prova/omnichat.html`, as mesmas origens em `par`, ainda com número.
- Nas páginas publicadas, as Linhas indexadas, os Estágios, os Ritos, o Funil e a Trilha dos quatro casos (ver `ds/INVENTARIO.md`). Entram com as variantes previstas.

## Vizinhos

- **Cartões em mosaico.** Vários itens sem ordem, para escolher qual ler.
- **Abas.** Itens longos, um de cada vez.
- **Antes e depois.** Dois lados que se comparam, não que acontecem juntos.

## Par nos posts

Passos, a proposta de sequência numerada com o número em Anton num disco de acento. Lá os discos alternam lime, azul e verde. Aqui todos levam o acento do caso, porque a página usa um acento só (regra 7 do `ds/RITMO.md`). O `par` conversa com a Lista dos posts, em que cada item tem o seu ícone adesivo.

## Código

```html
<!-- Em ordem -->
<ol class="steps" data-revelar>
  <li class="step">
    <span class="step__num" aria-hidden="true">1</span>
    <h3 class="step__titulo">Nome da etapa</h3>
    <p>…</p>
  </li>
</ol>

<!-- Par -->
<ul class="steps" data-layout="par" data-revelar>
  <li class="step">
    <img class="icone step__icone" src="assets/ds/icones/celular-azul.svg" alt="" width="44" height="44">
    <h3 class="step__titulo">Instagram</h3>
    <p>Chegavam com um objetivo implícito, moldado pelo anúncio que&nbsp;clicaram…</p>
  </li>
  <li class="step">
    <img class="icone step__icone" src="assets/ds/icones/megafone-azul.svg" alt="" width="44" height="44">
    <h3 class="step__titulo">Disparos de&nbsp;WhatsApp</h3>
    <p>Chegavam ainda mais comprimidos…</p>
  </li>
</ul>
```

Estilo em `assets/ds/componentes.css`, seção Steps (`.steps`, `.step`), e as duas colunas do `par` no bloco de 720px. Não tem script além do revelar.

**O que falta no código.** Nada para o `par` com ícone, que o CSS já aceita (`.step__icone`). As quatro variantes previstas entram na Fase 5.
