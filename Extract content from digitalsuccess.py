from playwright.sync_api import sync_playwright
import textwrap

def summarize_text(text, max_lines=12):
    """Simple summary: get top lines of content."""
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return "\n".join(lines[:max_lines])

def run():
    with sync_playwright() as p:
        print("🚀 Launching browser...")
        browser = p.chromium.launch(headless=True)  # Set headless=False if you want to see the browser
        context = browser.new_context()
        page = context.new_page()

        print("🌐 Navigating to https://www.kaspersky.co.in/")
        page.goto("https://www.kaspersky.co.in/", timeout=60000)
        page.wait_for_load_state("networkidle")  # Wait for the page to fully load

        print("📄 Extracting page content...")
        content = page.locator("body").inner_text()

        print("🧠 Generating summary...")
        summary = summarize_text(content)

        print("💾 Saving to kaspersky_summary.txt...")
        with open("kaspersky_summary.txt", "w", encoding="utf-8") as file:
            file.write("===== Summary =====\n")
            file.write(summary + "\n\n")
            file.write("===== Full Content =====\n")
            file.write(content)

        print("✅ Done! File saved as 'kaspersky_summary.txt'.")

        browser.close()

if __name__ == "__main__":
    run()
