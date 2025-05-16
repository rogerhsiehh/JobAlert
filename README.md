## 🧱 Components of the Workflow

### 1. **Web Scraper**
- Periodically scrapes job listings from [https://jobs.check24.de](https://jobs.check24.de) with filters applied (`query=data&languages=englisch`)
- Extracts job title, job link, and (optionally) location

### 2. **Data Tracker**
- Stores job links scraped each day in a dated `.txt` file (e.g. `jobs_2025-05-16.txt`)
- Compares today’s results with those from yesterday
- Identifies and isolates newly posted jobs not seen in previous runs

### 3. **Telegram Bot Messenger**
- Sends a concise message directly to the user via Telegram
- Uses the Telegram Bot API and a custom bot created via [@BotFather](https://t.me/BotFather)
- Delivers job titles and clickable links to your Telegram account in real-time

### 4. **Automation via `cron`**
- Executes the script automatically every day at **08:00 AM** using a cron job on macOS/Linux
- Runs silently in the background and logs activity to a file
- Ensures you stay updated without having to manually check the site
