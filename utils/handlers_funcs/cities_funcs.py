from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import bot
from states.low_price_state import LowPriceState
from states.high_price_state import HighPriceState
from states.bestdeal_state import BestDealState
from utils.requestsRapidAPI.get_city_id import get_city_id


async def get_cities(message: Message, command: str, state: FSMContext):
    """Вывод найденных городов"""
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        if command == 'bestdeal':
            data['sort'] = 'DISTANCE'
        else:
            data['sort'] = 'PRICE_LOW_TO_HIGH'
        data['city'] = message.text
        keyboard = get_city_id(data['city'])
        if keyboard:
            await bot.send_message(message.from_user.id, 'Выберите подходящий город', reply_markup=keyboard)
        else:
            await bot.send_message(message.chat.id, 'Нет подходящего варианта попробуйте еще раз')
            if command == 'lowprice':
                await LowPriceState.cities.set()
            elif command == 'highprice':
                await HighPriceState.cities.set()
            elif command == 'bestdeal':
                await BestDealState.cities.set()


async def cities_callback(callback: CallbackQuery, state: FSMContext, command):
    """Функция для получения ответа с кнопок городов"""
    dest_id = callback.data
    for data in callback.message.reply_markup.inline_keyboard:
        if data[0]['callback_data'] == callback.data:
            name = data[0]['text']
    await callback.answer()
    async with state.proxy() as data:
        data['city'] = name
        data['regionId'] = dest_id
    await bot.edit_message_text(f'Отличный выбор {callback.from_user.username}', callback.message.chat.id, callback.message.message_id)
    if command == 'lowprice':
        await LowPriceState.start_date.set()
    elif command == 'highprice':
        await HighPriceState.start_date.set()
    elif command == 'bestdeal':
        await BestDealState.start_date.set()
    await bot.send_message(callback.message.chat.id, 'Введите дату заезда (в формате *день-месяц-год*)',
                           parse_mode='Markdown')