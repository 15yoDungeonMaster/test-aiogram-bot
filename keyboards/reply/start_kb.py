from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config_data.config import DEFAULT_COMMANDS


start_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
buttons = []
for command, description in DEFAULT_COMMANDS[1:-1]:
    button = KeyboardButton(f'/{command}')
    buttons.append(button)

help_button = KeyboardButton('/помощь')

start_kb.row(*buttons).add(help_button)