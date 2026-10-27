/* Google Analytics 4. O ID de métricas fica só aqui — as quatro páginas
   carregam este arquivo, então trocar a propriedade é uma linha. */
const GA_MEASUREMENT_ID = "G-FZ28CNHCEJ";

(() => {
  /* Abrir os arquivos direto do disco, ou servidos na própria máquina
     ou na rede de casa para conferir, não conta como visita: só o site
     publicado deve alimentar a propriedade. */
  if (location.protocol === "file:") return;
  const host = location.hostname;
  if (["localhost", "127.0.0.1", "[::1]"].includes(host)) return;
  if (/\.(local|localhost|test)$/.test(host)) return;
  if (/^(10\.|192\.168\.|172\.(1[6-9]|2\d|3[01])\.)/.test(host)) return;

  /* O site publicado não sabe se a visita vem do wifi de casa. Quem avisa é
     o navegador: abrir o site uma vez com ?interno=1 grava a marca neste
     aparelho e a medição para. Com ?interno=0 a marca sai. */
  const MARCA = "jm-interno";
  try {
    const pedido = new URLSearchParams(location.search).get("interno");
    if (pedido === "1") localStorage.setItem(MARCA, "1");
    if (pedido === "0") localStorage.removeItem(MARCA);
    if (localStorage.getItem(MARCA) === "1") return;
  } catch (e) {}

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };

  gtag("js", new Date());
  gtag("config", GA_MEASUREMENT_ID);

  const tag = document.createElement("script");
  tag.async = true;
  tag.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_MEASUREMENT_ID;
  document.head.appendChild(tag);
})();
