from loader import dp, types, bot
from keyboards.reply.start_kb import start_kb


@dp.message_handler(commands=['start', 'старт'])
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id, 'Добро пожаловать в бота!\n'
                              'Данный бот предназначен для быстрого и легкого поиска отелей',
        reply_markup=start_kb
    )
