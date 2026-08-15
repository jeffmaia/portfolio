(() => {
  const nav = document.querySelector(".site-nav");
  const toggle = document.getElementById("nav-toggle");
  const menu = document.getElementById("nav-menu");
  if (!nav || !toggle || !menu) return;

  /* Mesmo ponto de corte do CSS: acima disso a barra cabe inteira e o painel
     não existe mais. */
  const wide = window.matchMedia("(min-width: 861px)");

  function setOpen(open) {
    menu.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    document.body.classList.toggle("has-nav-open", open);
  }

  toggle.addEventListener("click", () => {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });

  /* Qualquer item leva para outro lugar — da própria página ou de fora —,
     então o painel fecha junto com o clique. */
  menu.addEventListener("click", e => {
    if (e.target.closest("a")) setOpen(false);
  });

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") setOpen(false);
  });

  /* Girar o aparelho para paisagem pode cruzar o ponto de corte com o painel
     aberto, e aí ele sumiria deixando a rolagem travada. */
  wide.addEventListener("change", e => {
    if (e.matches) setOpen(false);
  });

  setOpen(false);
})();
