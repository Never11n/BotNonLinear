from aiogram import Bot, Dispatcher, executor, types
import wolframalpha

client = wolframalpha.Client("QPQT9K-UQH266YG92")



bot = Bot('6356964227:AAGnMM33z6JWgAzajB7vnhfVfvgFZ7sHFZU')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привіт! Я Нелінійний бот. Мене стоврили для вирішення нелінійних рівнянь та інших прикладів.")

@dp.message_handler()
async def echo_message(message: types.Message):
    equation = message.text
    res = client.query(equation)
    output = next(res.results).text
    await message.answer(output)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    
    
    
