# Destaque

`Callout` · uma frase ou um trecho curto que a Seção existe para carregar, separado do texto corrido para o leitor apressado achar.

## Use quando

- **O que o caso deixa, no fim.** Uma frase de tese que fecha a conta, com o rótulo e um parágrafo que a explica. Use a frase na tinta, no Resultado.
- **A virada no meio do caso.** Uma pergunta ou uma descoberta que muda a direção da história, com uma legenda que diz de onde ela veio. Use a frase no papel.
- **O que destravou uma etapa.** Uma ou duas linhas com o critério ou a decisão que fez a coisa andar. Use `nota`.
- **O que deu errado no caminho.** O tropeço e a regra que nasceu dele, com título. Use `atrito`.

## Não use quando

- A frase tem um número que prova o caso. Use Dado.
- É a fala de alguém com nome, como a de quem usou o produto. Use Antes e depois `citacao`, porque o Destaque é a voz do caso e não a do usuário.
- A frase só reforça o parágrafo de cima. Deixe no texto. Negrito no parágrafo também não serve, porque some na leitura rápida.
- É o convite para conversar e o Próximo caso. É o fechamento do Resultado, com texto e Botão.
- É uma lista de itens do mesmo tipo. Use Cartões em mosaico.

## Anatomia

**Frase na tinta.**

1. Caixa, `div.callout.superficie-tinta`, obrigatória.
2. Rótulo, `span.badge` com `data-variant="acento"`, obrigatório. Diz o que a frase é ("O que eu levo daqui").
3. Frase, `p.callout__frase`, obrigatória. Anton no degrau `display`, caixa alta.
4. Corpo, `p.prosa`, obrigatório. Um parágrafo que explica a frase.

**Frase no papel.**

1. Caixa, `div.callout`, obrigatória. Sem fundo, sem contorno e sem recuo, na mesma margem do texto.
2. Frase, `p.callout__frase`, obrigatória. Anton no degrau `display`.
3. Legenda, `p.callout__legenda`, obrigatória. No degrau `apoio`, diz de onde a frase veio ou o que ela resume.

**Nota.**

1. Caixa, `div.callout` com `data-variant="nota"`, obrigatória. Uma régua de 2px em `border` em cima.
2. Rótulo, `p.t-rotulo.callout__rotulo`, obrigatório. Nomeia a nota ("O que destravou").
3. Texto, `p`, obrigatório. Um parágrafo curto.

**Atrito.**

1. Caixa, `div.callout` com `data-variant="atrito"`, obrigatória. Fundo `muted`, contorno de 2px em `border` e raio `radius`.
2. Ícone, `img.icone` com o `alerta` do acento da página, obrigatório.
3. Título, `h3`, obrigatório. Diz o tropeço numa frase ("A primeira tentativa não foi essa").
4. Texto, `div.prosa`, obrigatório. Um ou dois parágrafos, e o último diz a regra que ficou.

## Variantes

| Forma | Como se escreve | Peso no ritmo | Quando |
| --- | --- | --- | --- |
| Frase na tinta | `.callout.superficie-tinta` | Forte | O que o caso deixa, no Resultado |
| Frase no papel | `.callout`, sem atributo | Médio | A virada no meio do caso |
| Nota | `.callout` com `data-variant="nota"` | Médio | O que destravou uma etapa |
| Atrito | `.callout` com `data-variant="atrito"` | Médio | O que deu errado e a regra que ficou |

Pelo `ds/RITMO.md`, forte é a tinta ou o acento chapado em área grande. A frase no papel não tem fundo, e por isso é média, mesmo com o Anton.

A nota tem o rótulo em cima do texto no celular e, a partir de 720px, o rótulo num terço à esquerda e o texto nos dois terços à direita.

O atrito tem o ícone em cima no celular e, a partir de 720px, o ícone na margem esquerda, com o título e o texto alinhados à direita dele.

O atrito sai da tinta, onde morava no site de hoje. A tinta da página é uma só (D4), e é a do Resultado. O fundo `muted` com o ícone de alerta separa o atrito do texto sem gastar a parada escura.

## Limites

- Uma frase na tinta por página, no Resultado, depois do Dado em grupo.
- Frase de até seis linhas em 390px e até quatro no desktop, como a do modelo. A frase tem no máximo 20 caracteres por linha de largura (`20ch`), para o Anton não virar parágrafo.
- Legenda e corpo de até três linhas no desktop.
- Rótulo da nota de até três palavras. Texto da nota de até três linhas no desktop.
- Título do atrito de até duas linhas. Texto do atrito de até dois parágrafos.
- Até uma frase no papel além da frase na tinta, nunca na mesma Seção.
- No máximo um Destaque médio por Seção. A regra 3 do `ds/RITMO.md` diz o mesmo. Ela dizia "um Destaque por página", e mudou na Onda 2 porque o Processo com IA tem três atritos e o Inpulse duas notas.

