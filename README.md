> 💡 You can follow the `check24.py` file in this repository as an example implementation.  
> 💡 Don’t forget to add your **Telegram Bot Token** and **Telegram User ID** to enable notifications.

## 🧱 Components of the Workflow

### 1. **Web Scraper**
- Periodically scrapes job listings from [https://jobs.check24.de](https://jobs.check24.de) with filters applied (`query=data&languages=englisch`)
- Extracts job title, job link, and (optionally) location 

### 2. **Data Tracker**
- Stores job links scraped each day in a dated `.txt` file (e.g. `jobs_2025-05-16.txt`)
- Compares today’s results with those from yesterday
- This is an example image of test file, to see the case of 3 new job created

<img src="image/Screenshot 2025-05-16 at 11.34.04.png" alt="3 New Jobs Found" title="3 New Jobs Found" width="600">

- Identifies and isolates newly posted jobs not seen in previous runs

### 3. **Telegram Bot Messenger**
- Sends a concise message directly to the user via Telegram

<img src="image/IMG_C50EA1ED95B8-1.jpeg" alt="3 New Jobs Found" title="3 New Jobs Found" width="200">

- Uses the Telegram Bot API and a custom bot created via [@BotFather](https://t.me/BotFather)
- Delivers job titles and clickable links to your Telegram account in real-time

### 4. **Automation via `cron`**
- Executes the script automatically every day at **08:00 AM** using a cron job on macOS/Linux
- Runs silently in the background and logs activity to a file
- Ensures you stay updated without having to manually check the site



---

## 🤖 How to Set Up Your Telegram Bot

To receive job alerts on your phone, follow these steps to create and use a Telegram bot:

### 🔹 1. Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Start the chat and send the command:  
   ```
   /newbot
   ```
3. Follow the prompts:
   - Choose a name (e.g., `Check24 Job Alert Bot`)
   - Choose a unique username ending in `bot` (e.g., `check24_alert_bot`)
4. BotFather will reply with your **Bot Token**, like this format:
   ```
   123456789:ABCDefGhIjKlmNoPQRstuVWXyz
   ```
   Save this — you’ll need it in your script as `BOT_TOKEN`

### 🔹 2. Get Your Telegram User ID

1. Search Telegram for [@userinfobot](https://t.me/userinfobot)
2. Start it — it replies with:
   ```
   ID: 123456789
   ```
   Use this as `TELEGRAM_USER_ID`

### 🔹 3. Start Your Bot

Before it can message you, open a chat with your bot (e.g., [https://t.me/check24_alert_bot](https://t.me/check24_alert_bot)) and press **Start**.

---

## ⏰ How to Automate the Script Daily with `cron`

You can run the job tracker script every morning using `cron`.
You can also follow this excellent video tutorial by Corey Schafer:  
**[Automating with Cron (YouTube)](https://www.youtube.com/watch?v=QZJ1drMQz1A&t=210s&ab_channel=CoreySchafer)**

### 🔹 1. Open the Crontab Editor

```bash
crontab -e
```

### 🔹 2. Add a Daily Job Entry(change your file path accordingly)

```bash
0 8 * * * /opt/anaconda3/bin/python3 /Users/yourname/Desktop/project/check24.py >> /Users/yourname/Desktop/project/cron_log.txt 2>&1
```

- `0 8 * * *` → Run every day at **8:00 AM**
- Update paths as needed for your system and Python environment
- Output and error logs are saved to `cron_log.txt`

### 🔹 3. Save and Exit

- In `vim`: press `Esc`, then type `:wq` and press Enter
- In `nano`: press `Ctrl + O`, `Enter`, then `Ctrl + X`

You’ll see `crontab: installing new crontab` — that means it’s active.

### 🔹 4. Confirm it’s Set

```bash
crontab -l
```

You should see your scheduled job.

---

🎉 That’s it! Your system now auto-scrapes job listings every morning and sends you Telegram alerts when new jobs appear.
