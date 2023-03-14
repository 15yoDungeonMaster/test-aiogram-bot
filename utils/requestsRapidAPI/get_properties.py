import json
import pprint
from typing import Union

import requests
from aiogram.dispatcher import FSMContext
from config_data.config import url_properties_list, url_for_summary, headers
from loader import db_history


def get_address(hotel_id):
    url = url_for_summary

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotel_id
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    address = json.loads(response.text)['data']['propertyInfo']['summary']['location']['address']['addressLine']
    return address


async def get_properties(command: str, state: FSMContext):
    url = url_properties_list
    async with state.proxy() as data:
        payload = {
            "currency": "USD",
            "eapid": 1,
            "locale": "ru_RU",
            "siteId": 300000001,
            "destination": {"regionId": data['regionId']},
            "checkInDate": data['checkInDate'],
            "checkOutDate": data['checkOutDate'],
            "rooms": data['rooms'],
            "resultsStartingIndex": 0,
            "resultsSize": data['resultsSize'],
            "sort": data['sort'],
            "filters": {
            }
        }
        if command == 'highprice':
            payload['filters'] = {'price': {'max': 1000, 'min': 500}}
        elif command == 'bestdeal':
            payload['filters'] = {'price': {'max': data["max_price"], 'min': data["min_price"]}}
        user_id = data['id']
    # pprint.pprint(payload)
    try:
        response = requests.request("POST", url, json=payload, headers=headers)
        if response:

            try:
                if command == 'highprice':
                    data = json.loads(response.text)['data']['propertySearch']['properties'][::-1]
                else:
                    data = json.loads(response.text)['data']['propertySearch']['properties']

                if data:
                    return normalize_str(data, user_id, command)
                else:
                    return 'По вашему запросу ничего не найдено. Попробуйте снова /start'
            except KeyError as a:
                return 'Ошибка ответа сервера, попробуйте еще раз. /start'
    except BaseException as e:
        return 'Ошибка:( /start'


def normalize_str(hotels: list, user_id: int, command: str):
    """Преобразовать полученные данные в форматированную строку"""

    if hotels:
        normalized_str = {}

        for num, i_hotel in enumerate(hotels):
            description = f'Отель - {i_hotel["name"]}\n' \
                          f'Адрес - {get_address(i_hotel["id"])}\n' \
                          f'Цена за ночь - {i_hotel["price"]["displayMessages"][0]["lineItems"][0]["price"]["formatted"]} \n' \
                          f'Цена за указанный период - {i_hotel["price"]["displayMessages"][1]["lineItems"][0]["value"][:-5]}\n' \
                          f'Сайт отеля: hotels.com/h{i_hotel["id"]}.Hotel-Information\n'
            normalized_str[i_hotel["id"]] = description
        db_history.set_data(user_id, command, hotels)

        return normalized_str
    else:
        return 'По вашему запросу ничего не найдено. Попробуйте снова /start'
