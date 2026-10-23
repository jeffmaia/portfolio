# Instrução para a próxima sessão

Cole o bloco abaixo como primeira mensagem de uma sessão nova, aberta na pasta do repositório, na branch `claude/amazing-ride-r8h0h8`.

```
Vamos seguir com o plano do Jeff DS no site. Antes de qualquer coisa, leia
CLAUDE.md, ds/PLANO.md, ds/FUNDAMENTOS.md e ds/COMPONENTES.md, nessa ordem.

Onde estamos. As Fases 0, 1 e 2 estão fechadas e commitadas. O modelo de
Caso é a variação 4 (sumário e mosaico), em ds/prova/variacoes/v4.html,
gerada por ds/prova/variacoes.py com as partes comuns de ds/prova/comum.py.
O código do sistema mora em assets/ds/ (tokens.css, componentes.css,
componentes.js, icones/, ilustracoes/). O site publicado ainda não mudou.

O que fazer agora é a Fase 3, o modelo de documentação, como descrito em
ds/PLANO.md. Comece me trazendo o plano da fase, sem criar telas novas,
e só siga depois que eu aprovar.

Antes de começar, me pergunte o que ainda está pendente comigo:
1. Aprovar a lista de 15 componentes de ds/COMPONENTES.md.
2. Decidir se a Passagem entre páginas e a Cena dos casos ficam (D3).
3. Publicar os tokens no artifact do Jeff DS, no grupo Site
   (https://claude.ai/artifact/YNnxB84kgyyzzUeY25XyeA).

Regras que não podem cair:
- Textos em português do Brasil, sem hífen, travessão ou dois pontos na
  escrita corrida. Palavra curta de ligação nunca termina linha de título.
- Hover só com mouse, dentro de (hover: hover) and (pointer: fine). No
  toque, :active, foco e alvos de 44px.
- Toda interação que muda estado tem movimento. Nada troca seco. O realce
  de hover e toque fica só atrás das palavras.
- Acentos (lime, azul, verde) nunca viram texto, borda única ou foco.
- Tudo funciona sem JS e com movimento reduzido.
- Para conferir, sirva a raiz do repositório na porta 4173. Nesta máquina
  existe .claude/serve.js (fora do git); em outra, python3 -m http.server
  4173 resolve.
- Commit só quando eu pedir.
```

## O que ficou de fora da Fase 2

- Gráfico e Imagem, os dois componentes que o Omnichat não usa, ainda não têm código.
- A linha que detecta a volta pelo histórico mora no script da cabeça de cada página de prova (`ds/prova/comum.py`, função `cabeca`). Toda página migrada na Fase 4 em diante precisa dela.
- A prova antiga, `ds/prova/omnichat.html`, continua no ar como registro. O modelo é a `v4.html`.
