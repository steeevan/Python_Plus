import cv2
import torch

class ObjectDetector:
    def __init__(self,
                 face_cascade_path='haarcascade_frontalface_default.xml',
                 eye_cascade_path='haarcascade_eye.xml'):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + eye_cascade_path)

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        results = []

        for (x, y, w, h) in faces:
            # Region of interest for eyes inside face
            face_roi_gray = gray[y:y + h, x:x + w]

            # Detect eyes in the face ROI
            eyes = self.eye_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=5)

            # Adjust eye coordinates relative to the full frame
            eyes_adjusted = [(x + ex, y + ey, ew, eh) for (ex, ey, ew, eh) in eyes]

            # Store face and its eyes as a dictionary
            results.append({
                "face": (x, y, w, h),
                "eyes": eyes_adjusted
            })

        return results
class YOLODetector:
    def __init__(self,model_name='yolov5'):
        self.model = torch.hub.load('ultralytics/yolov5',model_name,pretrained = True)
        self.model.conf = 0.3 # confidence threshold
    
    def detect(self,frame):
        img_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.model(img_rgb)
        return results