## Comportamento

1. **Mouse.** Não tem. O Destaque não é alvo. Um Link dentro do corpo segue a ficha do Link.
2. **Toque.** Não tem.
3. **Foco.** Não recebe foco.
4. **Movimento.** O Destaque inteiro leva `data-revelar` e entra subindo 16px em `dur-lenta` com `ease-saida`. As partes não entram uma a uma.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- A frase é parágrafo, não título. Ela não entra na lista de títulos e não confunde quem navega por eles. A caixa alta vem do CSS, e o texto no HTML é escrito normal.
- O atrito tem `h3`, porque é o que o leitor apressado mais precisa achar, e quem navega por títulos o encontra.
- O rótulo da nota é parágrafo. O texto da nota é curto e se lê junto.
- O ícone do atrito tem `alt` vazio. O título já diz o que é.
- Papel sobre tinta, tinta sobre papel e tinta sobre `muted` passam com folga.

## Onde aparece

- Modelo de Caso, frase na tinta no Resultado. "O que eu levo daqui", "A interface não é mais o objeto principal do trabalho. O objeto é a decisão."
- Nas páginas publicadas, a frase na tinta é a Declaração final (`.fecho--unido`) dos quatro casos. No Inpulse, "Desejo do usuário e aposta do time raramente são a mesma coisa."
- Frase no papel, o Grito (`.grito`). No Processo, "O que sobra pra gente?", com a legenda "A pergunta que o time fez quando ficou claro que o rascunho do documento e da primeira tela sairia automático." No Inpulse, "O calendário doía mais que o boletim."
- Nota, a Linha de nota (`.linha-nota`). No Processo, "O que destravou", "Mudar o critério antes da rotina." No Inpulse, "O aluno de medicina" e "O que a gente cortou". No Mapa, "Relatórios por eixo".
- Vitrine, no palco do Destaque. A nota e a frase no papel do Inpulse, o atrito "Aqui eu cortei rápido demais" do Processo e a frase na tinta do Omnichat, uma por Seção.
- Atrito (`.atrito`), só no Processo, três vezes. "A primeira tentativa não foi essa", "Aqui eu cortei rápido demais" e "A conta estava sendo lida ao contrário".

## Vizinhos

- **Dado.** Quando o que fica é um número com fonte.
- **Antes e depois `citacao`.** Quando a frase é de alguém com nome.
- **Cartão `muted`.** Também tem fundo mist, mas é moldura de dados ou de itens, sem ícone de alerta nem a regra que ficou.
- **Etiqueta.** O rótulo da frase na tinta é uma Etiqueta, não um Destaque.

## Par nos posts

BlocoTinta, o card escuro com a frase, para a frase na tinta. CenaPagina, a frase grande em Anton com subtítulo, para a frase no papel. A nota e o atrito não têm par, porque o post não tem texto corrido para separar.

## Código

```html
<!-- Frase na tinta, no Resultado -->
<div class="callout superficie-tinta" data-revelar>
  <span class="badge" data-variant="acento">O que eu levo daqui</span>
  <p class="callout__frase">A&nbsp;interface não é&nbsp;mais o&nbsp;objeto principal do&nbsp;trabalho. O&nbsp;objeto é&nbsp;a&nbsp;decisão.</p>
  <p class="prosa">O que o agente pode decidir sozinho, o que ele precisa verificar antes de agir e como mostra isso para quem precisa confiar no resultado.</p>
</div>

<!-- Frase no papel -->
<div class="callout" data-revelar>
  <p class="callout__frase">O que sobra pra&nbsp;gente?</p>
  <p class="callout__legenda">A pergunta que o time fez quando ficou claro que o rascunho do documento e da primeira tela sairia automático.</p>
</div>

<!-- Nota -->
<div class="callout" data-variant="nota" data-revelar>
  <p class="t-rotulo callout__rotulo">O que destravou</p>
  <p>Mudar o critério antes da rotina. Parei de avaliar entregável e passei a avaliar decisão.</p>
</div>

<!-- Atrito -->
<div class="callout" data-variant="atrito" data-revelar>
  <img class="icone" src="assets/ds/icones/alerta-lime.svg" alt="" width="48" height="48">
  <h3>A primeira tentativa não foi&nbsp;essa</h3>
  <div class="prosa">
    <p>Cada um usava o Claude do seu jeito, e a gente passou a gerar documento mais rápido e alinhar menos.</p>
    <p>A skill compartilhada nasceu como conserto disso, não como ideia de eficiência.</p>
  </div>
</div>
```

Estilo em `assets/ds/componentes.css`, seção Callout (`.callout`). Não tem script além do revelar.

Na Onda 2 o recuo e o raio saíram do `.callout` e foram para a `.callout.superficie-tinta`, e a frase no papel, a `nota` e o `atrito` entraram. A frase na tinta do Omnichat ficou igual, conferida elemento por elemento em 390, 768 e 1440px.
