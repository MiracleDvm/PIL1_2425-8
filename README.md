# ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffffff) ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=ffffff) ![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=ffffff) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=ffffff)

# Projet intégrateur de l'année 2024-2025 - Groupe 8: IFRI Comotorage

Ce projet est une application de gestion de services de transport, permettant aux utilisateurs de réserver des trajets, de gérer des paiements, et d'interagir avec un système de notifications. Il est conçu pour être utilisé à la fois par les utilisateurs finaux et les administrateurs.

## Fonctionnalités clés
- **Gestion des utilisateurs** : Inscription, connexion et gestion des profils.
- **Réservations de trajets** : Les utilisateurs peuvent réserver des trajets selon leur disponibilité.
- **Système de paiement** : Intégration d'un module de paiement pour faciliter les transactions.
- **Notifications** : Système de notifications pour informer les utilisateurs des mises à jour et des changements.
- **Surveillance du système** : Outils pour surveiller les performances et l'état du système.

## Tech Stack

| Technologie      | Description                                      |
|------------------|--------------------------------------------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=ffffff) | Langage de programmation utilisé pour le backend. |
| ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=ffffff) | Framework web pour le développement du backend. |
| ![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vue.js&logoColor=ffffff) | Framework JavaScript pour le développement du frontend. |
| ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=ffffff) | Outil de conteneurisation pour le déploiement. |

## Instructions d'installation

### Prérequis
- Python 3.12 ou supérieur
- Node.js et npm
- Docker (facultatif, pour le déploiement)

### Étapes d'installation
1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/MiracleDvm/PIL1_2425-8.git
   cd PIL1_2425-8
   ```

2. **Installer les dépendances backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Installer les dépendances frontend**
   ```bash
   cd frontend
   npm install
   ```

4. **Configurer l'environnement**
   - Créez un fichier `.env` à la racine du dossier `backend` et ajoutez les variables d'environnement nécessaires (voir `settings.py` pour les détails).

5. **Exécuter les migrations de la base de données**
   ```bash
   python manage.py migrate
   ```

6. **Lancer le serveur backend**
   ```bash
   python manage.py runserver
   ```

7. **Lancer le serveur frontend**
   ```bash
   cd frontend
   npm run serve
   ```

## Utilisation

Après avoir démarré les serveurs, vous pouvez accéder à l'application via votre navigateur à l'adresse `http://localhost:8000` pour le backend et `http://localhost:8080` pour le frontend.

### Exemples d'utilisation
- Pour vous inscrire, accédez à la page de connexion et suivez les instructions.
- Pour réserver un trajet, naviguez vers la section des réservations et suivez les étapes.

## Structure du projet

Voici un aperçu de la structure du projet et des principales fonctionnalités de chaque répertoire :

```
PIL1_2425-8/
├── backend/                  # Code backend de l'application
│   ├── authentication/       # Gestion des utilisateurs (inscription, connexion)
│   ├── errors/               # Gestion des erreurs et middleware
│   ├── logs/                 # Fichiers journaux de l'application
│   ├── monitoring/           # Outils de surveillance du système
│   ├── notifications/         # Gestion des notifications
│   ├── payments/             # Gestion des paiements
│   ├── reservations/         # Gestion des réservations de trajets
│   ├── trips/                # Gestion des trajets
│   ├── users/                # Gestion des profils utilisateurs
│   ├── manage.py             # Script de gestion de l'application
│   ├── settings.py           # Configuration des paramètres de l'application
│   └── urls.py               # Routes de l'application
├── frontend/                 # Code frontend de l'application
│   ├── src/                  # Code source de l'application Vue.js
│   ├── deploy/               # Scripts et configurations pour le déploiement
│   └── database/             # Base de données SQLite
└── requirements.txt          # Dépendances Python
```

## Contribuer

Les contributions sont les bienvenues ! Pour contribuer, veuillez suivre ces étapes :
1. Forkez le projet.
2. Créez une nouvelle branche (`git checkout -b feature/MonNouveauFeature`).
3. Apportez vos modifications et committez-les (`git commit -m 'Ajout d'une nouvelle fonctionnalité'`).
4. Poussez vers la branche (`git push origin feature/MonNouveauFeature`).
5. Ouvrez une Pull Request.

Merci de votre intérêt pour le projet !
