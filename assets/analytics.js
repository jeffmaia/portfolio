/* Google Analytics 4. O ID de métricas fica só aqui — as quatro páginas
   carregam este arquivo, então trocar a propriedade é uma linha. */
const GA_MEASUREMENT_ID = "G-FZ28CNHCEJ";

(() => {
  /* Abrir os arquivos direto do disco não conta como visita: só o site
     publicado deve alimentar a propriedade. */
  if (location.protocol === "file:") return;

  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };

  gtag("js", new Date());
  gtag("config", GA_MEASUREMENT_ID);

  const tag = document.createElement("script");
  tag.async = true;
  tag.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_MEASUREMENT_ID;
  document.head.appendChild(tag);
})();
