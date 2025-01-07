from aiogram import Router, F, types

from texts.get_str import get_str

menu_router = Router()


@menu_router.message(F.text == get_str('texts/buttons/google.txt'))
async def feedback(message: types.Message):
    await message.answer(get_str('texts/info/google.txt'))


@menu_router.message(F.text == get_str('texts/buttons/yandex.txt'))
async def feedback(message: types.Message):
    await message.answer(get_str('texts/info/yandex.txt'))


@menu_router.message(F.text == get_str('texts/buttons/vk.txt'))
async def feedback(message: types.Message):
    await message.answer(get_str('texts/info/vk.txt'))
