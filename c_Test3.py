
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)  # Add slow motion
        page = browser.new_page()
        
        print("Opening Bing...")
        page.goto("https://www.bing.com", timeout=100000)  # 10-second timeout

        print("Typing query...")
        page.fill('xpath=//*[@id="sb_form_q"]', "India vs England Cricket match")
        page.keyboard.press("Enter")

        print("Waiting for results...")
        page.wait_for_selector("li.b_algo h2 a", timeout=100000)
        page.wait_for_selector("li.nth-child(10) h2 a", timeout=100000)
        
        print("Search results loaded.")

        first_result = page.locator("li.nth-child(10) h2 a").first
        page.wait_for_timeout(50000)
       
        first_result.click()

        print("Clicked second result.")
        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    run()