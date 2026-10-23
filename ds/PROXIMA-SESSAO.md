# Instrução para a próxima sessão

Cole o bloco abaixo como primeira mensagem de uma sessão nova, aberta na pasta do repositório, na branch `claude/amazing-ride-r8h0h8`.

```
Vamos seguir com o plano do Jeff DS no site. Antes de qualquer coisa, leia
CLAUDE.md e siga o roteiro de leitura dele, começando por ds/PLANO.md.

Onde estamos. As Fases 0 a 3 estão fechadas. A documentação está em ds/
(fichas, GUIA, RECEITAS, RITMO) e os tokens do Site já estão no artifact do
Jeff DS. O plano publicado (https://claude.ai/artifact/GGthPLy5robgxFnJX69QQj)
mostra esse estado. O site publicado ainda não mudou.

Antes de começar, me pergunte o que ainda está pendente comigo.
1. Decidir se o Link de voltar para os casos volta ao Topo do caso.
2. Decidir se o Problema do modelo troca de peça, já que repete o mosaico
   do Processo (ver o fim de ds/RITMO.md).
3. Confirmar que o Botão fica sempre lime, mesmo em caso azul ou verde.

Depois traga o plano da Fase 4, o piloto, sem criar telas, e espere a
minha aprovação. Ele começa por transformar o mosaico e a seção do modelo
em componentes.

Regras que não podem cair estão no CLAUDE.md. Commit só quando eu pedir.
```

## O que fica para a Fase 4

- O mosaico e a seção ao lado do Sumário (`.bloco-sec`) só existem no CSS da variação 4. Viram componente antes do piloto.
- O modelo foi gerado sem `data-revelar`.
- As Abas mudam a altura da página a cada troca.
- O grupo de Dados do modelo escreve o tamanho do número com `style` no HTML.
- Gráfico e Imagem continuam sem código. Entram na Fase 5.
