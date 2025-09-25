import os
from telebot import types
import telebot
import yt_dlp

TOKEN = "5546500115:AAHMn-Cm8lLCHlpNEZxcY_jVUywWThw2Or8"
bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def kbhjv(message):
    if bot.get_chat_member('@ra92a7', message.from_user.id).status == 'left':
        k1 = types.InlineKeyboardButton('ra92a7', url='https://t.me/ra92a7')
        ch = types.InlineKeyboardMarkup(row_width=1)
        ch.add(k1)
        bot.send_message(
            message.chat.id,
            text="<b>عليك الاشتراك بالقناة أولاً</b>",
            reply_markup=ch,
            parse_mode='html'
        )
        return False
    else:
        bot.send_message(
            message.chat.id,
            text="<b>اهلا بك في بوت تنزيل من مواقع التواصل واليوتيوب</b>",
            parse_mode='html'
        )
        return True


# دالة يوتيوب فقط
@bot.message_handler(func=lambda message: "youtube.com" in message.text or "youtu.be" in message.text)
def youtube_handler(message):
    chat_id = message.chat.id
    if not kbhjv(message):
        return
    url = message.text

    j1 = types.InlineKeyboardButton('تنزيل فيديو', callback_data='yt_video')
    j2 = types.InlineKeyboardButton('تنزيل صوت', callback_data='yt_audio')
    ff = types.InlineKeyboardMarkup(row_width=2)
    ff.add(j1, j2)

    bot.send_message(chat_id, "اختار الخيار اللي تحبه من يوتيوب", reply_markup=ff)
    users[chat_id] = url


# دالة عامة لأي رابط ثاني (تنزل فيديو فقط)
@bot.message_handler(func=lambda message: message.text.startswith("http"))
def any_link_handler(message):
    chat_id = message.chat.id
    if not kbhjv(message):
        return
    url = message.text

    try:
        ydl_opts = {
            "quiet": True,
            "cookiefile": "cookies2.txt",
            "outtmpl": "file.mp4",
            "format": "mp4",
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "فيديو")

        # إرسال الفيديو فقط
        with open("file.mp4", "rb") as f:
            bot.send_video(chat_id, f, caption=title)

        os.remove("file.mp4")

    except Exception as e:
        bot.send_message(chat_id, f"صار خطأ: {e}")


# كولباك لليوتيوب (فيديو/صوت)
@bot.callback_query_handler(func=lambda call: call.data in ["yt_video", "yt_audio"])
def youtube_download(call):
    chat_id = call.message.chat.id
    if not kbhjv(call.message):
        return
    url = users.get(chat_id)
    if not url:
        bot.send_message(chat_id, "ماكو رابط")
        return

    try:
        ydl_info_opts = {"quiet": True, "cookiefile": "cookies.txt"}
        with yt_dlp.YoutubeDL(ydl_info_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get("title", "فيديو")

        if call.data == "yt_video":
            ydl_opts = {
            "quiet": True,
            "cookiefile": "cookies.txt",
            "outtmpl": "file.mp4",
            "format": "mp4"
        }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            with open('file.mp4', "rb") as file:
                bot.send_video(chat_id, file, caption=title)
            os.remove('file.mp4')

        elif call.data == "yt_audio":
            ydl_opts = {
            "quiet": True,
            "cookiefile": "cookies.txt",
            "outtmpl": "file.mp4",
            "format": "mp4"
        }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            
            os.rename('file.mp4', 'file.mp3')
            
            with open ('file.mp3', 'rb') as file:
                
                bot.send_audio( chat_id,file, caption=title)
                os.remove('file.mp3')

    except Exception as e:
        bot.send_message(chat_id, f"صار خطأ: {e}")


print("البوت شغال")
bot.infinity_polling()