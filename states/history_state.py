from aiogram.dispatcher.filters.state import State, StatesGroup


class HistoryState(StatesGroup):
    """ Класс состояний для команды /history """
    get_data = State()
    del_data = State()