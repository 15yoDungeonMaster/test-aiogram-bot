from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp, bot


@dp.message_handler(commands=['cancel'])
async def cancel(state: FSMContext):
    await bot.answer('Отменяю все состояния')
    return state.finish()