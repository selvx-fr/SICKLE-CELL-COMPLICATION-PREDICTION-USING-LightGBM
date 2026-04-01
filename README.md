# 🩺 Sickle Cell Complication Prediction System

An AI-powered web application that predicts potential complications in Sickle Cell Disease using machine learning and provides risk analysis, insights, and clinical decision support.

Built using a Flask backend, LightGBM machine learning model, and an interactive dashboard for real-time predictions.

---

## 🚀 Features

### 🧠 AI Complication Prediction

* Enter patient clinical data
* Predicts multiple Sickle Cell complications using trained ML model
* Outputs:

  * Predicted complication
  * Confidence score
  * Top probable complications

### 📊 Risk Analysis

* Provides risk level (Low / Medium / High)
* Helps in early detection of severe conditions
* Supports clinical decision-making

### 📈 Interactive Dashboard

* Visual representation using charts
* Clean and user-friendly interface
* Real-time result updates

### 🗂️ Patient Data Management

* Stores patient records in database
* Enables history tracking
* Supports future analysis

### ⚡ Real-Time Processing

* Instant prediction results
* Efficient data preprocessing and model inference

---

## 🏗️ Tech Stack

**Backend:** Flask, Python
**Machine Learning:** LightGBM
**Frontend:** HTML, CSS, JavaScript
**Database:** SQLite
**Libraries:** NumPy, Joblib

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/sickle-cell-prediction.git
cd sickle-cell-prediction
pip install flask lightgbm numpy joblib
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📡 API

**POST /predict**

* Input: Patient clinical data
* Output: Prediction JSON (complication, risk level, confidence)

---

## 📊 Output

* Predicted complication
* Risk level (Low / Medium / High)
* Confidence score
* Ranked list of complications

---

## 🧪 Testing

* Unit Testing
* Integration Testing
* Functional Testing

---

## 📈 Advantages

* Early detection of complications
* Improves patient care and monitoring
* Fast and accurate predictions
* Cost-effective solution
* Scalable for real-world deployment

---

## 🔮 Future Enhancements

* Integration with cloud platforms
* Advanced deep learning models
* Mobile application support
* Enhanced data security
* Larger dataset training
