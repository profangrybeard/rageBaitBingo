"""Render the print editions in print/ to pdf/ using headless Chromium.

Usage (from the repo root):
    pip install playwright pypdf
    python -m playwright install chromium
    python tools/render_pdfs.py

The pages load Big Shoulders from Google Fonts. Render with a network
connection, or install Big Shoulders Display and Big Shoulders Text locally,
or the PDFs fall back to Arial Narrow.

Expected page counts are checked after rendering. If a count changes, the
print layout broke. Fix the CSS, do not update the number.
"""
import asyncio
import pathlib
import sys

from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
JOBS = [
    # (source html, output pdf, expected pages)
    ("print/player-cards.html", "pdf/player-cards.pdf", 15),
    ("print/caller-packet.html", "pdf/caller-packet.pdf", 6),
    ("print/wrap-up-lecture-sheet.html", "pdf/wrap-up-lecture-sheet.pdf", 3),
]


async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for src, out, _ in JOBS:
            await page.goto((ROOT / src).as_uri())
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(400)
            await page.pdf(
                path=str(ROOT / out),
                format="Letter",
                print_background=True,
                prefer_css_page_size=True,
            )
            print(f"rendered {out}")
        await browser.close()


def check():
    from pypdf import PdfReader

    ok = True
    for _, out, expected in JOBS:
        n = len(PdfReader(str(ROOT / out)).pages)
        flag = "ok" if n == expected else f"EXPECTED {expected}"
        if n != expected:
            ok = False
        print(f"{out}: {n} pages {flag}")
    return ok


if __name__ == "__main__":
    asyncio.run(render())
    sys.exit(0 if check() else 1)
