import os

from dotenv import load_dotenv

load_dotenv()

# Токен телеграмм бота
BOT_TOKEN = str(os.getenv("STICKERPACK_BOT_TOKEN"))

# Идентификатор администратора
admins_id = [
    942850147
]
