# Receitas de página

Uma receita é a ordem dos componentes numa página e onde cada um senta na grade. Não tem cor nem forma própria. O que pode variar de um caso para outro está marcado como livre, o resto é fixo.

São duas receitas, a do Caso e a da Home. A do Caso sai do modelo aprovado, `ds/prova/variacoes/v4.html`, e já está publicada no Omnichat, `case-omnichat.html`. Os dois saem do mesmo gerador, `ds/prova/caso.py`. A da Home é a direção para a Fase 6, e ainda não foi provada numa página.

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

Dentro do conteúdo, os blocos sentam num mosaico de seis colunas, o grupo de Cartões `data-layout="mosaico"`. Os tamanhos são `meio` (3), `terco` (2) e `dois-tercos` (4), em `data-tamanho`. No celular todo bloco ocupa a largura inteira. A página é `main.caso`, e o Topo é `header.topo`, com `topo__texto`, `topo__ficha` e `topo__salto`.

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
- **Título.** Diz o que foi feito, não o nome do projeto. Até quatro linhas no celular. Se passar, o título encurta, e a régua do display não muda.
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

Direção para a Fase 6. O hero e a Lista de casos foram construídos e aprovados na Onda 5 da Fase 5, e estão montados juntos no palco da vitrine. A Home publicada passa para eles na Fase 6.

| | Parte | Componentes |
| --- | --- | --- |
| 1 | Hero | A frase "O ofício continua o mesmo. O jeito de fazer, não." na largura toda, com as cores atrás das palavras e os adesivos em volta. Abaixo dela, a linha de apoio sobre o que o Jeff faz |
| 2 | Lista de casos | Um Cartão por caso, na ordem da fila |
| 3 | Rodapé | Igual ao do caso |

**Hero.** A frase é a própria cena (ver `ds/fichas/hero.md` e `ds/ROTEIRO-HERO.md`). Na chegada ela vai do rascunho à página pronta, uma vez, em uns 3,2s, e na rolagem só se desloca um pouco. Duas linhas do tablet para cima e seis no celular. No desktop a primeira tela deixa ver o rótulo e o alto dos primeiros Cartões da Lista. Sem JS ou com movimento reduzido, a página chega pronta.

**Lista de casos.** Ocupa o lugar da Cena dos casos, que saiu. É uma `section.lista-casos` com o rótulo "Quatro casos" (`h2.section__rotulo`) e um mosaico de Cartões `caso`, um por caso, todos `meio` (ver a ficha do Cartão). Cada Cartão leva o acento do próprio caso (`data-acento` no Cartão) e tem, nesta ordem, o rótulo com o número e o nome do caso, o título do caso como `h3`, a frase de apoio, e na base do acento o Dado `salto` em tamanho de grupo, a ficha compacta (papel e duração numa linha) e um Link `seguir`, "Ver o caso". Não há Botão dentro da lista. Quatro Botões lado a lado disputariam entre si, e a ação principal da Home é escolher um caso.

Do tablet para cima são dois Cartões por linha, com as partes alinhadas de um Cartão para o outro. No celular, um debaixo do outro.

**O que sai.** O convite ao manifesto (D7), a seta de descer e a cena com o orbe do número.

## Pontos fechados na Fase 4

1. **Voltar para os casos.** O Topo do caso não tem Link `voltar`. O Sumário e o menu já levam para fora, e o piloto ficou idêntico ao modelo aprovado.
2. **Revelar.** Cada filho de Seção leva `data-revelar`. O Topo não leva.
3. **Mosaico e Seção.** As duas viraram componente em `assets/ds/componentes.css` (ver as fichas do Cartão e da Seção).
