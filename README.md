# 🍽️ Gestionnaire de Recettes Django

![Django](https://img.shields.io/badge/Django-5.2.6-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11+-yellow.svg)

Un gestionnaire de recettes de cuisine moderne et élégant, développé avec Django. Cette application permet de créer, consulter, noter et commenter des recettes, avec un système de recherche avancé par ingrédients.

## ✨ Fonctionnalités

### 🎯 Fonctionnalités principales
- **📖 Gestion complète des recettes** - Création, modification, publication
- **🥕 Catalogue d'ingrédients** - Gestion des ingrédients avec quantités et unités
- **⭐ Système de notation** - Notation de 1 à 5 étoiles
- **💬 Commentaires** - Système de commentaires modéré
- **🔍 Recherche avancée** - Recherche par ingrédients, catégories, temps
- **❤️ Favoris** - Sauvegarde des recettes préférées

### 🎨 Interface utilisateur
- **Design moderne** avec Bootstrap 5
- **Interface responsive** mobile-first
- **Dark/Light mode** 
- **Animations fluides** et expérience utilisateur optimisée
- **Grille visuelle** type Pinterest pour les recettes

## 🏗️ Architecture du projet

```
gestionnaire_recettes/
├── config/                 # Configuration du projet
├── recipes/               # Application recettes
├── ingredients/           # Application ingrédients  
├── profiles/              # Profils utilisateurs et favoris
├── comments/              # Système de commentaires
└── templates/             # Templates globaux
```

## 🚀 Installation

```bash
# Cloner le repository
git clone https://github.com/IvanBayiha18/Gestionnaire_de_recette.git
cd gestionnaire-recettes

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur de développement
python manage.py runserver
```

## 📋 Prérequis

- Python 3.11+
- Django 5.2.6
- Bootstrap 5.3
- SQLite (développement) / PostgreSQL (production)

## 🎯 Objectifs du projet

### 🎓 Pédagogiques
- **Maîtrise avancée de Django** - Modèles, vues, templates
- **Architecture modulaire** - Découpe en applications cohérentes
- **Tests unitaires** - Développement piloté par les tests
- **UX/UI moderne** - Intégration Bootstrap et design responsive

### 💼 Professionnels  
- **Portfolio qualité** - Code propre et documentation complète
- **Bonnes pratiques** - PEP8, architecture MVC, sécurité
- **Gestion de projet** - Versionning Git avec commits atomiques

## 👩‍💻 Développement

### Structure des applications
```python
# Chaque application suit la structure Django classique
app/
├── models.py          # Modèles de données
├── views.py           # Logique métier
├── urls.py            # Routes
├── templates/         # Templates HTML
├── static/           # CSS, JS, images
└── tests.py          # Tests unitaires
```

### Méthodologie de développement
- **Développement feature par feature**
- **Tests écrits avant l'implémentation** (TDD)
- **Revue de code et corrections**
- **Documentation au fil de l'eau**

## 📸 Aperçu

*(Des captures d'écran seront ajoutées au fur et à mesure du développement)*

## 🤝 Contribution

Ce projet est développé dans un cadre d'apprentissage. Les suggestions d'amélioration sont les bienvenues !

## 📝 Licence

Ce projet est open source et disponible sous licence MIT.

## 👤 Auteur

Développé avec passion dans le cadre de l'apprentissage de Django.

---

**💡 Note** : Ce README évoluera au fur et à mesure du développement du projet avec des captures d'écran, des gifs de démonstration et des instructions détaillées.

---
