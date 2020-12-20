#from bot import bot, storage
from filters.bot_commands import default_commands

async def startup(dp):

    await default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=startup, skip_updates = True)