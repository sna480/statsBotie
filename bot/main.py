import asyncio
import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv

from bot.handlers.commands import cmd_router
from bot.handlers.menu import menu_router

load_dotenv()
dp = Dispatcher()
bot = Bot(os.environ['API_BOT'])


async def main():
    print("i've fucking BORN!!!")
    dp.include_routers(cmd_router, menu_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('*fucking DIES*')
