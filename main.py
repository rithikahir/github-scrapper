from playwright.sync_api import sync_playwright
from supabase import create_client

# =============================
# SUPABASE CONFIG
# =============================
SUPABASE_URL = "https://uqzfftgzscnehvweqdbr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVxemZmdGd6c2NuZWh2d2VxZGJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE1NTY0MjEsImV4cCI6MjA4NzEzMjQyMX0.iKc-06f6k9VSt6kmsoFvy5rsRZXImj9MvzfUbbMf1Ng"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


PROFILE_URL = "https://github.com/shantanujain18"


def scrape_profile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(PROFILE_URL)
        page.wait_for_timeout(3000)

        # Wait for profile to load
        page.wait_for_selector('span.p-nickname')


        username = page.locator('span.p-nickname').inner_text()
        name = page.locator('span.p-name').inner_text()

        bio_locator = page.locator('.p-note')
        bio = bio_locator.inner_text() if bio_locator.count() > 0 else ""

        followers = page.locator('a[href$="?tab=followers"] span').first.inner_text()
        following = page.locator('a[href$="?tab=following"] span').first.inner_text()

        repos = page.locator('a[href$="?tab=repositories"] span').first.inner_text()

        browser.close()

        return {
            "username": username,
            "name": name,
            "bio": bio,
            "followers": followers,
            "following": following,
            "repositories": repos,
        }


def save_to_supabase(data):
    response = supabase.table("github_profiles").insert(data).execute()
    print(response)
    print("✅ Data saved to Supabase successfully")



if __name__ == "__main__":
    profile_data = scrape_profile()
    print(profile_data)

    save_to_supabase(profile_data)
