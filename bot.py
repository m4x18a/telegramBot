import telebot
import configure
from logic import languages_list, Translate

bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     "Hi! I'm bot-translator.\n"
                     "Write any text, you want to translate.\n"
                     "\n"
                     "Bot detects initial language automatically.\n"
                     "Destination language by default is English.\n"
                     "\n"
                     "If you want to change destination language,\n"
                     "send 'your text'-'destination language'.\n"
                     "\n"
                     "Example: How are you?-fr\n"
                     "(bot will translate to french)\n"
                     "\n"
                     "You can get list of languages by command /lang")

@bot.message_handler(commands=['lang'])
def send_welcome(message):
    bot.send_message(message.chat.id, '\n'.join(languages_list))

@bot.message_handler(func=lambda m: True)
def translate_msg(message):
    query = str(message.text).split('-')
    example = Translate()
    if len(query) == 1:
        bot.send_message(message.chat.id, example.translate_msg(query[0]).text)
    elif len(query) > 1:
        example.src_lang = 'auto'
        example.dest_lang = query[1]
        bot.send_message(message.chat.id, example.translate_msg(query[0]).text)


bot.infinity_polling()
