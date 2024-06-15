from aiogram import types
from aiogram.dispatcher.dispatcher import Command

from loader import dispatcher


@dispatcher.message_handler(Command("subscribe"))
async def command_error(message: types.Message):
    await message.answer("Ссылка на телеграмм канал:\n")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="Подпишись", url="https://t.me/okei_56ru"))

    await message.answer(text="Пожалуйста, подпишитесь на канал", reply_markup=keyboard)
