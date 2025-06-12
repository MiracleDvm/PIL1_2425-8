# IFRI Comotorage 🚗💨

**IFRI Comotorage** est une plateforme web innovante qui facilite le covoiturage entre étudiants de l'IFRI en mettant en relation les conducteurs et les passagers. Grâce à une interface intuitive et une gestion automatisée des trajets, cette application optimise le partage des déplacements vers le campus.

---

## 🌟 Fonctionnalités principales

✔ **Inscription et connexion sécurisées**  
✔ **Choix du statut (Conducteur/Passager)**  
✔ **Gestion des réservations de trajet**  
✔ **Messagerie instantanée pour la coordination**  
✔ **Paiement sécurisé des trajets**  
✔ **Historique des paiements et transactions**  
✔ **Zones favorites et préférences de trajet**  
✔ **Notifications en temps réel**  
✔ **Suivi avancé des erreurs et des performances**  

---

## 🛠 Technologies utilisées

### **Backend**
- **Django** - Framework backend robuste
- **Django REST Framework** - API REST puissante
- **PostgreSQL** - Base de données relationnelle
- **Gunicorn** - Serveur d’application performant
- **Redis** - Gestion du cache et des files d’attente
- **Nginx** - Serveur proxy pour le déploiement
- **Firebase** - Authentification et notifications push
- **Docker** - Conteneurisation pour un déploiement efficace

### **Frontend**
- **Vue.js** - Framework JavaScript réactif
- **Vuex** - Gestion centralisée des états
- **Axios** - Communication API
- **Bootstrap** / **Tailwind CSS** - UI moderne et responsive

---

## 🚀 Installation et mise en route

### **Pré-requis**
📌 **Node.js** installé  
📌 **Python 3+** installé  
📌 **Docker** pour le déploiement  

### **Installation Backend**

**1️⃣ Clonez le dépôt :**
*bash*
git clone https://github.com/votre-repo/ifri-comotorage.git
cd ifri-comotorage/backend

**2️⃣ Créez un environnement virtuel et installez les dépendances :**
*bash*
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Configurez les variables d’environnement .env et appliquez les migrations :
*bash*
python manage.py migrate

4️⃣ Lancez le serveur :
*bash*
python manage.py runserver

## **Installation Frontend**
**1️⃣ Accédez au dossier frontend :**
*bash*
cd ../frontend
**2️⃣ Installez les dépendances :**
*bash*
npm install
**3️⃣ Lancez le serveur de développement :**
*bash*
npm run dev
## **🏗 Déploiement avec Docker**
Lancez l’application complète avec Docker et **docker-compose** :
*bash*
docker-compose up --build

## **🛡 Sécurité & Optimisation**
**🔒 Protection des accès** avec JWT et Firebase Auth **📊 Suivi des erreurs** via un middleware dédié **📂 Gestion avancée des fichiers et logs 🚀 Optimisation des performances** avec Redis

## **🤝 Contribuer**
Nous accueillons toutes les suggestions et contributions ! **✅ Forkez** le projet **✅ Créez une branche** pour vos modifications **✅ Ouvrez une pull request**

Merci pour votre intérêt et votre soutien à **IFRI Comotorage ! 🚗💨**