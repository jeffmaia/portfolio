# Handoff: Portfólio de Cases (Jeff Maia — Product Design Manager)

## Overview
Site de portfólio de 4 páginas: uma Home com listagem de cases, e três páginas de case de produto (Omnichat, Inpulse, Mapa de Experiência). Cada case segue a mesma estrutura narrativa: contexto → processo/descoberta → resultado, com dados/gráficos simples e um CTA de contato no fim.

## About the Design Files
The files in `pages/` are **design references built as interactive HTML prototypes**, not production code to copy directly. They use a proprietary component runtime (custom `<x-dc>`/`<sc-for>`/`<sc-if>` template tags and a `support.js` runtime) that only exists in the design tool — **do not ship these files or their tags as-is**. The task is to **recreate these designs in the target codebase's environment** (React, Vue, plain static site, etc. — whichever the project already uses, or the best fit if none exists yet), reproducing the layout, content, interactions and visual system described below using standard HTML/CSS/JS or the framework's own component model.

Ignore tags/attributes like `<x-dc>`, `<helmet>`, `<sc-for>`, `<sc-if>`, `data-comment-anchor`, and the `<script type="text/x-dc" data-dc-script>` block's exact API — read them as pseudocode for "loop over this list" / "conditionally render this" / "this is the component's state and event handlers."

