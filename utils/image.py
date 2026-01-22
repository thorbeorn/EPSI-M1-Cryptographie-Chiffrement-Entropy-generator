import cv2
from ultralytics import YOLO

def detect_People_In_Picture(image_Path, output_Picture_Filename):
    model = YOLO('models/' + 'yolov8m.pt')
    image = cv2.imread(image_Path)
    
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    l = clahe.apply(l)
    enhanced = cv2.merge([l, a, b])
    enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
    
    results = model(enhanced, 
                   conf=0.20,
                   imgsz=2176,
                   agnostic_nms=True,
                   max_det=500, 
                   verbose=False)
    
    nombre_personnes = 0
    for result in results:
        for box in result.boxes:
            if int(box.cls[0]) == 0:
                nombre_personnes += 1
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f'Personne {confidence:.2f}'
                cv2.putText(image, label, (x1, y1 - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imwrite(output_Picture_Filename, image)
    
    return nombre_personnes