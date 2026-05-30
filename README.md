#  Le Cœur Battant - Diagnostic Intelligent

Il s'agit d'une application web de **Machine Learning** permettant de prédire le risque de maladie cardiaque d'un patient en fonction de ses données cliniques (âge, cholestérol, tension, etc.).

##  Fonctionnalités
- **Interface Moderne** : Design soigné avec Streamlit et CSS personnalisé.
- **Diagnostic en temps réel** : Analyse instantanée des données saisies.
- **Machine Learning** : Modèle prédictif basé sur des données cliniques réelles (UCI Dataset).

##  Technologies utilisées
- **Python** (Langage principal)
- **Streamlit** (Framework Web)
- **Scikit-Learn** / **Joblib** (IA et sérialisation)
- **Pandas/Numpy** (Traitement des données)

##  Installation locale
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/emeen1/Heart-Disease-Predictor.git
   
## Exécution 
1. Installez les dépendances :
   ```bash
   pip install streamlit pandas numpy joblib scikit-learn
2. Lancez l'application :
   ```bash
   streamlit run app.py
## Structure du projet
- **app.py** : Code de l'application Streamlit.
- **heart_model.pkl** : Modèle de prédiction entraîné.
- **scaler.pkl** : Transformateur pour la normalisation des données.
- **columns.pkl** : Structure des données d'entrée.
- **Heart_disease/** : Contient le dataset original.
## Auteur : 
@Imane NOUAM 
