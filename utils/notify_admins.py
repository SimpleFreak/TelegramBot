import logging

from aiogram import Dispatcher

from data.config import admins_id


async def on_startup_notify(dispatcher: Dispatcher):
    for admin in admins_id:
        try:
            text = "Бот запущен"
            await dispatcher.bot.send_message(chat_id=admin, text=text)
        except Exception as exception:
            logging.exception(exception)
