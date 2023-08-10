import cv2
import pyvirtualcam
import numpy as np
from insightface.app import FaceAnalysis
import insightface
from PIL import Image


# Capture video from the webcam
cap = cv2.VideoCapture(0)
app = FaceAnalysis(providers=['CUDAExecutionProvider'],allowed_modules=['detection', 'recognition'] , name="buffalo_s")
app.prepare(ctx_id=0)


source = np.array(Image.open("macron.jpg").convert('RGB'))
source_face = app.get(source)[0]

model_swap = insightface.model_zoo.get_model("inswapper_128.onnx", providers=['CUDAExecutionProvider'])

with pyvirtualcam.Camera(width=640, height=480, fps=20, device="/dev/video10") as cam:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = app.get(frame)

        if len(face_locations) > 0:
                frame = model_swap.get(frame, face_locations[0], source_face, paste_back=True)

        frame = np.fliplr(frame)
        cam.send(frame)
        cam.sleep_until_next_frame()

cap.release()
