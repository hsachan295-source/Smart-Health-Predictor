🩺 SmartHealth Predictor — Streamlit App

A machine learning-powered web application that predicts disease risk based on lifestyle and health parameters using a Decision Tree model.

🚀 Live Demo

👉 Click here to use the app

(Add your Streamlit / Render / Vercel link here)

📁 Project Structure
project/
│
├── app.py                  # Main Streamlit entry point
├── decision_tree_model.pkl # Trained ML model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
└── pages/
    ├── __init__.py
    ├── predict.py          # Prediction form page
    ├── model_info.py       # Model insights & visualization
    └── about.py            # About project
⚙️ Installation & Setup
Step 1 — Install dependencies
pip install -r requirements.txt
Step 2 — Run the application
streamlit run app.py
Step 3 — Open in browser
http://localhost:8501
📊 Features
🧠 Machine Learning-based prediction
📥 User input form for health data
📈 Model visualization (Decision Tree + Feature Importance)
⚡ Fast and interactive UI using Streamlit
🎯 Model Details
Algorithm: Decision Tree Classifier
Criterion: Entropy
Max Depth: 3
Accuracy: ~75%
Target Variable: disease_risk
0 → No Risk
1 → At Risk
Input Features: 15 health & lifestyle attributes
🛠️ Tech Stack
Python 🐍
Scikit-learn 🤖
Pandas & NumPy 📊
Streamlit 🌐
⚠️ Important Note

Ensure that the file decision_tree_model.pkl is placed in the same directory as app.py.

📌 Future Improvements
🔥 Improve model accuracy (80%+)
📊 Add more visual analytics
🌍 Deploy on cloud with custom domain
📱 Mobile-friendly UI
👨‍💻 Author

Harsh Sachan
📧 hsachan295@gmail.com

🔗 LinkedIn
