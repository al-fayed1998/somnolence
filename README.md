Somnolence Detection Project

Description

Ce projet vise à développer un système de détection de somnolence en temps réel, principalement pour des applications dans la sécurité routière. Le modèle utilise des techniques de traitement d’image pour analyser les expressions faciales et les mouvements oculaires afin de détecter les signes de somnolence. En cas de détection, un signal d’alarme sonore est déclenché pour avertir l’utilisateur.

Contenu du Projet

	•	alarm.mp3 : Fichier audio utilisé comme alarme sonore en cas de détection de somnolence.
	•	beta.mp4 et ecole.mp4 : Vidéos utilisées pour tester la détection en temps réel.
	•	drowsiness_detection.py : Script principal de détection de somnolence.
	•	haarcascade_frontalface_default.xml : Classifieur Haar utilisé pour la détection des visages.
	•	shape_predictor_68_face_landmarks.dat et shape_predictor_70_face_landmarks.dat : Modèles pour prédire les points de repère du visage (yeux, nez, bouche).
	•	vidéo_somnolence.mp4 et video_alfa.mp4 : Vidéos démonstratives du projet en action.

Installation

Prérequis

Avant de pouvoir exécuter ce projet, vous devez vous assurer que les éléments suivants sont installés :

	•	Python 3.x
	•	pip (gestionnaire de paquets Python)

Bibliothèques Python

Installez les dépendances nécessaires à l’aide de la commande suivante :

pip install -r requirements.txt

Si le fichier requirements.txt n’est pas fourni, vous pouvez installer les bibliothèques manuellement :

pip install opencv-python
pip install dlib
pip install imutils
pip install numpy
pip install playsound

Utilisation

	1.	Assurez-vous d’avoir une webcam connectée.
	2.	Exécutez le script de détection de somnolence : python drowsiness_detection.py

	3.	Le programme analysera les mouvements oculaires en temps réel et déclenchera une alarme sonore en cas de détection de somnolence.

Fonctionnalités

	•	Détection en temps réel : Le programme analyse le flux vidéo pour détecter les signes de somnolence.
	•	Signal d’alarme : En cas de somnolence détectée, une alarme sonore (fichier alarm.mp3) est activée.
	•	Prédiction des points de repère du visage : Utilisation de modèles pré-entraînés pour identifier les points de repère du visage, notamment les yeux pour détecter les clignements prolongés.

Méthodes Utilisées

	•	OpenCV : Utilisé pour la capture et le traitement des images.
	•	Dlib : Utilisé pour la détection des points de repère du visage, en particulier les yeux.
	•	Playsound : Utilisé pour jouer l’alarme sonore.

Améliorations Futures

	•	Optimisation de l’algorithme pour réduire les faux positifs.
	•	Intégration de capteurs supplémentaires pour améliorer la précision de la détection.
	•	Déploiement du projet sous forme d’application mobile ou d’outil embarqué pour les véhicules.

Résultats

Le projet a été testé avec plusieurs vidéos de démonstration (beta.mp4, vidéo_somnolence.mp4) et a montré des résultats prometteurs pour la détection de somnolence basée sur les expressions faciales.

Auteurs

	•	Mouhammad Thahir Ousmane
	•	Toute contribution future est la bienvenue via des pull requests ou des issues sur le dépôt GitHub.

