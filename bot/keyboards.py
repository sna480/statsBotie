from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from texts.get_str import get_str


async def menu_keyboard():
    menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Гугл')],
        [KeyboardButton(text='Яндекс')],
        [KeyboardButton(text='ВК 😭')],
        [KeyboardButton(text='Хром?..')]
    ], resize_keyboard=True, input_field_placeholder=f'тут был артур')
    return menu
