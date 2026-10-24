# Sumário

`Table of contents` · as Seções do caso, cada uma com o seu ícone e a da vez marcada. No desktop é uma coluna fixa ao lado do conteúdo, e abaixo de 1100px vira um trilho de marcas na borda direita.

## Use quando

A página tem de quatro a seis Seções numeradas, que é o Caso. O leitor escaneia antes de ler e precisa saber em que parte está, quanto já passou e como pular para outra.

## Não use quando

- O destino é outra página. Use o Cabeçalho.
- A página não tem Seções numeradas, como a Home. Ela fica sem Sumário.
- São menos de quatro ou mais de seis Seções. Com menos o Sumário não tem o que mostrar, com mais o trilho não cabe no celular (regra 12 do `ds/RITMO.md`). Junte ou divida Seções antes.
- A ideia é medir quanto falta para acabar. A Régua de leitura saiu, e o Sumário mostra partes, não porcentagem.
- Os itens são partes de uma Seção. Use a peça daquela Seção, como Abas ou Passos.

## Anatomia

1. Caixa, `nav.sumario` com `data-sumario` e `aria-label="Neste caso"`, obrigatória. É o primeiro filho do `main.caso`.
2. Título, `p.t-rotulo.sumario__titulo`, "Neste caso". Some no trilho.
3. Lista, `ol.sumario__lista` com `id`, obrigatória. Um `a.sumario__item` por Seção, apontando para o `id` dela. Dentro, o ícone adesivo do acento em 32px, o número em `.sumario__num` e o nome em `.sumario__nome`. O nome é o mesmo do rótulo da Seção.
4. Botão do trilho, `button.sumario__botao`, obrigatório. Nasce com `hidden` e o script mostra. Leva `aria-controls` para a lista, o texto "Seções deste caso" só para leitor de tela e uma marca (`span.sumario__seg`) por Seção.
5. Aviso, `span.sumario__aviso`, obrigatório e vazio no HTML. O script escreve nele o nome da Seção durante a rolagem.

## Variantes

Não há atributo. A forma muda com a largura e com o script.

| | Forma |
| --- | --- |
| A partir de 1100px | Coluna de 260px à esquerda do conteúdo, fixa a 96px do topo enquanto a página rola |
| Abaixo de 1100px, com JS | Trilho de marcas finas na borda direita, dentro da margem, que abre a lista de lado |
| Abaixo de 1100px, sem JS | A lista aberta no topo do caso, antes do Topo |

No trilho cada marca tem um estado. As Seções lidas ficam em tinta, a da vez cresce e ganha o acento, e as que faltam ficam no papel.

O Sumário não vai para a superfície tinta.

## Limites

- Um por página, só no Caso.
- De quatro a seis itens, um por Seção. O CSS escalona a chegada até o sexto.
- Nome de até duas palavras, numa linha na coluna de 260px. No trilho, número e nome cabem juntos no aviso, que não quebra linha.
- Um ícone por item, sem repetir dentro do Sumário. Fora dele os ícones podem voltar (regra 8 do `ds/RITMO.md`).

## Comportamento

1. **Mouse.** O nome ganha `muted` como marca texto e o ícone sobe e inclina, em `dur-media` com `ease-saida`. O item da vez não se mexe no hover.
2. **Toque.** No `:active` o nome ganha a marca no acento. Todo item tem pelo menos `alvo` (44px). No trilho o botão tem `alvo` de largura e a altura de todas as marcas, mesmo que o que se vê seja só a margem.
3. **Foco.** O anel de 2px em `ring`. Escolher um item rola até a Seção. No trilho, o botão abre a lista e leva o foco ao primeiro item. Esc fecha e devolve o foco ao botão, e um toque fora, a escolha de um item ou o foco saindo do Sumário também fecham.
4. **Movimento.** Quando muda a Seção da vez, o nome ganha a marca no acento e o ícone cresce e gira, em `dur-media`. No trilho, a marca da vez cresce e muda de cor no mesmo tempo. Enquanto a página rola, o nome da Seção desliza para o lado das marcas e some `dur-lenta` depois que a rolagem para. A lista entra de lado em `dur-lenta`, com os itens chegando um a um em `dur-media`. Perto do Rodapé o trilho sai pela direita, e o nome da Seção não aparece mais por cima dele.
5. **Sem JS.** Nenhum item marcado e os links pulam para a Seção. Abaixo de 1100px a lista fica aberta no topo do caso.
6. **Movimento reduzido.** As transições vão a zero e o pulo para a Seção é direto. A marca da vez continua, só que sem movimento.

