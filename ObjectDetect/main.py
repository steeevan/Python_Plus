from camera import Camera
from detector import ObjectDetector
from utils import draw_boxes
import cv2

def main():
    # Initialize camera (0 = default webcam; change to 1 or 2 for USB camera)
    cam = Camera(camera_id=0)

    # Initialize object detector (face + eye cascades)
    detector = ObjectDetector()

    while True:
        # Get a frame from the camera
        frame = cam.get_frame()
        if frame is None:
            print(" Failed to get frame")
            break

        # Detect faces and eyes
        detections = detector.detect(frame)

        # Loop through each face detection
        for result in detections:
            face_box = result["face"]
            eye_boxes = result["eyes"]

            # Draw face box in blue
            draw_boxes(frame, [face_box], color=(255, 0, 0))

            # Draw eye boxes in green
            draw_boxes(frame, eye_boxes, color=(0, 255, 0))

        # Show the output
        cv2.imshow("Face + Eye Detection", frame)

        # Exit loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cam.release()

if __name__ == "__main__":
    main()
