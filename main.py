import time
import schedule
from config import TOKEN, CHANNELS, POST_INTERVAL_MIN
from scraper import fetch_news
from rss_reader import fetch_rss
from telegram_poster import post_news

def job():
    scraped = fetch_news()
    rss = fetch_rss()
    combined = scraped + rss
    post_news(TOKEN, CHANNELS, combined)

schedule.every(POST_INTERVAL_MIN).minutes.do(job)

print("Bot Running...")

while True:
    schedule.run_pending()
    time.sleep(5)
