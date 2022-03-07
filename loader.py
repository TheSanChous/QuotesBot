from aiogram import Bot, Dispatcher, types
import logging

from data.config import BOT_TOKEN
from utils.dbstorage.dbstorage import DbStorage

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = DbStorage()
dp = Dispatcher(bot, storage=storage)

