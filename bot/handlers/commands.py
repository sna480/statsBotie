from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command

from bot.keyboards import menu_keyboard
from texts.get_str import get_str

cmd_router = Router()


@cmd_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(get_str('texts/start.txt'), parse_mode=ParseMode.MARKDOWN, reply_markup=await menu_keyboard())


@cmd_router.message(Command('about'))
async def start(message: types.Message):
    await message.answer(get_str('texts/about.txt'), parse_mode=ParseMode.MARKDOWN)


@cmd_router.message(Command('wtf'))
async def start(message: types.Message):
    await message.answer(get_str('texts/wtf.txt'), parse_mode=ParseMode.MARKDOWN)