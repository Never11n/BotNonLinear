from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6356964227:AAGnMM33z6JWgAzajB7vnhfVfvgFZ7sHFZU')
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Привіт! Я Нелінійний бот. Мене стоврили для вирішення нелінійних рівнянь та інших прикладів.")

@dp.message_handler()
async def strHandle(message):
    str_equation = message
    await message.answer(str_equation)
    

executor.start_polling(dp)

