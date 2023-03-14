from aiogram.types import Message, InputMediaPhoto
from aiogram.dispatcher import FSMContext
from loader import bot
from utils.requestsRapidAPI.get_properties import get_properties
from utils.requestsRapidAPI.get_photo import get_images


async def user_ready(chat_id, state: FSMContext, command: str):
    async with state.proxy() as data:

        text = await get_properties(command=command, state=state)
        if isinstance(text, dict):
            for key, value in text.items():

                if data['photo']:
                    url_photo = get_images(key, data['count_photo'])
                    if url_photo:
                        await bot.send_media_group(chat_id, media=[InputMediaPhoto(media=link, caption=value) for link in url_photo])
                        await bot.send_message(chat_id, f'{value}')
                    else:
                        await bot.send_message(chat_id, 'Фото не нашлось')
                        await bot.send_message(chat_id, f'{value}')
                else:
                    await bot.send_message(chat_id, f'{value}')
        else:
            await bot.send_message(chat_id, text)
    await state.finish()