import telegram
from telegram_bot import settings

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)

# ngrok http 8000
bot.set_webhook("https://1340c36176db.ngrok.io/chatbot/Service/")