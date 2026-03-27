# 🫀 Sickle Cell Complication Prediction System

An AI-powered healthcare dashboard that predicts potential complications in patients with Sickle Cell Disease using clinical data. This system combines machine learning, data visualization, and patient history tracking to support clinical decision-making.

---

## 🚀 Features

### 🧠 AI Prediction Engine
- Predicts top 15 possible complications  
- Provides:
  - Primary complication  
  - Risk level (Low / Moderate / High)  
  - Confidence score  
- Uses trained LightGBM model  

### 📊 Interactive Dashboard
- Beautiful UI with real-time animations  
- Displays:
  - Patients analyzed  
  - Predictions today  
  - Model accuracy  
  - High-risk alerts  

### 🧾 Patient Data Input
Accepts clinical parameters:
- Hemoglobin (Hb)  
- WBC, RBC, Platelets  
- Reticulocytes  
- Bilirubin, LDH  
- Pain type & intensity  
- Demographics (age, gender, blood group)  

### 📋 Patient History
- Stores last 50 patient records  
- Includes:
  - Prediction results  
  - Clinical values  
  - Risk levels  
- Search functionality available  

### 📈 Analytics
Charts for:
- Complication distribution  
- Risk distribution  
- Age-based trends  

---

## 🏗️ Tech Stack

### Frontend
- HTML, CSS (Glassmorphism UI)  
- JavaScript  
- Chart.js  

### Backend
- Python  
- Flask  

### Machine Learning
- LightGBM  
- Scikit-learn  
- Joblib  

### Database
- SQLite  

---

## 📂 Project Structure

```
project/
│
├── app.py
├── templates/
│   └── index.html
├── patients.db
├── lgb_model_24_clinical.pkl
├── scaler_24_clinical.pkl
├── complication_mapping_24_clinical.pkl
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```
git clone https://github.com/selvx-fr/sickle-cell-ai.git
cd sickle-cell-ai
```

### 2️⃣ Install Dependencies
```
pip install flask numpy scikit-learn joblib
```

### 3️⃣ Run the Application
```
python app.py
```

### 4️⃣ Open in Browser
```
http://127.0.0.1:5000/
```

---

## 🔌 API Endpoints

### 🔹 Predict Complication

**POST** `/predict`

#### Request Body:
```
{
  "Patient_Name": "John",
  "Age": 25,
  "Gender": "Male",
  "Blood_Group": "O+",
  "Hb": 7.5,
  "WBC": 12.5,
  "RBC": 3.2,
  "Platelets": 250,
  "Reticulocytes": 2.5,
  "Bilirubin": 1.2,
  "LDH": 450,
  "Pain_Type": "Bone Pain",
  "Pain_Intensity": "High"
}
```

#### Response:
```
{
  "complication": "Acute Chest Syndrome",
  "risk": "High",
  "confidence": 87.5,
  "top_predictions": [...]
}
```

---

### 🔹 Get Patient History

**GET** `/history`

Returns last 50 patient records.

---

## 🧠 How It Works

1. User enters clinical data in UI  
2. Data is sent to Flask backend  
3. Backend:
   - Encodes categorical values  
   - Scales numerical features  
   - Runs ML model  
4. Model outputs probabilities  
5. System:
   - Selects complication  
   - Assigns risk level  
   - Stores result in database  
6. UI displays results + analytics  

---

## 🎯 Use Cases

- Clinical decision support  
- Early risk detection  
- Hospital dashboards  
- Academic ML healthcare projects  

---

## ⚠️ Disclaimer

This system is for educational and research purposes only.  
It should not be used as a substitute for professional medical diagnosis.

---

## 🔮 Future Improvements

- Deploy on cloud (AWS / Render)  
- Add authentication (doctor login)  
- Improve model accuracy  
- Real-time patient monitoring  
- Integration with hospital systems  

---

## 👨‍💻 Author

**selvx-fr**  
AI & Full Stack Developer  

GitHub: https://github.com/selvx-fr
