import telebot
import configures
from googletrans import Translator

bot = telebot.TeleBot(configures.config['token'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm bot-translator. Write any text, you want to translate.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    translator = Translator()
    result = translator.translate(message.text)
    bot.send_message(message.chat.id, result.text)

bot.infinity_polling()