## Fidelity
**High-fidelity.** Colors, typography, spacing and copy are final. Recreate pixel-close using the design tokens below (or the codebase's existing tokens if this design system is adopted there). All body copy is in Portuguese and should be reproduced verbatim.

## Design System
Built on a design system called **Industry**: light steel-blue-on-white wireframe aesthetic. Key rules:
- **Blueprint objects**: every card, figure and the primary button are square-cornered, hairline-bordered boxes with a small "+" crosshair mark drawn in each of the 4 corners (implemented in the source as `.blueprint` + four `<i class="corner tl/tr/bl/br">` children — recreate as 4 small absolutely-positioned plus-sign glyphs/SVGs at each corner of the bordered box). Cards/figures have **no fill** (transparent), except the one solid primary button (accent fill) and occasional light accent-tinted highlight states.
- **Typography**: headings in Barlow Condensed, body text in Barlow. Headings are tight line-height (~0.9–1.2) and slightly negative letter-spacing on large sizes.
- **Color**: light ground (near-white, `#f2f2f3`-ish), near-black text (`#1d1f20`-ish), single steel-blue accent (`#5980a6`-ish) with a 100–900 tonal ramp. Light ramp steps (100–300) for tints/hovers/borders, 500 as base accent, 700–900 for accent text-on-light and pressed states.
- **Buttons/tags**: `.btn-primary` = solid accent fill, square corners; `.btn-secondary`/`.btn-ghost` = outlined/text; `.tag` variants (`accent`, `neutral`, `outline`) are small square-cornered pill-less labels.
- **Grid**: strong modular grid, generous gaps, section rhythm via horizontal hairline dividers (`border-top`) rather than background color changes.
- **Images**: treated "duotone" — desaturated and tinted with the accent color, framed the same way as cards (square, hairline border, corner marks).
- Full token values, component markup and states are in `pages/_ds/industry-40b7f81b-dcc7-48da-abee-61879f51ed00/styles.css` and its `readme.md` — read those directly for exact hex/spacing/font-size values rather than guessing.

## Site Structure & Navigation
A sticky top nav appears on all 4 pages, identical except for the active-link state:
- Brand/logo text (links Home): "Jeff Maia | Product Designer Manager"
- Links: Home, Omnichat, Inpulse, Mapa de experiência
- Divider, then a LinkedIn link (external, new tab) and a solid primary-button-styled WhatsApp link (external, new tab, `https://wa.me/5511977346175`)
- Nav background is a translucent blur over the page background, with a bottom hairline border.

Every case page ends with a full-width bordered "blueprint" CTA bar: a line of body copy + a "Próximo caso →" secondary button (linking to the next case in sequence) + the WhatsApp primary button. Case order/cycle: Omnichat → Inpulse → Mapa de Experiência → (back to Home via nav).

## Screens / Views

### 1. Home (`pages/Home.dc.html`)
**Purpose**: Portfolio landing page; introduces the designer and links to the 3 cases.

**Layout**: Single column, max-width ~1180px centered, generous vertical padding (~76px top).
- **Header/Hero**: optional small uppercase kicker line with a short rule ("Product design · IA no processo" — currently toggled off by default, it's a tweakable prop). Large H1 (clamp ~38–76px, line-height ~0.98): "O ofício continua o mesmo. / O jeito de fazer, não." (second line in muted gray). Below it, a paragraph (~19px) subhead: "Ajudo times de produto e design a integrar IA no processo real de trabalho, não só na ferramenta."
- **Cases section**: header row with label "Isso na prática, nos projetos abaixo", a horizontal rule, and a small "03 casos" tag on the right. Below, a responsive grid (auto-fit, min 300px cols) of 3 case cards, each a `.blueprint` box, min-height ~340px, containing top-to-bottom: index label ("Caso 01" etc.) + role tag on the right, a big accent-colored stat number (e.g. "+8%"), a stat label sentence, a divider, an H3 title, a summary paragraph, and a "Ver o caso →" link pinned to the bottom. Hovering a card tints its background/border with the accent.
  - Card 1 → Omnichat: role "Product Design Manager", stat "+8%", stat label "Conversão de leads qualificados nos agentes de vendas conversacionais", title "Redesenhando a verificação de intenção dos agentes conversacionais", summary "A maior perda de conversão não estava na interface, estava na camada onde a intenção do lead entra no sistema."
  - Card 2 → Inpulse: role "Idealizador · Mentor · UX/UI", stat "−25%", stat label "Queda na média de recuperação por semestre por aluno", title "Solução que ajudou a diminuir a recuperação dos alunos", summary "Boletim, calendário acadêmico e comunicação em um app, para alunos de medicina que viviam em movimento."
  - Card 3 → Mapa de Experiência: role "Idealizador · Mentor", stat "+48", stat label "Pontos de NPS, de 33 negativos para 15 positivos em 16 campus", title "Como um mapa de experiência ajudou a deixar o NPS positivo", summary "Um relatório visual em formato de tabuleiro que fez 16 campus lerem a pesquisa e agirem sobre ela."
- **"Como eu trabalho" section**: top hairline divider, two-column grid: left = small accent label "Como eu trabalho", H2-ish statement "Antes de desenhar a tela, desenhar a decisão." + explanatory paragraph; right = "Métodos recorrentes" label + a wrapped row of 8 outline tags (Mapa de afinidade, Análise temática, Experimento de desejabilidade, Story mapping, Cocriação, Benchmark, Prototipagem navegável, Desenho de interface).
- **Contact CTA bar**: `.blueprint` box, copy "Quer conversar sobre um problema de produto parecido com algum desses? Me chama no WhatsApp ou no LinkedIn." + LinkedIn secondary button + WhatsApp primary button.

**Interactions**: Case cards tint on hover (background + border color transition, ~0.3s). `showKicker` is a boolean tweak (default off) toggling the small kicker line above the H1.

### 2. Case: Omnichat (`pages/Case Omnichat.dc.html`)
**Purpose**: Case study — redesigning intent verification in conversational sales agents. Result: +8% qualified-lead conversion.

**Layout**: Same shell (nav, max-width ~1180px, 64px top padding).
- **Header**: 2-col grid (≈1.35fr / 0.65fr). Left: 3 tags (Omnichat / Agentic Experience (AX) / accent tag "Agentes conversacionais"), H1 "Redesenhando a verificação de intenção dos agentes conversacionais", subhead paragraph. Right: `.blueprint` stat figure, huge "+8%" number, caption "Conversão de leads qualificados nos agentes de vendas conversacionais, medida em produção."
- **01 — Contexto / 02 — O problema**: 2-column text section (no cards), each with a small accent label + 2 paragraphs. Below that, 2 side-by-side `.blueprint` cards: "Instagram" (tag "origem A") and "Disparos de WhatsApp" (tag "origem B"), each with a short paragraph.
- **03 — Processo, "Cinco camadas de um artefato de design"**: interactive two-pane layout. Left pane: a vertical list of 5 clickable `.blueprint` rows (numbered 01–05, each with a title), fixed height ~560px scroll list. Right pane: a detail `.blueprint` panel (fixed height 560px) showing the selected layer's id, title, "Decisão de design" paragraph, and "Efeito na conversão" paragraph (accent-colored) pinned near the bottom. On narrow containers, the left list collapses and is replaced by prev/next arrow buttons + dot pagination under the detail panel (responsive behavior driven by container width, not viewport — should become a simple breakpoint in real CSS).
  - Layer 01 "A arquitetura de prompt como superfície de design", 02 "Jornada mapeada por origem do lead", 03 "Limites de decisão do agente redesenhados", 04 "Leitura de desvio em vez de leitura completa", 05 "Teste controlado em produção" — see source file for full decision/effect copy per layer.
- **04 — Antes e depois**: header with title "O mesmo lead de Instagram, nas duas versões da fronteira de entrada" + "Reproduzir conversa" secondary button + helper caption. Two side-by-side `.blueprint` chat panels ("Antes" tag "conversa abandonada"; "Depois" tag "lead convertido"), each a vertical list of chat bubbles (bot messages left-aligned with accent-tinted background, lead messages right-aligned plain). Some "Depois" bubbles carry a small "camada NN" button that jumps the layer-selector above to that layer. Messages fade/animate in sequentially when "Reproduzir conversa" is clicked (autoplays once on load too).
- **05 — Resultado**: 2-column text: left = 2 paragraphs on the +8% result; right = "Aprendizado" label, pull-quote-style statement "A interface não é mais o objeto principal do trabalho. O objeto principal é a decisão.", + paragraph.
- **Contact CTA bar** (see Site Structure) → next case: Inpulse.

**Interactions**: Layer list — click to select, hover tints row; selecting animates the detail panel content. Chat replay — button restarts a staggered fade-in of the "Depois" messages (~620ms interval per message, 7 messages). Tweakable props exist for `chatLayout` (side-by-side vs stacked), `autoplayChat`, `startLayer`.

### 3. Case: Inpulse (`pages/Case Inpulse.dc.html`)
**Purpose**: Case study — a student app (grades, calendar, communication) for medical students. Result: −25% recovery-exam rate.

**Layout**: Same shell.
- **Header**: 2-col grid. Left: tags (Inpulse / Idealizador · Mentor · UX/UI / accent "Graduação em medicina"), H1 "Solução que ajudou a diminuir a recuperação dos alunos", subhead explaining the grading methodology. Right: `.blueprint` stat figure "−25%" + caption "A média de recuperação por semestre por aluno caiu de 8 em 10 para 6 em 10."
- **01 — Contexto**: 2-col — left: 2 paragraphs of context; right: "Ficha do projeto" key/value rows (Duração: 10 meses; Jeff: Idealizador, mentor, designer UX e UI; Pedro Anjos: Designer UI).
- **Before/after quote section**: 2 side-by-side `.blueprint` blockquotes. "Antes" (outline tag) — a critical student quote (NPS score 2), footer attribution. "Depois" (accent tag, accent-tinted background) — a positive quote, footer attribution. (Full quote text is in the source file — reproduce verbatim, it's real user research.)
- **02 — Descoberta**: 2-col. Left: heading "Qual a melhor maneira de entregar um boletim e informações eficazes" + 2 paragraphs on discovery method, then a sub-block "O aluno de medicina" with a paragraph + "Abrir o protótipo completo" link (external Figma prototype link). Right: an embedded Figma prototype iframe inside a `.blueprint` frame (~640px tall) — recreate as an actual embed or a placeholder/screenshot with a link, per what the target stack supports.
- **03 — Experimento**: heading "Qual funcionalidade o aluno quer primeiro" + 2 paragraphs on methodology. 3-up row of small `.blueprint` cards defining desirability levels: "Entusiasta", "Receptivo", "Indiferente" (each with a one-line definition). Below: a 2-col highlight (H3 "Aparentemente a falta de um calendário doía mais que um boletim" + paragraph + "Reproduzir resultado" secondary button). Then a `.blueprint` panel "Reações por funcionalidade" (caption "de 10 participantes") containing a 2-column grid of 6 named feature rows (Próximas Avaliações, Faltas, Situação Atual, Últimas Avaliações, Calendário, Planejar Estudos), each row = 3 stacked horizontal bar-charts (Receptivo/Entusiasta/Indiferente counts, out of 10, values shown at the end of each bar) plus a legend row at the bottom (3 color swatches). Bars animate width-in on load / replay.
- **Full-bleed image band**: a ~480px-tall cropped/zoomed product screenshot strip (Framer-hosted asset — replace with the client's real screenshot asset).
- **05 — Resultado**: heading "Agora alunos têm mais tempo para estudar" + paragraph. 4-up stat cards (`.blueprint`): "93% dos alunos acessando o app", "45% acessando uma vez ao dia", "4,8 de CSAT", "−25% de recuperação por semestre por aluno" (last one accent-tinted background). Then "Ferramentas e métodos" — a wrapped row of 12 outline tags.
- **Contact CTA bar** → next case: Mapa de Experiência.

**Interactions**: Bar chart widths animate in (~500ms delay then 1s ease) on mount and on "Reproduzir resultado" click. Tweakable prop `animateBars` (boolean, default true) can disable the animation (render at full width immediately) — useful for a "reduced motion" preference.

### 4. Case: Mapa de Experiência (`pages/Case Mapa de Experiencia.dc.html`)
**Purpose**: Case study — an interactive "board game"-style experience map report that turned a negative NPS across 16 campuses positive. Result: +48 NPS points.

**Layout**: Same shell.
- **Header**: 2-col grid. Left: tags (UX Research / UX Strategy / accent "Pesquisa e NPS"), H1 "Como um mapa de experiência ajudou a deixar o NPS positivo", subhead on the 12-brand/16-campus context. Right: `.blueprint` stat figure "+48" + caption "Pontos de NPS. A nota geral partiu de 33 pontos negativos e chegou a 15 pontos."
- **01 — A pergunta**: 2-col — left: heading "Como ajudar cada campus a entender o motivo da nota negativa..." + paragraph; right: "Ficha do projeto" key/value rows (Duração: 3 meses; Jeff: Idealizador e mentor; Anna Marsillac: Pesquisadora; Lucas Dias, Natália Dantas: Designers).
- **02 — Só um relatório não é suficiente**: 2-col — left: paragraph; right: `.blueprint` "Nota geral de NPS" panel with a "Reproduzir" button, a horizontal NPS scale bar (−100 to +100, a center tick, an accent-colored range indicator that animates position/width on load or replay) and two callout numbers ("−33 antes", "+15 depois").
- **03 — Processo, "Destaques do processo"**: same interactive layer-list + detail-panel pattern as Omnichat's layers section, but with 3 steps: "01 Entender os dados do NPS", "02 Complementar os dados", "03 Ideação" — each has a title, two body paragraphs, and a "Consequência" callout. (No responsive pager variant coded here — simpler 2-col grid.)
- **04 — Solução, "O mapa"**: heading + "Abrir o mapa completo" secondary link (external Figma link). 2-col: paragraph describing the interactive map's views; a "Eixos do mapa" tag list (9 outline tags: Saúde mental, Saúde física, Vida financeira, Expectativa de futuro, Dores, Experiência com a instituição, Sugestões, Aplicativos, Oportunidades). Below: caption "Clique na imagem para ampliar. Use as setas para navegar.", then a `.blueprint` image carousel — one large image at a time, prev/next arrow buttons overlaid, a caption row (current label · position of total) and 5 numbered dot-buttons to jump directly to a slide. Clicking the image opens a fullscreen lightbox (dark overlay, image centered, caption, click or Escape to close). Then a 2-col "Relatórios por eixo" text block + "Ferramentas e métodos" tag list (9 outline tags).
- **05 — Resultado**: 2-col — left: heading "Atingimos grande parte do ecossistema" + paragraph on the access increase; right: `.blueprint` panel "Usuários únicos no primeiro mês" (header shows "+4.350%" in accent) with 2 horizontal bar rows: "Sem o mapa de experiência" = 20, "Com o mapa de experiência" = 890 (bars animate width-in; the 890 bar is visually near 100% width, the 20 bar proportionally tiny).
- **Contact CTA bar** → next case: Omnichat (completes the 3-case loop).

**Interactions**: NPS scale bar and access bars animate on mount/replay (same pattern as Inpulse's bars). Layer/step selector: click to switch active step, animated colored state (accent fill on selected row). Image carousel: prev/next buttons wrap around; dot buttons jump directly; click-to-zoom lightbox with Escape-to-close. Tweakable prop `animateNumbers` (boolean, default true), same purpose as Inpulse's `animateBars`.

## Interactions & Behavior (cross-cutting)
- **Animated bar/gauge charts** (Inpulse desirability bars, Mapa NPS gauge, Mapa access bars): render at 0 width, animate to final width ~260–500ms after mount using an eased transition (`cubic-bezier(.2,.8,.2,1)`, ~1–1.2s). Each has a "Reproduzir"/"Reproduzir resultado" button to replay the animation. Provide a way to skip/disable the animation (the tweak props above) for reduced-motion users.
- **Selectable layer/step lists** (Omnichat's 5 layers, Mapa's 3 steps): a list of rows; clicking one sets it active, swaps the detail panel's content, and gives the active row a solid accent background with light text. Rows have a subtle hover tint when inactive.
- **Chat replay** (Omnichat): a scripted two-column conversation replay revealing messages one at a time on a timer; a button restarts it from the top.
- **Image carousel + lightbox** (Mapa de Experiência): arrow navigation with wraparound, dot indicators, and a click-to-zoom fullscreen view closable by click or Escape.
- **Hover states**: case cards (Home) and layer/feature rows tint background + border on hover using the accent ramp; buttons/tags use the design system's built-in hover/pressed/focus states (see `styles.css`).
- No responsive breakpoints beyond CSS grid auto-fit reflow and one JS-driven container-width check (Omnichat's layer list collapsing to a pager below ~720px container width) — a real implementation should just use a CSS media/container query.

## State Management
Each case page manages simple local UI state (no global store needed):
- Active tab/layer/step index (number) per interactive selector section.
- A "grown"/animation-triggered boolean flag (per chart) to sequence the width/position transitions after mount, replayable via a button.
- Home: currently-hovered card index (for hover tint), and a `showKicker` toggle.
- Omnichat: chat message reveal counter (autoplay timer), active layer, hover state, and a container-width-driven boolean for the responsive list/pager swap.
- Mapa de Experiência: active step, active carousel slide index, lightbox open/closed + which image, gauge/bar "grown" flag.
No data fetching — all content (copy, stats, chart values, image URLs) is static and hardcoded per page; move it into whatever content/data layer the target codebase uses (CMS, JSON, props) rather than hardcoding again if that's the pattern there.

## Design Tokens
Do not hand-copy hex values from this doc — read `pages/_ds/industry-40b7f81b-dcc7-48da-abee-61879f51ed00/styles.css` (and its `readme.md`) directly for the authoritative CSS variables: `--color-bg`, `--color-text`, `--color-neutral-100..900`, `--color-accent-100..900`, `--font-heading` (Barlow Condensed), `--font-body` (Barlow), `--space-*`, `--radius-*` (effectively 4px, square corners), `--shadow-sm/md/lg`. The bundle `_ds_bundle.js` implements the actual component classes (`.btn`, `.tag`, `.card`, `.blueprint`, `.nav`, etc.) referenced throughout the pages.

## Assets
- Product screenshots and photography are currently placeholder/reference images hosted on Framer's CDN (`framerusercontent.com`) — these are stand-ins and must be replaced with the client's real screenshots/photography before shipping.
- Two external Figma prototype embeds/links (Inpulse student app prototype, Mapa de Experiência interactive map) — these are live client Figma files; keep the links or replace with the team's current file URLs.
- Icons: none custom — the design system uses thin-stroke Lucide icons where icons appear (none are used directly in these 4 pages beyond the corner "+" marks, which are drawn via small CSS/SVG marks, not an icon font).

## Files
```
pages/
  Home.dc.html                          — Home / listing page
  Case Omnichat.dc.html                 — Case: Omnichat
  Case Inpulse.dc.html                  — Case: Inpulse
  Case Mapa de Experiencia.dc.html      — Case: Mapa de Experiência
  _ds/industry-40b7f81b-dcc7-48da-abee-61879f51ed00/
    styles.css                          — design tokens + component CSS (source of truth for exact values)
    readme.md                           — design system usage guide
    _ds_bundle.js                       — compiled component implementations referenced by the pages
```
Open any `.dc.html` file in a browser to see the live, interactive reference (it's a self-contained prototype — no build step needed to view it).
