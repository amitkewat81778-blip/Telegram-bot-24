import feedparser

RSS_URLS = [
    "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "https://cointelegraph.com/rss",
    "https://decrypt.co/feed",
    "https://news.bitcoin.com/feed/"
]

def fetch_rss():
    news = []
    for url in RSS_URLS:
        try:
            feed = feedparser.parse(url)
            if feed.entries:
                entry = feed.entries[0]
                news.append({
                    "title": entry.title,
                    "summary": getattr(entry, "summary", ""),
                    "link": entry.link
                })
        except:
            pass
    return news
