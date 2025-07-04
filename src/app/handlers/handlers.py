from aiogram import types

from app.bot import dp


@dp.message()
async def echo_all(message: types.Message) -> None:
    try:
        if message.text:
            await message.answer(message.text)

        elif message.sticker:
            await message.answer_sticker(message.sticker.file_id)

        elif message.photo:
            await message.answer_photo(message.photo[-1].file_id)

        elif message.voice:
            await message.answer_voice(message.voice.file_id)

        elif message.video:
            if message.video.file_size > 50_000_000:
                await message.answer("Видео слишком большое")
            else:
                await message.answer_video(message.video.file_id, caption=f"Видео: {message.caption}" if message.caption else None)

        elif message.document:
            await message.answer_document(message.document.file_id)

        elif message.video_note:
            await message.answer_video_note(message.video_note.file_id)

        else:
            await message.answer("хз как ответить на кружочки")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
