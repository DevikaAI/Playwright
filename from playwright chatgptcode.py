# open_chromium.py

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Launch Chromium browser
        browser = await p.chromium.launch(headless=False)  # headless=False opens GUI
        context = await browser.new_context()
        page = await context.new_page()
        
        # Open a website
        await page.goto("https:/google.com")

        # Wait to keep the browser open for 5 seconds
        await asyncio.sleep(5)

        # Close browser
        await browser.close()

# Run the async function
asyncio.run(main())