## Acessibilidade

- É uma `nav` com nome, "Neste caso", e a `ol` diz quantas Seções há.
- A Seção da vez leva `aria-current="true"`, posto pelo script. Não depende só da cor, porque o ícone gira e cresce, e no trilho a marca muda de tamanho.
- O ícone tem `alt` vazio. O nome já diz o que é.
- No trilho o botão tem `aria-expanded`. Fechada, a lista fica com `visibility: hidden` e sai do Tab e da leitura.
- O aviso tem `aria-hidden`. Ele repete na tela o que a rolagem já mostra, e lido a cada Seção seria ruído.
- Tinta sobre papel e sobre o acento passa com folga.

## Onde aparece

- Modelo de Caso e `case-omnichat.html`. "01 Contexto", "02 O problema", "03 Processo", "04 Antes e depois" e "05 Resultado", com os ícones robô, fronteira, camadas, diálogo e gráfico.
- A vitrine (`ds/vitrine/index.html`), com as cinco ondas da Fase 5 como Seções.
- Nas páginas publicadas não existe. Nasceu com a variação 4, e o trilho venceu a faixa no cabeçalho e o botão flutuante (ver `ds/FUNDAMENTOS.md`).

## Vizinhos

- **Cabeçalho.** Leva a outras páginas.
- **Seção.** O rótulo da Seção repete o número e o nome do item.
- **Abas.** Também se escolhe um item numa lista, mas dentro de uma Seção e sem rolar.

## Par nos posts

Sem par como peça. No carrossel o campo `secao` do rodapé esquerdo da Moldura diz onde o leitor está, como a marca da vez.

## Código

```html
<nav class="sumario" data-sumario aria-label="Neste caso">
  <p class="t-rotulo sumario__titulo">Neste caso</p>
  <ol class="sumario__lista" id="sumario-lista">
    <li><a class="sumario__item" href="#contexto"><img class="icone" src="assets/ds/icones/robo-azul.svg" alt="" width="32" height="32"><span class="sumario__num">01</span><span class="sumario__nome">Contexto</span></a></li>
    <li><a class="sumario__item" href="#problema"><img class="icone" src="assets/ds/icones/fronteira-azul.svg" alt="" width="32" height="32"><span class="sumario__num">02</span><span class="sumario__nome">O problema</span></a></li>
    <!-- um item por Seção -->
  </ol>
  <button class="sumario__botao" type="button" aria-expanded="false" aria-controls="sumario-lista" hidden><span class="sr">Seções deste caso</span><span class="sumario__seg" aria-hidden="true"></span><span class="sumario__seg" aria-hidden="true"></span><!-- uma marca por Seção --></button>
  <span class="sumario__aviso" aria-hidden="true"></span>
</nav>
```

O HTML sai de `ds/prova/caso.py`, função `sumario`, a partir da lista `SECOES`. Estilo em `assets/ds/componentes.css`, seção Sumário (`.sumario`), e a coluna fixa na receita `.caso`. Comportamento em `assets/ds/componentes.js`, bloco 4.

**O que falta no código.**

- Resolvido na Onda 1. Abrir o trilho leva o foco ao primeiro item, e o foco saindo do Sumário fecha a lista. Os tempos são tokens, o trilho começa em `altura-cabecalho`, e o nome da Seção não aparece mais sobre o Rodapé, quando o trilho já saiu de cena.
