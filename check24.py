import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

BOT_TOKEN = ""  # your telegram bot token
TELEGRAM_USER_ID = ""  # your telegram user ID

def send_telegram_message(new_jobs):
    message = "\n\n".join([f"{title}\n{link}" for title, link in new_jobs])
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_USER_ID,
        "text": f"📬 New CHECK24 Jobs Found:\n\n{message}",
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Telegram message sent.")
        else:
            print(f"❌ Telegram error: {response.text}")
    except Exception as e:
        print(f"❌ Telegram exception: {e}")


BASE_URL = "https://jobs.check24.de"
SEARCH_URL = f"{BASE_URL}/de/jobs/"
SAVE_DIR = "saved"
KEY_DATE_FORMAT = "%Y-%m-%d"

def fetch_jobs():
    all_jobs = []
    page = 1
    while True:
        print(f"Fetching page {page}...")
        params = {"query": "data", "languages": "englisch", "page": page}
        response = requests.get(SEARCH_URL, params=params)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        job_cards = soup.select("a.ch24-search-single-result")
        if not job_cards:
            break

        for card in job_cards:
            title_elem = card.find("h3")
            if title_elem:
                title = title_elem.text.strip()
                link = BASE_URL + card.get("href")
                all_jobs.append((title, link))
        page += 1

    return all_jobs

def save_jobs(jobs, date_str):
    os.makedirs(SAVE_DIR, exist_ok=True)
    filepath = os.path.join(SAVE_DIR, f"jobs_{date_str}.txt")
    with open(filepath, "w") as f:
        for title, link in jobs:
            f.write(f"{title}\n{link}\n")
    return filepath

def load_previous_links(date_str):
    filepath = os.path.join(SAVE_DIR, f"jobs_{date_str}.txt")
    if not os.path.exists(filepath):
        return set()
    with open(filepath, "r") as f:
        lines = f.readlines()
    return set(line.strip() for line in lines if line.startswith("https://"))

def notify_new_jobs(new_jobs):
    print(f"\n📬 {len(new_jobs)} new job(s) found today:")
    for title, link in new_jobs:
        print(f"{title}\n{link}\n")

def main():
    today = datetime.now().strftime(KEY_DATE_FORMAT)
    yesterday = (datetime.now() - timedelta(days=1)).strftime(KEY_DATE_FORMAT)

    jobs_today = fetch_jobs()
    links_today = set(link for _, link in jobs_today)
    links_yesterday = load_previous_links(yesterday)

    new_links = links_today - links_yesterday
    new_jobs = [(title, link) for title, link in jobs_today if link in new_links]

    save_jobs(jobs_today, today)

    if new_jobs:
        notify_new_jobs(new_jobs)
        send_telegram_message(new_jobs)
    else:
        print("✅ No new jobs compared to yesterday.")

if __name__ == "__main__":
    main()