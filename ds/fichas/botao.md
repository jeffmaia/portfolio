# Botão

`Button` · a ação mais importante de um trecho da página, numa pílula com contorno de tinta e o lime no fundo.

## Use quando

Existe uma ação que leva adiante e ela é a principal daquele trecho. No fechamento do caso, ir para o próximo. No rodapé, chamar no WhatsApp. O leitor precisa achar essa ação sem procurar.

## Não use quando

- O destino está dentro de uma frase. Use Link, que fica sublinhado no meio do texto.
- A ação é voltar para os casos, seguir para uma seção, sair do site ou voltar ao topo. Use Link com a variante certa (`voltar`, `seguir`, `externo`, `topo`).
- Já existe um Botão `primary` no mesmo trecho. O segundo vira `outline` ou vira Link.
- Não há ação nenhuma, só um rótulo. Use Etiqueta.
- É um item do menu. Use o item do Cabeçalho, que tem a sua própria marca.

## Anatomia

1. Rótulo, obrigatório. Diz o destino ou o verbo, nunca "clique aqui". Quando o destino tem nome, ele entra depois de uma vírgula ("Próximo caso, Inpulse").
2. Seta, opcional, num `span` com `aria-hidden="true"` depois do rótulo. `→` para seguir dentro do site, `↗` para sair dele.

O elemento é `<a>` quando o Botão leva a outra página e `<button>` quando age na própria página. Nunca um `div`.

## Variantes

| `data-variant` | Como fica | Quando |
| --- | --- | --- |
| sem atributo (`primary`) | Fundo `primary` (lime), texto e contorno em tinta | A ação principal do trecho |
| `outline` | Fundo transparente, texto e contorno em `foreground` | A segunda ação, quando ela precisa ter cara de botão |

O fundo do `primary` é sempre lime, também nos casos de acento azul ou verde. É a regra 2 do plano, em que `primary` aponta para o lime. O acento da página fica com as Etiquetas, os Cartões e o Dado.

Na superfície tinta o contorno vira papel, porque `border` troca por dentro. O fundo lime e o texto em tinta continuam iguais.

## Limites

- Um `primary` por trecho. Numa página de caso são dois no total, o do fechamento e o do rodapé.
- O rótulo cabe numa linha em 390px. Na prática, até umas cinco palavras.
- O contorno é sempre tinta (ou papel na superfície tinta). O acento nunca vira a borda nem o texto.

## Comportamento

1. **Mouse.** O Botão inverte, com fundo em `foreground` e texto em `background`, e a seta anda 3px para a direita. Tudo em `dur-media` com `ease-saida`.
2. **Toque.** No `:active` ele desce 2px em `dur-rapida`. Onde o ponteiro é o dedo a altura mínima é `alvo` (44px). Com mouse, 40px.
3. **Foco.** O anel de 2px em `ring`, afastado 3px. Nada mais muda.
4. **Movimento.** Fundo, cor e seta mudam com transição. Nenhum estado troca seco.
5. **Sem JS.** Nada muda, é um link ou um botão nativo.
6. **Movimento reduzido.** As transições vão a zero. A inversão de cor continua, só que instantânea.

**Desabilitado.** Com `disabled` ou `aria-disabled="true"`, o contorno vira tracejado e a opacidade cai a 60%. A forma muda, não só o tom, e o hover e o pressionado deixam de existir.

## Acessibilidade

- O nome é o rótulo. A seta fica escondida do leitor de tela.
- Quando sai do site (`↗`), abre em outra aba com `target="_blank"` e `rel="noopener"`. O rótulo diz para onde vai ("WhatsApp"), então quem ouve sabe que sai.
- Num `<a>` desabilitado, `aria-disabled="true"` e nada de `href`, para não ser seguido pelo teclado.
- Texto em tinta sobre lime passa com folga. Ver `ds/CONTRASTE.md`.

## Onde aparece

- Modelo de Caso, no fechamento. "Próximo caso, Inpulse".
- Modelo de Caso, no rodapé, sobre a tinta. "WhatsApp +55 11 97734-6175".
- Nas páginas publicadas, o Botão principal (`.btn-green`) está no rodapé das cinco páginas. O Próximo caso de hoje (`.proximo-link`) é um link solto, e vira Botão na migração.

## Vizinhos

- **Link.** Leva a outro lugar sem ser a ação principal, ou mora dentro do texto.
- **Etiqueta.** Tem a mesma pílula, mas não age.
- **Item do Cabeçalho.** Navegação entre páginas, dentro do menu.

## Par nos posts

TagCard, a tag preenchida com o acento. No post ninguém clica, então o par é só de forma.

## Código

```html
<!-- Leva a outra página -->
<a class="button" href="case-inpulse.html">Próximo caso, Inpulse <span aria-hidden="true">→</span></a>

<!-- Sai do site -->
<a class="button" href="https://wa.me/5511977346175" target="_blank" rel="noopener">WhatsApp +55 11 97734-6175 <span aria-hidden="true">↗</span></a>

<!-- Segunda ação -->
<a class="button" data-variant="outline" href="#">Rótulo <span aria-hidden="true">→</span></a>

<!-- Age na página, desabilitado -->
<button class="button" type="button" disabled>Rótulo</button>
```

Estilo em `assets/ds/componentes.css`, seção Button (`.button`), e a altura de toque no bloco `@media (pointer: coarse)`. Não tem script.

**O que falta no código.** Nada para o uso atual. A variante `outline` ainda não aparece em nenhuma página.
