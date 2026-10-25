# Cabeçalho

`Header` e `Sheet` · a barra fixa no topo de toda página, com a marca que leva à Home e o botão que abre o menu por cima da página.

## Use quando

Toda página do site, sempre igual. O leitor precisa saber de quem é o site e chegar a qualquer outra página de qualquer ponto da rolagem. É parte fixa da receita de Toda página (ver `ds/RECEITAS.md`), logo depois do Pular para o conteúdo.

## Não use quando

- O destino é uma parte da mesma página. Use Sumário.
- É a ação principal do trecho. Use Botão. O menu não carrega ação, só lugares.
- O contato é o convite da página. Use o Rodapé, que tem a chamada e o Botão do WhatsApp. No menu o contato fica pequeno, abaixo dos itens.
- A ideia é uma segunda barra fixa, de aviso ou de progresso. Não entra. A Régua de leitura saiu (ver `ds/COMPONENTES.md`), e cada barra fixa a mais rouba altura da leitura.
- É o Manifesto. Ele saiu do menu pela D7.

## Anatomia

**A barra.**

1. Pular para o conteúdo, `a.pular`, obrigatório. Vem antes do `header`, fora da tela até receber foco, e aponta para `#conteudo`.
2. Caixa, `header.header`, com `div.container.header__inner` dentro. Obrigatória.
3. Marca, `a.marca`, obrigatória. Leva à Home. "Jeff Maia" em Anton num `b` e "Product Design Manager" num `span`, que some abaixo de 720px. O `aria-label` leva os dois.
4. Botão do menu, `button.menu-botao`, obrigatório. Leva `data-sheet-botao`, `aria-expanded` e `aria-controls="menu"`. Dentro, o ícone de dois traços com `aria-hidden` e as duas palavras, "Menu" e "Fechar", na mesma célula da grade.

**O menu.**

5. Painel, `div.sheet` com `id="menu"`, logo depois da barra. Dentro, `nav.sheet__inner` com `aria-label="Principal"`.
6. Itens do site, `ul.sheet__lista`, com um `a.sheet__item` por página e o nome num `span`. Home primeiro, depois os casos na ordem da fila. A página atual leva `aria-current="page"`.
7. Contato, `div.sheet__contato`, com o rótulo "Contato" e os Links externos para o LinkedIn e o WhatsApp em `ul.sheet__secundaria`.
8. Fundo escurecido, `div.sheet__fundo`. Quem cria é o script, e por isso não vai no HTML.

## Variantes

Uma forma só, sempre no papel. A barra não muda de cor com o que passa por trás e a assinatura não encolhe até o J, como faziam a Barra com assinatura e o Menu em painel do site de hoje. A retícula de pontos sobre a página também sai.

O que muda com a largura é só a marca. Abaixo de 720px fica "Jeff Maia" sozinho.

## Limites

- Um por página.
- Até seis itens do site no menu. Hoje são cinco, Home e os quatro casos. O CSS escalona a chegada até o sexto, e passou disso o menu pede grupos com rótulo.
- Nome do item em uma linha em 390px, no degrau `sub`.
- Até dois links no Contato.
- A barra tem `altura-cabecalho` (66px, com o traço). O painel, o fundo e o trilho do Sumário começam abaixo dela, e mudar a barra é mudar o token.

## Comportamento

1. **Mouse.** A marca ganha o acento como marca texto atrás de "Jeff Maia". O item do menu ganha a mesma marca atrás do nome. O botão do menu ganha `muted` no fundo. Tudo em `dur-media` com `ease-saida`.
2. **Toque.** No `:active` o item ganha a marca texto em `dur-rapida`, e o botão do menu ganha `muted` e desce 1px. Botão, itens e links do Contato têm pelo menos `alvo` (44px). A marca chega a `alvo` onde o ponteiro é o dedo.
3. **Foco.** O anel de 2px em `ring`. Ao abrir, o foco vai para o primeiro item do menu. Esc fecha e devolve o foco ao botão. Um toque no fundo escurecido também fecha, e o menu fecha sozinho quando o foco sai dele, pelo Tab depois do último link.
4. **Movimento.** Abrindo, o painel desce do cabeçalho com a borda de baixo correndo para baixo e a página por trás escurece, em `dur-lenta` com `ease-saida`. Os itens chegam um depois do outro em `dur-media`, com um terço de `dur-rapida` entre cada um. Fechando, sobe mais rápido do que desceu, em `dur-media` com `ease-troca`. No botão, "Menu" sobe e sai, "Fechar" sobe e entra, e os dois traços giram até virar um xis, sem o botão mudar de largura.
5. **Sem JS.** O botão some e o menu fica aberto no fluxo, logo abaixo da barra, com todos os links à vista. Nada se perde.
6. **Movimento reduzido.** As transições vão a zero. O painel aparece e some sem descer, e a palavra troca sem subir.

