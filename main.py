from telegram import Bot
from telegram.ext import Updater
from config import bot_token

def main():
    bot = Bot(bot_token)
    updater = Updater(bot = bot)
