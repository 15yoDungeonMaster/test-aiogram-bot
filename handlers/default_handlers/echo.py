from loader import dp, types, bot


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f'Не могу распознать эту команду.')   # ответить на конкретное сообщение
    # await message.answer(message.text) # ответить в чате бота
    # await bot.send_message(message.from_user.id, message.text)  # ответить в личку на сообщение из группы

