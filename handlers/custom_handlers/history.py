import json
import pprint

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot, db_history
from states.history_state import HistoryState
from keyboards.inline.history_kb import history_kb
from keyboards.inline.answer_kb import answer_kb


@dp.message_handler(commands=['history'])
async def history_start(message: Message):
    await bot.send_message(message.from_user.id, 'Выберите действие', reply_markup=history_kb)


@dp.callback_query_handler()
async def history_action_callback(callback: CallbackQuery):
    await callback.answer()
    if callback.data == '0':
        await bot.send_message(callback.from_user.id, 'Вы уверены что хотите очистить историю?', reply_markup=answer_kb)
        await HistoryState.del_data.set()
    else:

        await bot.edit_message_text('Введите сколько записей вывести', callback.message.chat.id,
                                    callback.message.message_id)
        await HistoryState.get_data.set()


@dp.message_handler(state=HistoryState.get_data)
async def get_history_data(message: Message, state: FSMContext):
    data = db_history.get_data(int(message.from_user.id), int(message.text))
    for row in data:
        hotels = '\n'.join([hotel['name'] for hotel in json.loads(row[2])])
        await bot.send_message(message.from_user.id, f'Дата: {row[0]}\n'
                                                     f'Команда: {row[1]}\n'
                                                     f'Отели:\n'
                                                     f'{hotels}')

    await state.finish()


@dp.callback_query_handler(state=HistoryState.del_data)
async def del_history_data(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'Да':
        db_history.del_data(int(callback.from_user.id))
        await bot.edit_message_text('Операция успешно выполнена!', callback.message.chat.id, callback.message.message_id)
    else:
        await bot.edit_message_text('Операция прервана!', callback.message.chat.id, callback.message.message_id)
    await state.finish()