import streamlit as st
import joblib
import pandas as pd
import numpy as np

# ==========================================
# 0. CONFIGURATION & STYLE GLOBAL
# ==========================================
st.set_page_config(
    page_title="Le Cœur Battant",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Chargement de FontAwesome pour les icônes
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">', unsafe_allow_html=True)

# Gestion de la navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

def go_to_prediction():
    st.session_state['page'] = 'prediction'

def go_to_home():
    st.session_state['page'] = 'home'

# ==========================================
# 1. CHARGEMENT DU MODÈLE
# ==========================================
@st.cache_resource
def load_data():
    try:
        model = joblib.load('heart_model.pkl')
        scaler = joblib.load('scaler.pkl')
        cols = joblib.load('columns.pkl')
        return model, scaler, cols
    except:
        return None, None, None

model, scaler, model_columns = load_data()

# ==========================================
# 2. CSS AVANCÉ (DÉGRADÉ ROUGE/NOIR)
# ==========================================
st.markdown("""
    <style>
    /* --- FOND DÉGRADÉ ROUGE -> NOIR --- */
    .stApp {
        /* Dégradé diagonal : Rouge sombre (Haut Gauche) vers Noir (Bas Droite) */
        background: linear-gradient(135deg, #450a0a 0%, #000000 70%);
        color: white;
    }

    /* --- NAVBAR STYLE --- */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 50px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        background: rgba(0,0,0,0.3); /* Légèrement sombre pour lisibilité */
    }
    .brand {
        font-size: 1.2rem;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
        color: white;
        text-decoration: none;
    }

    /* --- HERO SECTION --- */
    .hero-container {
        text-align: center;
        padding-top: 60px;
        padding-bottom: 40px;
    }
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 1.1;
        /* Texte blanc avec une légère ombre rouge */
        color: white;
        text-shadow: 0px 0px 20px rgba(220, 38, 38, 0.5);
        margin-bottom: 20px;
    }
    .hero-sub {
        font-size: 1.3rem;
        color: #d1d5db; /* Gris clair */
        margin-bottom: 40px;
    }

    /* --- TICKER ANIMATION (Images qui défilent) --- */
    .ticker-wrap {
        width: 100%;
        overflow: hidden;
        background-color: transparent;
        padding: 40px 0;
        /* Masque pour fondre les bords dans le dégradé */
        mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
    }
    .ticker {
        display: flex;
        width: fit-content;
        animation: scroll 25s linear infinite;
    }
    .ticker-item {
        width: 250px;
        height: 150px;
        margin-right: 20px;
        border-radius: 12px;
        overflow: hidden;
        background: rgba(255, 255, 255, 0.05); /* Fond vitré */
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }
    .ticker-item img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }

    /* --- BOUTON STYLISÉ (BLANC SUR FOND ROUGE) --- */
    div.stButton > button {
        background-color: white;
        color: #450a0a; /* Texte rouge sombre */
        border: none;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: 800;
        font-size: 1.1rem;
        transition: all 0.3s;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
        width: 100%;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #f87171; /* Devient rouge clair au survol */
        color: white;
        box-shadow: 0 0 25px rgba(248, 113, 113, 0.6);
    }
    
    /* --- STYLE DU FORMULAIRE --- */
    .result-card {
        padding: 20px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        gap: 20px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. PAGE D'ACCUEIL (HOME)
# ==========================================
if st.session_state['page'] == 'home':

    # 1. Navbar
    st.markdown("""
    <div class="navbar">
        <div class="brand">
            <i class="fa-solid fa-heart-pulse"></i>
            Le Cœur Battant
        </div>
        <div style="font-size: 0.9rem; color: #d1d5db;">
            <i class="fa-solid fa-circle-check" style="color:#10b981;"></i> Système Opérationnel
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. Hero Section
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">Votre santé<br>c'est notre priorité</h1>
        <p class="hero-sub">
            Bienvenue sur notre plateforme de diagnostic nouvelle génération.<br>
            Prédiction précoce. Risque maîtrisé.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 3. Le Bouton "Découvrir" CENTRÉ
    # Astuce : On utilise des colonnes vides [3, 2, 3] pour serrer le bouton au milieu
    col_gauche, col_centre, col_droite = st.columns([3, 2, 3])
    
    with col_centre:
        if st.button("DÉCOUVRIR MAINTENANT"):
            go_to_prediction()
            st.rerun()

    # 4. Ticker Animation (Défilement)
    # Images style médical / dashboard
    images = [
        "https://i.postimg.cc/wBzcTh3R/Design-sans-titre.png",
        "https://i.postimg.cc/rpyjN1TB/Design-sans-titre-(1).png",
        "https://i.postimg.cc/1XDDQXPp/Design-sans-titre-(2).png",
        "https://images.unsplash.com/photo-1530026405186-ed1f139313f8?w=500&auto=format&fit=crop&q=60",
        "https://i.postimg.cc/fWvb6YQR/Design-sans-titre-(3).png",
        # On duplique pour l'effet infini
        "https://i.postimg.cc/wBzcTh3R/Design-sans-titre.png",
        "https://i.postimg.cc/rpyjN1TB/Design-sans-titre-(1).png",
        "https://i.postimg.cc/1XDDQXPp/Design-sans-titre-(2).png",
    ]

    images_html = "".join([f'<div class="ticker-item"><img src="{img}"></div>' for img in images])

    st.markdown(f"""
    <br><br>
    <div class="ticker-wrap">
        <div class="ticker">
            {images_html}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. PAGE PRÉDICTION (FORMULAIRE)
# ==========================================
elif st.session_state['page'] == 'prediction':

    if model is None:
        st.error("🚨 Erreur : Fichiers .pkl manquants.")
        st.stop()

    # Petit bouton retour stylé en haut à gauche
    if st.button("← Retour"):
        go_to_home()
        st.rerun()

    st.markdown("""
        <h2 style='text-align: center; margin-bottom: 40px; color: white;'>
            <i class="fa-solid fa-clipboard-user" style="color:#f87171;"></i> Formulaire Clinique
        </h2>
    """, unsafe_allow_html=True)

    # --- LE FORMULAIRE ---
    with st.container():
        
        colA, colB = st.columns(2)
        
        with colA:
            st.markdown('<h4 style="color:#fca5a5"><i class="fa-solid fa-user"></i> Patient</h4>', unsafe_allow_html=True)
            age = st.number_input("Âge (Années)", 20, 100, 50)
            sex = st.selectbox("Sexe", ["Homme", "Femme"])
            cp = st.selectbox("Douleur Thoracique", ["Typique (Angina)", "Atypique", "Douleur non-angineuse", "Asymptomatique"])
            resting_bp = st.number_input("Tension (mm Hg)", 90, 200, 120)
            chol = st.number_input("Cholestérol (mg/dl)", 100, 600, 200)

        with colB:
            st.markdown('<h4 style="color:#fca5a5"><i class="fa-solid fa-heart-pulse"></i> Examens</h4>', unsafe_allow_html=True)
            fbs = st.selectbox("Glycémie > 120 mg/dl ?", ["Non", "Oui"])
            restecg = st.selectbox("ECG au repos", ["Normal", "Anomalie ST-T", "Hypertrophie"])
            thalach = st.number_input("Fréquence Cardiaque Max", 60, 220, 150)
            exang = st.selectbox("Douleur à l'effort ?", ["Non", "Oui"])
            oldpeak = st.number_input("Dépression ST", 0.0, 6.0, 1.0)

    st.markdown("<br><hr style='border-color: rgba(255,255,255,0.2)'><br>", unsafe_allow_html=True)

    # Bouton Analyser CENTRÉ
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        predict_btn = st.button("LANCER L'ANALYSE CLINIQUE", type="primary", use_container_width=True)

    # --- LOGIQUE ET RÉSULTAT ---
    if predict_btn:
        input_dict = {col: 0 for col in model_columns}
        
        input_dict['age'] = age
        input_dict['trestbps'] = resting_bp
        input_dict['chol'] = chol
        input_dict['thalch'] = thalach
        input_dict['oldpeak'] = oldpeak
        input_dict['sex'] = 1 if sex == "Homme" else 0
        input_dict['fbs'] = 1 if fbs == "Oui" else 0
        input_dict['exang'] = 1 if exang == "Oui" else 0
        
        if cp == "Atypique": input_dict['cp_atypical angina'] = 1
        elif cp == "Douleur non-angineuse": input_dict['cp_non-anginal'] = 1
        elif cp == "Typique (Angina)": input_dict['cp_typical angina'] = 1
            
        if restecg == "Normal": input_dict['restecg_normal'] = 1
        elif restecg == "Anomalie ST-T": 
            for c in input_dict: 
                if 'st-t' in c: input_dict[c] = 1
        elif restecg == "Hypertrophie": 
            for c in input_dict: 
                if 'hypertrophy' in c: input_dict[c] = 1

        # Prédiction
        df_input = pd.DataFrame([input_dict])
        df_scaled = scaler.transform(df_input)
        prediction = model.predict(df_scaled)[0]
        proba = model.predict_proba(df_scaled)[0][1] * 100

        # --- AFFICHAGE RÉSULTAT ---
        if prediction == 1:
            st.markdown(f"""
            <div class="result-card" style="background: rgba(69, 10, 10, 0.9); border-left: 6px solid #ef4444;">
                <i class="fa-solid fa-triangle-exclamation fa-3x" style="color: #fca5a5;"></i>
                <div>
                    <h3 style="color: #fca5a5; margin:0;">RISQUE ÉLEVÉ ({proba:.1f}%)</h3>
                    <p style="color: white; margin:0;">Le modèle détecte des indicateurs préoccupants.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card" style="background: rgba(6, 78, 59, 0.9); border-left: 6px solid #10b981;">
                <i class="fa-solid fa-shield-heart fa-3x" style="color: #6ee7b7;"></i>
                <div>
                    <h3 style="color: #6ee7b7; margin:0;">RISQUE FAIBLE ({proba:.1f}%)</h3>
                    <p style="color: white; margin:0;">Les indicateurs sont rassurants.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()