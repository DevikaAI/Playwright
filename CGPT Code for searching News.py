from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for headless
        context = browser.new_context()
        page = context.new_page()

        print("🌐 Opening Bing...")
        page.goto("https://www.bing.com", timeout=60000)

        print("🔎 Typing search query...")
        # Wait for search inDemoPlaywright/CGPT Code for searching News.py DemoPlaywright/digital_success_content.txt DemoPlaywright/digital_success_summary.txt DemoPlaywright/Extract content from digitalsuccess.py DemoPlaywright/from playwright chatgptcode.py DemoPlaywright/kaspersky_summary.txt DemoPlaywright/PlaywrightKeyfunctions.py DemoPlaywright/tamil_oneindia_summary.txt
        # put to be visible
        search_input = page.locator('//*[@id="sb_form_q"]')
        search_input.wait_for(timeout=10000)

        # Fill the input field
        search_input.fill("South Africa vs Australia latest news")

        # ✅ Press Enter to submit the search
        search_input.press("Enter")

        print("⏳ Waiting for results to load...")
        try:
            page.wait_for_selector("li.b_algo h2 a", timeout=15000)
        except:
            print("❌ Search results not loaded.")
            browser.close()
            return

        print("📰 Extracting top 5 news headlines...\n")
        headlines = page.locator("li.b_algo h2 a")
        count = headlines.count()

        if count == 0:
            print("❌ No news found.")
        else:
            for i in range(min(5, count)):
                title = headlines.nth(i).text_content()
                url = headlines.nth(i).get_attribute("href")
                print(f"{i+1}. {title.strip()}\n   🔗 {url}")

        browser.close()

if __name__ == "__main__":
    run()
