from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import bot
from states.low_price_state import LowPriceState
from states.high_price_state import HighPriceState
from states.bestdeal_state import BestDealState
from keyboards.inline.answer_kb import answer_kb
from utils.handlers_funcs.user_ready import user_ready


async def get_hotels_count(message: Message, state: FSMContext, command: str):
    if not message.text.isdigit() or 0 > int(message.text) > 10:
        await bot.send_message(message.chat.id, 'Ошибка ввода. Количество должно быть *числом от 1 до 10*\n'
                                                'Попробуйте еще раз.', parse_mode='Markdown')
        if command == 'lowprice':
            await LowPriceState.hotels_count.set()
        elif command == 'highprice':
            await HighPriceState.hotels_count.set()
        elif command == 'bestdeal':
            await BestDealState.hotels_count.set()

    else:
        async with state.proxy() as data:
            data['resultsSize'] = int(message.text)
        await bot.send_message(message.chat.id, f'Хорошо, сейчас я покажу вам {message.text} отелей')
        await bot.send_message(message.chat.id, 'Нужно ли показывать фотографии отелей?', reply_markup=answer_kb)
        if command == 'lowprice':
            await LowPriceState.photo.set()
        elif command == 'highprice':
            await HighPriceState.photo.set()
        elif command == 'bestdeal':
            await BestDealState.photo.set()


async def photo_callback(callback: CallbackQuery, state: FSMContext, command: str):
    await callback.answer()
    if callback.data == 'Да':
        await bot.edit_message_text('Сколько фото выводить? (число от 1 до 10)', callback.message.chat.id, callback.message.message_id)
        async with state.proxy() as data:
            data['photo'] = True
            if command == 'lowprice':
                await LowPriceState.count_photo.set()
            elif command == 'highprice':
                await HighPriceState.count_photo.set()
            elif command == 'bestdeal':
                await BestDealState.count_photo.set()
    else:
        async with state.proxy() as data:
            data['photo'] = False
        await bot.edit_message_text('Подбираю отели...',
                                    callback.message.chat.id, callback.message.message_id)
        if command in ['lowprice', 'highprice']:
            await user_ready(callback.from_user.id, state, command=command)
        else:
            await BestDealState.min_price.set()


async def get_photo_count(message: Message, state: FSMContext, command: str):
    if not message.text.isdigit() or 0 > int(message.text) > 10:
        await bot.send_message(message.chat.id, 'Ошибка ввода. Количество должно быть *числом от 1 до 10*\n'
                                                'Попробуйте еще раз.', parse_mode='Markdown')
        if command == 'lowprice':
            await LowPriceState.count_photo.set()
        elif command == 'highprice':
            await HighPriceState.count_photo.set()
        elif command == 'bestdeal':
            await BestDealState.count_photo.set()
    else:
        async with state.proxy() as data:
            data['count_photo'] = int(message.text)
        if command in ['lowprice', 'highprice']:
            await bot.send_message(message.chat.id, 'Подбираю отели...')
            await user_ready(message.from_user.id, state, command)
        else:
            await bot.send_message(message.from_user.id, 'Введите минимальную стоимость *за ночь* в USD($)', parse_mode='Markdown')
            await BestDealState.min_price.set()


