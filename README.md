# 🩺 Disease Risk Predictor — Streamlit App

Decision Tree model se disease risk predict karne wala Streamlit web application.

---

## 📁 Project Structure

```
project/
│
├── app.py                  # Main Streamlit entry point
├── decision_tree_model.pkl # Trained ML model
├── requirements.txt        # Python dependencies
├── README.md               # Yeh file
│
└── pages/
    ├── __init__.py
    ├── predict.py          # Prediction form page
    ├── model_info.py       # Model details + visualizations
    └── about.py            # About project page
```

---

## 🚀 Kaise Chalao

### Step 1 — Dependencies install karo
```bash
pip install -r requirements.txt
```

### Step 2 — App run karo
```bash
streamlit run app.py
```

### Step 3 — Browser mein kholo
```
http://localhost:8501
```

---

## 📊 Pages

| Page | Description |
|---|---|
| 🏠 Home / Predict | Patient details dalo, prediction lo |
| 📊 Model Info | Feature importance, tree visualization |
| 📖 About | Project info aur tech stack |

---

## 🎯 Model Details

- **Algorithm:** Decision Tree Classifier
- **Criterion:** Entropy
- **Max Depth:** 3
- **Target:** `disease_risk` (0 = No Risk, 1 = At Risk)
- **Features:** 15 health & lifestyle inputs

---

## ⚠️ Note

`decision_tree_model.pkl` file `app.py` ke saath **same folder** mein honi chahiye.
