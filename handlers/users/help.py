from aiogram import types
from aiogram.dispatcher.dispatcher import Command

from loader import dispatcher


@dispatcher.message_handler(Command("help"))
async def command_help(message: types.Message):
    await message.answer("Чтобы воспользоваться ботом, "
                         "тебе нужно загрузить свою фотографию и "
                         "выбрать тему для стикерпака")
