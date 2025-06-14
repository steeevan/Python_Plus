import cv2

def draw_boxes(frame, boxes, color=(0, 255, 0), thickness=2):
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
