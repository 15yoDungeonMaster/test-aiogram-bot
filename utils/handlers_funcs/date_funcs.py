from datetime import datetime
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import bot
from states.low_price_state import LowPriceState
from states.high_price_state import HighPriceState
from states.bestdeal_state import BestDealState


async def get_checkin_date(message: Message, state: FSMContext, command):
    if message.text.replace('-', '').isdigit():
        try:
            check_in_date = datetime.strptime(message.text, '%d-%m-%Y').date()
            async with state.proxy() as data:
                data['checkInDate'] = {'day': check_in_date.day, 'month': check_in_date.month, 'year': check_in_date.year}
            await bot.send_message(message.chat.id, 'Отлично, теперь введите дату уезда (в формате *день-месяц-год*)',
                                   parse_mode='Markdown')
            if command == 'lowprice':
                await LowPriceState.end_date.set()
            elif command == 'highprice':
                await HighPriceState.end_date.set()
            elif command == 'bestdeal':
                await BestDealState.end_date.set()
        except ValueError:
            await bot.send_message(message.chat.id, 'Дата введена некорректно! Попробуйте еще раз')
            if command == 'lowprice':
                await LowPriceState.start_date.set()
            elif command == 'highprice':
                await HighPriceState.start_date.set()
            elif command == 'bestdeal':
                await BestDealState.start_date.set()
    else:
        await bot.send_message(message.chat.id, 'Дата введена некорректно! Попробуйте еще раз')
        if command == 'lowprice':
            await LowPriceState.start_date.set()
        elif command == 'highprice':
            await HighPriceState.start_date.set()
        elif command == 'bestdeal':
            await BestDealState.start_date.set()

async def get_checkout_date(message: Message, state: FSMContext, command):
    if message.text.replace('-', '').isdigit():
        try:
            check_out_date = datetime.strptime(message.text, '%d-%m-%Y').date()
            async with state.proxy() as data:
                data['checkOutDate'] = {'day': check_out_date.day, 'month': check_out_date.month, 'year': check_out_date.year}
            await bot.send_message(message.chat.id, f'Сколько взрослых будет в поездке?(Введите число)')
            if command == 'lowprice':
                await LowPriceState.adult_rooms.set()
            elif command == 'highprice':
                await HighPriceState.adult_rooms.set()
            elif command == 'bestdeal':
                await BestDealState.adult_rooms.set()
        except ValueError:
            await bot.send_message(message.chat.id, 'Дата введена некорректно! Попробуйте еще раз')
            if command == 'lowprice':
                await LowPriceState.end_date.set()
            elif command == 'highprice':
                await HighPriceState.end_date.set()
            elif command == 'bestdeal':
                await BestDealState.end_date.set()
    else:
        await bot.send_message(message.chat.id, 'Дата введена некорректно! Попробуйте еще раз')
        if command == 'lowprice':
            await LowPriceState.end_date.set()
        elif command == 'highprice':
            await HighPriceState.end_date.set()
        elif command == 'bestdeal':
            await BestDealState.end_date.set()