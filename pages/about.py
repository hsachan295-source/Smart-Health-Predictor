import streamlit as st

def show():
    st.markdown("### 📖 About This Project")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea20, #764ba220);
                border-radius: 16px; padding: 1.5rem; margin-bottom: 1.5rem;
                border-left: 5px solid #667eea;">
        <h4 style="color:#667eea; margin:0">🩺 Disease Risk Predictor</h4>
        <p style="margin-top:0.5rem; color:#333;">
            Yeh ek Machine Learning based web application hai jo ek patient ki
            health & lifestyle details lekar predict karta hai ki usse disease ka
            risk hai ya nahi.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🧠 Model Details")
        st.markdown("""
        | Parameter | Value |
        |---|---|
        | Algorithm | Decision Tree Classifier |
        | Criterion | Entropy |
        | Max Depth | 3 |
        | Random State | 42 |
        | Framework | scikit-learn |
        | Format | Pickle (.pkl) |
        """)

    with col2:
        st.markdown("#### 🎯 Target Variable")
        st.markdown("""
        | Class | Meaning |
        |---|---|
        | `0` | No Disease Risk |
        | `1` | Disease Risk Present |
        """)

        st.markdown("#### 📊 Dataset")
        st.markdown("""
        - **Name:** health_lifestyle_dataset.csv
        - **Features:** 15 input columns
        - **Task:** Binary Classification
        - **Split:** 67% Train / 33% Test
        """)

    st.markdown("---")
    st.markdown("#### 🔬 Features Used for Prediction")

    features_info = [
        ("🆔 id", "Patient ka unique ID"),
        ("🎂 age", "Patient ki umra (saal mein)"),
        ("⚧ gender", "Male = 1, Female = 0"),
        ("⚖️ bmi", "Body Mass Index"),
        ("🚶 daily_steps", "Rozana chalane ke steps"),
        ("😴 sleep_hours", "Rozana ki neend (ghante)"),
        ("💧 water_intake_l", "Pani pine ki matra (litre)"),
        ("🍽️ calories_consumed", "Rozana ki calories"),
        ("🚬 smoker", "Smoker hai? (1=Yes, 0=No)"),
        ("🍺 alcohol", "Alcohol leta hai? (1=Yes, 0=No)"),
        ("❤️ resting_hr", "Resting Heart Rate (bpm)"),
        ("🩸 systolic_bp", "Systolic Blood Pressure"),
        ("🩸 diastolic_bp", "Diastolic Blood Pressure"),
        ("🧪 cholesterol", "Cholesterol level (mg/dL)"),
        ("👨‍👩‍👧 family_history", "Family mein bimari ki history? (1=Yes, 0=No)"),
    ]

    c1, c2 = st.columns(2)
    for i, (feat, desc) in enumerate(features_info):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""
            <div style="background:#f8f9ff; border-radius:8px; padding:0.6rem 1rem;
                        margin-bottom:0.5rem; border-left: 3px solid #667eea;">
                <b>{feat}</b><br>
                <small style="color:#666;">{desc}</small>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 🏗️ Tech Stack")

    techs = [
        ("🐍", "Python 3.x", "Programming Language"),
        ("🌐", "Streamlit", "Web UI Framework"),
        ("🤖", "scikit-learn", "ML Library"),
        ("📊", "Matplotlib", "Visualization"),
        ("🔢", "NumPy", "Numerical Computing"),
        ("🗃️", "Pickle", "Model Serialization"),
    ]

    cols = st.columns(3)
    for i, (icon, name, desc) in enumerate(techs):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="metric-card" style="margin-bottom:1rem;">
                <h3>{icon}</h3>
                <p style="font-weight:600; margin:0; color:#333;">{name}</p>
                <p style="font-size:0.8rem; color:#888; margin:2px 0 0 0;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <p style="text-align:center; color:#999; font-size:0.85rem;">
        Made with ❤️ using Streamlit & scikit-learn
    </p>
    """, unsafe_allow_html=True)
