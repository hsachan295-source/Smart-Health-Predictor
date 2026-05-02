import streamlit as st

st.set_page_config(
    page_title="Disease Risk Predictor",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
    }

    .main-header h1 {
        font-size: 2.4rem;
        font-weight: 700;
        margin: 0;
    }

    .main-header p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin-top: 0.5rem;
    }

    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
    }

    .metric-card h3 {
        color: #667eea;
        font-size: 1.8rem;
        margin: 0;
        font-weight: 700;
    }

    .metric-card p {
        color: #666;
        margin: 4px 0 0 0;
        font-size: 0.9rem;
    }

    .predict-btn > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 0.7rem 2rem !important;
        border-radius: 10px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
    }

    .result-box-high {
        background: linear-gradient(135deg, #ff6b6b, #ee0979);
        color: white;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 8px 24px rgba(238,9,121,0.3);
    }

    .result-box-low {
        background: linear-gradient(135deg, #56ab2f, #a8e063);
        color: white;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 8px 24px rgba(86,171,47,0.3);
    }

    .result-box-high h2, .result-box-low h2 {
        font-size: 2rem;
        margin: 0;
    }

    .result-box-high p, .result-box-low p {
        font-size: 1rem;
        margin-top: 0.5rem;
        opacity: 0.92;
    }

    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #333;
        padding: 0.5rem 0;
        border-bottom: 2px solid #667eea;
        margin-bottom: 1rem;
    }

    .sidebar .sidebar-content {
        background: #f8f9ff;
    }

    .stSlider > div > div > div > div {
        background: #667eea !important;
    }

    div[data-testid="stSidebarNav"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🩺 Disease Risk Predictor</h1>
    <p>Health Lifestyle Analysis powered by Decision Tree AI Model</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🗂️ Navigation")
page = st.sidebar.radio("", ["🏠 Home / Predict", "📊 Model Info", "📖 About"], label_visibility="collapsed")

if page == "🏠 Home / Predict":
    from pages.predict import show
    show()
elif page == "📊 Model Info":
    from pages.model_info import show
    show()
elif page == "📖 About":
    from pages.about import show
    show()
