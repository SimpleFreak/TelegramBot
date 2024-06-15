from aiogram import types
from aiogram.dispatcher.dispatcher import Command

from loader import dispatcher


@dispatcher.message_handler(Command("source_code"))
async def source_code(message: types.Message):
    await message.answer("Исходный код доступен по ссылке:\n"
                         "https://github.com/AndreyRazin007/ProFrog_Hackathon_2024")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Перейти на GitHub",
                                            url="https://github.com/AndreyRazin007/telegram_bot/tree/main"))

    await message.answer("Нажмите кнопку, чтобы перейти на GitHub:",
                         reply_markup=keyboard)
