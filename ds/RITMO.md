# Regras de ritmo

O equivalente do guia de variação dos posts. O guia de decisão diz qual componente serve para uma ideia. Estas regras dizem como os componentes se combinam numa página e de um caso para o outro, para o leitor não reconhecer o molde antes de ler o conteúdo.

## Peso

Toda peça tem um peso, como nos posts. É ele que regula o ritmo.

| Peso | O que é | Exemplos |
| --- | --- | --- |
| Leve | Texto no papel, sem caixa | Contexto, parágrafos, Link, Passos |
| Médio | Caixa no papel ou no `muted`, ícones | Cartões, Antes e depois, Abas, Dado em grupo, Gráfico |
| Forte | Acento chapado em área grande, tinta, número no degrau `numero` | Dado `salto`, Destaque na tinta, Imagem `sangria` |

## Na página

1. **Uma parada de tinta.** Além do rodapé, só uma área da página fica na tinta (D4). No Caso é o Destaque do Resultado.
2. **Um forte além do topo.** O topo já tem o Salto. No resto da página cabe um peso forte, e no Caso ele é a parada de tinta. Uma Imagem `sangria` entra no lugar dela, nunca junto.
3. **Um Destaque por página.** A frase que fica é uma só. Destaque `nota` e `atrito`, quando existirem, são médios e cabem até dois.
4. **Texto antes da peça.** Toda seção abre com texto. Duas peças médias seguidas, sem texto entre elas, só no Resultado, onde o Dado em grupo e o Destaque fecham a conta juntos.
5. **Três parágrafos no máximo** antes de uma peça. Passou disso, a seção está contando duas coisas e vira duas seções.
6. **Medida de leitura.** Texto corrido com no máximo 66 caracteres por linha, em qualquer largura de tela.
7. **Um acento.** A página inteira usa o acento declarado no `html`. Os outros dois não aparecem, nem em ícone. A única exceção é o Botão, que é sempre lime.
8. **Um ícone, uma vez.** Fora do Sumário, o mesmo ícone não se repete na página. No Sumário cada seção tem o seu.
9. **Uma ilustração de cena por caso**, no Topo, presa ao indicador. O resto da página fala com ícones.
10. **Um conjunto de Abas por página.**

## Entre seções

11. **Peso alternado.** Duas seções seguidas não fecham com a mesma peça. Se a forma precisa se repetir, o arranjo muda (por exemplo, dois Cartões `meio` numa seção e um `dois-tercos` com quatro `terco` na seguinte) e o acento chapado entra em só uma delas.
12. **De quatro a seis seções numeradas** no Caso, contando Contexto e Resultado. Menos que isso o Sumário não tem o que mostrar. Mais que isso o trilho do celular não cabe.

## Entre casos

13. **Acento.** Dois casos seguidos na fila nunca têm o mesmo acento. A fila de hoje cumpre (lime, azul, verde, azul, e volta ao lime).
14. **Seção 02 diferente.** Os quatro casos não abrem o meio com a mesma peça. Se o Omnichat mostra o problema em Cartões, o próximo mostra com outra coisa.
15. **Fechamento.** O texto do Destaque e o convite mudam com o caso. O convite fala do tipo de problema que o caso resolve, nunca uma frase genérica de contato.

## Checklist antes de publicar

1. O acento do `html` é o do caso, e nenhum outro acento aparece além do lime do Botão?
2. Há só uma parada de tinta além do rodapé, e um Destaque só?
3. Toda seção abre com texto, e nenhuma tem mais de três parágrafos antes da peça?
4. Duas seções seguidas fecham com a mesma peça no mesmo arranjo?
5. Algum ícone se repete fora do Sumário?
6. A seção 02 abre com a mesma peça do caso anterior na fila?
7. Todo hover está dentro de `(hover: hover) and (pointer: fine)`, e todo alvo de toque tem 44px?
8. Toda troca de estado tem movimento, e a página funciona sem JS e com movimento reduzido?
9. Nenhum título termina linha com palavra curta de ligação?

## Onde o modelo de Caso esbarra nestas regras

O Problema e o Processo da variação 4 fecham as duas com Cartões em mosaico. A regra 11 deixa passar, porque o arranjo muda (dois `meio` e depois um `dois-tercos` com quatro `terco`) e só o Processo tem o acento chapado. Se você achar que é repetição demais, o Problema é o candidato a trocar de peça.
