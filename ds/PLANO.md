# Jeff DS no site

Plano para levar a identidade do Jeff DS, hoje feita para os posts do LinkedIn, para este portfólio. O plano completo, com inventário e fases, está publicado em https://claude.ai/artifact/GGthPLy5robgxFnJX69QQj. Este arquivo guarda o que foi decidido, para qualquer sessão continuar daqui.

O Jeff DS (tokens, cores, tipografia, componentes dos posts) está em https://claude.ai/artifact/YNnxB84kgyyzzUeY25XyeA.

## Estado

Fases 0, 1 e 2 fechadas. Próxima é a Fase 3. O site publicado ainda não mudou, porque a prova é uma página à parte. O modelo de Caso é `ds/prova/variacoes/v4.html`. A instrução para abrir a próxima sessão está em `ds/PROXIMA-SESSAO.md`.

Entregas da Fase 1, em `ds/`. `INVENTARIO.md` (matriz peça por página medida nas páginas reais), `capturas/index.html` (cada peça em 390, 768 e 1440px), `CONTRASTE.md`, `PORQUES.md` (os comentários do CSS e do HTML por peça) e `auditoria/` (os scripts que refazem tudo). A pasta do Industry foi para `arquivo/handoff/`.

Entregas da Fase 2.

- `ds/COMPONENTES.md`. A lista revisitada. As 54 peças da Fase 1 viram 14 componentes, porque boa parte delas só existia para sustentar a identidade antiga. Substitui as fusões do `INVENTARIO.md`.
- `ds/FUNDAMENTOS.md`. Cor, escala tipográfica fluida, espaço, grade, estados, movimento.
- `assets/ds/tokens.css`, `assets/ds/componentes.css` e `assets/ds/componentes.js`. O código, ainda usado só pela prova.
- `ds/prova/omnichat.html`. O caso do Omnichat montado só com o Jeff DS.

Segunda rodada da Fase 2, a pedido seu.

- `ds/REFERENCIAS.md`. Pesquisa de design editorial (grade suíça, medida de leitura, notas de margem, colunas, capítulos, grade quebrada) e o que cada variação tira dela.
- `ds/prova/variacoes/`. Seis variações da página do Omnichat, com índice em `index.html`. A 4 virou o modelo, as outras ficam como registro. Geradas por `ds/prova/variacoes.py`, que usa as partes comuns de `ds/prova/comum.py`.
- `assets/ds/icones/`. Ícones adesivo nos três acentos, 15 do kit do Jeff DS e 6 novos (camadas, fronteira, celular, megafone, verifica, rota). Gerados por `ds/icones/gerar.py`.
- `assets/ds/ilustracoes/`. Duas cenas do caso, fronteira e salto, presas ao indicador de 24% para 32%. Geradas por `ds/ilustracoes/gerar.py`.
- Menu com Home junto dos casos e o contato menor, abaixo. Rodapé sem "Fora daqui", com Voltar ao topo na linha de baixo.
- Carregamento que monta a tela em camadas (esboço, grade, componentes, textos, cores), o hero da Home ao contrário. Dura no mínimo 1,6s, mesmo com a página pronta.

Terceira rodada. A variação 4 (sumário e mosaico) foi escolhida como modelo de Caso.

- Movimento em toda troca de estado. Hover e toque com marca texto que corre só por trás das palavras, menu que desce com os itens chegando um a um, botão do menu que troca a palavra e vira xis, rolagem suave até a seção e até o topo, aba que entra subindo.
- Carregamento ao contrário quando se volta pelo histórico. A tela chega pronta e se desmonta até sobrar o esboço.
- Ficha do projeto e indicador lado a lado entre 720 e 1099px.
- Sumário vira um componente. Abaixo de 1100px ele é um trilho de marcas na borda direita, escolhido entre três formas testadas (faixa no cabeçalho, botão flutuante e trilho).

Ajustes que você fez na Fase 2. Uma página de exemplo só, a do Omnichat, que usa 12 dos 14 componentes. Revisitar a lista de componentes, que estava grande demais. E a regra do hover, que vale para o site todo (regra 5 abaixo). Toda interação que muda o estado de algo tem movimento.

Pendente com você. Aprovar a lista de componentes, agora 15 com o Sumário. Decidir se a Passagem entre páginas e a Cena dos casos ficam (D3 manteve as duas). Publicar os tokens no artifact do Jeff DS, no grupo Site, depois da aprovação.

## Decisões da Fase 0

| | Decisão | Status |
| --- | --- | --- |
| D1 | O site adota o Jeff DS inteiro. Saem o verde marca texto, a trama e a Instrument Serif. | Aprovada |
| D2 | Um Jeff DS só, com núcleo da marca e duas superfícies, Posts e Site, no mesmo artifact. | Aprovada |
| D3 | O hero fica, com formato novo (ver abaixo). A cena dos casos, a passagem com o J e o revelar ficam repintados. A onda e a trama saem. | Ajustada |
| D4 | A tinta vira superfície pontual, no rodapé e em no máximo uma parada por página. O topo do caso deixa de ser escuro. | Aprovada |
| D5 | Acento dominante por caso. Processo em lime, Omnichat em azul, Inpulse em verde, Mapa em azul. | Aprovada |
| D6 | Só HTML, CSS e JS, sem servidor e sem build. Usar a nomenclatura e os tokens do shadcn. | Ajustada |
| D7 | O manifesto sai desta versão e será repensado no futuro. Continua no ar até a Fase 6. | Ajustada |
| D8 | Arquivar a pasta `handoff/`, que descreve o sistema Industry, já obsoleto. | Aprovada |

