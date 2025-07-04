from aiogram import types
from aiogram.filters import Command

from app.bot import dp


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("ЦАО ЦАО! Я эхо-бот. Навали мне кринжа)")
