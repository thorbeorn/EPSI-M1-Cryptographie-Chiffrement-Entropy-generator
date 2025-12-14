# 🎲 Générateur d’Entropie Basé sur une Caméra Urbaine et la Météo

## 📌 Description du projet

Ce projet implémente un **générateur d’entropie original** basé sur des **événements réels et imprévisibles** du monde physique.

L’idée principale est d’exploiter :

* une **caméra publique en direct** (Place de la Comédie à Montpellier),
* le **nombre de personnes présentes à un instant T**,
* des **données météorologiques dynamiques** issues de l’API Open-Meteo,

afin de produire une **clé cryptographique de 256 bits** reposant sur de l’entropie réelle.

Ce générateur répond à la consigne suivante :

> **Créer un générateur d’entropie avec l’idée la plus originale possible.**

---

## 💡 Principe de fonctionnement

L’entropie est générée à partir d’une chaîne d’événements indépendants, difficiles à prédire et non déterministes :

1. 📹 **Caméra en direct (ViewSurf – Place de la Comédie, Montpellier)**

   * Sélection aléatoire d’une vidéo du jour
   * Extraction d’une image à un instant T
   * Détection automatique des personnes présentes

2. 👥 **Nombre de personnes détectées**

   * Ce nombre varie constamment et dépend de facteurs humains impossibles à prévoir
   * Il constitue la **première source d’entropie**

3. 🌍 **Génération de coordonnées géographiques**

   * Le nombre de personnes est utilisé comme **seed**
   * Il permet de dériver une latitude et une longitude

4. 🌦 **Données météo réelles (Open-Meteo API)**

   * Température
   * Humidité
   * Pression
   * Vent
   * Précipitations
   * Couverture nuageuse, etc.

5. 🔢 **Traitement numérique des données météo**

   * Suppression des valeurs nulles ou non numériques
   * Transformation mathématique pour produire un nombre aléatoire exploitable

6. 🔐 **Génération d’une clé cryptographique 256 bits**

   * Combinaison du nombre de personnes et des données météo
   * Création d’une clé forte en **bytes** et en **hexadécimal**

---

## 🧠 Pourquoi cette source est entropique ?

| Source                     | Justification                          |
| -------------------------- | -------------------------------------- |
| 👥 Mouvement humain        | Impossible à prédire précisément       |
| 📷 Instant T aléatoire     | Dépend du moment d’exécution           |
| 🌦 Météo réelle            | Variable, chaotique et non contrôlable |
| 🌍 Géolocalisation dérivée | Dépend directement du monde réel       |
| 🔗 Chaînage des étapes     | Amplifie l’imprévisibilité             |

➡️ L’ensemble forme une **entropie hybride humaine + environnementale**.

---

## 🗂 Structure du projet

```bash
.
├── utils/
│   ├── viewSurf.py
│   ├── video.py
│   ├── image.py
│   ├── open_meteo.py
│   ├── json.py
│   ├── key.py
│   └── file_and_folder.py
├── temp/
│   ├── Comedie_video.mp4
│   └── Comedie_pic.jpg
├── output/
│   ├── Comedie_people_Detecter.jpg
│   ├── Meteo_data.json
│   └── generated_key.txt
├── main.py
└── README.md
```

---

## 🚀 Utilisation

### 1️⃣ Installer de l'environnement

### Créer un environnement virtuel
```bash
python3 -m venv .venv
```

### Activer l'environnement virtuel
### Sur macOS/Linux :
```bash
source .venv/bin/activate
```
### Sur Windows :
```bash
.venv\Scripts\activate
```

# Installer les packages nécessaires
```bash
pip install -r requirements.txt
```

### 2️⃣ Lancer le générateur

```bash
python3 main.py
```

### 3️⃣ Résultat

* 📸 Image avec détection des personnes
* 📄 Données météo sauvegardées en JSON
* 🔐 Clé 256 bits générée et enregistrée

Exemple de sortie :

```
CLÉ 256 BITS GÉNÉRÉE
Format hexadécimal: e4a1c9...
Format bytes: b'\xe4\xa1\xc9...'
Longueur: 32 bytes (256 bits)
```

---

## 🔒 Sécurité et limites

⚠️ Ce projet est **pédagogique** et expérimental :

* Il démontre la **créativité dans la génération d’entropie**

---

## 📚 Technologies utilisées

* **Python**
* **OpenCV / IA (détection de personnes)**
* **API Open-Meteo**
* **ViewSurf (caméra publique)**
* **JSON**
* **Cryptographie (clé 256 bits)**

---

## ✨ Conclusion

Ce projet montre qu’il est possible de générer de l’entropie à partir :

* du comportement humain,
* de phénomènes naturels,
* et de données temps réel,

en sortant complètement des sources classiques (horloge, pseudo-aléatoire, seeds statiques).

🎯 **Un générateur d’entropie original, vivant et ancré dans le monde réel.**