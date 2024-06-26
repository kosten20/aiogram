from dotenv import dotenv_values
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import keyboards

config = dotenv_values(".env")

bot = Bot(token=config['token'])
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    info_bot = await bot.get_me()
    text = f'''Добро пожаловать в бота {info_bot.first_name}.
С помощь него вы сможете узнать часто используемые команды различных языков программирования.
В настоящем руководстве вы узнаете команды из python, javaScript'''
    await message.answer(text, reply_markup=keyboards.start_kb)

@dp.message(F.text.lower() == 'посмотреть команды')
async def get_lst_command(message: Message):
    text = 'Выберите любой язык'
    await message.answer(text, reply_markup=keyboards.lst_lang_prog)

@dp.message(F.text.lower() == 'получить ссылки на яп')
async def get_lst_command(message: Message):
    text = 'Ссылки'
    await message.answer(text, reply_markup=keyboards.lst_lang_url)

@dp.callback_query(keyboards.Get_info.filter(F.query.in_(['python', 'javascript'])))
async def get_info_python(query: CallbackQuery, callback_data: keyboards.Get_info):
    text = '''Перед вами список команд отсортированный по частоте использования.
    Выбери интересующию команду'''
    data = query.data
    if 'python' in data:
        await query.message.answer(text, reply_markup=keyboards.lst_commands_python)
    elif 'javascript' in data:
         await query.message.answer(text, reply_markup=keyboards.lst_commands_javascript)

@dp.callback_query(keyboards.Get_info.filter(F.query.in_(['function', 'let', 'print', 'def'])))
async def get_info_python(query: CallbackQuery, callback_data: keyboards.Get_info):
    text = '''много много инфы'''
    await query.message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())