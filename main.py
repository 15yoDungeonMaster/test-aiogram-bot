from loader import dp
from aiogram.utils import executor
from utils.startup_funcs.bot_online import bot_online
import handlers


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_online)

