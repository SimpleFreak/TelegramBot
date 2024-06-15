from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dispatcher


@dispatcher.message_handler(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         "Чтобы получить свой стикерпак, "
                         "загрузи свою фотографию и выбери тему стикерпака!")
