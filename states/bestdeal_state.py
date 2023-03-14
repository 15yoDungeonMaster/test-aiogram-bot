from aiogram.dispatcher.filters.state import State, StatesGroup


class BestDealState(StatesGroup):
    """ Класс состояний для команды /bestdeal """
    cities = State()
    hotels_count = State()       # max 10
    photo = State()
    count_photo = State()   # max 10
    adult_rooms = State()
    children_rooms = State()
    start_date = State()
    end_date = State()
    min_price = State()
    max_price = State()
