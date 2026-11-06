// Renderiza HTML -> PNG (infográficos) e HTML -> PDF (slides). Uso: node tools/render.mjs  (puppeteer-core + chromium)
import puppeteer from "puppeteer-core";
import fs from "fs";
import path from "path";
import { pathToFileURL } from "url";
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const b = await puppeteer.launch({ executablePath: "/usr/bin/chromium", args: ["--no-sandbox"], headless: true });
const what = process.argv[2] || "all";

if (what === "all" || what === "info") {
  const dir = path.join(root, "tools/_info");
  fs.mkdirSync(path.join(root, "assets/infograficos"), { recursive: true });
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith(".html"))) {
    const p = await b.newPage();
    await p.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
    await p.goto(pathToFileURL(path.join(dir, f)).href, { waitUntil: "networkidle0" });
    await p.evaluate(() => document.fonts.ready);
    const over = await p.evaluate(() => { const bd = document.body; return [bd.scrollHeight, innerHeight, [...document.querySelectorAll(".body > *")].some((e) => e.getBoundingClientRect().bottom > document.querySelector(".foot").getBoundingClientRect().top)]; });
    await p.screenshot({ path: path.join(root, "assets/infograficos", f.replace(".html", ".png")) });
    console.log(f, over);
    await p.close();
  }
}
if (what === "all" || what === "slides") {
  for (const d of ["apresentacao-cliente", "treinamento-vendedor"]) {
    const p = await b.newPage();
    await p.setViewport({ width: 1280, height: 720 });
    await p.goto(pathToFileURL(path.join(root, "slides", d, "index.html")).href + "?print", { waitUntil: "networkidle0" });
    await p.evaluate(() => document.fonts.ready);
    const n = await p.evaluate(() => document.querySelectorAll(".slide").length);
    fs.mkdirSync(path.join(root, "assets/pdf"), { recursive: true });
    await p.pdf({ path: path.join(root, "assets/pdf", `slides-${d}.pdf`), width: "1280px", height: "720px", printBackground: true, pageRanges: "" });
    console.log(d, n, "slides");
    await p.close();
  }
}
await b.close();
