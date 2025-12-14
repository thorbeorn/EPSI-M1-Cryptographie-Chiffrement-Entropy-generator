from utils.viewSurf import get_Random_Video_Page_Today_Link, get_Link_From_Video_Page_Link, Download_Video_From_Video_Link
from utils.video import extract_Random_Picture_From_Video
from utils.image import detect_People_In_Picture
from utils.file_and_folder import init_File_And_Folder, remove_Temp_File
from utils.open_meteo import get_Meteo_Information_At_Location_To_JSON
from utils.json import remove_null_and_not_numeric, multiply_value_json
from utils.key import generate_256bit_key

import json

LINKS = {
    "Camera_Comedie": "https://viewsurf.com/univers/ville/vue/14664-france-languedoc-roussillon-montpellier-place-de-la-comedie",
    "Meteo_Base_Url": "https://api.open-meteo.com/v1/forecast?latitude=<latitude>&longitude=<longitude>&current=temperature_2m,precipitation,rain,wind_speed_10m,wind_direction_10m,wind_gusts_10m,relative_humidity_2m,apparent_temperature,is_day,showers,snowfall,weather_code,cloud_cover,surface_pressure,pressure_msl"
}
TEMP_OUTPUT = {
    "temp_folder": "temp/",
    "Camera_Comedie_video": "temp/Comedie_video.mp4",
    "Camera_Comedie_Picture": "temp/Comedie_pic.jpg"
}
OUTPUT = {
    "folder": "output/",
    "People_Detected_Comedie_Picture": "output/Comedie_people_Detecter.jpg",
    "Meteo_Data_JSON": "output/Meteo_data.json",
    "Key_File": "output/generated_key.txt"
}
removeTempFile = True

init_File_And_Folder(TEMP_OUTPUT, OUTPUT)

def Number_People_Detected_Comedie() :
    randomVideoPageLink = get_Random_Video_Page_Today_Link(LINKS["Camera_Comedie"])
    print(randomVideoPageLink)
    VideoLink = get_Link_From_Video_Page_Link(randomVideoPageLink)
    print(VideoLink)
    Download_Video_From_Video_Link(VideoLink, TEMP_OUTPUT["Camera_Comedie_video"])
    extract_Random_Picture_From_Video(TEMP_OUTPUT["Camera_Comedie_video"], TEMP_OUTPUT["Camera_Comedie_Picture"])
    temp_Number_People_Detected_Comedie = detect_People_In_Picture(TEMP_OUTPUT["Camera_Comedie_Picture"], OUTPUT["People_Detected_Comedie_Picture"])
    if removeTempFile :
        remove_Temp_File(TEMP_OUTPUT)
    return temp_Number_People_Detected_Comedie

def Meteo_Information_At_location(seed):
    raw_json_data = get_Meteo_Information_At_Location_To_JSON(seed, LINKS["Meteo_Base_Url"])
    formated_json = remove_null_and_not_numeric(raw_json_data)
    with open(OUTPUT["Meteo_Data_JSON"], "w", encoding="utf-8") as f:
        json.dump(formated_json, f, ensure_ascii=False, indent=2)
    return multiply_value_json(formated_json)

Number_People = Number_People_Detected_Comedie()
Number_Meteo = Meteo_Information_At_location(Number_People)
key_bytes, key_hex = generate_256bit_key(Number_People, Number_Meteo, OUTPUT['Key_File'])

print(f"\n{'='*60}")
print(f"CLÉ 256 BITS GÉNÉRÉE")
print(f"{'='*60}")
print(f"Format hexadécimal: {key_hex}")
print(f"Format bytes: {key_bytes}")
print(f"Longueur: {len(key_bytes)} bytes ({len(key_bytes)*8} bits)")
print(f"Sauvegardée dans: {OUTPUT['Key_File']}")
print(f"{'='*60}\n")