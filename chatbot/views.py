from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .tasks import pearsonR, recommend, input_validation, extract_text
import telegram
import json
# Create your views here.

bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)

def index(request):
    return HttpResponse("Hello")

@csrf_exempt
def Service(request):
    json_string = request.body
    telegram_update = json.loads(json_string) # dict type

    chat_id = telegram_update['message']['chat']['id']

    received_text = telegram_update['message']['text']
    text = ""

    if(input_validation(received_text)==0):
        text = "Please put in the exact data."

    else:
        recommend_list = recommend(received_text)
        text = extract_text(recommend_list)

    bot.sendMessage(chat_id=chat_id, text=text)
    return HttpResponse('Success')