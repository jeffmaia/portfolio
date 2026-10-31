# Arquivo

`CodeBlock` · um arquivo de texto mostrado como ele é, com o nome na barra e o componente que ele descreve logo acima.

## Use quando

- **O próprio arquivo é a prova.** O caso fala de um documento que alguém ou a IA lê, e mostrar o texto dele diz mais que descrever. No Design system, o MD do Modal, que diz à IA quando usar, como se comporta e como responde em cada tela.
- **O arquivo descreve um componente que se vê.** O componente vem em cima, como imagem, e o arquivo embaixo, para o leitor ligar uma coisa à outra.

## Não use quando

- É uma tela ou um protótipo, sem texto de arquivo. Use Imagem `moldura`.
- O texto é a voz de quem usou o produto. Use Antes e depois `citacao`.
- São etapas que produzem o arquivo. Use Passos `estagios`, e o Arquivo pode vir depois deles para mostrar a saída.
- O texto tem mais de umas quarenta linhas. Corte no trecho que prova o ponto. O arquivo inteiro não é leitura de caso.
- É uma frase que o leitor precisa levar embora. Use Destaque.

## Anatomia

1. Caixa, `figure.arquivo`, obrigatória.
2. Componente, `div.arquivo__componente` com o `img`, opcional. Moldura de tinta com raio e o `muted` por baixo, na largura inteira.
3. Documento, `div.arquivo__doc`, obrigatório. Contorno de tinta, raio e fundo `background`.
4. Barra, `p.arquivo__barra`, obrigatória. Fundo `muted`, o nome do arquivo em `span.arquivo__nome` e, opcional, uma Etiqueta à direita.
5. Texto, `pre.arquivo__texto`, obrigatório. O Markdown cru, em `font-codigo`, com as linhas de título em negrito (`b`).
6. Legenda, `figcaption.figure__legenda`, opcional. A mesma da Imagem.

## Variantes

Não tem `data-variant`. O que muda é o que entra.

| Forma | Como fica | Quando |
| --- | --- | --- |
| Com o componente | O componente em cima, na largura inteira, e o arquivo embaixo | O arquivo descreve algo que se vê |
| Sozinho | Só a barra e o texto | O arquivo não tem par visual |
| Com selo | Uma Etiqueta na barra | O arquivo não é o original. "Reconstituição", quando o original ficou com a empresa |

Não entra na superfície tinta. O Arquivo é peça média e mora no papel.

## Limites

- Um Arquivo por Seção, e conta como a Imagem da Seção (regra 10 do `ds/RITMO.md`).
- Até umas quarenta linhas de texto.
- Componente deitado ocupa a largura inteira. Lado a lado com o arquivo ele encolhia até não se ler, e por isso a peça é sempre empilhada.
- Quando o arquivo não é o original, o selo e a legenda dizem isso. Arquivo reconstituído sem aviso não entra.

## Comportamento

1. **Mouse.** Não tem. O Arquivo não é alvo.
2. **Toque.** Não tem, pelo mesmo motivo.
3. **Foco.** Não recebe foco. O texto quebra a linha e nunca abre rolagem para o lado, então não precisa de foco para rolar.
4. **Movimento.** Entra com o revelar da página. Nenhum movimento próprio.
5. **Sem JS.** Aparece pronto.
6. **Movimento reduzido.** Aparece pronto.

## Acessibilidade

- A caixa é uma `figure`, e a legenda dá o nome dela.
- O `img` do componente tem `alt` que descreve o que se vê, porque ele é prova e não enfeite.
- O texto é texto de verdade num `pre`, lido linha a linha pelo leitor de tela. Os `#` do Markdown ficam, porque são parte do arquivo.
- Tinta sobre papel e tinta sobre o `muted` passam com folga.

## Onde aparece

- Design system, Seção 03, "Os componentes passaram a nascer no código". O Modal no claro e no escuro, exportado do Figma, e o `modal.md` com o selo "Reconstituição". A legenda diz que o arquivo original ficou no repositório da Omnichat.

## Vizinhos

- **Imagem `moldura`.** Mostra uma tela. O Arquivo mostra um texto que se lê.
- **Passos `estagios`.** Mostram como o arquivo nasce. O Arquivo mostra o que saiu.
- **Destaque.** Uma frase para levar embora. O Arquivo é um documento inteiro.

## Par nos posts

Sem par. Os posts não mostram arquivos, e texto de código num carrossel ficaria abaixo do tamanho mínimo de leitura.

## Código

```html
<figure class="arquivo" data-revelar>
  <div class="arquivo__corpo">
    <div class="arquivo__componente"><img src="assets/casos/design-system/modal-claro-escuro.png" alt="O Modal do design system no tema claro e no escuro…" width="1198" height="451" loading="lazy" decoding="async"></div>
    <div class="arquivo__doc">
      <p class="arquivo__barra"><span class="arquivo__nome">modal.md</span><span class="badge">Reconstituição</span></p>
      <pre class="arquivo__texto"><b># Modal</b>

Sobreposição que interrompe o fluxo principal…</pre>
    </div>
  </div>
  <figcaption class="figure__legenda">O Modal, exportado do Figma, e o MD dele reconstituído…</figcaption>
</figure>
```

O HTML sai de `pecas.arquivo` em `ds/prova/pecas.py`, que recebe o Markdown cru e põe as linhas de título em negrito. Estilo em `assets/ds/componentes.css`, seção Arquivo (`.arquivo`), e o token `--font-codigo` em `assets/ds/tokens.css`. Não tem script além do revelar.
