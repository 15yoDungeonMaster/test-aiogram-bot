from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from states.low_price_state import LowPriceState
from utils.handlers_funcs.start import start
from utils.handlers_funcs.cities_funcs import get_cities, cities_callback
from utils.handlers_funcs.date_funcs import get_checkin_date, get_checkout_date
from utils.handlers_funcs.rooms_funcs import get_adult_rooms, child_info_callback, get_child_rooms
from utils.handlers_funcs.properties_funcs import get_hotels_count, photo_callback, get_photo_count



@dp.message_handler(commands=['lowprice'])
async def lowprice_start(message: Message):
    await start(message, command='lowprice')


@dp.message_handler(state=LowPriceState.cities)
async def lowprice_get_cities(message: Message, state: FSMContext):
    await get_cities(message, state=state, command='lowprice')


@dp.callback_query_handler(state=LowPriceState.cities)
async def lowprice_cities_callback(callback: CallbackQuery, state: FSMContext):
    await cities_callback(callback, state=state, command='lowprice')


@dp.message_handler(state=LowPriceState.start_date)
async def lowprice_checkin_date(message: Message, state: FSMContext):
    await get_checkin_date(message, state=state, command='lowprice')


@dp.message_handler(state=LowPriceState.end_date)
async def lowprice_checkin_date(message: Message, state: FSMContext):
    await get_checkout_date(message, state=state, command='lowprice')


@dp.message_handler(state=LowPriceState.adult_rooms)
async def lowprice_adult_rooms(message: Message, state: FSMContext):
    await get_adult_rooms(message, state=state, command='lowprice')


@dp.callback_query_handler(state=LowPriceState.adult_rooms)
async def lowprice_child_info_callback(callback: CallbackQuery, state: FSMContext):
    await child_info_callback(callback, state, command='lowprice')


@dp.message_handler(state=LowPriceState.children_rooms)
async def lowprice_get_child_rooms(message: Message, state: FSMContext):
    await get_child_rooms(message, state, command='lowprice')


@dp.message_handler(state=LowPriceState.hotels_count)
async def lowprice_get_hotel_count(message: Message, state: FSMContext):
    await get_hotels_count(message, state, command='lowprice')


@dp.callback_query_handler(state=LowPriceState.photo)
async def lowprice_photo_callback(callback: CallbackQuery, state: FSMContext):
    await photo_callback(callback, state, command='lowprice')


@dp.message_handler(state=LowPriceState.count_photo)
async def lowprice_get_photo_count(message: Message, state: FSMContext):
    await get_photo_count(message, state, command='lowprice')



