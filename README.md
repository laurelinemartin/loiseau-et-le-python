# loiseau-et-le-python

Programmer en Python et à l’aide du module Pygame le jeu “Flappy Bird” de A à Z.

## Age : +13 ans

## Temps : 2j

## Prérequis : Base en programmation sont un plus, mais pas obligatoire.

# Notions :

- Fonctions
- Conditions
- Boucles
- Classes
- Affichage graphique (SDL)
- Python / Pygame

# Fonctionnalités :

- Affichage graphique (avec Pygame / SDL)
- Générer un tuyau de longueur aléatoire
- Gestion de l’oiseau (flèche haut ou barre espace pour monter)
- Perdre quand collision ou sol atteint

# Déroulement :

Un enfant par poste.

- Jour 1 :
    - Définir les fonctionnalités du jeu
        
        Comment va fonctionner le Jeu ? Y a t’il un ou plusieurs joueurs ? Avec quels objets il interagit ? Comment on gagne / on perd ?
        
        - Représentation joueur = une classe
        - Représentation tuyau = une classe
        - Fin du jeu = une fonction
        - Les variables globales
        - Un main pour faire tourner le jeu
    - Introduction à Python/Pygame
        
        Utilisation de SDL simplifié. Manipulation de pixel dans une fenêtre graphique.
        
    - Coder
        1. La fenêtre graphique
        2. L’oiseau
        3. Mouvement vers le haut de l’oiseau
        4. Mouvement vers le bas de l’oiseau

- Jour 2 :
    - Coder
        1. Tuyaux
        2. Mouvement d’un tuyau / le faire revenir au début quand il disparaît à la fin
        3. Gestion de la collision
        4. Gestion du toucher du sol et du plafond
        5. Calcul du score

# Évaluation :

Le jeu fonctionne :

- Possibilité de faire un saut vers le haut en appuyant sur une touche
- Chute de l’oiseau
- Arrêt du jeu (ou image de Fin de jeu) quand on touche le sol, le plafond ou un poteau
- Affichage du scor

# Retours :

Top. Simple à préparer. Je suis pas trop rentrée dans la notion de classe mais ça va ils ont bien compris l’idée (c’est un objet, je peux en créer plusieurs, bon le constructeur est passé à la trappe).

3 enfants  qui avaient des idées. Après le fait de connaître le jeu duquel on s’inspire aide paqs mal.

# Ressources :
Idée de code pour le Flappy que je n’ai pas suivi (mais qui a bien sauvé pour les FPS) : https://www.geeksforgeeks.org/how-to-make-flappy-bird-game-in-pygame/

Objets en Python : https://openclassrooms.com/fr/courses/6900856-learn-programming-with-python/6993151-create-python-objects

Doc du pygame.time : https://www.pygame.org/docs/ref/time.html
