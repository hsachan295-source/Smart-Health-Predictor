import streamlit as st
import pickle
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.tree import plot_tree

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '..', 'decision_tree_model.pkl')
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def show():
    model = load_model()

    st.markdown("### 📊 Decision Tree Model Information")
    st.markdown("Yahan apke trained model ki poori details hain.")

    # ── Model Parameters ──────────────────────────────────────────
    st.markdown('<div class="section-title">⚙️ Model Parameters</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    params = [
        ("🌳 Max Depth", model.max_depth),
        ("📐 Criterion", model.criterion),
        ("🌿 Min Samples Leaf", model.min_samples_leaf),
        ("✂️ Min Samples Split", model.min_samples_split),
    ]
    for col, (label, val) in zip([c1, c2, c3, c4], params):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{val}</h3>
                <p>{label}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    params2 = [
        ("📊 Total Features", model.n_features_in_),
        ("🏷️ Classes", len(model.classes_)),
        ("🔢 Total Nodes", model.tree_.node_count),
        ("📏 N Leaves", model.tree_.n_leaves),
    ]
    for col, (label, val) in zip([c1, c2, c3, c4], params2):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{val}</h3>
                <p>{label}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Feature Names ─────────────────────────────────────────────
    st.markdown('<div class="section-title">📋 Input Features</div>', unsafe_allow_html=True)

    feature_labels = {
        'id': '🆔 Patient ID',
        'age': '🎂 Age',
        'gender': '⚧ Gender',
        'bmi': '⚖️ BMI',
        'daily_steps': '🚶 Daily Steps',
        'sleep_hours': '😴 Sleep Hours',
        'water_intake_l': '💧 Water Intake (L)',
        'calories_consumed': '🍽️ Calories Consumed',
        'smoker': '🚬 Smoker',
        'alcohol': '🍺 Alcohol',
        'resting_hr': '❤️ Resting HR',
        'systolic_bp': '🩸 Systolic BP',
        'diastolic_bp': '🩸 Diastolic BP',
        'cholesterol': '🧪 Cholesterol',
        'family_history': '👨‍👩‍👧 Family History',
    }

    cols = st.columns(3)
    for i, feat in enumerate(model.feature_names_in_):
        with cols[i % 3]:
            st.markdown(f"✅ `{feat}` — {feature_labels.get(feat, feat)}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Feature Importance ────────────────────────────────────────
    st.markdown('<div class="section-title">🏆 Feature Importance</div>', unsafe_allow_html=True)

    importances = model.feature_importances_
    features = list(model.feature_names_in_)
    sorted_idx = np.argsort(importances)[::-1]

    fig, ax = plt.subplots(figsize=(10, 5))
    colors = ['#667eea' if imp > 0.05 else '#c8d0f7' for imp in importances[sorted_idx]]
    bars = ax.bar(
        [features[i] for i in sorted_idx],
        importances[sorted_idx],
        color=colors,
        edgecolor='white',
        linewidth=0.8,
        width=0.6
    )
    ax.set_title("Feature Importance — Decision Tree", fontsize=14, fontweight='bold', pad=12)
    ax.set_ylabel("Importance Score", fontsize=11)
    ax.set_xlabel("Features", fontsize=11)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_facecolor('#fafafa')
    fig.patch.set_facecolor('white')
    for bar, imp in zip(bars, importances[sorted_idx]):
        if imp > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.002,
                    f'{imp:.3f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── Decision Tree Visualization ───────────────────────────────
    st.markdown('<div class="section-title">🌳 Decision Tree Visualization</div>', unsafe_allow_html=True)

    fig2, ax2 = plt.subplots(figsize=(20, 8))
    plot_tree(
        model,
        feature_names=list(model.feature_names_in_),
        class_names=['No Risk (0)', 'At Risk (1)'],
        filled=True,
        rounded=True,
        fontsize=9,
        ax=ax2,
        impurity=True,
        proportion=False,
    )
    ax2.set_title("Decision Tree — max_depth=3", fontsize=14, fontweight='bold', pad=10)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()

    st.info("💡 **Blue nodes** → No Risk class dominant | **Orange nodes** → Disease Risk class dominant")
