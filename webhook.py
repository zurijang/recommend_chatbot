import telegram
from telegram_bot import settings

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)

# ngrok http 8000
bot.set_webhook("https://bb8c4045997f.ngrok.io/chatbot/Service/")