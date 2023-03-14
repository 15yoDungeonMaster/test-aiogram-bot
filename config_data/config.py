from dotenv import find_dotenv, load_dotenv
import os

if not find_dotenv():
    exit('Не удалось найти файл ..env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
RAPID_API_KEY = os.getenv('RAPID_API_KEY')

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("lowprice", "Поиск дешевых отелей"),
    ("highprice", "Поиск дорогих отелей"),
    ("bestdeal", "Поиск отелей наиболее подходящих по цене и удаленности от центра города"),
    ("history", "Узнать вашу историю поиска"),
    ("help", "Вывести справку"),
)

headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

url_for_city_id = 'https://hotels4.p.rapidapi.com/locations/v3/search'
url_for_summary = 'https://hotels4.p.rapidapi.com/properties/v2/get-summary'
url_properties_list = 'https://hotels4.p.rapidapi.com/properties/v2/list'

