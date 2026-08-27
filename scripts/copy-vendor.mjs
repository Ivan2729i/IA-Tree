import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";

const files = [
    {
        source: resolve("node_modules/chart.js/dist/chart.umd.js"),
        target: resolve("static/vendor/chart.umd.js")
    }
];

for (const file of files) {
    mkdirSync(dirname(file.target), { recursive: true });
    copyFileSync(file.source, file.target);
}

console.log("Vendor assets sincronizados.");
