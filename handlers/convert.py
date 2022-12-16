from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datetime import datetime
from pytz import timezone

class FSMState(StatesGroup):
  SET_SECOND_ZONE = State()
  FINISH = State()

async def set_first_zone(message: types.Message):
  await message.answer('Введите время и зону в формате "Часы:Минуты Регион/Город", например "10:00 Europe/Moscow"')

  await FSMState.SET_SECOND_ZONE.set()

async def set_second_zone(message: types.Message, state: FSMContext):
  message_split = message.text.split()

  time = message_split[0]

  zone = message_split[1]

  await state.update_data(tz1=zone, time1=time)

  await message.answer('Теперь введите второй часовой пояс в формате "Регион/Город", например "Asia/Krasnoyarsk"')

  await FSMState.next()

async def finish_convert(message: types.Message, state: FSMContext):
  data = await state.get_data()

  tz1 = timezone(data['tz1'])
  tz2 = timezone(message.text)
  
  time1 = data['time1']
  time2 = tz1.localize(datetime.strptime(time1, "%H:%M")).astimezone(tz2).strftime("%H:%M")

  await message.answer(f"Время {data['time1']} {data['tz1']} в зоне {message.text}: {time2}")

  await state.finish()


def register_handlers_convert(dp):
  dp.register_message_handler(set_first_zone, commands=['convert'])
  dp.register_message_handler(set_second_zone, state=FSMState.SET_SECOND_ZONE)
  dp.register_message_handler(finish_convert, state=FSMState.FINISH)

