import torch
import cv2
import numpy as np

class YOLODetector:
    def __init__(self, model_path='yolov5s.pt', conf_thres=0.3):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.model.conf = conf_thres

    def detect(self, frame):
        results = self.model(frame)
        detections = results.xyxy[0]  # tensor: (x1, y1, x2, y2, conf, cls)
        return detections, results

    def draw_boxes(self, frame, detections):
        for *xyxy, conf, cls in detections:
            label = self.model.names[int(cls)]
            if label in ['car', 'bus', 'truck', 'motorcycle']:
                cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])),
                                      (int(xyxy[2]), int(xyxy[3])), (0, 255, 0), 2)
                cv2.putText(frame, f'{label} {conf:.2f}',
                            (int(xyxy[0]), int(xyxy[1]) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return frame
