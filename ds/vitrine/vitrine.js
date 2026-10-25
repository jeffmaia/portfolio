/* ============================================================
   Vitrine. O quadro da amostra de cada peça e o palco da ficha.

   O quadro mostra uma página de verdade na largura escolhida (390,
   768 ou 1440px). Quando a largura não cabe na coluna, a página é
   reduzida inteira, como num zoom, e continua respondendo ao mouse,
   ao toque e ao teclado. O botão da largura escolhida fica no lime.

   Sem este arquivo os botões somem e o quadro mostra a página na
   largura da coluna.
   ============================================================ */
(() => {
  for (const palco of document.querySelectorAll("[data-palco]")) {
    const janela = palco.querySelector(".palco__janela");
    const quadro = janela.querySelector("iframe");
    const botoes = [...palco.querySelectorAll("[data-largura]")];
    const ALTURA = Number(palco.dataset.altura) || 800;
    let largura = 0;

    function aplicar(w) {
      largura = w;
      const borda = janela.offsetWidth - janela.clientWidth;
      const cabe = palco.clientWidth - borda;
      const escala = Math.min(1, cabe / w);
      quadro.style.width = `${w}px`;
      quadro.style.height = `${ALTURA}px`;
      quadro.style.transform = `scale(${escala})`;
      janela.style.width = `${w * escala + borda}px`;
      janela.style.height = `${ALTURA * escala + borda}px`;
      botoes.forEach((b) => {
        const esta = Number(b.dataset.largura) === w;
        b.setAttribute("aria-pressed", String(esta));
        if (esta) b.removeAttribute("data-variant");
        else b.dataset.variant = "outline";
      });
    }

    // Abre na largura pedida, ou na maior que cabe sem reduzir.
    const pedida = Number(palco.dataset.larguraInicial);
    const cabem = botoes.map((b) => Number(b.dataset.largura)).filter((w) => w <= palco.clientWidth);
    aplicar(cabem.includes(pedida) ? pedida : Math.max(390, ...cabem));

    botoes.forEach((b) => b.addEventListener("click", () => aplicar(Number(b.dataset.largura))));
    new ResizeObserver(() => aplicar(largura)).observe(palco);
  }
})();
