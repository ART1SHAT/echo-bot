import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# 1. Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# 2. Инициализируем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()


# 3. Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("ЦАО ЦАО! Я эхо-бот. Навали мне кринжа)")


# 4. Обработчик всех сообщений
@dp.message()
async def echo_all(message: types.Message):
    try:
        # Если есть текст - отправляем его обратно
        if message.text:
            await message.answer(message.text)

        # Если есть стикер - пересылаем его
        elif message.sticker:
            await message.answer_sticker(message.sticker.file_id)

        # Если есть фото - пересылаем его
        elif message.photo:
            await message.answer_photo(message.photo[-1].file_id)

        # voice
        elif message.voice:
            await message.answer_voice(message.voice.file_id)

        # video
        elif message.video:
            # Проверка на размер видео
            if message.video.file_size > 50_000_000:  # 50MB
                await message.answer("Видео слишком большое")
            else:
                await message.answer_video(message.video.file_id, caption=f"Видео: {message.caption}" if message.caption else None)

        # document
        elif message.document:
            await message.answer_document(message.document.file_id)

        # Для других типов kringe
        else:
            await message.answer("хз как ответить на кружочки")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")


# 5. Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    # try:
    #     asyncio.run(main())
    # except KeyboardInterrupt:
    #     print('Exit')
