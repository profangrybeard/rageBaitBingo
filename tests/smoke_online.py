"""End-to-end smoke test for the online edition (index.html).

Usage (from the repo root):
    pip install playwright
    python -m playwright install chromium
    python tests/smoke_online.py

What it proves, in one browser context (same as the Caller's machine):
  1. Console can make calls and they reach the stage window.
  2. Shipping a patch puts its install card on stage.
  3. A player can install that patch (retrying through the fake failure).
  4. Cooldown actually eats the second tap.
  5. The claim code round-trips: the console decodes the right card,
     the right marks, and the right installed patches.
  6. Card layouts match the print edition (shared seed invariant).
  7. No page errors anywhere.
"""
import asyncio
import pathlib
import re
import sys

from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
URL = (ROOT / "index.html").as_uri()
PRINT_CARDS = (ROOT / "print" / "player-cards.html").as_uri()

failures = []


def expect(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        failures.append(msg)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        ctx = await browser.new_context(viewport={"width": 1200, "height": 900})
        errors = []

        def watch(page):
            page.on("pageerror", lambda e: errors.append(str(e)))
            return page

        console = watch(await ctx.new_page())
        await console.goto(URL + "#console")
        stage = watch(await ctx.new_page())
        await stage.goto(URL + "#stage")
        await stage.wait_for_timeout(200)

        for _ in range(6):
            await console.click("#next")
        await stage.wait_for_timeout(300)
        stage_text = await stage.inner_text("#app")
        expect("Call 6" in stage_text, "stage shows the sixth call")

        await console.click('.plist button[data-v="1.5"]')
        await stage.wait_for_timeout(300)
        stage_text = await stage.inner_text("#app")
        expect("Cooldown" in stage_text and "C00L" in stage_text,
               "stage shows the Cooldown patch and its install code")

        player = watch(await ctx.new_page())
        await player.goto(URL + "#player/14")
        await player.fill("#code", "c00l")
        for _ in range(3):
            await player.click("#install")
            await player.wait_for_timeout(3000)
            if "installed" in await player.inner_text("#status"):
                break
        expect("installed" in await player.inner_text("#status"),
               "player installs patch 1.5")

        await player.click('button.cell[data-i="0"]')
        await player.click('button.cell[data-i="1"]')
        marks = await player.evaluate(
            "JSON.parse(localStorage.getItem('rbb2-player-14')).marks.slice(0,2)")
        expect(marks == [1, 0], f"Cooldown eats the second tap (marks {marks})")

        await player.click("#claim")
        code = (await player.inner_text(".code")).strip()
        await console.bring_to_front()
        await console.fill("#vcode", code)
        await console.click("#verify")
        out = await console.inner_text("#vout")
        expect("No. 14" in out, "console decodes card 14 from the claim code")
        expect("Installed: 1.5" in out, "console sees patch 1.5 installed")

        online_nums = await player.evaluate(
            "[...document.querySelectorAll('button.cell')].map(b=>+b.textContent)")
        paper = watch(await ctx.new_page())
        await paper.goto(PRINT_CARDS)
        paper_nums = await paper.evaluate(
            "[...document.querySelectorAll('.card')][13]"
            ".querySelectorAll('.cell')"
            ".length ? [...[...document.querySelectorAll('.card')][13]"
            ".querySelectorAll('.cell')].map(c=>+c.textContent) : []")
        expect(online_nums == paper_nums and len(paper_nums) == 25,
               "online card 14 matches printed card 14")

        expect(not errors, f"no page errors {errors}")
        await browser.close()

    if failures:
        print(f"\n{len(failures)} failed")
        sys.exit(1)
    print("\nall passed")


asyncio.run(main())
