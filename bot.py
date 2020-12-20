import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app import config

# loop = asyncio.get_event_loop()
bot = Bot(token=config.bot_token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot)




# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates = True)
