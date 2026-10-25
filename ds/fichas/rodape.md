# Rodapé

`Footer` · a parada de tinta que fecha toda página, com o convite para conversar, as páginas e o voltar ao topo.

## Use quando

Toda página do site, no fim, depois do `main`, sempre igual. Quem chegou ao fim precisa de um próximo passo, que é conversar ou ver outra página. É parte fixa da receita de Toda página (ver `ds/RECEITAS.md`).

## Não use quando

- O fechamento é do caso, com o convite e o Próximo caso. Ele mora dentro do Resultado, como texto e Botão, e muda de página para página. O Rodapé é o mesmo em todas.
- A página quer outra área na tinta. O Rodapé não conta na regra da parada de tinta (D4). A da página é o Destaque.
- O destino é uma parte da página. Use Sumário. Voltar ao topo é a única exceção, e é um Link `topo`.
- A ideia é uma coluna de links de fora. O Rodapé tem duas saídas, WhatsApp e LinkedIn, ambas na chamada. A coluna "Fora daqui" do site de hoje sai.

## Anatomia

1. Caixa, `footer.footer.superficie-tinta`, com `div.container` dentro. Obrigatória.
2. Chamada, `div.footer__chamada`, obrigatória. O título `h2.t-titulo`, o Botão para o WhatsApp e o Link `externo` para o LinkedIn, nessa ordem.
3. Páginas, `nav.footer__col` com `aria-label="Páginas"`, obrigatória. O rótulo "Páginas" num `p.t-rotulo` e a lista de Links, Home e os casos na ordem da fila. A página atual leva `aria-current="page"`, perde o sublinhado e ganha peso 700.
4. Linha de baixo, `div.footer__meta`, obrigatória. A assinatura "Jeff Maia · São Paulo, Brasil" em `t-rotulo` à esquerda e o Link `topo`, "Voltar ao topo", à direita.

A chamada e as páginas dividem a `div.footer__grade`. Uma coluna no celular, e dois terços mais um terço a partir de 720px.

## Variantes

Uma forma só, sempre na superfície tinta. Dentro dela `foreground`, `border` e `ring` viram papel, e o Botão e os Links funcionam sem regra própria. O único acento é o lime de fundo do Botão (ver a ficha do Botão).

## Limites

- Um por página, sempre o último bloco.
- Um Botão, o do WhatsApp.
- Título da chamada de até três linhas em 390px.
- As páginas são a mesma lista do menu, na mesma ordem, até seis.
- Nenhum ícone nem ilustração. O que o Rodapé precisa dizer cabe no texto.

## Comportamento

1. **Mouse.** O Botão inverte para papel com texto em tinta e a seta anda. Os Links ganham o acento como marca texto atrás das palavras, com o texto em tinta. A seta do `externo` anda na diagonal e a do `topo` sobe. Tudo em `dur-media` com `ease-saida`.
2. **Toque.** No `:active` o Botão desce 2px e os Links ganham a marca texto em `dur-rapida`. Onde o ponteiro é o dedo, todo alvo tem pelo menos `alvo` (44px). Com mouse, os Links da lista de páginas têm 32px.
3. **Foco.** O anel de 2px em `ring`, que na tinta é papel.
4. **Movimento.** Voltar ao topo rola até o começo da página. Quando o Rodapé entra na tela, o trilho do Sumário sai de cena para não cobrir o que está nele.
5. **Sem JS.** Igual. Voltar ao topo pula direto.
6. **Movimento reduzido.** As transições vão a zero e Voltar ao topo pula, sem rolar.

## Acessibilidade

- O `footer` é a região de informação da página. O título da chamada é um `h2` e entra na navegação por títulos.
- A lista das páginas é uma `nav` com nome próprio, "Páginas", para não se confundir com o menu ("Principal"). O rótulo é parágrafo, não título, e a lista não entra na navegação por títulos debaixo da chamada.
- A página atual não depende de cor. Perde o sublinhado e ganha peso.
- As setas ficam escondidas do leitor de tela. WhatsApp e LinkedIn abrem em outra aba com `rel="noopener"`.
- Papel sobre tinta passa com folga, e tinta sobre o lime do Botão também. Ver `ds/CONTRASTE.md`.

## Onde aparece

- A Home, os quatro casos, o modelo de Caso e a vitrine. "Quer conversar sobre um problema parecido?", o Botão "WhatsApp +55 11 97734-6175", o Link "linkedin.com/in/maiajeff", as páginas e "Voltar ao topo".
- Nas páginas publicadas, o Rodapé de contato (`.footer`) das cinco páginas, com a coluna "Fora daqui" e o Voltar ao topo sentado no morro da onda.

## Vizinhos

- **Fechamento do caso.** O convite e o Próximo caso dentro do Resultado, que mudam por página.
- **Destaque na tinta.** A parada de tinta da página, no meio do conteúdo.
- **Cabeçalho.** Leva às mesmas páginas, do topo e a qualquer momento.

## Par nos posts

Fechamento, a última página do carrossel, com a chamada e o contato.

## Código

```html
<footer class="footer superficie-tinta">
  <div class="container">
    <div class="footer__grade">
      <div class="footer__chamada">
        <h2 class="t-titulo">Quer conversar sobre&nbsp;um&nbsp;problema parecido?</h2>
        <a class="button" href="https://wa.me/5511977346175" target="_blank" rel="noopener">WhatsApp +55 11 97734-6175 <span aria-hidden="true">↗</span></a>
        <a class="link" data-variant="externo" href="https://www.linkedin.com/in/maiajeff/" target="_blank" rel="noopener">linkedin.com/in/maiajeff <i aria-hidden="true">↗</i></a>
      </div>
      <nav class="footer__col" aria-label="Páginas">
        <p class="t-rotulo">Páginas</p>
        <ul>
          <li><a class="link" href="index.html">Home</a></li>
          <li><a class="link" href="case-omnichat.html" aria-current="page">Omnichat</a></li>
          <!-- um Link por página, na ordem do menu -->
        </ul>
      </nav>
    </div>
    <div class="footer__meta">
      <span class="t-rotulo">Jeff Maia · São Paulo, Brasil</span>
      <a class="link" data-variant="topo" href="#top">Voltar ao topo <i aria-hidden="true">↑</i></a>
    </div>
  </div>
</footer>
```

O HTML sai de `ds/prova/comum.py`, função `rodape`. Estilo em `assets/ds/componentes.css`, seção Footer (`.footer`), e a altura de toque no bloco `@media (pointer: coarse)`. A tinta mora em `assets/ds/tokens.css`, `.superficie-tinta`. Não tem script próprio. `#top` não precisa de um elemento com esse `id`, porque o navegador entende como o começo da página.

**O que falta no código.**

- Resolvido na Onda 1. A página atual perde o sublinhado e ganha peso (`.footer__col a[aria-current="page"]`), o rótulo virou "Páginas" num parágrafo, e a `nav` também se chama "Páginas", porque a lista começa pela Home.
