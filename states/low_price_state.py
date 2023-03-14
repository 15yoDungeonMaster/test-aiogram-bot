

from aiogram.dispatcher.filters.state import State, StatesGroup


class LowPriceState(StatesGroup):
    """ Класс состояний для команды /lowprice """
    cities = State()
    hotels_count = State()       # max 10
    photo = State()
    count_photo = State()   # max 10
    adult_rooms = State()
    children_rooms = State()
    start_date = State()
    end_date = State()

