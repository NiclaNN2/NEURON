# NEURON

Ce dossier contient plusieurs modèles basés sur le papier Distinct.

On modifie les fichiers hoc pour inclure la température dans le modèle.

Voir le README de chaque modèle.

dca3b_T : fichier de base, non modifié.

ca3b_celsius : la température est modifiée de façon uniforme et constante avec un bouton.

ca3b_T : la temperature est modifiée sur le soma de façon constante, en fonction de la position.

ca3b_celsius_t : la température est modifiée sur le soma en fonction de la positon et du temps. Dans les figures, on n’utilise plus la procédure run() mais la procédure integrate() qui permet de modifier les choses en fonction du temps. Vérifier l’exploitation avec init&run.
