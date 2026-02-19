from playwright.sync_api import sync_playwright

def test_login_page_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://architect-testing.projectsmate.com/login")

        # Wait properly
        page.get_by_text("Sign in with Google").wait_for()
        page.locator("input").first.wait_for()

        # Assertions
        assert page.get_by_text("Sign in with Google").is_visible()
        assert page.locator("input").nth(0).is_visible()
        assert page.locator("input").nth(1).is_visible()
        assert page.get_by_role("button", name="Login").is_visible()

        browser.close()
