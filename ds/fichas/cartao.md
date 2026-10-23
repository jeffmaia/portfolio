# Cartão

`Card` · a caixa do sistema, com contorno de tinta, raio de 12 e fundo no papel, no `muted` ou no acento. Sozinho é moldura, e em grupo vira mosaico.

## Use quando

- **Vários itens do mesmo tipo, para passar os olhos em todos.** De dois a seis, cada um com ícone, nome e um parágrafo curto. O leitor precisa ver todos antes de escolher qual ler. Use o grupo em mosaico.
- **Os dados do projeto.** Duração, Jeff e Time, no Topo do caso. Use o Cartão `muted` com a ficha.
- **A moldura de um número ou de uma cena.** O Salto e a ilustração do caso moram num Cartão do acento.

## Não use quando

- A ordem dos itens é o assunto. Use Passos.
- Cada item é longo e o leitor vai ler um ou dois. Use Abas.
- É a mesma coisa antes e depois. Use Antes e depois.
- É uma frase que precisa ficar na memória. Use Destaque.
- A caixa só serviria para separar um texto do resto. Texto corrido não leva moldura.

## Anatomia

**O Cartão.**

1. Caixa, `article.card` quando o item faz sentido sozinho (uma camada, uma origem), `div.card` quando é moldura (a ficha, o Salto). Obrigatória.
2. Ícone adesivo, opcional. Do acento do caso, com `aria-hidden`.
3. Rótulo, opcional. `p.t-rotulo`, com o número do item ("Camada 01") quando outras partes da página apontam para ele.
4. Título, `h3`, obrigatório no mosaico. No degrau `lead`, em negrito.
5. Texto, `p.t-apoio`, obrigatório no mosaico. Um parágrafo.
6. Efeito, opcional. `p.card__efeito`, com o rótulo "Efeito" e uma frase sobre o que o item mudou.

**O grupo em mosaico.**

1. Caixa, `div.cards` com `data-layout="mosaico"`. Uma grade de seis colunas que ocupa a largura da coluna de conteúdo.
2. Os Cartões, cada um com `data-tamanho`.

## Variantes

| Atributo | Valor | Como fica | Quando |
| --- | --- | --- | --- |
| `data-variant` | sem atributo | Fundo `background` | O padrão |
| | `muted` | Fundo `muted` (mist) | A ficha do projeto, e o que é informação de apoio |
| | `acento` | Fundo `acento`, texto em tinta | O Salto, e um item que o mosaico quer marcar |
| `data-tamanho` | `meio` | Metade da linha | Itens de mesmo peso, em pares |
| | `terco` | Um terço da linha | Itens curtos, em trios |
| | `dois-tercos` | Dois terços no desktop, a linha inteira no tablet | O item que abre o grupo e pesa mais |

Os tamanhos por largura, em colunas de seis.

| | até 719px | de 720 a 1099px | a partir de 1100px |
| --- | :-: | :-: | :-: |
| `meio` | 6 | 3 | 3 |
| `terco` | 6 | 2 | 2 |
| `dois-tercos` | 6 | 6 | 4 |

No celular todo Cartão ocupa a linha inteira, um debaixo do outro.

Na superfície tinta o contorno vira papel, porque `border` troca por dentro. O `muted` e o `acento` continuam com texto em tinta.

## Limites

- De dois a seis Cartões num mosaico. Um item só é moldura, e mais de seis vira Abas ou duas Seções.
- Um Cartão `acento` por mosaico, e o acento chapado em só uma de duas Seções seguidas (regra 11 do `ds/RITMO.md`).
- Um mosaico de Cartões por página, fora o Topo e o Dado em grupo. O modelo usa no Processo.
- As linhas somam seis colunas. Fecham nas duas larguras dois, quatro ou seis `meio`, e três ou seis `terco`. No arranjo do Processo, um `dois-tercos` seguido de quatro `terco`, o desktop fecha e o tablet deixa a quinta camada sozinha na última linha. É assim no modelo aprovado.
- Título de até duas linhas e texto de até seis linhas no Cartão `terco` do desktop. Passou disso, o item é longo e pede Abas.

## Comportamento

1. **Mouse.** Não tem. O Cartão não é alvo. Se um dia virar link, a ficha muda antes.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** O grupo inteiro leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. Os Cartões não entram um a um, para a leitura do grupo não esperar.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- No mosaico os Cartões são `article`, cada um com o seu `h3`. Quem navega por títulos acha cada item.
- O ícone é decorativo. O título já diz o que é.
- A ordem de leitura é a ordem do HTML, que é a mesma da grade. O mosaico nunca reordena com CSS.
- Tinta sobre papel, mist e acento passa com folga. Ver `ds/CONTRASTE.md`.

## Onde aparece

- Modelo de Caso, Topo. A ficha do projeto num Cartão `muted` e o Salto num Cartão do acento, com a ilustração do salto.
- Modelo de Caso, Processo. Cinco camadas em mosaico, a primeira em `dois-tercos` e no acento ("A arquitetura de prompt como superfície de design"), as outras quatro em `terco`.
- Modelo de Caso, Problema. Duas origens em `meio`, "Instagram" e "Disparos de WhatsApp".
- Modelo de Caso, Resultado. Quatro Cartões `meio` com o Dado em grupo (ver a ficha do Dado).
- Nas páginas publicadas, a Ficha do projeto dos quatro casos.

## Vizinhos

- **Passos.** Quando a ordem é o assunto, ou são duas coisas ao mesmo tempo.
- **Abas.** Quando cada item é longo e se lê um de cada vez.
- **Dado.** O número que mora dentro do Cartão, não o Cartão.
- **Destaque.** Uma frase sozinha, sem moldura de item.

## Par nos posts

Cards, a sequência de dois a três cartões com rótulo e frase. Lá o último cartão é a conclusão e leva a cor mais forte. Aqui o mosaico não tem ordem de leitura, e quem leva o acento é o item que abre o grupo.

## Código

```html
<!-- Grupo em mosaico -->
<div class="cards" data-layout="mosaico" data-revelar>
  <article class="card" data-tamanho="dois-tercos" data-variant="acento">
    <img class="icone" src="assets/ds/icones/lapis-azul.svg" alt="" width="48" height="48">
    <p class="t-rotulo">Camada 01</p>
    <h3>A arquitetura de prompt como superfície de design</h3>
    <p class="t-apoio">Parar de tratar o prompt como configuração técnica…</p>
    <p class="card__efeito"><span class="t-rotulo">Efeito</span> Tornou a conversa um objeto de design…</p>
  </article>
  <article class="card" data-tamanho="terco">…</article>
</div>

<!-- Ficha do projeto -->
<div class="card" data-variant="muted">
  <p class="t-rotulo card__titulo">Ficha do projeto</p>
  <dl class="ficha">
    <div><dt>Duração</dt><dd>…</dd></div>
  </dl>
</div>
```

Estilo em `assets/ds/componentes.css`, seção Card (`.card`, `.ficha`). Não tem script além do revelar.

**O que falta no código.**

- Nada para o uso atual. O mosaico, que morava no CSS da variação 4 com as classes `.mosaico` e `.tile`, já está em `componentes.css` como `.cards[data-layout="mosaico"]`.
