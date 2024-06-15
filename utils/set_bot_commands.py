from aiogram import Dispatcher, types


async def set_default_commands(dispathcer: Dispatcher):
    await dispathcer.bot.set_my_commands([
        types.BotCommand(command="start", description="Запустить бота"),
        types.BotCommand(command="help", description="Помощь по боту"),
        types.BotCommand(command="subscribe",
                         description="Подписка на телеграмм канал"),
        types.BotCommand(command="source_code",
                         description="Посмотреть исходный код")
    ])
