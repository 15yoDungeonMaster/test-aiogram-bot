from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


answer_kb = InlineKeyboardMarkup(row_width=2).row(InlineKeyboardButton(text='Да', callback_data='Да')).row(
    InlineKeyboardButton(text='Нет', callback_data='Нет'))
