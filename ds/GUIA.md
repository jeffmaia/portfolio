# Guia de decisão

Qual componente para qual ideia. É a primeira coisa a ler antes de montar uma seção nova, e o equivalente do "Imagem única, qual usar" dos posts.

O caminho é sempre o mesmo. Comece pelo que a seção precisa mostrar, ache a linha na tabela, confira o Não use quando da ficha e só então escolha a variante. Nunca comece pela forma que ficaria bonita.

Se nenhuma linha serve, não invente uma peça na página. Escreva a ficha do componente novo em `ds/fichas/`, seguindo `_modelo.md`, e traga para aprovar antes do código.

## O que não se escolhe

Estas peças estão em toda página de caso, sempre no mesmo lugar, e não passam por este guia. Quem diz onde ficam são as receitas, em `ds/RECEITAS.md`.

- **Cabeçalho**, com o menu (Sheet).
- **Sumário**, das seções do caso.
- **Seção**, a moldura de cada parte, com rótulo numerado e título.
- **Rodapé**, na tinta.

## A seção precisa mostrar

| A seção precisa mostrar | Use | E não |
| --- | --- | --- |
| O número que prova o caso, com o valor de antes | Dado, `salto` | Dado no grupo, que perde o antes |
| Os números que fecham a conta, de dois a quatro | Dado em grupo | Gráfico, que pede série ou proporção |
| Um número sem antes, sozinho numa seção | Dado | Destaque, que é para frase |
| Uma frase que o leitor precisa levar embora | Destaque | Texto em negrito, que some no parágrafo |
| O que o caso deixa, no fim | Destaque na tinta | Um segundo Destaque no papel |
| O que deu errado no caminho e a regra que nasceu disso | Destaque, `atrito` | Linha de nota, que é para o que destravou |
| O que destravou uma etapa, em uma ou duas linhas | Destaque, `nota` | Um parágrafo a mais no texto |
| A mesma coisa antes e depois, em uma dimensão | Antes e depois | Duas colunas de texto, que escondem o paralelo |
| Uma mudança em várias dimensões ao mesmo tempo | Antes e depois, `confronto` | Antes e depois simples, que vira dois blocos longos |
| A mesma interação antes e depois da solução | Antes e depois, `conversa` | Confronto, que perde o ritmo da troca |
| A fala de quem usou, com autoria | Antes e depois, `citacao` | Destaque, que é a voz do caso e não do usuário |
| Etapas em ordem, com texto longo em cada uma | Passos | Abas, que escondem a ordem |
| Duas coisas que acontecem ao mesmo tempo | Passos, `par` | Passos simples, que faz a segunda parecer depois da primeira |
| Entrada, o que acontece no meio e saída | Passos, `estagios` | Três Cartões com setas, que dão o mesmo peso ao meio |
| Etapas em que cada uma filtra a anterior | Passos, `funil` | Passos simples, que não mostra o estreitamento |
| Um caminho curto de três marcos | Passos, `trilha` | Passos simples, que vira lista |
| Ritos de time e o que mudou em cada um | Passos, `ritos` | Cartões, que dão peso de destaque a cada rito |
| De dois a seis itens do mesmo tipo, para passar os olhos em todos | Cartões em mosaico | Abas, que mostram um de cada vez |
| De três a seis itens longos, para ler um de cada vez | Abas | Cartões, que empurram a página para baixo |
| Os dados do projeto (duração, papel, time) | Cartão `muted` com a ficha | Etiquetas, que são para assunto |
| O assunto do caso | Etiquetas | Rótulo solto, que não agrupa |
| Uma grandeza antes e depois, em tempo ou quantidade | Gráfico, `barras` | Dois Dados, que não mostram a proporção |
| Proporção de respostas entre grupos | Gráfico, `pilhas` | Barras soltas, que perdem o total de cada grupo |
| Posição numa escala com sinal, antes e depois | Gráfico, `escala` | Dois Dados, que escondem onde fica o zero |
| Uma tela ou protótipo | Imagem, `moldura` | Imagem sem moldura, que flutua no papel |
| Várias telas na ordem do percurso | Imagem, `galeria` | Abas, que escondem a sequência |
| Uma imagem que é ambiente, não objeto | Imagem, `sangria` | Moldura, que a transforma em tela |
| A ação principal do trecho | Botão | Link, que some ao lado do texto |
| Um destino no meio do texto, ou voltar, seguir, sair, subir | Link e as variantes | Botão, que disputa com a ação principal |

## Qual forma, dentro de cada componente

A tabela acima já aponta a variante. Esta parte diz o que existe no código hoje e o que entra na Fase 5. Variante prevista se escreve na ficha antes de existir na página.

| Componente | No código hoje | Prevista |
| --- | --- | --- |
| Botão | `primary`, `outline` | |
| Link | sem variante, `voltar`, `seguir`, `externo`, `topo` | |
| Etiqueta | papel, `acento`, `tinta` | |
| Seção | uma forma só | |
| Cartão | papel, `muted`, `acento`, grupo `mosaico` com `meio`, `terco` e `dois-tercos` | |
| Dado | sozinho, `salto`, grupo em mosaico com ícone | |
| Passos | padrão, `par` | `estagios`, `funil`, `trilha`, `ritos` |
| Abas | vertical | |
| Antes e depois | lados, conversa | `confronto`, `citacao` |
| Destaque | frase, na tinta | `nota`, `atrito`, frase no papel |
| Gráfico | | `barras`, `pilhas`, `escala` |
| Imagem | | `moldura`, `galeria`, `sangria` |
| Sumário | coluna fixa, trilho abaixo de 1100px | |
| Cabeçalho e Rodapé | uma forma | |

## As três escolhas que mais confundem

**Cartões em mosaico, Abas ou Passos.** As três mostram vários itens. A pergunta é como o leitor vai ler.
- Se a ordem é o assunto, Passos.
- Se ele precisa ver todos antes de escolher qual ler, Cartões em mosaico. É a escolha do modelo de Caso para as cinco camadas do Omnichat, porque a página é feita para quem escaneia antes de ler.
- Se cada item é longo e ele vai ler um ou dois, Abas.

**Dado, Destaque ou Gráfico.** As três chamam o olho no meio do texto.
- Um valor, com uma frase que diz de onde veio, é Dado.
- Uma frase, sem número, é Destaque.
- Um valor que só se entende ao lado de outros, numa série ou numa escala, é Gráfico.

**Botão ou Link.** Há um Botão `primary` por trecho, e ele é a ação que leva adiante. Tudo o mais que leva a outro lugar é Link.

## O que a Fase 4 resolveu

- **Seção.** Ficou com a forma do modelo de Caso, numa coluna só ao lado do Sumário, e a `lado` saiu.
- **Mosaico.** Virou o grupo de Cartões (`data-layout="mosaico"`), com os tamanhos em `data-tamanho`. O Dado em grupo mora nele.
