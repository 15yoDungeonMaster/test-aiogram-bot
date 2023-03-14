import json
import pprint
from config_data.config import url_for_summary, headers
import requests


def get_images(id, count_images):

    url = url_for_summary

    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": id
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    data = json.loads(response.text)['data']['propertyInfo']['propertyGallery']['images']
    images_url = []

    count = count_images
    while True:
        for url in data:
            if count == 0:

                break
            count -= 1
            url = url['image']['url']
            images_url.append(url)
        return images_url
