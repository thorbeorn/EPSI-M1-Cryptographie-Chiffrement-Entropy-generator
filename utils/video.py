import cv2
import os
from datetime import datetime, timedelta
import random

def extract_Random_Picture_From_Video(video_Path, output_Picture_Filename) :
    try :
        date_Today = datetime.now()
        seed = os.path.getsize(video_Path) + (date_Today.hour * 60 * 60 + date_Today.minute * 60 + date_Today.second) * date_Today.day * date_Today.month
        random.seed(seed)
        vidcap = cv2.VideoCapture(video_Path)
        frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        seconds = round(frames / fps)
        video_time = timedelta(seconds=seconds).seconds
        vidcap.set(cv2.CAP_PROP_POS_MSEC, random.uniform(1, video_time) * 1000)
        success,image = vidcap.read()
        if success:
            cv2.imwrite(output_Picture_Filename, image)
    except Exception as e:
        raise(e)