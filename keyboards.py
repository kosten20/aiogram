from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters.callback_data import CallbackData
start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Посмотреть команды')
        ],
        [
            KeyboardButton(text='Получить ссылки на яп')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='введите свою команду зы',
    selective=True
)

class Get_info(CallbackData, prefix='info'):
    query: str

lst_lang_prog = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='python', callback_data=Get_info(query='python').pack()),
            InlineKeyboardButton(text='javaScript', callback_data=Get_info(query='javascript').pack())
        ]
    ]
)

lst_lang_url = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='python', url='https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.python.org/&ved=2ahUKEwjIp8nylq2FAxUvExAIHf44DmwQFnoECA4QAQ&usg=AOvVaw0QREvGsjwHKp2GtoYvs1JH'),
            InlineKeyboardButton(text='javaScript', url='https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.javascript.com/&ved=2ahUKEwiQ7fmxl62FAxXjKhAIHbRaBj8QFnoECBEQAQ&usg=AOvVaw2t3n3FoztAEJ6zUU6XdzS5')
        ]
    ]
)

lst_commands_python = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='print', callback_data=Get_info(query='print').pack())],
        [InlineKeyboardButton(text='def', callback_data=Get_info(query='def').pack())]
    ]
)

lst_commands_javascript = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='function', callback_data=Get_info(query='function').pack())],
        [InlineKeyboardButton(text='let', callback_data=Get_info(query='let').pack())]
    ]
)