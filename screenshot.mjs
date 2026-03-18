import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const url = process.argv[2] || 'http://localhost:3000';
const label = process.argv[3] || '';

const screenshotDir = path.join(__dirname, 'temporary screenshots');
if (!fs.existsSync(screenshotDir)) fs.mkdirSync(screenshotDir, { recursive: true });

// Find next screenshot number
const existing = fs.readdirSync(screenshotDir).filter(f => f.startsWith('screenshot-'));
let nextNum = 1;
if (existing.length > 0) {
    const nums = existing.map(f => parseInt(f.match(/screenshot-(\d+)/)?.[1] || '0'));
    nextNum = Math.max(...nums) + 1;
}

const filename = label ? `screenshot-${nextNum}-${label}.png` : `screenshot-${nextNum}.png`;
const filepath = path.join(screenshotDir, filename);

(async () => {
    const browser = await puppeteer.launch({
        headless: 'new',
        args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 900 });
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
    await new Promise(r => setTimeout(r, 1000));
    // Scroll through the page to trigger IntersectionObserver reveals
    await page.evaluate(async () => {
        const totalHeight = document.body.scrollHeight;
        const step = 400;
        for (let y = 0; y < totalHeight; y += step) {
            window.scrollTo(0, y);
            await new Promise(r => setTimeout(r, 150));
        }
        window.scrollTo(0, 0);
        await new Promise(r => setTimeout(r, 500));
    });
    await page.screenshot({ path: filepath, fullPage: true });
    console.log(`Screenshot saved: ${filepath}`);
    await browser.close();
})();
