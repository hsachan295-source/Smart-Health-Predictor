# 🩺 SmartHealth Predictor — Streamlit App

A machine learning-powered web application that predicts disease risk based on lifestyle and health parameters using a Decision Tree model.

---

## 🚀 Live Demo

👉 https://smart-health-predictor-cy2oyhvpsfaw5f2cvsq3xy.streamlit.app/

---

## 📁 Project Structure

```
project/
│
├── app.py
├── decision_tree_model.pkl
├── requirements.txt
├── README.md
│
└── pages/
    ├── __init__.py
    ├── predict.py
    ├── model_info.py
    └── about.py
```

---

## ⚙️ Installation & Setup

### Step 1 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 2 — Run the application

```bash
streamlit run app.py
```

### Step 3 — Open in browser

```
http://localhost:8501
```

---

## 📊 Features

* Machine Learning-based prediction
* User-friendly input form
* Model visualization (Decision Tree)
* Fast UI using Streamlit

---

## 🎯 Model Details

* Algorithm: Decision Tree Classifier
* Criterion: Entropy
* Max Depth: 3
* Accuracy: ~75%
* Target: disease_risk

  * 0 = No Risk
  * 1 = At Risk

---

## 🛠️ Tech Stack

* Python
* Scikit-learn
* Pandas
* Streamlit

---

## ⚠️ Important Note

Make sure `decision_tree_model.pkl` is in the same folder as `app.py`.

---

## 👨‍💻 Author

Harsh Sachan
Email: [hsachan295@gmail.com](mailto:hsachan295@gmail.com)
LinkedIn: https://www.linkedin.com/in/harsh-sachan-b3b24a2a2

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

