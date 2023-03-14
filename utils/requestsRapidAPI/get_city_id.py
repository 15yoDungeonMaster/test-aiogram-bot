import pprint

import requests
import json
from config_data.config import url_for_city_id, headers
from keyboards.inline.cities_kb import get_cities_button

url = url_for_city_id


def get_city_id(city: str):
    querystring = {"q": city, "locale": "ru_RU"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        if response:
            data = json.loads(response.text)
            data_for_buttons = {}

            for i_item in data['sr']:
                if i_item['type'] == 'CITY':
                    name = i_item['regionNames']['fullName']
                    id = i_item['gaiaId']
                    data_for_buttons[name] = id
            return get_cities_button(data_for_buttons)
    except BaseException as e:
        return 'No response'

