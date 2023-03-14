
from typing import Optional
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import bot
from states.bestdeal_state import BestDealState
from keyboards.inline.answer_kb import answer_kb
from utils.handlers_funcs.user_ready import user_ready


async def get_min_price(message: Message, state: FSMContext, command: str):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['min_price'] = int(message.text)
        await bot.send_message(message.from_user.id, 'Введите максимальную стоимость *за ночь* в USD($)',
                               parse_mode='Markdown')
        await BestDealState.max_price.set()
    else:
        await bot.send_message(message.from_user.id, 'Стоимость должна быть числом!\nПопробуйте еще раз.')
        await BestDealState.min_price.set()


async def get_max_price(message: Message, state: FSMContext, command: str):
    if message.text.isdigit():
        async with state.proxy() as data:
            data['max_price'] = int(message.text)
        await bot.send_message(message.from_user.id, 'Подбираю отели...')
        await user_ready(message.from_user.id, state, command)
    else:
        await bot.send_message(message.from_user.id, 'Стоимость должна быть числом!\nПопробуйте еще раз.')
        await BestDealState.max_price.set()