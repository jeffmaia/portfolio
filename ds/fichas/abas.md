# Abas

`Tabs` · várias saídas do mesmo tipo, lidas uma de cada vez, com a lista dos nomes na esquerda e o painel aberto na direita.

## Use quando

A seção tem de três a seis itens do mesmo tipo e cada um tem nome de frase, um parágrafo de texto e às vezes um efeito. O leitor escolhe qual abrir, e todos abertos de uma vez empurrariam o resto do caso para longe.

## Não use quando

- A ordem importa e precisa ser vista inteira. Use Passos.
- O leitor precisa comparar os itens entre si, ou passar os olhos por todos antes de ler. Use Cartões em mosaico. Foi o que o modelo de Caso fez com as cinco camadas do Omnichat.
- São dois itens. Use dois Cartões lado a lado.
- É o mesmo assunto antes e depois. Use Antes e depois.
- O texto de cada item é uma linha. Use uma lista no texto corrido.
- Um item esconde algo que a história do caso precisa. O que é essencial não pode depender de um clique.

## Anatomia

1. Caixa, `div.tabs` com `data-tabs`. É o que o script procura.
2. Lista, `div.tabs__lista` com `aria-label` que nomeia o conjunto. Dentro, um `button.tab` por item, com o número em `.t-rotulo` e o nome. Cada aba aponta para o seu painel com `aria-controls`.
3. Painéis, `div.tabs__paineis`. Dentro, um `div.tabs__painel` por item, com `id` e `tabindex="0"`.
4. Título do painel, `h3.tabs__painel-titulo`, obrigatório. Repete o número e o nome da aba. Sem script, é ele que nomeia cada item.
5. Texto, obrigatório. Um ou dois parágrafos.
6. Efeito, opcional. `p.tabs__efeito` com o rótulo "Efeito" e uma frase sobre o que o item mudou, num fundo `muted`.

O número não é enfeite. Outras seções apontam para ele ("Camada 02, jornada por origem", nas notas do Antes e depois).

## Variantes

Uma forma só, vertical, com a lista em 5 das 12 colunas e o painel nas outras 7. É o arranjo para nomes que são frases. Numa fileira horizontal eles só caberiam encurtados, e encurtar seria reescrever o conteúdo para caber no formato.

A aba escolhida ganha o `acento` no fundo. Na superfície tinta o texto das abas vira papel, e a escolhida continua com tinta sobre o acento, agora com contorno de papel.

## Limites

- De três a seis abas. Com duas, use Cartões. Com sete ou mais, a lista passa da altura do painel.
- Nome de até duas linhas na coluna da lista.
- Painel de até umas 120 palavras, contando o efeito.
- Um conjunto de Abas por página.

## Comportamento

1. **Mouse.** A aba que não está escolhida ganha `muted` no fundo, em `dur-media` com `ease-saida`.
2. **Toque.** No `:active` a aba ganha `muted`, e a escolhida mantém o acento. Toda aba tem pelo menos `alvo` (44px) de altura.
3. **Foco.** O anel de 2px em `ring`. Setas, Home e End movem o foco e já escolhem a aba (ativação automática). O Tab sai da lista e entra no painel aberto.
4. **Movimento.** O painel que chega sobe 8px e aparece em `dur-media` com `ease-saida`. A aba troca de fundo e de contorno no mesmo tempo.
5. **Sem JS.** A lista some e os painéis ficam todos abertos, um debaixo do outro, cada um com o seu título e um fio entre eles. Abaixo de 720px é igual, mesmo com JS, porque a lista aberta lê melhor que qualquer aba no celular.
6. **Movimento reduzido.** A troca de painel acontece sem a subida.

## Acessibilidade

- Segue o padrão de abas do WAI ARIA. O script põe `role="tablist"` na lista, `role="tabpanel"` e `aria-labelledby` nos painéis, `aria-selected` e o `tabindex` móvel nas abas. Abaixo de 720px ele tira esses papéis, porque ali não há abas.
- A aba escolhida não depende só da cor. Ganha contorno de 2px e peso 700.
- Com abas, o título de cada painel fica escondido e quem nomeia o painel é a aba. Na lista aberta os títulos voltam e entram na navegação por títulos.
- Tinta sobre o acento e sobre `muted` passa com folga.

## Onde aparece

- Prova antiga do Omnichat (`ds/prova/omnichat.html`), com as cinco camadas do artefato de design. "A arquitetura de prompt como superfície de design", "Jornada mapeada por origem do lead" e as outras três.
- Nas páginas publicadas, as cinco camadas do Omnichat e as saídas da camada no Processo com IA ("Visão de produto", "PRD", "User stories (US)", "Relatório de usabilidade").
- O modelo de Caso não usa Abas. As cinco camadas viraram Cartões em mosaico, para quem escaneia antes de ler.

## Vizinhos

- **Passos.** Quando a ordem é o assunto.
- **Cartão em mosaico.** Quando tudo precisa estar à vista.
- **Antes e depois.** Quando são duas versões da mesma coisa.

## Par nos posts

Sem par. O post não tem interação, e cada aba seria uma página do carrossel.

## Código

```html
<div class="tabs" data-tabs>
  <div class="tabs__lista" aria-label="Camadas do artefato" aria-orientation="vertical">
    <button class="tab" type="button" role="tab" id="aba-prompt" aria-controls="painel-prompt"><span class="t-rotulo">01</span>A arquitetura de prompt como superfície de design</button>
    <button class="tab" type="button" role="tab" id="aba-jornada" aria-controls="painel-jornada"><span class="t-rotulo">02</span>Jornada mapeada por origem do lead</button>
    <button class="tab" type="button" role="tab" id="aba-limites" aria-controls="painel-limites"><span class="t-rotulo">03</span>Limites de decisão do agente redesenhados</button>
  </div>
  <div class="tabs__paineis">
    <div class="tabs__painel" id="painel-prompt" tabindex="0">
      <h3 class="tabs__painel-titulo"><span class="t-rotulo">01</span>A arquitetura de prompt como superfície de design</h3>
      <p>Parar de tratar o prompt como configuração técnica.</p>
      <p class="tabs__efeito"><span class="t-rotulo">Efeito</span> Tornou a conversa um objeto de design.</p>
    </div>
    <!-- um painel por aba -->
  </div>
</div>
```

Estilo em `assets/ds/componentes.css`, seção Tabs (`.tabs`, `.tab`, `.tabs--js`). Comportamento em `assets/ds/componentes.js`, bloco 3, que só liga as abas a partir de 720px.

**O que falta no código.**

- Resolvido na Fase 4. Os painéis moram na mesma célula da grade, com a altura do maior, e o escondido sai com `visibility`. Trocar de aba não muda mais a altura da página.
- As abas já nascem com `role="tab"` no HTML, enquanto a lista só ganha `role="tablist"` pelo script. Sem script a lista fica escondida e não chega a ser lida, mas o certo é o script pôr os dois.
