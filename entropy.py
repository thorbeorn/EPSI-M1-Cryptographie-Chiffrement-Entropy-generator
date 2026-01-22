from utils.viewSurf import get_Random_Video_Page_Today_Link, get_Link_From_Video_Page_Link, Download_Video_From_Video_Link
from utils.video import extract_Random_Picture_From_Video
from utils.image import detect_People_In_Picture
from utils.open_meteo import get_Meteo_Information_At_Location_To_JSON
from utils.json import remove_null_and_not_numeric, multiply_value_json
from utils.key import generate_256bit_key
from config import TEMP_OUTPUT, OUTPUT, LINKS, DEBUG
import hashlib
import time
import requests
import yt_dlp
import json

MAX_RETRIES = 3

def get_sky_entropy_value():
    """Récupère l'entropie des avions (OpenSky)"""
    try:
        url = "https://opensky-network.org/api/states/all?lamin=45.0&lomin=5.0&lamax=50.0&lomax=10.0"
        r = requests.get(url, timeout=3)
        h = hashlib.sha256(r.text.encode()).hexdigest()
        return int(h, 16)
    except:
        return time.time_ns()

def get_youtube_entropy_value():
    """Récupère l'entropie YouTube (Lofi Girl)"""
    try:
        ydl_opts = {'quiet': True, 'no_warnings': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info("https://www.youtube.com/watch?v=jfKfPfyJRdk", download=False)
            data = f"{info.get('view_count')}{time.time_ns()}"
            h = hashlib.sha256(data.encode()).hexdigest()
            return int(h, 16)
    except:
        return time.time_ns()
    
def Number_People_Detected_Comedie():
    for attempt in range(MAX_RETRIES):
        try:
            randomVideoPageLink = get_Random_Video_Page_Today_Link(LINKS["Camera_Comedie"])
            if DEBUG:
                print(f"Tentative {attempt + 1}: {randomVideoPageLink}")
            
            VideoLink = get_Link_From_Video_Page_Link(randomVideoPageLink)
            if DEBUG:
                print(f"Lien vidéo: {VideoLink}")
            
            Download_Video_From_Video_Link(VideoLink, TEMP_OUTPUT["Camera_Comedie_video"])
            extract_Random_Picture_From_Video(TEMP_OUTPUT["Camera_Comedie_video"], TEMP_OUTPUT["Camera_Comedie_Picture"])
            temp_Number_People_Detected_Comedie = detect_People_In_Picture(TEMP_OUTPUT["Camera_Comedie_Picture"], OUTPUT["People_Detected_Comedie_Picture"])
            
            if attempt > 0:
                print(f"✅ Réussi après {attempt + 1} tentatives")
            return temp_Number_People_Detected_Comedie
            
        except Exception as e:
            print(f"⚠️  Erreur tentative {attempt + 1}/{MAX_RETRIES}: {str(e)[:100]}")
            if attempt < MAX_RETRIES - 1:
                print(f"   Essai avec un autre lien...")
            else:
                print(f"❌ Échec après {MAX_RETRIES} tentatives. Utilisation du temps local.")
                return time.time_ns() % 100 # <--- On renvoie un nombre au lieu de crash

def Meteo_Information_At_location(seed):
    """Récupération météo avec gestion d'erreur"""
    try:
        raw_json_data = get_Meteo_Information_At_Location_To_JSON(seed, LINKS["Meteo_Base_Url"])
        formated_json = remove_null_and_not_numeric(raw_json_data)
        with open(OUTPUT["Meteo_Data_JSON"], "w", encoding="utf-8") as f:
            json.dump(formated_json, f, ensure_ascii=False, indent=2)
        return multiply_value_json(formated_json)
    except Exception as e:
        print(f"❌ Erreur météo: {e}")
        return time.time_ns() % 1000 # <--- Secours pour ne pas bloquer

def generate_single_number():
    # 1. Sources originales
    Number_People = Number_People_Detected_Comedie()
    Number_Meteo = Meteo_Information_At_location(Number_People)
    
    # 2. Nouvelles sources injectées
    Number_Sky = get_sky_entropy_value()
    Number_Music = get_youtube_entropy_value()
    
    # 3. Mélange XOR avec conversion forcée en INT (pour éviter les erreurs float)
    key_bytes, key_hex = generate_256bit_key(
        int(Number_People) ^ int(Number_Sky), 
        int(Number_Meteo) ^ int(Number_Music), 
        OUTPUT['Key_File']
    )
    
    seed = int(key_hex, 16)
    number = seed % 37 
    
    return number, key_hex