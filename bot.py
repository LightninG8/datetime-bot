from aiogram import executor

from create_bot import dp
from handlers import convert


async def on_startup(_):
  print('bot has been started')




convert.register_handlers_convert(dp)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