## Acessibilidade

- O nome do botão é a palavra que está na tela. A outra fica com `visibility: hidden` e sai da leitura.
- Fechado, o painel fica com `visibility: hidden`, que tira os links do Tab e do leitor de tela. Não usa `hidden` porque `hidden` não deixa animar.
- A página atual tem `aria-current="page"` e sublinhado de 2px. Não depende de cor.
- O Pular para o conteúdo é o primeiro Tab da página.
- Tinta sobre papel em todo texto. O acento só aparece como fundo, atrás das palavras e no botão aberto.

## Onde aparece

- A Home, os quatro casos, o modelo de Caso e a vitrine. A marca "Jeff Maia, Product Design Manager", os itens "Home", "Processo com IA", "Omnichat", "Inpulse" e "Mapa de experiência", e no Contato "LinkedIn" e "WhatsApp".

## Vizinhos

- **Sumário.** Leva às partes da mesma página, não a outras páginas.
- **Rodapé.** Repete os casos no fim e é quem faz o convite para conversar.
- **Link.** Os dois destinos do Contato são Links externos, não itens do menu.

## Par nos posts

Moldura, no cabeçalho que diz de quem é o post. O menu não tem par, porque no post não há para onde ir.

## Código

```html
<a class="pular" href="#conteudo">Pular para o caso</a>

<header class="header">
  <div class="container header__inner">
    <a class="marca" href="index.html" aria-label="Jeff Maia, Product Design Manager">
      <b>Jeff Maia</b><span>Product Design Manager</span>
    </a>
    <button class="menu-botao" type="button" data-sheet-botao aria-expanded="false" aria-controls="menu">
      <span class="menu-botao__icone" aria-hidden="true"><i></i><i></i></span>
      <span class="menu-botao__rotulos"><span>Menu</span><span>Fechar</span></span>
    </button>
  </div>
</header>

<div class="sheet" id="menu">
  <nav class="container sheet__inner" aria-label="Principal">
    <ul class="sheet__lista">
      <li><a class="sheet__item" href="index.html"><span>Home</span></a></li>
      <li><a class="sheet__item" href="case-omnichat.html" aria-current="page"><span>Omnichat</span></a></li>
      <!-- um item por página, na ordem da fila -->
    </ul>
    <div class="sheet__contato">
      <p class="t-rotulo">Contato</p>
      <ul class="sheet__secundaria">
        <li><a class="link" data-variant="externo" href="https://www.linkedin.com/in/maiajeff/" target="_blank" rel="noopener">LinkedIn <i aria-hidden="true">↗</i></a></li>
        <li><a class="link" data-variant="externo" href="https://wa.me/5511977346175" target="_blank" rel="noopener">WhatsApp <i aria-hidden="true">↗</i></a></li>
      </ul>
    </div>
  </nav>
</div>
```

O HTML sai de `ds/prova/comum.py`, função `cabecalho`. Estilo em `assets/ds/componentes.css`, seções Base (`.pular`) e Header e Sheet (`.header`, `.marca`, `.menu-botao`, `.sheet`). Comportamento em `assets/ds/componentes.js`, bloco 2.

**O que falta no código.**

- Resolvido na Onda 1. Os tempos da abertura são tokens, a altura da barra é `altura-cabecalho`, os links do Contato são Links `externo` com a seta escondida do leitor de tela, e o menu fecha quando o foco sai dele.
- O gerador recebe o texto do pular (`pular`) e a página atual (`atual`), que leva `aria-current="page"` no menu. Sem `aqui` nenhum item fica marcado, como na vitrine. Resolvido no passo 0 da Fase 6.
