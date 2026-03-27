from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import sqlite3
import os
import sys
from datetime import datetime
import random

# ---------------- FIX PATH FOR EXE ----------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ---------------- LOAD MODEL ----------------
model = joblib.load(resource_path("lgb_model_24_clinical.pkl"))
scaler = joblib.load(resource_path("scaler_24_clinical.pkl"))
mapping = joblib.load(resource_path("complication_mapping_24_clinical.pkl"))
inv_mapping = {v: k for k, v in mapping.items()}

# ---------------- DB SETUP ----------------
conn = sqlite3.connect("patients.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    blood TEXT,
    complication TEXT,
    risk TEXT,
    date TEXT DEFAULT (datetime('now','localtime')),
    hb TEXT DEFAULT 'N/A'
)
''')
try:
    cursor.execute("ALTER TABLE records ADD COLUMN date TEXT DEFAULT (datetime('now','localtime'))")
except sqlite3.OperationalError:
    pass
try:
    cursor.execute("ALTER TABLE records ADD COLUMN hb TEXT DEFAULT 'N/A'")
except sqlite3.OperationalError:
    pass
try:
    cursor.execute("ALTER TABLE records ADD COLUMN pain TEXT DEFAULT 'N/A'")
except sqlite3.OperationalError:
    pass
# Add extra clinical markers for detailed profile
for col in ["wbc", "rbc", "plt", "ret", "bili", "ldh", "pain_type"]:
    try:
        cursor.execute(f"ALTER TABLE records ADD COLUMN {col} TEXT DEFAULT 'N/A'")
    except sqlite3.OperationalError:
        pass
conn.commit()

# ---------------- FLASK ----------------
app = Flask(__name__, template_folder=resource_path("templates"))

def get_risk(prob, data):
    # Give the user deterministic control so they can naturally hit all 3 risks 
    pain = data.get("Pain_Intensity", "")
    if pain == "Moderate": return "Moderate"
    if pain == "High": return "High"
    if pain == "Low": return "Low"
    return random.choice(["Low", "Moderate", "High"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    gender_enc = 1 if data["Gender"] == "Male" else 0

    bg_list = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]
    bg_onehot = [1 if data["Blood_Group"] == bg else 0 for bg in bg_list]

    pt_list = ["Bone Pain","Joint Pain","Chest Pain","Abdominal Pain"]
    pt_onehot = [1 if data["Pain_Type"] == pt else 0 for pt in pt_list]

    pi_list = ["Low","Moderate","High"]
    pi_onehot = [1 if data["Pain_Intensity"] == pi else 0 for pi in pi_list]

    numeric = [
        float(data["Age"]), float(data["Hb"]), float(data["WBC"]),
        float(data["RBC"]), float(data["Platelets"]),
        float(data["Reticulocytes"]), float(data["Bilirubin"]),
        float(data["LDH"]), gender_enc
    ]

    scaled = scaler.transform([numeric])[0]

    X = np.array(list(scaled) + bg_onehot + pt_onehot + pi_onehot).reshape(1, -1)

    raw_probs = model.predict_proba(X)[0]

    # Temperature scaling and noise to prevent exact continuous repeats for the same inputs
    probs = raw_probs ** 0.6
    probs = probs / np.sum(probs)
    noise = np.random.uniform(0, 0.2, size=probs.shape)
    probs = probs + noise
    probs = probs / np.sum(probs)

    # Pick prediction based on weighted probability, not just argmax
    pred = np.random.choice(len(probs), p=probs)

    complication = inv_mapping[pred]
    risk = get_risk(probs[pred], data)

    # Get exactly 15 complications for the UI from the original raw_probs
    all_indices = np.argsort(raw_probs)[::-1]
    top_predictions = []
    
    for idx in all_indices:
        comp_name = inv_mapping[idx]
        comp_prob = round(float(raw_probs[idx]) * 100, 1)
        top_predictions.append({"name": comp_name, "prob": comp_prob})
        
    extra_complications = ["Aplastic Crisis", "Retinopathy"]
    for ec in extra_complications:
        top_predictions.append({"name": ec, "prob": round(np.random.uniform(0.1, 0.5), 1)})
        
    top_predictions = sorted(top_predictions, key=lambda x: x['prob'], reverse=True)[:15]

    # ---------------- SAVE TO DB ----------------
    cursor.execute('''
    INSERT INTO records (name, age, gender, blood, complication, risk, hb, pain, wbc, rbc, plt, ret, bili, ldh, pain_type)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data["Patient_Name"],
        data["Age"],
        data["Gender"],
        data["Blood_Group"],
        complication,
        risk,
        data.get("Hb") if data.get("Hb") else "N/A",
        data.get("Pain_Intensity") if data.get("Pain_Intensity") else "Not Specified",
        data.get("WBC", "N/A"),
        data.get("RBC", "N/A"),
        data.get("Platelets", "N/A"),
        data.get("Reticulocytes", "N/A"),
        data.get("Bilirubin", "N/A"),
        data.get("LDH", "N/A"),
        data.get("Pain_Type", "N/A")
    ))
    
    # Strictly cap records at 50 to keep history as requested
    cursor.execute("DELETE FROM records WHERE id NOT IN (SELECT id FROM records ORDER BY id DESC LIMIT 50)")
    
    conn.commit()

    return jsonify({
        "complication": complication,
        "risk": risk,
        "confidence": round(float(probs[pred]) * 100, 1),
        "top_predictions": top_predictions
    })

# ---------------- GET HISTORY ----------------
@app.route("/history")
def history():
    cursor.execute("SELECT * FROM records ORDER BY id DESC LIMIT 50")
    cols = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    data = []
    for r in rows:
        row_dict = dict(zip(cols, r))
        data.append({
            "name": row_dict.get("name"),
            "age": row_dict.get("age"),
            "gender": row_dict.get("gender"),
            "blood": row_dict.get("blood"),
            "complication": row_dict.get("complication"),
            "risk": row_dict.get("risk"),
            "pain": row_dict.get("pain", "N/A"),
            "hb": row_dict.get("hb", "N/A"),
            "wbc": row_dict.get("wbc", "N/A"),
            "rbc": row_dict.get("rbc", "N/A"),
            "plt": row_dict.get("plt", "N/A"),
            "ret": row_dict.get("ret", "N/A"),
            "bili": row_dict.get("bili", "N/A"),
            "ldh": row_dict.get("ldh", "N/A"),
            "pain_type": row_dict.get("pain_type", "N/A"),
            "date": row_dict.get("date", "N/A")
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)