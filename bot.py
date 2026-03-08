import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import openai

API_TOKEN = 'ВАШ_ТЕЛЕГРАМ_ТОКЕН'
OPENAI_API_KEY = 'ВАШ_OPENAI_KEY'
openai.api_key = OPENAI_API_KEY

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне сферу деятельности твоего бизнеса, и я создам 3 виральных сценария для Reels.")

@dp.message_handler()
async def generate_content(message: types.Message):
    # В идеале здесь должна быть проверка оплаты в БД
    user_input = message.text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Создай 3 сценария для Reels для бизнеса: {user_input}"}]
    )
    await message.answer(response.choices[0].message.content)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