## Regras que já valem

1. Lime, azul e verde nunca viram texto, nunca são a única borda de um controle e nunca são o anel de foco. Sobre o papel o contraste deles fica entre 1,1 e 1,5 para 1. Texto, borda e foco são sempre tinta.
2. Tokens com nomes do shadcn apontando para o Jeff DS. `background` paper, `foreground` ink, `primary` lime com texto em tinta, `secondary` azul, `muted` e `accent` mist, `border` e `ring` ink, `radius` 12px, gráficos em lime, azul e verde.
3. Componentes com nomes do shadcn (Button, Badge, Card, Tabs, Sheet, Dialog, Carousel, Table, Separator) e variantes por atributo de dados, sem React nem Tailwind.
4. Tudo funciona sem JS e com movimento reduzido.
5. Hover só existe onde há mouse. Toda regra de hover fica dentro de `@media (hover: hover) and (pointer: fine)`, e nada pode depender dele para ser descoberto. No toque, o retorno vem do pressionado (`:active`) e do foco, e todo alvo tem pelo menos 44px. A separação é por capacidade de entrada, nunca por largura de tela, e tablet com toque segue o celular.

## Fases

0. Decisões de base. Aprovada.
1. Inventário fechado e auditoria. Capturas em 390, 768 e 1440px, matriz peça por página, fusões, contraste, porquês extraídos dos comentários do CSS, pasta handoff arquivada.
2. Fundamentos do site. Escala tipográfica fluida, espaço, grade, estados, movimento, tokens no padrão shadcn e revisão da lista de componentes, provados numa página só, a do Omnichat.
3. Modelo de documentação. Ficha de dez campos, guia de decisão, receitas de Home e Caso, regras de ritmo, CLAUDE.md completo.
4. Piloto visual. A prova do Omnichat vira a página publicada, no lugar de `case-omnichat.html`.
5. Biblioteca completa, em cinco ondas.
6. Migração da Home e dos quatro casos. Manifesto sai do menu, do rodapé e da Home.
7. Governança.

## Hero

A frase continua a mesma e passa a ficar alinhada à esquerda. "O ofício continua o mesmo. O jeito de fazer, não." Ao lado, uma ilustração no estilo da marca que apoia a provocação, com movimento ligado à rolagem.

### O cuidado que muda tudo

A frase diz que uma coisa fica e outra vai embora. Se a ilustração inteira se desfaz na rolagem, ela contradiz a frase, porque diz que nada fica. O movimento precisa separar as duas metades. O jeito de fazer se desmonta e sai da tela. O ofício fica parado e termina sozinho no quadro.

### Ideias descartadas

1. Robô, cérebro com circuito ou o brilho de quatro pontas que virou símbolo de IA. São o lugar comum que a frase tenta evitar.
2. Mão humana e mão de robô, ou tela dividida em antes e depois. Contam uma disputa, e a frase fala de continuidade.
3. Partículas ou poeira se dissolvendo. É efeito genérico, pesa no celular e não diz o que fica.
4. Lápis que vira cursor. É literal demais e coloca a mudança na ferramenta, que é justamente o que o lead diz que não é o ponto.

### Recomendada. O esboço que sobra

Uma tela de produto pronta, desenhada no traço de 2px da marca, montada em camadas por cima de um esboço feito à mão. Na rolagem a tela se desmonta na ordem do que hoje a IA já produz. Primeiro saem as cores chapadas, depois os textos, depois os componentes, depois a grade. Cada camada desliza para fora do quadro com um leve giro, como adesivo descolando. No fim sobra só o esboço à mão, com uma anotação de quem decide, uma seta e um "por quê?".

O que fica é a decisão, que é o ofício. O que vai embora é a produção da tela, que é o jeito. Conversa direto com os casos, em que o protótipo já nasce desenvolvido e o design passa a decidir onde a atenção humana faz diferença.

### Alternativas

1. A mesa que esvazia. A cena "mesa" do Jeff DS com a pessoa cercada de ferramentas do jeito antigo, régua, post its, telas impressas. Na rolagem as ferramentas se soltam e saem, e ficam a pessoa e uma folha com a decisão. Tem gente na cena, o que aproxima, mas fica mais carregada ao lado de uma frase grande.
2. A pergunta que fica. A cena "pergunta" com a pessoa diante de uma parede de ícones adesivo. Os ícones se espalham e sobra um adesivo grande de interrogação. É a mais simples de produzir e a mais fraca de sentido, porque a pergunta não aparece na frase.

### Especificação do movimento

1. Ligado à rolagem, do topo da página até o hero sair da tela. Nada acontece sozinho com o tempo.
2. Cinco camadas saem em escada, cada uma com deslocamento e giro próprios, sempre para fora do quadro. O esboço não se move.
3. CSS com linha do tempo de rolagem onde o navegador suporta, e JS com `requestAnimationFrame` como reserva.
4. Sem JS ou com movimento reduzido aparece um quadro parado com as camadas levemente afastadas umas das outras, em vista explodida, que conta a mesma ideia sem movimento.
5. A ilustração é decorativa para leitor de tela. A frase carrega o sentido.
6. Desktop com a frase em 7 colunas e a ilustração em 5. No celular a frase vem primeiro e a ilustração entra abaixo, menor.
