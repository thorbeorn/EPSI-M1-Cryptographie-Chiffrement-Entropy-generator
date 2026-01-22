import requests
import random
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}

def get_Meteo_Information_At_Location_To_JSON(base_seed, base_url):
    try:
        date_Today = datetime.now()
        seed = base_seed + (date_Today.hour * 60 * 60 + date_Today.minute * 60 + date_Today.second) * date_Today.day * date_Today.month
        random.seed(seed)
        longitude_random = random.uniform(-180, 180)
        seed2 = base_seed + (date_Today.hour * 60 * 60 + date_Today.minute * 60 + date_Today.second) * date_Today.day * date_Today.month + longitude_random
        random.seed(seed2)
        latitude_random = random.uniform(-90, 90)

        formed_url = base_url.replace("<latitude>", str(latitude_random)).replace("<longitude>", str(longitude_random))
        req_Html = requests.get(formed_url, headers=headers)
        json_data = req_Html.json()
        return json_data
    except :
        raise("Impossible de récuperer le lien de la video random !")