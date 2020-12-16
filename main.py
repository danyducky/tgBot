from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import asyncio

bot = Bot(token = config.bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}')

  
@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привет')


@dp.message_handler(content_types = types.ContentTypes.TEXT)
async def answer(message: types.Message):
    if message.text in config.messages:
        await message.answer(f'Привет!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)