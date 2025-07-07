import asyncio
from playwright.async_api import async_playwright

#defining async function
async def playwright_function():
    #async steps handling ->function kulla step by step process add panna porom.p is the object
    async with async_playwright() as p:
        #Browser launching.async Overall manage panna .await step by step 
        browser = await p.chromium.launch(headless=False)
        #default ah headless true la erukum so browser launch aagathu
        #browser la page/tab create panna porom
        pages =await browser.new_page()
        #navigation
        await pages.goto("https://www.google.com")
        #function defined .now gonna call the function
           #main fn eppdithaann start aaganum nu solrom 
        await pages.wait_for_timeout(100)
        await browser.close()
        if __name__ == "__main__":
            asyncio.run(playwright_function())
            #white color for txt .attribute for yellow 



