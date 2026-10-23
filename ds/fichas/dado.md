# Dado

`Stat` · um número em Anton com a frase que diz do que ele é, sozinho, com o valor de antes ou em grupo.

## Use quando

- **Um número prova o caso.** É o resultado que justifica ler a página, e ele tem um antes. Use a variante `salto` no Topo do caso.
- **Alguns números fecham a conta.** Dois ou quatro números do mesmo resultado, cada um com a sua frase, no fim do caso. Use o grupo, que é um mosaico de Cartões com um Dado em cada.

## Não use quando

- O número só faz sentido com outros ao lado, numa série ou numa proporção. Use Gráfico.
- A mudança tem várias dimensões, ou não é um número. Use Antes e depois.
- O que precisa ficar na memória é uma frase. Use Destaque.
- O número está no meio de um raciocínio. Deixe no texto corrido, com a mesma vírgula decimal.
- Não há como dizer de onde o número veio. Sem fonte, o número não entra.

## Anatomia

1. Valor, obrigatório. Número com unidade curta (`32%`, `8 semanas`, `2 origens`), num `span` `.stat__valor`.
2. Valor de antes, só na variante `salto`. Riscado, acima do valor novo, num `span` `.stat__antes`.
3. Frase, obrigatória. Diz o que foi medido, como e em que período, num `p` `.stat__frase`. É a fonte do número, e por isso não sai.
4. Ícone adesivo, só no grupo e opcional. Do acento do caso, antes do valor, no Cartão e fora do `.stat`.

O valor nunca é título. Fica em `span`, para não entrar na lista de títulos de quem navega por eles.

## Variantes

| Forma | Como se escreve | Quando |
| --- | --- | --- |
| Sozinho | `.stat` | Um número sem antes |
| Salto | `.stat` com `data-variant="salto"` | O número que prova o caso, com o valor anterior riscado |
| Grupo | `.cards` com `data-layout="mosaico"`, e um `.stat` em cada Cartão `meio` | Os números que fecham a conta |

No grupo cada número mora num Cartão `meio` do papel, com o ícone em cima, e o valor desce do degrau `numero` para o `display`. Quem diminui o valor é o mosaico, pelo CSS, e nunca um `style` no HTML. Um debaixo do outro no celular, dois por linha a partir de 720px.

O grupo com fio em cima (`.stats`) sai. Ele era a forma da primeira prova, e o modelo de Caso trocou pelo mosaico. Manter as duas seria ter dois grupos para o mesmo trabalho.

O Dado não tem cor própria. O Salto mora num Cartão do acento (`data-variant="acento"`), e os Cartões do grupo ficam no papel, porque o acento chapado da página já está no Salto. Na superfície tinta o texto vira papel sozinho.

## Limites

- Um Salto por página, no topo. Ele é o número que a página promete.
- Um grupo por página, com dois ou quatro números. Três deixam um Cartão `meio` sozinho na linha, então corte um ou some um. Cinco ou mais viram tabela ou Gráfico.
- Valor de até 9 caracteres, contando a unidade. Acima disso o degrau `numero` quebra linha no celular.
- Frase de até 36 caracteres por linha, que é a largura que o estilo dá a ela. No Salto, até três linhas. No grupo, até duas.
- Vírgula decimal, no padrão brasileiro (`34,4%`).

## Comportamento

1. **Mouse.** Não tem. O Dado não é alvo.
2. **Toque.** Não tem, pelo mesmo motivo.
3. **Foco.** Não recebe foco.
4. **Movimento.** Entra com o revelar da página. No grupo quem leva `data-revelar` é o mosaico inteiro, que sobe 16px e aparece em `dur-lenta` com `ease-saida`.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- O risco do valor de antes não é lido. Por isso o Salto leva dois textos só para leitor de tela (`.sr`), "De" antes do valor antigo e "para" antes do novo. Quem ouve recebe "De 24% para 32%".
- O til de aproximação (`~40 mil`) é lido como "til" por alguns leitores. Escreva "cerca de" num `.sr` e esconda o til com `aria-hidden`.
- Tinta sobre o acento e sobre o papel passa com folga em qualquer degrau.

## Onde aparece

- Modelo de Caso, Salto no topo, num Cartão azul com a ilustração do salto ao lado. "De 24% para 32%", com a frase "A conversão de leads qualificados nas origens redesenhadas, medida em produção ao longo de 8 semanas…".
- Modelo de Caso, grupo no Resultado. Quatro Cartões `meio` com ícone, "+8%", "~40 mil", "8 semanas" e "2 origens".
- Nas páginas publicadas, o Salto (`.salto`) abre os quatro casos, e os Números do resultado (`.numeros`) fecham os quatro.

## Vizinhos

- **Gráfico.** Quando o número precisa de série, escala ou proporção para ser lido.
- **Antes e depois.** Quando a virada não cabe num número.
- **Destaque.** Quando o que fica é uma frase, não um valor.
- **Cartão.** É a moldura do Salto e de cada número do grupo, não um substituto do Dado.

## Par nos posts

Dado, o número em Anton num cartão de acento com legenda e fonte. NumeroSangrado, a variante gigante que corta a borda, fica só nos posts. Na tela o número precisa caber inteiro em 390px.

## Código

```html
<!-- Salto, dentro de um Cartão do acento -->
<div class="card" data-variant="acento">
  <div class="stat" data-variant="salto">
    <span class="stat__antes"><span class="sr">De </span>24%</span>
    <span class="stat__valor"><span class="sr">para </span>32%</span>
    <p class="stat__frase">A conversão de leads qualificados nas origens redesenhadas, medida em produção ao longo de 8 semanas.</p>
  </div>
</div>

<!-- Grupo, em mosaico de Cartões -->
<div class="cards" data-layout="mosaico" data-revelar>
  <div class="card" data-tamanho="meio">
    <img class="icone" src="assets/ds/icones/grafico-azul.svg" alt="" width="48" height="48">
    <div class="stat"><span class="stat__valor">+8%</span><p class="stat__frase">de conversão de leads qualificados, de 24% para 32%</p></div>
  </div>
  <div class="card" data-tamanho="meio">
    <img class="icone" src="assets/ds/icones/dialogo-azul.svg" alt="" width="48" height="48">
    <div class="stat"><span class="stat__valor"><span aria-hidden="true">~</span><span class="sr">cerca de </span>40 mil</span><p class="stat__frase">conversas comparadas em produção</p></div>
  </div>
</div>
```

Estilo em `assets/ds/componentes.css`, seção Stat (`.stat`), e o degrau do valor no grupo junto do mosaico, na seção Card. Não tem script além do revelar.

**O que falta no código.**

- O degrau `display` do grupo e o espaço de 12px entre o número e a frase já moram em `componentes.css`, junto do mosaico. O `style` saiu do HTML e o `.stats` saiu do CSS.
- O til de "~40 mil" já tem o texto para leitor de tela no modelo e na página publicada. As outras variações ficam como estavam.
