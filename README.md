# Système de Prédiction et d'Analyse pour un Concessionnaire Automobile

Ce projet vise à aider un concessionnaire automobile à analyser et prédire les préférences des clients en utilisant des techniques de Machine Learning (ML) et de Big Data. Les données sont stockées dans **Cassandra** et traitées avec **Apache Spark** pour une analyse distribuée. Le projet inclut l'exploration des données (EDA), le clustering avec K-Means, et la classification avec Random Forest.

---

## **Objectifs du Projet**
1. **Exploration des Données (EDA)** : Nettoyer et analyser les données pour comprendre les tendances et les corrélations.
2. **Clustering** : Appliquer l'algorithme K-Means pour segmenter les clients et les véhicules.
3. **Classification** : Utiliser Random Forest pour prédire les préférences des clients ou les catégories de véhicules.
4. **Intégration Big Data** : Utiliser Spark pour le traitement distribué et Cassandra pour le stockage des données.

---

## **Technologies Utilisées**
- **Apache Spark** : Pour le traitement distribué des données.
- **Cassandra** : Pour le stockage des données.
- **Python** : Pour l'analyse des données et le Machine Learning.
- **Jupyter Notebook** : Pour l'exploration interactive des données.
- **Docker** : Pour l'environnement de développement conteneurisé.
- **Seaborn/Matplotlib** : Pour la visualisation des données.

---

## **Structure du Projet**
-   dealer-auto-ml-spark-cassandra/
-   ├── data/
-   │ ├── raw/ # Données brutes (CSV, Excel, etc.)
-   │ ├── processed/ # Données nettoyées et prêtes pour l'analyse
-   ├── notebooks/
-   │ ├── EDA_clients.ipynb # Exploration des données clients
-   │ ├── EDA_catalogue.ipynb # Exploration des données catalogue
-   │ ├── EDA_immatriculation.ipynb # Exploration des données d'immatriculation
-   │ ├── clustering.ipynb # Clustering avec K-Means
-   │ ├── classification.ipynb # Classification avec Random Forest
-   ├── scripts/
-   │ ├── data_cleaning.py # Script de nettoyage des données
-   │ ├── spark_cassandra.py # Script pour interagir avec Spark et Cassandra
-   ├── docker-compose.yml # Configuration Docker pour Spark et Cassandra
-   ├── requirements.txt # Dépendances Python
-   ├── README.md # Documentation du projet

---

## **Installation**
1. **Cloner le Repository** :
   ```bash
-  git clone https://github.com/devAhansal/dealer-auto-ml-spark-cassandra.git
   cd dealer-auto-ml-spark-cassandra
2. **Démarrer l'Environnement Docker**
-  docker-compose up -d
3. **Accéder à Jupyter Notebook**
-  Ouvrez votre navigateur et accédez à http://localhost:8888.
-  Utilisez le token fourni dans les logs pour vous connecter.
4. **Exécuter les Notebooks** 
-  Ouvrez et exécutez les notebooks dans le dossier notebooks/.
5. **Accéder à cassandra**
-cqlsh 172.18.0.2 9042 -u cassandra -p cassandra

## **Auteurs**
AHANSAL SALAHEDDINE
EL KADAH RACHID
EL HMDI BRAHIM
