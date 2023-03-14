from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_cities_button(cities_dict):
    """
    Функция для создания inline клавиатуры с перечислением всех найденных городов
    :param cities_dict: Словарь, где ключ название города, значение rid
    """
    if not cities_dict:
        return 'Подходящий город не найден.'
    keyboard = InlineKeyboardMarkup(row_width=1)
    try:
        for name, data in cities_dict.items():
            keyboard.add(InlineKeyboardButton(name, callback_data=data))

    except (ValueError, KeyError):
        return 'Неизвестная ошибка при определении городов. /start'
    return keyboard
