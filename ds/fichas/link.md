# Link

`Link` · leva a outro lugar sem ser a ação principal. Sempre sublinhado, no meio do texto ou sozinho com uma seta que diz a direção.

## Use quando

- **Um destino no meio de uma frase.** O leitor segue lendo e o link está ali, sublinhado. Use sem variante.
- **Um destino sozinho, que não é a ação principal do trecho.** Voltar, seguir para outra página, sair do site ou subir até o topo. Use a variante que diz a direção.

## Não use quando

- É a ação principal do trecho, como ir para o próximo caso ou chamar no WhatsApp. Use Botão.
- É um item do menu. Use o item do Cabeçalho, que tem a sua própria marca.
- É uma Seção da mesma página. Use o Sumário. O Link `topo` é a única exceção, porque subir não é ir a uma Seção.
- Não leva a lugar nenhum, só nomeia. Use Etiqueta.
- O texto do link seria "clique aqui" ou "saiba mais". Reescreva a frase até o destino ter nome.

## Anatomia

1. Caixa, `a.link`, obrigatória. Sempre um `<a>` com `href`. Nunca um `button` com cara de link.
2. Texto, obrigatório. Diz o destino ("Ver o caso", "linkedin.com/in/maiajeff", "Voltar ao topo").
3. Seta, só nas variantes. Um `i` com `aria-hidden="true"`. Antes do texto no `voltar`, depois do texto nas outras.

## Variantes

| `data-variant` | Seta | Quando |
| --- | --- | --- |
| sem atributo | nenhuma | No meio do texto corrido |
| `voltar` | `←` antes do texto | Voltar a uma página de onde se veio |
| `seguir` | `→` depois do texto | Ir a outra página do site, sem ser a ação principal |
| `externo` | `↗` depois do texto | Sair do site. Abre em outra aba |
| `topo` | `↑` depois do texto | Voltar ao começo da página |

Com variante, o Link vira um bloco em linha, com a seta separada do texto por `space-8`. Por isso a variante não entra no meio de uma frase, onde ela impediria a quebra de linha. Um link para fora no meio do texto fica sem variante e sem seta.

Na superfície tinta o sublinhado e o texto viram papel, porque pedem `foreground`. O marca texto continua no acento, e o texto sobre ele volta a ser tinta.

## Limites

- Texto de até uma linha em 390px quando tem variante. No meio do texto, o tamanho é o da frase.
- Um Link `voltar` por página, no começo dela.
- Um Link `topo` por página, na linha de baixo do Rodapé.
- Até três Links com variante seguidos. Mais que isso é uma lista de navegação, e mora no Cabeçalho ou no Rodapé.

## Comportamento

1. **Mouse.** O acento corre da esquerda para a direita por trás das palavras, como um marca texto, e o texto fica em tinta. A seta anda na direção dela, 4px no `seguir` e no `voltar`, 3px para cima no `topo` e na diagonal no `externo`. Tudo em `dur-media` com `ease-saida`.
2. **Toque.** No `:active` o marca texto aparece em `dur-rapida`. Com variante, onde o ponteiro é o dedo, o alvo tem pelo menos `alvo` (44px). No meio do texto o alvo é a linha da frase, a única exceção do site aos 44px.
3. **Foco.** O anel de 2px em `ring`, afastado 3px. O marca texto não aparece no foco, para o anel não competir com ele.
4. **Movimento.** O marca texto e a seta mudam com transição, e nada troca seco. O `topo` rola até o começo da página.
5. **Sem JS.** Nada muda. É um link nativo.
6. **Movimento reduzido.** As transições vão a zero. O marca texto aparece inteiro de uma vez, e o `topo` pula sem rolar.

## Acessibilidade

- O sublinhado está sempre lá. No toque não existe hover para revelar que algo é clicável, e a cor sozinha não diria nada, porque o link tem a mesma cor do texto.
- O nome do link é o texto. A seta fica escondida do leitor de tela.
- O `externo` abre em outra aba com `target="_blank"` e `rel="noopener"`. O texto diz o destino ("WhatsApp", "linkedin.com/in/maiajeff"), e quem ouve sabe que sai do site.
- A página atual, numa lista de Links, leva `aria-current="page"` e uma marca que não é só cor (ver o Rodapé).
- Tinta sobre papel, papel sobre tinta e tinta sobre o acento passam com folga.

## Onde aparece

- Modelo de Caso, no fechamento, sem variante no meio da frase. "me chama no WhatsApp".
- Modelo de Caso, no Rodapé. "linkedin.com/in/maiajeff" como `externo`, as páginas sem variante e "Voltar ao topo" como `topo`.
- Modelo de Caso, no menu. "LinkedIn" e "WhatsApp" como `externo`.
- Vitrine, "Ver a ficha" e "Abrir em página inteira" como `seguir`, e "Vitrine" como `voltar` nas páginas de ficha.
- Nas páginas publicadas, o Link (`.link`), o Link solto (`.link-solto`, "Abrir o protótipo completo ↗" no Inpulse e "Abrir o mapa completo ↗" no Mapa) e o Voltar para os casos (`.voltar`, "← Todos os casos") dos quatro casos.

## Vizinhos

- **Botão.** A ação principal do trecho, numa pílula.
- **Item do Cabeçalho.** Navegação entre páginas, dentro do menu.
- **Etiqueta.** A mesma pílula do Botão, sem levar a lugar nenhum.

## Par nos posts

Sem par. No post ninguém clica, e o destino vai escrito na legenda.

## Código

```html
<!-- No meio do texto -->
<p>Se esse tipo de camada é um problema no seu produto, <a class="link" href="https://wa.me/5511977346175" target="_blank" rel="noopener">me chama no WhatsApp</a> ou veja o próximo caso.</p>

<!-- Sozinho, com direção -->
<a class="link" data-variant="voltar" href="index.html"><i aria-hidden="true">←</i> Todos os casos</a>
<a class="link" data-variant="seguir" href="case-omnichat.html">Ver o caso <i aria-hidden="true">→</i></a>
<a class="link" data-variant="externo" href="https://www.linkedin.com/in/maiajeff/" target="_blank" rel="noopener">linkedin.com/in/maiajeff <i aria-hidden="true">↗</i></a>
<a class="link" data-variant="topo" href="#top">Voltar ao topo <i aria-hidden="true">↑</i></a>
```

Estilo em `assets/ds/componentes.css`, seção Link (`.link`), e a altura de toque no bloco `@media (pointer: coarse)`. O marca texto é o mesmo do item do menu, do item do Sumário e da marca do Cabeçalho. Não tem script.

**Decidido.** O link no meio do texto não chega a 44px no toque, porque o alvo é a linha da frase. É a exceção que a WCAG aceita para links dentro de texto (critério 2.5.8), e ela está escrita na regra do site, no `CLAUDE.md` e nos Fundamentos.
