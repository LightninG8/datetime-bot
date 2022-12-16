from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import APP_TOKEN

bot = Bot(APP_TOKEN);
dp = Dispatcher(bot, storage=MemoryStorage())

