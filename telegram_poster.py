from telegram import Bot
from translator import to_hindi

def post_news(bot_token, channels, news):
    bot = Bot(token=bot_token)
    for item in news:
        title_hi = to_hindi(item.get("title", ""))
        summary_hi = to_hindi(item.get("summary", ""))
        msg = (
            f"🔸 *{title_hi}*\n"
            f"{summary_hi}\n"
            f"🔗 {item.get('url') or item.get('link')}"
        )
        for ch in channels:
            try:
                bot.send_message(chat_id=ch, text=msg, parse_mode='Markdown')
            except:
                pass
