from aiogram import Router, F, types

menu_router = Router()


@menu_router.message(F.text == 'Гугл')
async def feedback(message: types.Message):
    await message.answer('*инфа про гугл*')


@menu_router.message(F.text == 'Яндекс')
async def feedback(message: types.Message):
    await message.answer('я им не пользуюсь..')


@menu_router.message(F.text == 'ВК 😭')
async def feedback(message: types.Message):
    await message.answer('раньше классно было, щас хочу аккаунт снести')


@menu_router.message(F.text == 'Хром?..')
async def feedback(message: types.Message):
    await message.answer('._.')
