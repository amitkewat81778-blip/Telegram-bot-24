import requests
from bs4 import BeautifulSoup

def fetch_news():
    sources = {
        "CoinDesk": "https://www.coindesk.com/",
        "CoinTelegraph": "https://cointelegraph.com/",
        "AMBCrypto": "https://ambcrypto.com/",
        "Decrypt": "https://decrypt.co/",
        "Bitcoin.com": "https://news.bitcoin.com/"
    }
    news_list = []
    for name, url in sources.items():
        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.find("h2")
            if title:
                news_list.append({"source": name, "title": title.text.strip(), "url": url})
        except:
            pass
    return news_list
