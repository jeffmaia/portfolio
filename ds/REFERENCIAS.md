# Referências de design editorial

Pesquisa feita para tirar a página do Omnichat do lugar comum. A primeira prova da Fase 2 trocou a pele do site, mas manteve a estrutura de antes (rótulo, título, texto, bloco, repetido cinco vezes). Aqui estão os princípios que a pesquisa trouxe, e qual variação usa cada um. As variações estão em `ds/prova/variacoes/`.

## Os princípios

**Grade modular e assimetria.** A grade moderna vem da escola suíça, com Josef Müller-Brockmann e o *Grid Systems in Graphic Design* como referência principal. A grade dá a estrutura, e a assimetria é uma camada por cima dela. O layout parece livre, mas tudo alinha a âncoras comuns. Alinhamento à esquerda, muito branco e hierarquia objetiva são as marcas do estilo. Emil Ruder, em *Typography: A Manual of Design*, é a outra fonte para a grade assimétrica.

**Medida de leitura.** Bringhurst considera de 45 a 75 caracteres uma linha confortável numa coluna só, com 66 como o ideal. Em várias colunas, o número cai para algo entre 40 e 50. Outra forma de medir é cerca de 30 vezes o corpo da letra. Linha mais longa pede entrelinha maior. No CSS, a unidade `ch` mede o zero da fonte e não um caractere médio, então `66ch` não dá 66 caracteres exatos.

**Notas na margem.** O padrão das notas de Tufte põe o que é secundário (comentário, citação, figura pequena) na margem, ao lado do texto que comenta, sem interromper o argumento. Em tela estreita, a margem não cabe, e a nota precisa ir para dentro do fluxo. A biblioteca de padrões da Universidade de St Andrews separa aside, que corre paralelo ao texto, de citação destacada, que repete uma frase do próprio texto em corpo grande.

**Colunas, fios e quadros.** Colunas dão ritmo e abrem espaço para citações destacadas e quadros laterais. O jornal tradicional usa margens largas e colunas estruturadas para leitura longa.

**Rolagem que conta a história.** Sites de narrativa por rolagem usam a página como sequência, com aberturas de capítulo e tipografia grande. Uma tendência recente é sair da grade simétrica para composições assimétricas.

**Quebrar a grade.** Elementos que invadem a coluna vizinha ou se sobrepõem aos cantos de outros blocos. Funciona quando a grade continua visível em volta, para a quebra ser lida como intenção e não como erro.

## As seis variações

| | Variação | Princípio | O que muda na estrutura |
| --- | --- | --- | --- |
| 1 | Grade suíça | Grade modular assimétrica | O número da seção pendura na margem esquerda, o texto corre em seis colunas, o apoio senta à direita na mesma linha. As camadas viram uma tabela tipográfica de quatro colunas. |
| 2 | Coluna e margem | Notas de Tufte, medida de leitura | Uma coluna de 60 a 66 caracteres com capitular. Ficha, origens, efeitos e números vão para a margem. A declaração final vira citação destacada que atravessa a página. |
| 3 | Capítulos | Rolagem que conta a história | Hero dividido ao meio. Cada seção abre com número enorme e ícone grande, e as camadas alternam de lado, em zigue-zague. |
| 4 | Sumário e mosaico | Grade modular, leitura por varredura | Sumário fixo com ícones e o conteúdo em blocos de tamanhos diferentes. A primeira camada ganha o bloco maior. |
| 5 | Pôster | Quebrar a grade, tipografia como imagem | O indicador vira manchete em tamanho de cartaz, com a ilustração entre os dois números. Adesivos sobre os cantos, blocos deslocados linha a linha. |
| 6 | Jornal | Colunas, fios e quadros | Manchete, linha fina, crédito com fios, texto em três colunas, quadro de dados e a conversa como transcrição de entrevista. |

## O que é comum às seis

- Mesmo texto, mesmos tokens, mesmos componentes. Muda só a grade e a ordem de leitura.
- A ilustração do hero se liga ao indicador. As barras do antes e do depois estão na proporção de 24 para 32, com os 8 pontos de ganho em listras, e o número continua sendo o que o leitor vê primeiro. O número mora no HTML, não no desenho.
- Ícones adesivo do Jeff DS marcam seções e informações. Os que o kit não tinha foram desenhados na mesma gramática (ver abaixo).
- Menu com Home junto dos casos, e o que leva para fora (LinkedIn, WhatsApp) menor, abaixo. Rodapé sem a coluna "Fora daqui", com Voltar ao topo na linha de baixo.
- Carregamento que monta a tela em camadas, o mesmo gesto do hero da Home ao contrário.

## Ícones e ilustrações

- `ds/icones/gerar.py` gera os ícones nos três acentos. Do kit do Jeff DS vieram 15 (lupa, janela, alerta, diálogo, alvo, xis, pessoa, lâmpada, check, gráfico, olho, seta, calendário, lápis, robô). Seis foram desenhados para este caso, na mesma gramática de sombra sólida, corpo no acento e detalhe em papel. São eles camadas, fronteira, celular, megafone, verifica e rota.
- `ds/ilustracoes/gerar.py` gera as duas cenas do caso. Fronteira, com o lead chegando pelo celular e entrando pelo arco. Salto, com a pessoa passando da barra de antes para a de depois, a partir da cena escada do kit.

## Fontes

- [Grid Systems in Graphic Design, Thames and Hudson](https://thamesandhudson.com.au/?p=93182)
- [Müller-Brockmann, Grid and Design Philosophy, leitura de curso na CUNY](https://openlab.citytech.cuny.edu/langecomd3504fa2019/files/2018/10/MullerBrockmann_Grid_Des-Phil.pdf)
- [Typography: A Manual of Design, Emil Ruder](https://standardsmanual.com/products/typography-a-manual-of-design)
- [Swiss style, panorama de tendência](https://trends.daisyui.com/trend/swiss-style/)
- [Editorial Design, guia completo](https://madegooddesigns.com/editorial-design-guide/)
- [Editorial design, panorama de tendência](https://trends.daisyui.com/trend/editorial-design/)
- [Long form content, biblioteca de padrões de St Andrews](https://www.st-andrews.ac.uk/dpl/0.16.0/patterns/long-form-content/index.html)
- [Choose a comfortable measure, webtypography.net](https://webtypography.net/2.1.2)
- [The Elements of Typographic Style, resenha](https://guptadeepak.com/books/the-elements-of-typographic-style/)
- [Ideal measure on the web](https://vasilis.nl/nerd/ideal-measure-web/)
- [Tufte CSS](https://push.cx/assets/tufte-css/)
- [Notes, guia de Garrett Dimon](https://garrettdimon.com/guide/notes)
- [Media and editorial website design, Tubik](https://tubikstudio.com/blog/media-editorial-website-design/)
- [Editorial website design examples, Subframe](https://www.subframe.com/tips/editorial-website-design-examples)
- [10 creative websites, Kota](https://kota.co.uk/blog/10-creative-websites-to-inspire-your-next-web-design-2025-update)
- [Editorial layout, Awwwards](https://www.awwwards.com/inspiration/editorial-layout-mara)
