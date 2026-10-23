# Receitas de página

Uma receita é a ordem dos componentes numa página e onde cada um senta na grade. Não tem cor nem forma própria. O que pode variar de um caso para outro está marcado como livre, o resto é fixo.

São duas receitas, a do Caso e a da Home. A do Caso sai do modelo aprovado, `ds/prova/variacoes/v4.html`. A da Home é a direção para a Fase 6, e ainda não foi provada numa página.

## Toda página

**A cabeça do HTML.** Nesta ordem, sem pular nenhuma.

1. `<html lang="pt-BR" data-acento="…">`, com o acento do caso (D5). A Home usa `lime`.
2. O script de uma linha que põe a classe `js` e, quando se chega pelo voltar do navegador, a classe `volta`. Ele precisa vir antes de qualquer folha de estilo, porque é ele que faz o carregamento rodar ao contrário na volta. O texto está em `ds/prova/comum.py`, função `cabeca`.
3. `<title>` com o nome da página e "Jeff Maia".
4. Fontes, `assets/ds/tokens.css` e `assets/ds/componentes.css`.

**O corpo.** Sempre nesta ordem.

1. O Carregamento em camadas (`.carga`), que é decorativo e fica escondido do leitor de tela.
2. Pular para o conteúdo.
3. Cabeçalho, com o menu. A página atual leva `aria-current="page"` no menu e no rodapé.
4. `<main id="conteudo">`, com a receita da página.
5. Rodapé na tinta.
6. `assets/ds/componentes.js` no fim do corpo.

## Caso

O caso é feito para quem escaneia antes de ler. O Sumário diz onde se está, e o conteúdo vem em blocos de tamanhos diferentes.

### A grade

A partir de 1100px, o Sumário fica fixo numa coluna de 260px à esquerda e o conteúdo ocupa o resto. Abaixo disso a página tem uma coluna só, e o Sumário vira o trilho na borda direita.

Dentro do conteúdo, os blocos sentam num mosaico de seis colunas. Os tamanhos são `meio` (3), `terco` (2) e `dois-tercos` (4). No celular todo bloco ocupa a largura inteira.

### A ordem

| | Parte | Componentes | Fixo ou livre |
| --- | --- | --- | --- |
| 1 | Sumário | Sumário, com um ícone do acento por seção | Fixo. Os nomes das seções são livres |
| 2 | Topo do caso | Etiquetas, título (`h1`, `t-display`), frase de apoio (`t-sub`), Cartão `muted` com a ficha do projeto, Cartão do acento com o Dado `salto` e a ilustração do caso | Fixo |
| 3 | Contexto | Rótulo "01 · Contexto" e um parágrafo em `t-lead`. Sem título e sem componente | Fixo |
| 4 | Seções do meio | Rótulo numerado, título (`h2`, `t-titulo`), até três parágrafos e uma peça escolhida pelo guia | Livre, de duas a quatro seções |
| 5 | Resultado | Rótulo, título, texto, o Dado em grupo e o Destaque na tinta | Fixo. O Destaque é a parada de tinta da página |
| 6 | Fechamento | Um parágrafo com o convite e um Link para o WhatsApp, e o Botão para o próximo caso | Fixo |

### O Topo do caso

- **Etiquetas.** De duas a três. As primeiras ficam no papel, a última, que é o assunto mais específico, leva o acento.
- **Título.** Diz o que foi feito, não o nome do projeto. Até quatro linhas no celular.
- **Frase de apoio.** Diz onde estava o problema de verdade. Até três linhas no desktop.
- **Ficha do projeto.** Sempre Duração, Jeff e Time, nessa ordem. Em Jeff vai o papel e a responsabilidade numa frase só.
- **Salto.** O número que a página promete, com a frase que diz como foi medido. A ilustração da cena fica ao lado, presa ao indicador.

No desktop o título e a frase ocupam quatro das seis colunas e a ficha as outras duas. O Salto desce para a linha inteira. Entre 720 e 1099px a ficha e o Salto dividem a linha ao meio.

### As seções

- Cada seção é um `<section>` com `id`, rotulada pelo título com `aria-labelledby`. O Contexto, que não tem título, é rotulado pelo rótulo.
- O rótulo é número e nome com ponto do meio ("02 · O problema"), e o nome é o mesmo do Sumário.
- Toda seção abre com texto. A peça vem depois do texto, nunca antes.
- Os blocos que entram abaixo da dobra levam `data-revelar`. O Topo do caso não leva, porque já está na tela.

### O fechamento

O Destaque na tinta carrega o que o caso deixa, com a Etiqueta "O que eu levo daqui" no acento. Depois dele, o convite em texto, com o Link para o WhatsApp no meio da frase, e o Botão "Próximo caso, Nome". A fila dos casos é Processo, Omnichat, Inpulse, Mapa e volta ao Processo.

### Acento por caso

| Caso | Acento |
| --- | --- |
| Processo com IA | lime |
| Omnichat | azul |
| Inpulse | verde |
| Mapa de experiência | azul |

Ícones, Etiqueta do assunto, Cartões do acento, o Salto e a aba ou o item escolhido usam o acento do caso. O Botão continua lime (ver a ficha do Botão).

## Home

Direção para a Fase 6. Entra com o hero e a Lista de casos construídos na Fase 5.

| | Parte | Componentes |
| --- | --- | --- |
| 1 | Hero | A frase "O ofício continua o mesmo. O jeito de fazer, não." à esquerda, em 7 colunas, e a ilustração do esboço que sobra nas outras 5. Abaixo da frase, a linha de apoio sobre o que o Jeff faz |
| 2 | Lista de casos | Um Cartão por caso, na ordem da fila |
| 3 | Rodapé | Igual ao do caso |

**Hero.** A especificação inteira está em `ds/PLANO.md`, na seção Hero. Movimento ligado à rolagem, camadas saindo em escada e o esboço parado. Sem JS ou com movimento reduzido, a vista explodida parada. No celular a frase vem primeiro e a ilustração entra abaixo, menor.

**Lista de casos.** Ocupa o lugar da Cena dos casos, que saiu. Cada Cartão leva o acento do próprio caso (`data-acento` no Cartão) e tem, nesta ordem, o título do caso como `h3`, a frase de apoio, o Dado `salto` em tamanho de grupo, a ficha compacta (papel e duração numa linha) e um Link `seguir`, "Ver o caso". Não há Botão dentro da lista. Quatro Botões lado a lado disputariam entre si, e a ação principal da Home é escolher um caso.

No desktop são dois Cartões por linha. No celular, um debaixo do outro.

**O que sai.** O convite ao manifesto (D7), a seta de descer e a cena com o orbe do número.

## Pontos em aberto

1. **Voltar para os casos.** A receita antiga do Topo começava com um Link `voltar`. O modelo de Caso não tem esse link, porque o Sumário e o menu já levam para fora. Com a Home virando lista, vale decidir se ele volta.
2. **Revelar.** O modelo de Caso foi gerado sem `data-revelar`. A receita pede, e a página da Fase 4 precisa trazer.
3. **Mosaico e Seção.** As duas formas que o Caso usa e que ainda moram só no CSS da variação 4 (ver `ds/GUIA.md`).
