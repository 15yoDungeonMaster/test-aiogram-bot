from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from loader import bot, dp
from states.low_price_state import LowPriceState
from states.high_price_state import HighPriceState
from states.bestdeal_state import BestDealState


async def start(message: Message, command: str):
    """
    Начало работы команды поиска отелей
    """
    if command == 'lowprice':
        await LowPriceState.cities.set()
        await bot.send_message(message.from_user.id, 'Отлично! Вы выбрали поиск недорогих отелей.\n'
                                                     'К сожалению поиск по России сейчас не доступен:(\n'
                                                     'Введите город для поиска',
                               reply_markup=ReplyKeyboardRemove())
    elif command == 'highprice':
        await HighPriceState.cities.set()
        await bot.send_message(message.from_user.id, 'Отлично! Вы выбрали поиск дорогих отелей.\n'
                                                     'К сожалению поиск по России сейчас не доступен:(\n'
                                                     'Введите город для поиска',
                               reply_markup=ReplyKeyboardRemove())
    elif command == 'bestdeal':
        await BestDealState.cities.set()
        await bot.send_message(message.from_user.id, 'Отлично! Вы выбрали поиск лучшего предложения.\n'
                                                     'К сожалению поиск по России сейчас не доступен:(\n'
                                                     'Введите город для поиска',
                               reply_markup=ReplyKeyboardRemove())


