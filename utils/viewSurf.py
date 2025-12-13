import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random
import re
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def get_All_Video_Page_Today_Link(master_Link) : 
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        req_Html_Camera_Commedie = requests.get(master_Link, headers=headers)
        soup_Camera_Commedie = BeautifulSoup(req_Html_Camera_Commedie.text, 'html.parser')
        date_Today = datetime.now()
        list_Video_Link_Today = [
            "https://viewsurf.com" + span.parent.get('href') for span in soup_Camera_Commedie.select('#scroller > ul > li > a > span')
            if (lambda date_text: 
                datetime.strptime(date_text, "%d/%m %H:%M").replace(year=date_Today.year).date() == date_Today.date()
                if date_text else False
            )(span.get_text())
        ]
        nombre_videos = len(list_Video_Link_Today)
        seed = nombre_videos + (date_Today.hour * 60 * 60 + date_Today.minute * 60 + date_Today.second) * date_Today.day * date_Today.month
        random.seed(seed)
        return list_Video_Link_Today[random.randint(1, nombre_videos) - 1]
    except :
        raise("Impossible de récuperer le lien de la video random !")
def get_Random_Video_Page_Today_Link(master_Link) :
    try:
        req_Html = requests.get(master_Link, headers=headers)
        soup_HTML = BeautifulSoup(req_Html.text, 'html.parser')
        date_Today = datetime.now()
        list_Video_Link_Today = [
            "https://viewsurf.com" + span.parent.get('href') for span in soup_HTML.select('#scroller > ul > li > a > span')
            if (lambda date_text: 
                datetime.strptime(date_text, "%d/%m %H:%M").replace(year=date_Today.year).date() == date_Today.date()
                if date_text else False
            )(span.get_text())
        ]
        nombre_videos = len(list_Video_Link_Today)
        seed = nombre_videos + (date_Today.hour * 60 * 60 + date_Today.minute * 60 + date_Today.second) * date_Today.day * date_Today.month
        random.seed(seed)
        return list_Video_Link_Today[random.randint(1, nombre_videos) - 1]
    except :
        raise("Impossible de récuperer le lien de la video random !")

def get_Link_From_Video_Page_Link(video_Page_Link) :
    try:
        req_Html = requests.get(video_Page_Link, headers=headers)
        soup_Html = BeautifulSoup(req_Html.text, 'html.parser')
        video_UUID = soup_Html.select("#webcam-main-container > article > div:nth-child(1) > iframe")[0].get("src").split("?uuid=")[1].split("&")[0]
        return "https://deliverys4.quanteec.com/contents/encodings/vod/" + video_UUID + "/master.m3u8"
    except Exception as e:
        raise(e)
def Download_Video_From_Video_Link(video_Link, output_Video_Filename):
    try :
        response = requests.get(video_Link, headers=headers)
        response.raise_for_status()
        m3u8_content = response.text
        base_url = video_Link.rsplit('/', 1)[0]
        
        playlists = []
        segments = []
        init_segment = None
        for line in m3u8_content.split('\n'):
            line = line.strip()
            if line.startswith('#EXT-X-MAP'):
                match = re.search(r'URI="([^"]+)"', line)
                if match:
                    init_url = match.group(1)
                    if not init_url.startswith('http'):
                        init_segment = f"{base_url}/{init_url}"
                    else:
                        init_segment = init_url
            if line and not line.startswith('#'):
                if not line.startswith('http'):
                    url = f"{base_url}/{line}"
                else:
                    url = line
                
                if '.m3u8' in url:
                    playlists.append(url)
                else:
                    segments.append(url)
        
        if playlists:
            response = requests.get(playlists[-1], headers=headers)
            response.raise_for_status()
            m3u8_content = response.text
            base_url = playlists[-1].rsplit('/', 1)[0]
            segments = []
            init_segment = None
            for line in m3u8_content.split('\n'):
                line = line.strip()
                if line.startswith('#EXT-X-MAP'):
                    match = re.search(r'URI="([^"]+)"', line)
                    if match:
                        init_url = match.group(1)
                        if not init_url.startswith('http'):
                            init_segment = f"{base_url}/{init_url}"
                        else:
                            init_segment = init_url
                if line and not line.startswith('#'):
                    if not line.startswith('http'):
                        segment_url = f"{base_url}/{line}"
                    else:
                        segment_url = line
                    segments.append(segment_url)

        with open(output_Video_Filename, 'wb') as output_file:
            if init_segment:
                try:
                    response = requests.get(init_segment, headers=headers, timeout=30)
                    response.raise_for_status()
                    output_file.write(response.content)
                except Exception as e:
                    raise(f"Erreur lors du téléchargement du segment d'initialisation: {e}")
            else:
                raise("Aucun segment d'initialisation trouvé")

            for i, segment_url in enumerate(segments, 1):
                try:
                    response = requests.get(segment_url, headers=headers, timeout=30)
                    response.raise_for_status()
                    output_file.write(response.content)
                    
                except Exception as e:
                    raise(f"\nErreur lors du téléchargement du segment {i}: {e}")
        file_size = os.path.getsize(output_Video_Filename)
        if file_size < 1000:
            raise("Attention : le fichier semble très petit, il y a peut-être eu un problème")
        return output_Video_Filename
    except Exception as e:
        raise(e)