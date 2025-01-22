# **Système de Prédiction et d'Analyse pour un Concessionnaire Automobile**

Ce projet vise à aider un concessionnaire automobile à analyser et prédire les préférences des clients en utilisant des techniques de **Machine Learning (ML)** et de **Big Data**. Les données sont stockées dans **Cassandra** et traitées avec **Apache Spark** pour une analyse distribuée. Le projet inclut l'exploration des données (EDA), le clustering avec K-Means, et la classification avec Random Forest.

---

## **Objectifs du Projet**
1. **Exploration des Données (EDA)** : Nettoyer et analyser les données pour comprendre les tendances et les corrélations.
2. **Clustering** : Appliquer l'algorithme K-Means pour segmenter les véhicules.
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
- **Streamlit** : Pour l'interface utilisateur interactive.

---

## **Architecture du Projet**
Voici une représentation visuelle de l'architecture du projet :

![Arch big D](https://github.com/user-attachments/assets/f4db001f-e6d2-4baa-8f8d-f4d4230a2a2c)

### **Description de l'Architecture**
1. **Données Brutes** :
   - Les données brutes sont stockées dans des fichiers CSV (`data/raw/`).
   - Elles incluent les informations sur les clients, les véhicules, et les immatriculations.

2. **Traitement des Données** :
   - Les données sont nettoyées et transformées à l'aide de **Apache Spark**.
   - Les scripts et notebooks dans `notebooks/` effectuent l'exploration, le clustering, et la classification.

3. **Stockage des Données** :
   - Les données nettoyées et transformées sont stockées dans **Cassandra** pour une gestion efficace et scalable.

4. **Modèles de Machine Learning** :
   - Un modèle **Random Forest** est entraîné pour prédire les catégories de véhicules.
   - Le modèle est sauvegardé dans `models/random_forest_model/`.

5. **Interface Utilisateur** :
   - Une application **Streamlit** est utilisée pour interagir avec le modèle et afficher les prédictions.

6. **Docker** :
   - L'environnement est conteneurisé avec **Docker** pour une installation et une exécution simplifiées.

---

## **Structure du Projet**
Voici une représentation visuelle de la structure du projet :

![image](https://github.com/user-attachments/assets/65601a2e-0896-4379-b154-e976492171d4)
---

## **Installation**
1. **Cloner le Repository** :
   ```bash
   git clone https://github.com/devAhansal/dealer-auto-ml-spark-cassandra.git
   cd dealer-auto-ml-spark-cassandra
2. **Démarrer l'Environnement Docker** : 
   ```bash
   docker-compose up -d
3. **Accéder à Jupyter Notebook** :
   - Ouvrez votre navigateur et accédez à http://localhost:8888.
   - Utilisez le token fourni dans les logs pour vous connecter.   
4. **Accéder à Cassandra** :
   ```bash
   cqlsh 172.18.0.2 9042 -u cassandra -p cassandra
5. **Exécuter les Notebooks** :
   - Ouvrez et exécutez les notebooks dans le dossier notebooks/.
   - Lancer l'Application Streamlit :
   - Accédez à http://localhost:8501 pour utiliser l'interface de prédiction.

## **Utilisation**
1. **Exploration des Données** :
   - Exécutez les notebooks `01-eda-*.ipynb` pour explorer et nettoyer les données.

2. **Clustering** :
   - Exécutez `03-clustering.ipynb` pour segmenter les véhicules en clusters.

3. **Classification** :
   - Exécutez `04-classification.ipynb` pour entraîner un modèle Random Forest et prédire les catégories de véhicules.

4. **Application Streamlit** :
   - Utilisez l'application Streamlit (`src/main.py`) pour interagir avec le modèle et obtenir des prédictions en temps réel.

---

## **Auteurs**
- **AHANSAL SALAHEDDINE**
- **EL KADAH RACHID**
- **EL HMDI BRAHIM**
