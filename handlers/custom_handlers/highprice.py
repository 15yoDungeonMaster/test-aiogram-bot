from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from states.high_price_state import HighPriceState
from utils.handlers_funcs.start import start
from utils.handlers_funcs.cities_funcs import get_cities, cities_callback
from utils.handlers_funcs.date_funcs import get_checkin_date, get_checkout_date
from utils.handlers_funcs.rooms_funcs import get_adult_rooms, child_info_callback, get_child_rooms
from utils.handlers_funcs.properties_funcs import get_hotels_count, photo_callback, get_photo_count


@dp.message_handler(commands=['highprice'])
async def highprice_start(message: Message):
    await start(message, command='highprice')


@dp.message_handler(state=HighPriceState.cities)
async def highprice_get_cities(message: Message, state: FSMContext):
    await get_cities(message, state=state, command='highprice')


@dp.callback_query_handler(state=HighPriceState.cities)
async def highprice_cities_callback(callback: CallbackQuery, state: FSMContext):
    await cities_callback(callback, state=state, command='highprice')


@dp.message_handler(state=HighPriceState.start_date)
async def highprice_checkin_date(message: Message, state: FSMContext):
    await get_checkin_date(message, state=state, command='highprice')


@dp.message_handler(state=HighPriceState.end_date)
async def highprice_checkin_date(message: Message, state: FSMContext):
    await get_checkout_date(message, state=state, command='highprice')


@dp.message_handler(state=HighPriceState.adult_rooms)
async def highprice_adult_rooms(message: Message, state: FSMContext):
    await get_adult_rooms(message, state=state, command='highprice')


@dp.callback_query_handler(state=HighPriceState.adult_rooms)
async def highprice_child_info_callback(callback: CallbackQuery, state: FSMContext):
    await child_info_callback(callback, state, command='highprice')


@dp.message_handler(state=HighPriceState.children_rooms)
async def highprice_get_child_rooms(message: Message, state: FSMContext):
    await get_child_rooms(message, state, command='highprice')


@dp.message_handler(state=HighPriceState.hotels_count)
async def highprice_get_hotel_count(message: Message, state: FSMContext):
    await get_hotels_count(message, state, command='highprice')


@dp.callback_query_handler(state=HighPriceState.photo)
async def highprice_photo_callback(callback: CallbackQuery, state: FSMContext):
    await photo_callback(callback, state, command='highprice')


@dp.message_handler(state=HighPriceState.count_photo)
async def highprice_get_photo_count(message: Message, state: FSMContext):
    await get_photo_count(message, state, command='highprice')