import streamlit as st
import joblib
import numpy as np
import os

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'decision_tree_model.pkl')
    return joblib.load(model_path)

def show():
    model = load_model()

    st.markdown("### 📝 Patient Health Details Bharo")
    st.markdown("Sabhi fields fill karo aur prediction le lo.")

    st.markdown('<div class="section-title">👤 Personal Information</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        patient_id = st.number_input("🆔 Patient ID", min_value=1, max_value=99999, value=1001, step=1)
    with c2:
        age = st.slider("🎂 Age", min_value=1, max_value=100, value=35)
    with c3:
        gender = st.selectbox("⚧ Gender", ["Male", "Female"])
        gender_val = 1 if gender == "Male" else 0

    st.markdown('<div class="section-title">📏 Body Metrics</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        bmi = st.number_input("⚖️ BMI", min_value=10.0, max_value=60.0, value=22.5, step=0.1,
                              help="Body Mass Index (Normal: 18.5–24.9)")
    with c2:
        daily_steps = st.number_input("🚶 Daily Steps", min_value=0, max_value=30000, value=7000, step=100)
    with c3:
        sleep_hours = st.slider("😴 Sleep Hours", min_value=1.0, max_value=12.0, value=7.0, step=0.5)

    st.markdown('<div class="section-title">🥗 Diet & Lifestyle</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        water_intake = st.number_input("💧 Water Intake (L)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
    with c2:
        calories = st.number_input("🍽️ Calories Consumed", min_value=500, max_value=5000, value=2000, step=50)
    with c3:
        smoker_input = st.selectbox("🚬 Smoker?", ["No", "Yes"])
        smoker = 1 if smoker_input == "Yes" else 0

    c1, c2 = st.columns(2)
    with c1:
        alcohol_input = st.selectbox("🍺 Alcohol Consumer?", ["No", "Yes"])
        alcohol = 1 if alcohol_input == "Yes" else 0

    st.markdown('<div class="section-title">🏥 Medical Parameters</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        resting_hr = st.number_input("❤️ Resting HR (bpm)", min_value=40, max_value=150, value=72)
    with c2:
        systolic_bp = st.number_input("🩸 Systolic BP", min_value=80, max_value=220, value=120)
    with c3:
        diastolic_bp = st.number_input("🩸 Diastolic BP", min_value=40, max_value=140, value=80)

    c1, c2 = st.columns(2)
    with c1:
        cholesterol = st.number_input("🧪 Cholesterol (mg/dL)", min_value=100, max_value=400, value=180)
    with c2:
        family_history_input = st.selectbox("👨‍👩‍👧 Family History of Disease?", ["No", "Yes"])
        family_history = 1 if family_history_input == "Yes" else 0

    st.markdown("<br>", unsafe_allow_html=True)

    col_btn = st.columns([1, 2, 1])
    with col_btn[1]:
        st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
        predict_clicked = st.button("🔍 Disease Risk Predict Karo")
        st.markdown('</div>', unsafe_allow_html=True)

    if predict_clicked:
        input_data = np.array([[
            patient_id, age, gender_val, bmi, daily_steps,
            sleep_hours, water_intake, calories, smoker,
            alcohol, resting_hr, systolic_bp, diastolic_bp,
            cholesterol, family_history
        ]])

        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0]

        risk_pct = round(proba[1] * 100, 1)
        safe_pct = round(proba[0] * 100, 1)

        st.markdown("---")
        st.markdown("### 🎯 Prediction Result")

        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{risk_pct}%</h3>
                <p>⚠️ Disease Risk</p>
            </div>""", unsafe_allow_html=True)
        with r2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{safe_pct}%</h3>
                <p>✅ Safe Probability</p>
            </div>""", unsafe_allow_html=True)
        with r3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{'High 🔴' if prediction == 1 else 'Low 🟢'}</h3>
                <p>📊 Risk Level</p>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if prediction == 1:
            st.markdown(f"""
            <div class="result-box-high">
                <h2>⚠️ HIGH DISEASE RISK DETECTED</h2>
                <p>Is patient ko disease ka {risk_pct}% risk hai.<br>
                Kripya turant doctor se mile aur lifestyle improve kare.</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 💡 Recommendations")
            recs = []
            if bmi > 25: recs.append("🏃 BMI high hai — exercise badhao")
            if daily_steps < 5000: recs.append("🚶 Daily steps kam hai — 8000+ steps target karo")
            if sleep_hours < 6: recs.append("😴 Neend kam hai — 7-8 ghante so")
            if smoker: recs.append("🚬 Smoking band karo — sehat ke liye bahut hanikarak")
            if alcohol: recs.append("🍺 Alcohol reduce ya band karo")
            if cholesterol > 200: recs.append("🧪 Cholesterol high hai — diet control karo")
            if systolic_bp > 130: recs.append("🩸 BP high hai — low-sodium diet lo")
            if not recs:
                recs.append("👨‍⚕️ Doctor se regular checkup karte raho")
            for r in recs:
                st.warning(r)
        else:
            st.markdown(f"""
            <div class="result-box-low">
                <h2>✅ LOW DISEASE RISK</h2>
                <p>Bahut badhiya! Is patient ko sirf {risk_pct}% disease risk hai.<br>
                Apni healthy lifestyle continue rakho! 💪</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("#### 🌟 Keep it Up!")
            st.success("✅ Aapki lifestyle healthy hai. Aise hi bane raho!")
            st.info("📅 Saal mein ek baar doctor se routine checkup zaroor karwao.")
