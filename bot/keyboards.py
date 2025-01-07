from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from texts.get_str import get_str


async def menu_keyboard():
    menu = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=get_str('texts/buttons/google.txt'))],
        [KeyboardButton(text=get_str('texts/buttons/yandex.txt'))],
        [KeyboardButton(text=get_str('texts/buttons/vk.txt'))]
    ], resize_keyboard=True, input_field_placeholder=f'тут был артур')
    return menu
