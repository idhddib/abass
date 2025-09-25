import requests
from telebot import *
import os



#_______________________________




token = '5414907722:AAGRIPbyta1nGAeEc9hmVtKCI3s9QEGO--w'




bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])


def s(message):
	bot.send_message(message.chat.id,text='اهلاً بك في بوت الخاص بلبرمجه ارسل طلبك ...')
	

@bot.message_handler(content_types=['text'])


def t(message):
	text = message.text.strip()
	re = requests.get(f'https://sii3.top/api/code.php?text={text}').json()
	res = re['response']
	bot.send_message(message.chat.id,res)

print('تم تشغيل البوت بنجاح')	
	
bot.infinity_polling()
