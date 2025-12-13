from utils.viewSurf import get_Random_Video_Page_Today_Link, get_Link_From_Video_Page_Link, Download_Video_From_Video_Link
from utils.video import extract_Random_Picture_From_Video
from utils.image import detect_People_In_Picture
from utils.file_and_folder import init_File_And_Folder, remove_Temp_File

LINKS = {
    "Camera_Comedie": "https://viewsurf.com/univers/ville/vue/14664-france-languedoc-roussillon-montpellier-place-de-la-comedie"
}
TEMP_OUTPUT = {
    "temp_folder": "temp/",
    "Camera_Comedie_video": "temp/Comedie_video.mp4",
    "Camera_Comedie_Picture": "temp/Comedie_pic.jpg"
}
OUTPUT = {
    "folder": "output/",
    "People_Detected_Comedie_Picture": "output/Comedie_people_Detecter.jpg"
}

init_File_And_Folder(TEMP_OUTPUT, OUTPUT)
randomVideoPageLink = get_Random_Video_Page_Today_Link(LINKS["Camera_Comedie"])
print(randomVideoPageLink)
VideoLink = get_Link_From_Video_Page_Link(randomVideoPageLink)
print(VideoLink)
Download_Video_From_Video_Link(VideoLink, TEMP_OUTPUT["Camera_Comedie_video"])
extract_Random_Picture_From_Video(TEMP_OUTPUT["Camera_Comedie_video"], TEMP_OUTPUT["Camera_Comedie_Picture"])
Number_People_Detected_Comedie = detect_People_In_Picture(TEMP_OUTPUT["Camera_Comedie_Picture"], OUTPUT["People_Detected_Comedie_Picture"])
remove_Temp_File(TEMP_OUTPUT)

print(Number_People_Detected_Comedie)