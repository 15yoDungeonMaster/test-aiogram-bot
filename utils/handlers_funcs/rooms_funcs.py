from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import bot
from states.low_price_state import LowPriceState
from states.high_price_state import HighPriceState
from states.bestdeal_state import BestDealState
from keyboards.inline.answer_kb import answer_kb


async def get_adult_rooms(message: Message, state: FSMContext, command: str):
    if not message.text.isdigit():
        await bot.send_message(message.chat.id, 'Количество должно быть числом. Попробуйте еще раз.')
        if command == 'lowprice':
            await LowPriceState.adult_rooms.set()
        elif command == 'highprice':
            await HighPriceState.adult_rooms.set()
        elif command == 'bestdeal':
            await BestDealState.adult_rooms.set()
    else:
        async with state.proxy() as data:
            data['rooms'] = [{'adults': int(message.text)}]
        await bot.send_message(message.chat.id, 'Поедут ли в поездку дети?', reply_markup=answer_kb)


async def child_info_callback(callback: CallbackQuery, state: FSMContext, command: str):
    await callback.answer()
    if callback.data == 'Да':
        await bot.edit_message_text('Введите количество детей', callback.message.chat.id, callback.message.message_id)
        if command == 'lowprice':
            await LowPriceState.children_rooms.set()
        elif command == 'highprice':
            await HighPriceState.children_rooms.set()
        elif command == 'bestdeal':
            await BestDealState.children_rooms.set()
    else:
        await bot.edit_message_text('Записал. Я могу показать вам до 10 отелей. Введите число',
                                    callback.message.chat.id, callback.message.message_id)
        if command == 'lowprice':
            await LowPriceState.hotels_count.set()
        elif command == 'highprice':
            await HighPriceState.hotels_count.set()
        elif command == 'bestdeal':
            await BestDealState.hotels_count.set()


async def get_child_rooms(message: Message, state: FSMContext, command: str):
    if not message.text.isdigit():
        await bot.send_message(message.chat.id, 'Количество должно быть числом. Попробуйте еще раз.')
        if command == 'lowprice':
            await LowPriceState.children_rooms.set()
        elif command == 'highprice':
            await HighPriceState.children_rooms.set()
        elif command == 'bestdeal':
            await BestDealState.children_rooms.set()
    else:
        async with state.proxy() as data:
            data['rooms'][0]['children'] = [{'age': 5} for n in range(int(message.text))]
        await bot.send_message(message.chat.id, 'Записал. Я могу показать вам до 10 отелей. Введите число')
        if command == 'lowprice':
            await LowPriceState.hotels_count.set()
        elif command == 'highprice':
            await HighPriceState.hotels_count.set()
        elif command == 'bestdeal':
            await BestDealState.hotels_count.set()