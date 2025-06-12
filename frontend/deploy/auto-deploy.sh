#!/bin/bash
set -e

echo "=== Lancement du déploiement automatique du frontend ==="

# Se placer dans le dossier frontend
cd ../frontend

echo "Installation des dépendances NPM..."
npm install

echo "Construction du projet pour la production (build)..."
npm run build

echo "Build terminé !"

# Create target deploy folder if it doesn't exist
DEPLOY_DIR="../deploy/frontend_build"
mkdir -p "$DEPLOY_DIR"

echo "Copie des fichiers build dans le dossier de déploiement ($DEPLOY_DIR)..."
# La commande ci-dessous copie la sortie de build (ici supposée dans le dossier 'dist')
cp -r dist/* "$DEPLOY_DIR/"

echo "=== Déploiement du frontend terminé avec succès ==="
