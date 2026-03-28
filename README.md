# 🌱 Sugarcane Disease Prediction System

An AI-powered agricultural dashboard that detects diseases in sugarcane leaves using image data. This system combines deep learning, computer vision, and interactive visualization to assist farmers and researchers in early disease detection and treatment planning.

---

## 🚀 Features

### 🧠 AI Prediction Engine
- Predicts sugarcane leaf diseases from images  
- Provides:
  - Detected disease name  
  - Risk level (Low / Moderate / High)  
  - Confidence score  
  - Top 3 predictions  
- Uses trained MobileNetV2 CNN model

---

### 🔥 Explainable AI (Grad-CAM)
- Generates heatmap overlay on leaf images  
- Highlights infected regions  
- Helps understand model decision-making  

---

### 📊 Interactive Dashboard
- Modern UI with real-time animations  
- Displays:
  - Prediction confidence  
  - Risk severity  
  - Disease insights  
  - Visual heatmap output  

---

### 🖼️ Image Input System
- Upload sugarcane leaf image  
- Supports drag & drop and file upload  
- Automatically preprocesses:
  - Resize (224 × 224)  
  - Normalization  

---

### 📋 Disease Intelligence
Provides detailed information for each disease:
- Description  
- Cause  
- Pathology  
- Symptoms  
- Cure methods  
- Prevention strategies  

---

## 🏗️ Tech Stack

Frontend:
- HTML  
- CSS (Glassmorphism + animations)  
- JavaScript  

Backend:
- Python  
- Flask  

Machine Learning:
- TensorFlow / Keras  
- MobileNetV2  
- NumPy  
- Pillow  

---

## 📂 Project Structure

project/
│
├── app.py
├── index.html
├── sugarcane_model.h5
├── utils.py
│
├── static/
│   └── uploads/
│
└── README.md

---

## ⚙️ Installation & Setup

1. Clone the Repository
git clone https://github.com/selvx-fr/sugarcane-disease-detection.git
cd sugarcane-disease-detection

2. Install Dependencies
pip install flask tensorflow pillow numpy

3. Run the Application
python app.py

4. Open in Browser
http://localhost:5000

---

## 🔌 API Endpoint

POST /predict → Upload image → Get prediction JSON

---

## 🧠 How It Works

1. User uploads a sugarcane leaf image  
2. Image is preprocessed  
3. Model predicts disease  
4. Grad-CAM generates heatmap  
5. Results displayed in UI  

---

## 🎯 Use Cases

- Smart farming  
- Crop disease detection  
- Agricultural research  

---

## ⚠️ Disclaimer

For educational and research purposes only.

---

## 👨‍💻 Author

selvx-fr  
https://github.com/selvx-fr

---

