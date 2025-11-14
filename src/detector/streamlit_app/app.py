import streamlit as st
import cv2
import tempfile
import os
import sys
import requests
from pathlib import Path
from typing import Optional

# ✅ Add project root so Python finds your custom modules
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ✅ Import your components
from src.detector.yolo_detector import YOLODetector
from src.tracker.deep_sort_tracker import DeepSortTracker
from src.utils.config_loader import load_config

# ✅ Load config
config = load_config("config/config.yaml")

# ✅ Streamlit UI
st.set_page_config(page_title="Real-Time Vehicle AI", layout="wide")
st.title("🚗 Real-Time Vehicle AI System")

SAMPLE_VIDEO_URL = "https://cdn.pixabay.com/video/2016/02/14/2165-155327596_large.mp4"
SAMPLE_VIDEO_PATH = Path(PROJECT_ROOT) / "sample_videos" / "pixabay_dashboard.mp4"


def download_sample_video() -> Optional[Path]:
    """Download the demo dashboard video once so it can auto-play in the app."""
    SAMPLE_VIDEO_PATH.parent.mkdir(parents=True, exist_ok=True)
    if SAMPLE_VIDEO_PATH.exists() and SAMPLE_VIDEO_PATH.stat().st_size > 0:
        return SAMPLE_VIDEO_PATH

    with st.spinner("Downloading built-in dashboard demo..."):
        try:
            response = requests.get(SAMPLE_VIDEO_URL, stream=True, timeout=60)
            response.raise_for_status()
            with open(SAMPLE_VIDEO_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        except requests.RequestException as exc:
            st.error(f"Unable to download sample video: {exc}")
            return None
    return SAMPLE_VIDEO_PATH


def process_video(video_path: str, label: str):
    st.subheader(label)
    detector = YOLODetector()
    tracker = DeepSortTracker()

    cap = cv2.VideoCapture(video_path)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections, _ = detector.detect(frame)
        tracker.update(detections, frame)
        output_frame = detector.draw_boxes(frame, detections)
        stframe.image(output_frame, channels="BGR", use_container_width=True)

    cap.release()


uploaded_file = st.file_uploader("Upload a dashboard video", type=["mp4", "mov", "avi"])
auto_demo = st.sidebar.toggle("Auto-play built-in driving demo", value=True)

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name
    process_video(video_path, "Uploaded dashboard video")
    os.unlink(video_path)
elif auto_demo:
    sample_video = download_sample_video()
    if sample_video:
        process_video(str(sample_video), "Built-in driving dashboard demo")
else:
    st.info("Upload a dashboard recording or enable the built-in demo from the sidebar.")

