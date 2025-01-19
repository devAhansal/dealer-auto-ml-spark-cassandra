import streamlit as st
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
from pyspark.ml.feature import StringIndexerModel
from pyspark.ml.classification import RandomForestClassificationModel

# Initialiser une session Spark
spark = SparkSession.builder \
    .appName("StreamlitApp") \
    .getOrCreate()

# Charger le modèle PySpark sauvegardé
model_path = "./models/random_forest_model"


# Charger le modèle
model = RandomForestClassificationModel.load("./models/random_forest_model")
# model = PipelineModel.load(model_path)

# Mapping des clusters vers des noms et des images
cluster_names = {
    0: "Voitures moyennes/familiales",
    1: "Voitures économiques/compactes",
    2: "Voitures de luxe",
    3: "Voitures sportives"
}

cluster_images = {
    0: "images/familiales.png",
    1: "images/compactes.png",
    2: "images/luxe.png",
    3: "images/sportives.png"
}

# Titre de l'application
st.set_page_config(page_title="Prédiction de Catégorie de Véhicule", layout="centered", initial_sidebar_state="auto")
st.markdown(
    """
    <style>
    .main {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Prédiction de la Catégorie de Véhicule")

# Description
st.write("Entrez les informations du client pour prédire la catégorie de véhicule.")

# Champs de saisie des données du client
age = st.number_input("Âge", min_value=18, max_value=84, value=30)
taux = st.number_input("Taux", min_value=544, max_value=74185, value=544)
situation_familiale = st.selectbox("Situation Familiale", ['En Couple', 'Célibataire', 'Marié(e)', 'Divorcée'])
nb_enfants = st.number_input("Nombre d'Enfants à Charge", min_value=0, max_value=4, value=0)
deuxieme_voiture = st.selectbox("Possède une deuxième voiture", [False, True])

# Bouton pour prédire
if st.button("Prédire la Catégorie"):
    # Préparer les données d'entrée
    input_data = pd.DataFrame({
        "age": [age],
        "taux": [taux],
        "situationFamiliale": [situation_familiale],
        "nbEnfantsAcharge": [nb_enfants],
        "2eme voiture": [deuxieme_voiture],
    })

    # Convertir les données en DataFrame Spark
    input_spark_df = spark.createDataFrame(input_data)

    # Prédiction
    prediction = model.transform(input_spark_df)
    predicted_cluster = prediction.select("prediction").collect()[0][0]
    cluster_name = cluster_names[predicted_cluster]
    cluster_image_path = cluster_images[predicted_cluster]
    
    # Afficher le résultat
    st.success(f"La catégorie prédite du véhicule est : **{cluster_name}**")
    st.image(cluster_image_path, caption=f"Illustration de {cluster_name}", use_container_width=True)

# Section pour afficher des informations supplémentaires
st.sidebar.title("À propos")
st.sidebar.info(
    """
    Cette application utilise un modèle Random Forest pour prédire la catégorie de véhicule 
    en fonction des données clients. Veuillez entrer les informations nécessaires pour obtenir une prédiction.
    """
)