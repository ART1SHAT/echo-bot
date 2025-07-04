import asyncio
import logging

from app.bot import dp, bot
from app.settings import TOKEN

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
