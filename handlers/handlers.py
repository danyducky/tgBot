from app import config
from bot import dp, types


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привет, {message.from_user.first_name}')


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply(f'Привет')


@dp.message_handler(text=config.messages, content_types=types.ContentTypes.TEXT)
async def answer(message: types.Message):
    # [config.messages] содержит множество слов приветствия
    await message.answer(f'Привет!')