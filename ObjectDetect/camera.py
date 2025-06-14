import cv2
class Camera:
    def __init__(self,camera_id =0):
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            print("Camera {camera_id} failed to open")
        else:
            print("Camera {camera_id} connected")

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame
    
    def release(self):
        self.cap.release()
        cv2.destroyAllWindows


if __name__ == "__main__":
    cam = Camera(camera_id=1)

    while True:
        frame = cam.get_frame()
        if frame is None:
            print("Failed to capture Frame")
            break
        
        cv2.imshow("Camera Test",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
