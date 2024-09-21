import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from dotenv import load_dotenv

from app.routers.start import start_router


load_dotenv()
root_router = Router()
root_router.include_routers(start_router)


def main():
    TOKEN = os.getenv("TOKEN")

    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(root_router)
    return dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())