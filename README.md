# NEURON

Ce dossier contient plusieurs modèles basés sur le papier Distinct.

On modifie les fichiers hoc pour inclure la température dans le modèle.

ca3b : fichier de base, non modifié.

celsius : la température est modifiée de façon uniforme et constante avec un bouton.

t : la temperature est modifiée sur le soma de façon constante, en fonction de la position.

t_x : la température est modifiée sur le soma en fonction de la positon et du temps. Dans les figures, on n’utilise plus la procédure run() mais la procédure integrate() qui permet de modifier les choses en fonction du temps. Vérifier l’exploitation avec init&run.
9x : pas de stimulation

fichier : elle dépend d’un fichier texte
On utilise la procédure « lancer() » pour lancer les calculs.
Pour les figures disponibles, on se base sur les figures proposées dans Distinct.
On va proposer 3 panneaux de figures.

« no_stim »
on choisit alors le chauffage
les paramètres de conductance son ceux de la figure 9b mais on peut tout modifier.

« 9b-heat »
paramètres de la figure 9b (conductance+stim)
et on choisit le chauffgae

« 9e-heat »
paramètres de la figure 9e (conductance+stim)
et on choisit le chauffage
