import telebot
from flask import Flask, request
from decouple import config

token = config('TELEGRAM_TOKEN')
secret = config('SECRET')
url = config('WEBHOOK') + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)


@app.route("/"+secret, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(
        request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'Hello welcome!')
