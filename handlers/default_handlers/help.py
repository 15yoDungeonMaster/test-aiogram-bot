from config_data.config import DEFAULT_COMMANDS
from loader import dp, types, bot


@dp.message_handler(commands=['help', 'помощь'])
async def help_command(message: types.Message):
    text = [f'/{command} - {description}' for command, description in DEFAULT_COMMANDS[1:-1]]
    await bot.send_message(message.from_user.id, '\n'.join(text))