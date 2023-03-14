from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


history_kb = InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton(text='Посмотреть историю поиска', callback_data='1')).row(
    InlineKeyboardButton(text='Очистить историю поиска', callback_data='0'))