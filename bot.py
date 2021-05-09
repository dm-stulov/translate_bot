from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import translator

TOKEN = '1857129401:AAEbk3***********KHh6s9RObs'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi!\n Say me!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Let's go")


@dp.message_handler()
async def echo_message(msg: types.Message):
    msg.text = translator.translate(str(msg.text))
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
