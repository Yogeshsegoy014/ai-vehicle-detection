# src/tracker/deep_sort_tracker.py

from deep_sort_realtime.deepsort_tracker import DeepSort

class DeepSortTracker:
    def __init__(self):
        self.tracker = DeepSort(
            max_age=30,
            n_init=3,
            max_cosine_distance=0.4,
            nn_budget=None
        )

    def update(self, detections, frame):
        """
        detections: torch.Tensor from YOLO [x1, y1, x2, y2, confidence, class]
        frame: numpy.ndarray (BGR image)
        Returns: List of tracked objects
        """
        if detections is None or len(detections) == 0:
            return []

        dets_for_tracker = []
        for det in detections:
            x1, y1, x2, y2, conf, cls = det.tolist()
            bbox = [int(x1), int(y1), int(x2 - x1), int(y2 - y1)]  # x, y, w, h
            dets_for_tracker.append((bbox, conf, int(cls)))

        tracks = self.tracker.update_tracks(dets_for_tracker, frame=frame)

        result_tracks = []
        for track in tracks:
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()  # [left, top, right, bottom]
            result_tracks.append({
                "track_id": track_id,
                "bbox": ltrb,
                "class_id": track.det_class
            })

        return result_tracks

