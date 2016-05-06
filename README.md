# NEURON

Ce dossier contient plusieurs modèles basés sur le papier Distinct.

On modifie les fichiers hoc pour inclure la température dans le modèle.

Voir le README de chaque modèle.

ca3b : fichier de base, non modifié.

celsius : la température est modifiée de façon uniforme et constante avec un bouton.

t : la temperature est modifiée sur le soma de façon constante, en fonction de la position.

t_x : la température est modifiée sur le soma en fonction de la positon et du temps. Dans les figures, on n’utilise plus la procédure run() mais la procédure integrate() qui permet de modifier les choses en fonction du temps. Vérifier l’exploitation avec init&run.
9x : pas de stimulation

fichier : elle dépend d’un fichier texte
