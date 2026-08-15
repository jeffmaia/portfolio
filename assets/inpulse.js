(() => {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const bars = Array.from(document.querySelectorAll(".bar-fill"));
  const replayBtn = document.getElementById("replay-bars");
  let timer = null;

  // Cada barra vale de 0 a 10 participantes, então o valor × 10 já é a largura em %.
  const grow = () => bars.forEach(bar => { bar.style.width = Number(bar.dataset.value) * 10 + "%"; });
  const reset = () => bars.forEach(bar => { bar.style.width = "0%"; });

  function play(delay) {
    clearTimeout(timer);
    if (reduceMotion) { grow(); return; }
    reset();
    timer = setTimeout(grow, delay);
  }

  replayBtn.addEventListener("click", () => play(260));
  play(500);
})();
