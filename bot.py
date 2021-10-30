import telebot
import configure
from googletrans import Translator

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
    languages = [
        'af-afrikaans',
        'sq-albanian',
        'am-amharic',
        'ar-arabic',
        'hy-armenian',
        'az-azerbaijani',
        'eu-basque',
        'be-belarusian',
        'bn-bengali',
        'bs-bosnian',
        'bg-bulgarian',
        'ca-catalan',
        'ceb-cebuano',
        'ny-chichewa',
        'zh-cn-chinese (simplified)',
        'zh-tw-chinese (traditional)',
        'co-corsican', 'hr-croatian',
        'cs-czech', 'da-danish',
        'nl-dutch',
        'en-english',
        'eo-esperanto',
        'et-estonian',
        'tl-filipino',
        'fi-finnish',
        'fr-french',
        'fy-frisian',
        'gl-galician',
        'ka-georgian',
        'de-german',
        'el-greek',
        'gu-gujarati',
        'ht-haitian creole',
        'ha-hausa',
        'haw-hawaiian',
        'iw-hebrew',
        'he-hebrew',
        'hi-hindi',
        'hmn-hmong',
        'hu-hungarian',
        'is-icelandic',
        'ig-igbo',
        'id-indonesian',
        'ga-irish',
        'it-italian',
        'ja-japanese',
        'jw-javanese',
        'kn-kannada',
        'kk-kazakh',
        'km-khmer',
        'ko-korean',
        'ku-kurdish (kurmanji)',
        'ky-kyrgyz',
        'lo-lao',
        'la-latin',
        'lv-latvian',
        'lt-lithuanian',
        'lb-luxembourgish',
        'mk-macedonian',
        'mg-malagasy',
        'ms-malay',
        'ml-malayalam',
        'mt-maltese',
        'mi-maori',
        'mr-marathi',
        'mn-mongolian',
        'my-myanmar (burmese)',
        'ne-nepali',
        'no-norwegian',
        'or-odia',
        'ps-pashto',
        'fa-persian',
        'pl-polish',
        'pt-portuguese',
        'pa-punjabi',
        'ro-romanian',
        'ru-russian',
        'sm-samoan',
        'gd-scots gaelic',
        'sr-serbian',
        'st-sesotho',
        'sn-shona',
        'sd-sindhi',
        'si-sinhala',
        'sk-slovak',
        'sl-slovenian',
        'so-somali',
        'es-spanish',
        'su-sundanese',
        'sw-swahili',
        'sv-swedish',
        'tg-tajik',
        'ta-tamil',
        'te-telugu',
        'th-thai',
        'tr-turkish',
        'uk-ukrainian',
        'ur-urdu',
        'ug-uyghur',
        'uz-uzbek',
        'vi-vietnamese',
        'cy-welsh',
        'xh-xhosa',
        'yi-yiddish',
        'yo-yoruba',
        'zu-zulu']
    bot.send_message(message.chat.id, '\n'.join(languages))

@bot.message_handler(func=lambda m: True)
def translate_msg(message):
    query = str(message.text).split('-')
    translator = Translator()
    if len(query) == 1:
        result = translator.translate(message.text)
        bot.send_message(message.chat.id, result.text)
    elif len(query) > 1:
        result = translator.translate(query[0], dest=query[1].lstrip())
        bot.send_message(message.chat.id, result.text)


bot.infinity_polling()
