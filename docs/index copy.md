# Projet de Stage – OAI Private Network

Bienvenue dans la documentation du projet **OAI-Private-Network-main**, réalisé dans le cadre de mon stage de 2e année de BUT Réseaux & Télécommunications.

## Objectif du stage

Mettre en place un réseau 5G privé en utilisant la suite **OpenAirInterface (OAI)** :
- Déployer un **Core 5G (CN5G)**,
- Configurer un **gNodeB**,
- Connecter un **UE (User Equipment)** virtuel ou physique,
- Réaliser des **tests de connectivité et de performance**,
- Documenter toute la procédure pour une future reprise ou amélioration.

## Encadrants

- **Tuteur de stage** : M. Labiod  
- **Référent technique** : M. Clément  
- **Établissement** : IUT Créteil-Vitry, Université Paris-Est Créteil (UPEC)

## Environnement technique

- Distribution Linux : **Ubuntu 22.04**
- Processeur : **x86_64**
- SDR virtuel avec `--rfsim` (mode simulation radio)
- Matériel utilisé : **module Quectel RM500Q**
- Technologies utilisées :
  - Docker, Docker-compose
  - QMI (Qualcomm Modem Interface)
  - `quectel-CM` pour l’interface modem
  - `qmicli` pour les commandes de bas niveau

## Structure de la documentation

Cette documentation est divisée en plusieurs parties pour suivre l’évolution du projet :

1. **Installation** – Étapes d’installation des dépendances et outils
2. **Configuration** – Détails des fichiers et paramètres configurés
3. **Module Quectel** – Connexion avec carte SIM et diagnostic modem
4. **Commandes QMI** – Répertoire des commandes utiles et leur explication
5. **Tests** – Résultats des tests effectués
6. **Problèmes & Solutions** – Liste des blocages et résolutions
7. **Ressources** – Liens utiles et documentation externe
8. **Bilan** – Retours sur le projet, apprentissages et recommandations

## Suivi du projet

Les fichiers `.md` présents ici sont lisibles en WebUI grâce à l’intégration Markdown.  
Chaque section peut être consultée pour mieux comprendre les étapes du projet ou le reproduire dans un autre environnement.

---
