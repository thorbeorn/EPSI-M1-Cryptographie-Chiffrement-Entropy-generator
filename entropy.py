from utils.viewSurf import get_Random_Video_Page_Today_Link, get_Link_From_Video_Page_Link, Download_Video_From_Video_Link
from utils.video import extract_Random_Picture_From_Video
from utils.image import detect_People_In_Picture
from utils.open_meteo import get_Meteo_Information_At_Location_To_JSON
from utils.json import remove_null_and_not_numeric, multiply_value_json
from utils.key import generate_256bit_key
from config import TEMP_OUTPUT, OUTPUT, LINKS, DEBUG

import json

def Number_People_Detected_Comedie():
    randomVideoPageLink = get_Random_Video_Page_Today_Link(LINKS["Camera_Comedie"])
    if DEBUG:
        print(randomVideoPageLink)
    VideoLink = get_Link_From_Video_Page_Link(randomVideoPageLink)
    if DEBUG:
        print(VideoLink)
    Download_Video_From_Video_Link(VideoLink, TEMP_OUTPUT["Camera_Comedie_video"])
    extract_Random_Picture_From_Video(TEMP_OUTPUT["Camera_Comedie_video"], TEMP_OUTPUT["Camera_Comedie_Picture"])
    temp_Number_People_Detected_Comedie = detect_People_In_Picture(TEMP_OUTPUT["Camera_Comedie_Picture"], OUTPUT["People_Detected_Comedie_Picture"])
    return temp_Number_People_Detected_Comedie

def Meteo_Information_At_location(seed):
    raw_json_data = get_Meteo_Information_At_Location_To_JSON(seed, LINKS["Meteo_Base_Url"])
    formated_json = remove_null_and_not_numeric(raw_json_data)
    with open(OUTPUT["Meteo_Data_JSON"], "w", encoding="utf-8") as f:
        json.dump(formated_json, f, ensure_ascii=False, indent=2)
    return multiply_value_json(formated_json)

def generate_single_number():
    Number_People = Number_People_Detected_Comedie()
    Number_Meteo = Meteo_Information_At_location(Number_People)
    key_bytes, key_hex = generate_256bit_key(Number_People, Number_Meteo, OUTPUT['Key_File'])
    seed = int(key_hex, 16)
    number = seed % 37
    return number, key_hex