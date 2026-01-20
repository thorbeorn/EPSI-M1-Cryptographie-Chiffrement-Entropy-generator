# 🎲 Générateur d’Entropie Hybride Basé sur le Monde Réel

## 📌 Présentation du projet

Ce projet implémente un **générateur d’entropie original et expérimental**, fondé sur des **phénomènes réels, humains et environnementaux**, puis exploité dans des **visualisations statistiques** et une **roulette pseudo-aléatoire**.

L’objectif est de démontrer qu’il est possible de produire une **clé cryptographique 256 bits** à partir :

* du **comportement humain** (caméra urbaine),
* de **données météorologiques réelles**,
* et de les réutiliser comme **seed fort** pour des systèmes aléatoires.

> 🎯 **Consigne respectée : créer un générateur d’entropie avec une idée originale, ancrée dans le monde réel.**

---

## 🧠 Principe général

L’entropie est construite par **chaînage de sources indépendantes et imprévisibles** :

### 1️⃣ Caméra urbaine en direct (Place de la Comédie – Montpellier)

* Récupération d’une vidéo publique (ViewSurf)
* Extraction d’une image à un instant T
* Détection automatique des personnes (OpenCV / IA)

➡️ **Le nombre de personnes détectées constitue la première source d’entropie**

---

### 2️⃣ Dérivation géographique

* Le nombre de personnes est utilisé comme **seed**
* Génération de coordonnées GPS (latitude / longitude)

---

### 3️⃣ Données météo réelles (API Open-Meteo)

Récupération dynamique de données environnementales :

* Température
* Humidité
* Pression atmosphérique
* Vent
* Précipitations
* Couverture nuageuse
* etc.

➡️ Ces données sont :

* réelles,
* chaotiques,
* impossibles à prédire précisément.

---

### 4️⃣ Génération de la clé cryptographique

* Nettoyage et transformation numérique des données
* Combinaison :

  * nombre de personnes
  * météo
* Génération d’une **clé cryptographique de 256 bits**

Formats produits :

* `bytes`
* `hexadécimal`

---

## 🔐 Exploitation de la clé générée

La clé 256 bits n’est pas seulement générée :
elle est **réutilisée comme graine forte** pour deux démonstrations visuelles.

---

### 📊 Nuage de points pseudo-aléatoire

* La clé hexadécimale est convertie en seed
* Génération de **1000 nombres pseudo-aléatoires (0–36)**
* Visualisation sous forme de **nuage de points**

➡️ Objectif :

* observer la distribution
* illustrer la qualité du seed issu de l’entropie réelle

📁 Sortie :

```
output/nuage_points.png
```

---

### 🎰 Roulette de casino (interface graphique)

* Roulette européenne (0 à 36)
* La clé 256 bits sert de seed cryptographique
* Chaque lancer utilise :

  * la clé
  * un nonce temporel
* Animation réaliste (Tkinter)
* Historique des tirages

➡️ Démonstration concrète de l’utilisation d’une entropie réelle
dans un **système pseudo-aléatoire interactif**

---

## 📂 Nouvelle structure du projet

```bash
.
├── .venv/                  # Environnement virtuel
├── config.py               # Configuration globale
├── entropy.py              # Génération de l’entropie et de la clé
├── graphique.py            # Nuage de points
├── roulette.py             # Roulette graphique
├── main.py                 # Point d’entrée du projet
├── requirements.txt
├── README.md
│
├── utils/                  # Fonctions utilitaires
│   ├── viewSurf.py
│   ├── video.py
│   ├── image.py
│   ├── open_meteo.py
│   ├── key.py
│   └── file_and_folder.py
│
├── models/                 # Modèles IA (détection)
├── temp/                   # Fichiers temporaires
│   ├── Comedie_video.mp4
│   └── Comedie_pic.jpg
│
└── output/                 # Résultats
    ├── Comedie_people_Detecter.jpg
    ├── Meteo_data.json
    ├── generated_key.txt
    └── nuage_points.png
```

---

## 🚀 Installation et exécution

### 1️⃣ Création de l’environnement virtuel

```bash
python3 -m venv .venv
```

### Activation

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 2️⃣ Installation des dépendances

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Lancer le projet

```bash
python3 main.py
```

---

## 📤 Résultats générés

* 📸 Image avec détection des personnes
* 📄 Données météo sauvegardées en JSON
* 🔐 Clé cryptographique 256 bits
* 📊 Nuage de points
* 🎰 Roulette interactive

Exemple de sortie :

```
CLÉ 256 BITS GÉNÉRÉE
Format hexadécimal: e4a1c9...
Format bytes: b'\xe4\xa1\xc9...'
Longueur: 32 bytes (256 bits)
```

---

## 🔒 Sécurité et limites

⚠️ **Projet pédagogique et expérimental**

* Ne remplace pas un TRNG certifié
* Dépend de services externes (caméra, API météo)
* Objectif : **créativité, compréhension et expérimentation**

---

## 🧪 Concepts abordés

* Entropie réelle
* Hybridation humain / environnement
* Seed cryptographique
* Pseudo-aléatoire
* Visualisation statistique
* Interfaces graphiques
* Cryptographie appliquée

---

## ✨ Conclusion

Ce projet démontre qu’il est possible de :

* capter de l’entropie depuis le monde réel,
* l’amplifier par chaînage de sources,
* produire une clé cryptographique robuste,
* et l’exploiter concrètement dans des systèmes aléatoires.

🎯 **Un générateur d’entropie vivant, original et ancré dans la réalité.**