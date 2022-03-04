from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from data import config
from utils.dbstorage.dbstorage import DbStorage

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = DbStorage()
dp = Dispatcher(bot, storage=storage)

