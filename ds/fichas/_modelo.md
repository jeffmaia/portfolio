# Ficha modelo

Toda ficha de componente do site segue este molde. São dez campos fixos, sempre nesta ordem, e depois deles o código. O campo que mais pesa é o Não use quando, porque é ele que aponta para o vizinho certo.

Uma ficha por arquivo, em `ds/fichas/`, com o nome do componente em português e minúsculas (`botao.md`, `dado.md`). O título é o nome em português, e logo abaixo vem o nome do shadcn entre crases.

Copie o bloco abaixo e preencha. Campo que não se aplica fica escrito, com o motivo. Nunca some.

```markdown
# Nome

`NomeShadcn` · uma frase que diz o trabalho do componente na página.

## Use quando

A situação de conteúdo que pede este componente. Começa pelo que a seção
precisa mostrar, não pela forma.

## Não use quando

Cada caso em que parece servir e não serve, sempre com o vizinho que serve
no lugar. "A frase é a conclusão do caso, use Destaque."

## Anatomia

As partes, na ordem em que aparecem. Diga qual é obrigatória e qual é
opcional, e o elemento de HTML de cada uma.

## Variantes

Cada valor de data-variant (e de outros atributos de dados), o que muda e
quando escolher. Inclui como fica na superfície tinta.

## Limites

Números. Quantos por página, quantos itens, quantas linhas, largura de
texto. O que acontece quando passa do limite.

## Comportamento

Os estados e o movimento, sempre nesta ordem.
1. Mouse. O que o hover faz, dentro de (hover: hover) and (pointer: fine).
2. Toque. O que o :active faz e a altura do alvo.
3. Foco. O anel, e se o componente muda algo além dele.
4. Movimento. Cada troca de estado com o token de duração e de curva.
5. Sem JS. Como fica, e se continua inteiro.
6. Movimento reduzido. O que vai a zero e o que muda de forma.

## Acessibilidade

Papel e nomes para leitor de tela, ordem de teclado, o que é escondido e por
quê, contraste do que tem texto.

## Onde aparece

Páginas e trechos reais, com o texto que está lá. O modelo de Caso
(ds/prova/variacoes/v4.html) primeiro, depois as páginas publicadas.

## Vizinhos

Os componentes com quem ele mais se confunde, cada um com a diferença em
meia frase.

## Par nos posts

O componente do Jeff DS dos posts que faz o mesmo trabalho no carrossel, ou
"sem par" e o motivo.

## Código

O HTML canônico, pronto para copiar. Depois, onde mora o estilo e o
comportamento (arquivo e seletor), e o que ainda falta no código.
```

## Por que estes dez

São os dez campos aprovados no plano da Fase 0, com um ajuste. O Comportamento ganhou uma ordem fixa de seis itens, porque é nele que as regras do site moram e é onde uma ficha mais esquece algo. Hover só com mouse, toque com `:active` e 44px, movimento em toda troca de estado, e tudo funcionando sem JS e com movimento reduzido.

O Código fica fora da conta. Ele não explica uso, só entrega a peça.

## Regras de escrita da ficha

- Português do Brasil, frase curta, sem hífen, travessão ou dois pontos na escrita corrida.
- Valores sempre pelo nome do token (`dur-media`, `acento`, `alvo`), nunca o número solto. O número entra entre parênteses quando ajuda a ler.
- Exemplos com o texto real das páginas, nunca inventado.
- Um campo não repete outro. Se o limite já diz "um por página", a anatomia não diz de novo.
