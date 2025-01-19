-- Création du keyspace
CREATE KEYSPACE concessionnaire 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1} 
AND durable_writes = true;

-- Table catalogue
CREATE TABLE concessionnaire.catalogue (
    nom text PRIMARY KEY,
    couleur text,
    longueur text,
    marque text,
    nbplaces int,
    nbportes int,
    occasion boolean,
    prix decimal,
    puissance int
);

-- Table catalogue_clusters
CREATE TABLE concessionnaire.catalogue_clusters (
    marque text,
    nom text,
    couleur text,
    longueur text,
    nbplaces int,
    nbportes int,
    prediction int,
    prix decimal,
    puissance int,
    PRIMARY KEY (marque, nom, couleur)
) WITH CLUSTERING ORDER BY (nom ASC, couleur ASC);

-- Table clients
CREATE TABLE concessionnaire.clients (
    immatriculation text PRIMARY KEY,
    "2eme voiture" boolean,
    age int,
    nbenfantsacharge int,
    sexe text,
    situationfamiliale text,
    taux int
);

-- Table immatriculation
CREATE TABLE concessionnaire.immatriculation (
    immatriculation text PRIMARY KEY,
    couleur text,
    longueur text,
    marque text,
    nbplaces int,
    nbportes int,
    nom text,
    occasion boolean,
    prix decimal,
    puissance int
);

-- Table immatriculations_clusters
CREATE TABLE concessionnaire.immatriculations_clusters (
    immatriculation text PRIMARY KEY,
    couleur text,
    longueur text,
    marque text,
    nbplaces int,
    nbportes int,
    nom text,
    occasion boolean,
    prediction int,
    prix decimal,
    puissance int
);

-- Index sur la colonne 'occasion' dans la table immatriculations_clusters
CREATE INDEX immatriculations_clusters_occasion_idx 
ON concessionnaire.immatriculations_clusters (occasion);