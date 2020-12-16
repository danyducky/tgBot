from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import asyncio

async def main():
    bot = Bot(token = config.bot_token)
    dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет')
    

if __name__ == '__main__':
    main()