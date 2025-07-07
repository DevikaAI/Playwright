import os
from playwright.sync_api import sync_playwright

SESSION_FILE = "gmail_state.json"

def save_gmail_session(context):
    page = context.new_page()
    page.goto("https://mail.google.com")
    print("🔐 Please log in to Gmail manually in the opened browser window.")
    input("✅ After inbox is fully loaded, press Enter here to save session...")
    context.storage_state(path=SESSION_FILE)
    print("✅ Gmail session saved.")

def scrape_latest_10_emails(context):
    page = context.new_page()
    page.goto("https://mail.google.com/mail/u/0/#inbox")
    print("📨 Waiting for Gmail to load...")
    page.wait_for_selector("tr.zA", timeout=2000000)

    # Get all visible email rows (limit to 10)
    emails = page.query_selector_all("tr.zA")[:10]

    if not emails:
        print("❌ No emails found.")
        return

    print("\n📬 Latest 10 Emails:\n" + "-" * 40)

    for i, email_row in enumerate(emails, 1):
        sender = email_row.query_selector("span.zF") or email_row.query_selector("span.yX.xY span[email]")
        subject = email_row.query_selector("span.bog")

        sender_text = sender.inner_text().strip() if sender else "Unknown"
        subject_text = subject.inner_text().strip() if subject else "No subject"

        print(f"{i}. 🧾 From: {sender_text}")
        print(f"   📝 Subject: {subject_text}")
        print("-" * 40)

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        if os.path.exists(SESSION_FILE):
            print("🔁 Using saved Gmail session.")
            context = browser.new_context(storage_state=SESSION_FILE)
        else:
            print("🆕 No session found. Login required.")
            context = browser.new_context()
            save_gmail_session(context)

        scrape_latest_10_emails(context)
        browser.close()

if __name__ == "__main__":
    main()
