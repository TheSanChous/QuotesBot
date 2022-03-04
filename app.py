from aiogram import executor, types

from loader import dp
from quotes.repository import QuotesRepository
from utils.db_api.database import DbContext
from utils.dbstorage.dbstorage import DbStorage
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

import handlers


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)