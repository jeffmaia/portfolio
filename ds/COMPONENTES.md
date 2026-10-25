# Componentes, revisitados

A Fase 1 contou 54 peças e chegou a 29 componentes juntando as parecidas. Ainda é muito, e o motivo é que a conta partiu do site de hoje. Boa parte das peças existe para sustentar a identidade antiga (a onda, a trama, o verde marca texto, a cena com orbe) e perde a razão de ser quando o site passa para o Jeff DS.

Esta revisão parte do outro lado. A pergunta não é "como junto as 54", é "do que um caso precisa para contar a história dele no Jeff DS". A resposta são **15 componentes**, mais os fundamentos e quatro receitas de página.

Aprovada por você em 23 de outubro de 2026, na abertura da Fase 3. O modelo de Caso, `ds/prova/variacoes/v4.html`, já é montado com ela.

## Os 15 componentes

Os nomes seguem o shadcn quando existe um equivalente (decisão D6).

| Componente | Nome shadcn | O que absorve das 54 peças | No Omnichat |
| --- | --- | --- | :-: |
| Cabeçalho | Header e Sheet | Barra com assinatura, Botão de menu, Menu em painel (sem a retícula de pontos) | sim |
| Rodapé | Footer | Rodapé de contato, e Voltar ao topo como um link dele | sim |
| Botão | Button | Botão principal, Próximo caso | sim |
| Link | Link | Link, Link solto, Voltar para os casos | sim |
| Etiqueta | Badge | Etiquetas de assunto | sim |
| Seção | Section | Seção, Cabeçalho de seção, Bloco com rótulo | sim |
| Cartão | Card | Ficha do projeto, e a moldura de qualquer bloco que precise de borda | sim |
| Dado | Stat | Salto, Números do resultado | sim |
| Passos | Steps | Linhas indexadas, Estágios, Ritos, Funil, Trilha | sim |
| Abas | Tabs | Abas | sim |
| Antes e depois | Compare | Confronto, Conversa, Citação | sim |
| Destaque | Callout | Grito, Declaração final, Linha de nota, Atrito | sim |
| Gráfico | Chart | Barras, Pilhas, Escala de NPS | não |
| Imagem | Figure | Moldura, Galeria, Sangria | não |
| Sumário | Table of contents | Nasceu com a variação 4. As seções do caso com ícone, a da vez marcada. No celular vira um trilho na borda direita | sim |

O Omnichat usa 13 dos 15. É por isso que ele basta como página de prova.

## O que vira fundamento, e não componente

Estas peças não têm forma própria. São regras que todo componente segue, e moram em `ds/FUNDAMENTOS.md` e em `assets/ds/tokens.css`.

- **Micro rótulo, Abertura, Corpo de texto** viram estilos de texto da escala tipográfica.
- **Contêiner de página** vira a grade.
- **Superfícies papel e tinta** viram dois temas de superfície, com os tokens trocando por dentro.
- **Revelar na entrada** vira regra de movimento.
- **Pular para o conteúdo** vira parte da base de acessibilidade.

## O que sai junto com a identidade antiga

Estas peças só existem por causa do sistema de hoje. No Jeff DS elas não têm função, e por isso não entram.

- **Onda.** D3 já tirou. Sem onda, também saem o morro da seta e a física na rolagem.
- **Seta de descer.** Morava no morro da onda. Sem ele, o convite para rolar é o próprio conteúdo aparecendo abaixo da dobra.
- **Orbe do número e Trilho de pontos.** Só existiam dentro da cena e somem em tela estreita já hoje.
- **Régua de leitura.** É uma barra verde que mede a rolagem. O caso é curto o bastante para não precisar dela, e ela não tem par no Jeff DS.
- **Carrossel de tela estreita.** No celular, as Abas passam a ser uma lista aberta, um item debaixo do outro. Ler cinco painéis em fila é mais fácil do que deslizar um carrossel.
- **Convite ao manifesto.** Sai com o manifesto, pela D7.

## Passagem entre páginas e Cena dos casos

A D3 tinha mantido as duas, repintadas. Decidido na abertura da Fase 3.

- **Passagem entre páginas** vira fundamento. Ela já tinha sido trocada na Fase 2 pelo Carregamento em camadas, com a cortina que desce no clique, e é ele que fica (ver `ds/FUNDAMENTOS.md`). A cortina com o J sai.
- **Cena dos casos** sai. Na Home os casos passam a ser uma lista de Cartões, um por caso, que é a receita Lista de casos.

## As quatro receitas de página

Uma receita é uma composição de componentes, sem regra visual própria.

1. **Topo do caso.** Etiquetas, título, frase de apoio, a ficha e um Dado em destaque. O Link de voltar saiu na Fase 4.
2. **Fechamento do caso.** Destaque na tinta, com o que o caso deixa, e um Botão para o próximo caso.
3. **Hero da Home.** A frase é a própria cena, do rascunho à página pronta. Construído na Onda 5 (ver `ds/fichas/hero.md`), entra na migração da Home.
4. **Lista de casos.** Cartões `caso`, um por caso, no lugar da Cena. Construída na Onda 5, entra com a Home.

## A conta

| Destino | Peças |
| --- | :-: |
| Absorvidas pelos 15 componentes | 35 |
| Viram fundamento (inclui a Passagem, que virou Carregamento) | 8 |
| Viram receita (Topo do caso, Ações do fim, Hero) | 3 |
| Saem (inclui a Cena dos casos) | 8 |
| **Total da Fase 1** | **54** |
