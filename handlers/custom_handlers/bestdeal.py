from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from loader import dp
from states.bestdeal_state import BestDealState
from utils.handlers_funcs.start import start
from utils.handlers_funcs.cities_funcs import get_cities, cities_callback
from utils.handlers_funcs.date_funcs import get_checkin_date, get_checkout_date
from utils.handlers_funcs.rooms_funcs import get_adult_rooms, child_info_callback, get_child_rooms
from utils.handlers_funcs.properties_funcs import get_hotels_count, photo_callback, get_photo_count
from utils.handlers_funcs.price_funcs import get_min_price, get_max_price



@dp.message_handler(commands=['bestdeal'])
async def bestdeal_start(message: Message):
    await start(message, command='bestdeal')


@dp.message_handler(state=BestDealState.cities)
async def bestdeal_get_cities(message: Message, state: FSMContext):
    await get_cities(message, state=state, command='bestdeal')


@dp.callback_query_handler(state=BestDealState.cities)
async def bestdeal_cities_callback(callback: CallbackQuery, state: FSMContext):
    await cities_callback(callback, state=state, command='bestdeal')


@dp.message_handler(state=BestDealState.start_date)
async def bestdeal_checkin_date(message: Message, state: FSMContext):
    await get_checkin_date(message, state=state, command='bestdeal')


@dp.message_handler(state=BestDealState.end_date)
async def bestdeal_checkin_date(message: Message, state: FSMContext):
    await get_checkout_date(message, state=state, command='bestdeal')


@dp.message_handler(state=BestDealState.adult_rooms)
async def bestdeal_adult_rooms(message: Message, state: FSMContext):
    await get_adult_rooms(message, state=state, command='bestdeal')


@dp.callback_query_handler(state=BestDealState.adult_rooms)
async def bestdeal_child_info_callback(callback: CallbackQuery, state: FSMContext):
    await child_info_callback(callback, state, command='bestdeal')


@dp.message_handler(state=BestDealState.children_rooms)
async def bestdeal_get_child_rooms(message: Message, state: FSMContext):
    await get_child_rooms(message, state, command='bestdeal')


@dp.message_handler(state=BestDealState.hotels_count)
async def bestdeal_get_hotel_count(message: Message, state: FSMContext):
    await get_hotels_count(message, state, command='bestdeal')


@dp.callback_query_handler(state=BestDealState.photo)
async def bestdeal_photo_callback(callback: CallbackQuery, state: FSMContext):
    await photo_callback(callback, state, command='bestdeal')


@dp.message_handler(state=BestDealState.count_photo)
async def bestdeal_get_photo_count(message: Message, state: FSMContext):
    await get_photo_count(message, state, command='bestdeal')


@dp.message_handler(state=BestDealState.min_price)
async def bestdeal_min_price(message: Message, state: FSMContext):
    await get_min_price(message, state, command='bestdeal')


@dp.message_handler(state=BestDealState.max_price)
async def bestdeal_max_price(message: Message, state: FSMContext):
    await get_max_price(message, state, command='bestdeal')
