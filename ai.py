import requests
import telebot
import json

token = '5414907722:AAGRIPbyta1nGAeEc9hmVtKCI3s9QEGO--w'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def isns(m):
    chat_id = m.chat.id
    bot.send_message(chat_id, text='اهلاََ في بوت الذكاء ارسل الطلب الذي تريدة')

@bot.message_handler(func=lambda message: True)
def jbsi(m):
    chat_id = m.chat.id
    user = m.text
    params = {
        "gpt-5-mini": user
    }
    
    url = "https://sii3.top/api/openai.php"

    try:
        response = requests.get(url, params=params)
        
        # استخراج الرد فقط من JSON
        data = json.loads(response.text)
        bot.send_message(chat_id, data["response"])
        
    except Exception as e:
        bot.send_message(chat_id, text=str(e))

print('البوت شغال')       
bot.infinity_polling()