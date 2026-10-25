# Cartão

`Card` · a caixa do sistema, com contorno de tinta, raio de 12 e fundo no papel, no `muted` ou no acento. Sozinho é moldura, e em grupo vira mosaico.

## Use quando

- **Vários itens do mesmo tipo, para passar os olhos em todos.** De dois a seis, cada um com ícone, nome e um parágrafo curto. O leitor precisa ver todos antes de escolher qual ler. Use o grupo em mosaico.
- **Os dados do projeto.** Duração, Jeff e Time, no Topo do caso. Use o Cartão `muted` com a ficha.
- **A moldura de um número ou de uma cena.** O Salto e a ilustração do caso moram num Cartão do acento.
- **Um caso na Lista de casos da Home.** O título do caso, a frase de apoio, o número que ele promete e o caminho para a página. Use o Cartão `caso`, no mosaico com `meio`.

## Não use quando

- A ordem dos itens é o assunto. Use Passos.
- Cada item é longo e o leitor vai ler um ou dois. Use Abas.
- É a mesma coisa antes e depois. Use Antes e depois.
- É uma frase que precisa ficar na memória. Use Destaque.
- A caixa só serviria para separar um texto do resto. Texto corrido não leva moldura.
- O Cartão `caso` levaria um Botão. Na Lista são quatro lado a lado, e quatro Botões disputariam entre si. Use o Link `seguir`.

## Anatomia

**O Cartão.**

1. Caixa, `article.card` quando o item faz sentido sozinho (uma camada, uma origem), `div.card` quando é moldura (a ficha, o Salto). Obrigatória.
2. Ícone adesivo, opcional. Do acento do caso, com `aria-hidden`.
3. Rótulo, opcional. `p.t-rotulo`, com o número do item ("Camada 01") quando outras partes da página apontam para ele.
4. Título, `h3`, obrigatório no mosaico. No degrau `lead`, em negrito.
5. Texto, `p.t-apoio`, obrigatório no mosaico. Um parágrafo.
6. Efeito, opcional. `p.card__efeito`, com o rótulo "Efeito" e uma frase sobre o que o item mudou.

**O Cartão de caso.** Nesta ordem.

1. Caixa, `article.card` com `data-variant="caso"` e o acento do caso em `data-acento`, obrigatória.
2. Rótulo, `p.t-rotulo`, obrigatório, com o número na fila e o nome do caso ("02 · Omnichat"). O título do caso nem sempre diz de quem ele é.
3. Título, `h3`, obrigatório, o mesmo do Topo do caso.
4. Frase, `p.t-apoio`, obrigatória, a frase de apoio do Topo.
5. Base, `div.card__base`, obrigatória, no acento. Dentro, o Dado `salto` no tamanho de grupo, a ficha numa linha (`p.card__ficha`, papel e duração) e o Link `seguir`, "Ver o caso", com o nome do caso só para o leitor de tela.

**O grupo em mosaico.**

1. Caixa, `div.cards` com `data-layout="mosaico"`. Uma grade de seis colunas que ocupa a largura da coluna de conteúdo.
2. Os Cartões, cada um com `data-tamanho`.

## Variantes

| Atributo | Valor | Como fica | Quando |
| --- | --- | --- | --- |
| `data-variant` | sem atributo | Fundo `background` | O padrão |
| | `muted` | Fundo `muted` (mist) | A ficha do projeto, e o que é informação de apoio |
| | `acento` | Fundo `acento`, texto em tinta | O Salto, e um item que o mosaico quer marcar |
| | `caso` | O alto no papel e a base no acento do caso, com o número | Um caso na Lista de casos da Home |
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

No Cartão `caso` o acento entra só na base, para os quatro lado a lado não virarem quatro blocos chapados disputando o olho. Sobre o acento o marca texto do Link corre em papel (`--marca`), porque acento sobre acento não se veria. Lado a lado, os Cartões `caso` dividem as linhas da grade (subgrid). O rótulo, o título, a frase, o Dado, a ficha e o Link de um ficam na mesma altura que os do vizinho, e as bases saem alinhadas por cima e por baixo, por mais que um título tenha uma linha a mais. Onde não há subgrid, a base só desce até o pé.

Na superfície tinta o contorno vira papel, porque `border` troca por dentro. O `muted` e o `acento` continuam com texto em tinta.

## Limites

- De dois a seis Cartões num mosaico. Um item só é moldura, e mais de seis vira Abas ou duas Seções.
- Um Cartão `acento` por mosaico, e o acento chapado em só uma de duas Seções seguidas (regra 11 do `ds/RITMO.md`).
- Um mosaico de Cartões por página, fora o Topo e o Dado em grupo. O modelo usa no Processo. Na Home, o mosaico é a Lista de casos.
- Na Lista de casos, um Cartão `caso` por caso, na ordem da fila, sempre `meio`. Cada um leva o acento do próprio caso, e é a única peça do site que mostra os três acentos na mesma página.
- As linhas somam seis colunas. Fecham nas duas larguras dois, quatro ou seis `meio`, e três ou seis `terco`. No arranjo do Processo, um `dois-tercos` seguido de quatro `terco`, o desktop fecha e o tablet deixa a quinta camada sozinha na última linha. É assim no modelo aprovado.
- Título de até duas linhas e texto de até seis linhas no Cartão `terco` do desktop. Passou disso, o item é longo e pede Abas.

