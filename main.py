from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5671453448:AAH8ut0LZ8njliJugzsqTrhK4swwwulWq8w'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def hello(message: types.Message):
    await message.reply(text="hello")

@dp.message_handler(commands="help")
async def help(message: types.Message):
    await message.reply(text="I will help you")



if __name__ == '__main__':
    print('Bot Started')
    executor.start_polling(dp, skip_updates=True)

