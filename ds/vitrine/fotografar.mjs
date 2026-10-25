// Fotografa as cenas do estudo do hero em 1440 e 390px, para as prévias
// paradas de ds/vitrine/estudo/hero/index.html.
//
// Usa o playwright-core da auditoria. Com o site servido em
// http://localhost:4173:
//   node ds/vitrine/fotografar.mjs [caminho do Chrome]
import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath } from "node:url";

const aqui = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(aqui, "../auditoria/auditar.mjs"));
const { chromium } = require("playwright-core");

const BASE = process.env.BASE || "http://localhost:4173";
const CHROME = process.argv[2] || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const TAMANHOS = [[1440, 900], [390, 844]];

const navegador = await chromium.launch({ executablePath: CHROME });
for (const [w, h] of TAMANHOS) {
  const pagina = await navegador.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  for (const n of [1, 2, 3]) {
    await pagina.goto(`${BASE}/ds/vitrine/estudo/hero/cena-${n}.html`, { waitUntil: "networkidle" });
    await pagina.evaluate(() => document.fonts.ready);
    await pagina.screenshot({ path: path.join(aqui, `estudo/hero/cena-${n}-${w}.png`) });
  }
  await pagina.close();
}
await navegador.close();