## Comportamento

1. **Mouse.** Não tem. O Cartão não é alvo, nem o `caso`. Se um dia virar link, a ficha muda antes. No `caso`, só o Link de dentro reage, com a marca em papel.
2. **Toque.** Não tem. O Link do Cartão `caso` tem 44px.
3. **Foco.** Não recebe foco.
4. **Movimento.** O grupo inteiro leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. Os Cartões não entram um a um, para a leitura do grupo não esperar.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- No mosaico os Cartões são `article`, cada um com o seu `h3`. Quem navega por títulos acha cada item.
- O ícone é decorativo. O título já diz o que é.
- No Cartão `caso`, o Link diz ao leitor de tela qual caso abre ("Ver o caso, Omnichat"), porque os quatro Links da Lista têm o mesmo texto. O antes e o depois do Dado são lidos como "De 24% para 32%".
- A ordem de leitura é a ordem do HTML, que é a mesma da grade. O mosaico nunca reordena com CSS.
- Tinta sobre papel, mist e acento passa com folga. Ver `ds/CONTRASTE.md`.

## Onde aparece

- Modelo de Caso, Topo. A ficha do projeto num Cartão `muted` e o Salto num Cartão do acento, com a ilustração do salto.
- Modelo de Caso, Processo. Cinco camadas em mosaico, a primeira em `dois-tercos` e no acento ("A arquitetura de prompt como superfície de design"), as outras quatro em `terco`.
- Modelo de Caso, Problema. Duas origens em `meio`, "Instagram" e "Disparos de WhatsApp".
- Modelo de Caso, Resultado. Quatro Cartões `meio` com o Dado em grupo (ver a ficha do Dado).
- Nas páginas publicadas, a Ficha do projeto dos quatro casos.
- Vitrine, na amostra e no palco do Cartão de caso, a Lista de casos da Home com os quatro casos. "Reconstruindo o processo de produto e design com Claude no centro", de 2 meses para 1 semana, no lime. "Verificação de intenção dos agentes conversacionais", de 24% para 32%, no azul. "Solução que ajudou a diminuir a recuperação dos alunos", de 8 em 10 para 6 em 10, no verde. "Como um mapa de experiência ajudou a deixar o NPS positivo", de −33 para +15, no azul. A Home publicada ainda usa a cena dos casos, e passa para a Lista na Fase 6.

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

<!-- Cartão de caso, na Lista de casos -->
<div class="cards" data-layout="mosaico" data-revelar>
  <article class="card" data-variant="caso" data-acento="azul" data-tamanho="meio">
    <p class="t-rotulo">02 · Omnichat</p>
    <h3>Verificação de intenção dos agentes conversacionais</h3>
    <p class="t-apoio">A maior perda de conversão não estava na interface…</p>
    <div class="card__base">
      <div class="stat" data-variant="salto">
        <span class="stat__antes"><span class="sr">De </span>24%</span>
        <span class="stat__valor"><span class="sr">para </span>32%</span>
        <p class="stat__frase">de conversão de leads qualificados nas origens redesenhadas</p>
      </div>
      <p class="card__ficha">Product Design Manager · 4 meses</p>
      <a class="link" data-variant="seguir" href="case-omnichat.html"><span>Ver o caso<span class="sr">, Omnichat</span></span> <i aria-hidden="true">→</i></a>
    </div>
  </article>
</div>

<!-- Ficha do projeto -->
<div class="card" data-variant="muted">
  <p class="t-rotulo card__titulo">Ficha do projeto</p>
  <dl class="ficha">
    <div><dt>Duração</dt><dd>…</dd></div>
  </dl>
</div>
```

Estilo em `assets/ds/componentes.css`, seção Card (`.card`, `.ficha`, e `.card__base` e `.card__ficha` no Cartão `caso`). Não tem script além do revelar. O HTML da Lista de casos sai das funções `cartao_caso` e `lista_casos` de `ds/prova/comum.py`, com o texto do Topo de cada caso em `CASOS`. O texto do Link fica dentro de um `span`, para o nome do caso só para o leitor de tela não abrir um vão a mais antes da seta.

**O que falta no código.**

- Nada para o uso atual. O mosaico, que morava no CSS da variação 4 com as classes `.mosaico` e `.tile`, já está em `componentes.css` como `.cards[data-layout="mosaico"]`.

O Cartão `caso` entrou na Onda 5 e foi aprovado por você na vitrine em 24 de outubro de 2026, depois do alinhamento das bases lado a lado.
