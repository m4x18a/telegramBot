import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2079048524:AAHUkOPfpdnjtjntvZ-a8iIgfxgb-ArUAxo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЯ t-bot!")

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)