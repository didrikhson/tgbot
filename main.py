import pymongo
from aiogram import Bot, types, Dispatcher

API_TOKEN = '5671453448:AAH8ut0LZ8njliJugzsqTrhK4swwwulWq8w'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

my_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

bot_db = my_client["bot_db"]

users_collection = bot_db["users"]

@dp.message_handler(commands="start")




# import logging
#
# from aiogram import Bot, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.webhook import SendMessage
# from aiogram.utils.executor import start_webhook
#
#
# API_TOKEN = '5671453448:AAH8ut0LZ8njliJugzsqTrhK4swwwulWq8w'
#
# # webhook settings
# WEBHOOK_HOST = 'https://didrikhson.com'
# WEBHOOK_PATH = '/path/to/api'
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# # webserver settings
# WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_PORT = 443
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands="start")
# async def hello(message: types.Message):
#     await message.reply(text="hello")
#
# @dp.message_handler(commands="help")
# async def help(message: types.Message):
#     await message.reply(text="I will help you")
#
#
#
# if __name__ == '__main__':
#     print('Bot Started')
#     executor.start_polling(dp, skip_updates=True)

