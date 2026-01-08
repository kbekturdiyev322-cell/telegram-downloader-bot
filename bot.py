import telebot
import subprocess

TOKEN = "8478801034:AAGZfXDb9_Vv1MczaZaOW5_hXyXZkk0Og0Q"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Salom 👋\nInstagram / TikTok / YouTube link yubor 🙂"
    )

@bot.message_handler(func=lambda message: True)
def download(message):
    url = message.text

    try:
        bot.reply_to(message, "⏳ Yuklanmoqda...")

        cmd = ["yt-dlp", "-f", "mp4", url]
        subprocess.run(cmd)

        bot.reply_to(message, "✅ Tayyor (serverga saqlandi)")

    except Exception as e:
        bot.reply_to(message, f"❌ Xato: {e}")

bot.infinity_polling()
