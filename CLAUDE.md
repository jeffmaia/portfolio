# Portfólio Jeff Maia

Site estático em HTML, CSS e JS puros, servido pelo GitHub Pages. Sem servidor e sem build.

O site está migrando para o Jeff DS. Antes de criar ou mudar qualquer página, leia `ds/PLANO.md`. Ele guarda as decisões aprovadas, a fase atual e a direção do hero.

A pasta `arquivo/` guarda material que não vale mais, como o `handoff` do sistema Industry. Não use como referência.

Textos do site e da documentação em português do Brasil, sem hífen, travessão ou dois pontos na escrita corrida.

Hover só existe onde há mouse. Toda regra de hover fica dentro de `@media (hover: hover) and (pointer: fine)`, e nada no site pode depender dele para ser descoberto. No toque, o retorno vem de `:active` e do foco, e todo alvo tem pelo menos 44px. Vale para o site inteiro.

Toda interação que muda o estado de algo tem movimento, com os tokens de duração e curva de `assets/ds/tokens.css`. Nada troca seco. O realce de hover e de toque fica só atrás das palavras, nunca na largura toda da caixa.
