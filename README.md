# 🚗 Real-Time AI Vehicle Detection System

A production-ready **real-time vehicle detection and analysis system** built using **YOLOv5, DeepSORT, Streamlit, and AI models**.  
This application detects vehicles from dashboard videos, tracks them across frames, zooms into a selected vehicle, identifies brand/model, and generates scene descriptions.

---

## ✨ Features

### 🔍 **1. Real-Time Vehicle Detection**
- YOLO-based vehicle detection  
- Works on videos, images, and webcam feed  
- High accuracy and optimized performance

### 🎯 **2. Object Tracking with DeepSORT**
- Assigns unique IDs  
- Tracks vehicles frame-by-frame  
- Smooth multi-object tracking

### 🔎 **3. Zoom & Identify Vehicle**
- Click a vehicle → zoom view  
- Predicts **brand, model, type, and country**

### 🧠 **4. AI Scene Description**
- GPT-powered explanation of what is happening in the video  
- Great for analytics & autonomous driving assistance

### 🖼️ **5. Image Captioning (BLIP/CLIP)**
- Generates captions for individual frames or full images

### ⚡ **6. Modern Streamlit UI**
- Clean, responsive, fast  
- Hosting-ready (Streamlit Cloud)

---

## 📁 Project Structure

```
REAL_TIME_VEHICLE_AI_SYSTEM/
│── app.py
│── requirements.txt
│── config/
│── src/
│   ├── detector/
│   ├── tracker/
│   ├── utils/
│   ├── ai/
│── assets/
```

---

## ▶️ Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/Yogeshsegoy014/ai-vehicle-detection.git
cd ai-vehicle-detection
```

### 2. (Optional) Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## ☁️ Hosting (Streamlit Cloud)

1. Go to: https://share.streamlit.io  
2. Click **Deploy App**  
3. Select:
   - Repo: `Yogeshsegoy014/ai-vehicle-detection`
   - Branch: `main`
   - App file: `app.py`
4. Add Secrets:

```
OPENAI_API_KEY = "your_key_here"
```

5. Click **Deploy**

Your live link will be ready in 1–2 minutes.

---

## 🧩 Tech Stack

- **Python**
- **YOLOv5** – Object Detection  
- **DeepSORT** – Tracking  
- **Streamlit** – UI  
- **OpenCV** – Video & image processing  
- **NumPy** – Array operations  
- **Pillow** – Image conversions  
- **GPT** – AI scene description  
- **BLIP / CLIP** – Image captioning  

---

## 📜 License
Open-source project. Free to use.

---

## 🙌 Author
**Yogeshwari Senthilkumar**  
Full Stack Developer
