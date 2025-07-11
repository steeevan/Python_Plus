from camera import Camera
from detector import YOLODetector
import cv2
import time

def main():
    # Initialize camera
    cam = Camera(camera_id=0)

    # Initialize YOLO detector
    detector = YOLODetector(model_name='yolov5s')

    # Setup scoreboard timing
    last_update_time = time.time()
    object_count = 0
    scoreboard_value = 0

    while True:
        # Get frame from camera
        frame = cam.get_frame()
        if frame is None:
            print("Failed to get frame")
            break

        # Detect objects in frame
        results = detector.detect(frame)
        detections = results.xyxy[0]

        # Count all detected objects
        object_count = len(detections)

        # Draw bounding boxes for all detections
        for det in detections:
            x1, y1, x2, y2, conf, cls_id = det
            class_id = int(cls_id)
            label = results.names[class_id]

            # Draw bounding box and label
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Update the scoreboard every second
        current_time = time.time()
        if current_time - last_update_time >= 1.0:
            scoreboard_value = object_count
            last_update_time = current_time

        # Draw the scoreboard
        cv2.rectangle(frame, (10, 10), (300, 50), (0, 0, 0), -1)
        cv2.putText(frame, f"Objects Detected: {scoreboard_value}", (15, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Show the frame
        cv2.imshow("Live Object Detection", frame)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()

if __name__ == "__main__":
    main()
