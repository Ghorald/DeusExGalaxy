# DeusExGalaxy
## Organisation du projet



# Utiliser Git Bash
## Installer git-scm et mettre en place le projet

* Télécharger le .exe à [cette adresse](https://git-scm.com/downloads).
* Se rendre à l'endroit désiré dans l'explorateur de fichier, et ouvrir Git Bash (avec un clic droit). Une fenêtre de terminal devrait s'ouvrir.
* Entrer les commandes `git config --global user.name "Votre pseudo"` et `git config --global user.mail "Votre mail"` (Vous pouvez ne pas rentrer votre mail, mais c'est une bonne pratique pour signer les commits en général).
* Entrer la commande `git clone https://github.com/Ghorald/DeusExGalaxy.git`, et entrez vos identifiants GitHub.

Vous devrez maintenant avoir le projet et ses fichiers (ainsi qu'un dossier `.git`) à l'endroit où vous l'avez cloné.

## Workflow commits

Avant de commencer à travailler, vous devez pull le projet pour récupérer le travail effectué depuis votre dernière modification avec cette commande `git pull`, puis entrer vos identifiants.

Une fois que vous travaillé sur le projet (créer/modifier un projet), vous devrez l'envoyer sur GitHub.
Il faut d'abord noter les fichiers que vous désirez ajouter à cette nouvelle version avec la commande `git add .`. Vous pouvez aussi `git add chemin/vers/le/fichier`, le "." permet juste de sélectionner tout le projet, et donc d'ajouter à la nouvelle toutes vos modifications.
Une fois ces fichiers marqués, il faut créer la nouvelle version avec la commande `git commit -m "message descriptif accompagnant le commit"`, puis envoyer cette version sur GitHub avec `git push`.

## Branches et méthodes de travail

Généralement, on crée une branche pour une nouvelle fonctionnalité.
La commande pour créer une branche est `git branch nom_de_la_branche`. Git Bash affiche normalement la branche actuelle du projet entre parenthèses après le chemin.
Pour changer de branche, on utilise `git checkout branche_de_destination`.
Petite précision, utiliser la touche Tab permet d'auto-compléter les noms de branches, ou par défaut d'afficher la liste de toutes les branches (très utile).

Quand le travail sur une branche est terminé, on peut la merge dans la branche master, c'est-à-dire mélanger les fichiers des deux branches selon leurs modifications. Cette partie de git se fait sur GitHub. On crée une Pull Request en sélectionnant les deux branches qu'on veut merger, et on merge enfin la pull request.

Si on n'a plus besoin de la branche d'origine, on peut la supprimer (ATTENTION, NE JAMAIS SUPPRIMER LA BRANCHE MAIN). 
Pour cela, on utilisera deux commandes :
`git branch -d nom_de_la_branche` supprimera la branche locale, et il suffit d'envoyer cette suppression sur GitHub pour effacer totalement cette branche `git push origin --delete nom_de_la_branche`.
Pour notre projet, on devrait pas avoir besoin de supprimer des branches, donc on évitera de le faire pour pas perdre du travail sans faire gaffe.

## Commandes pratiques

Une commande extrêmement pratique de git est `git status`. Cette commande affiche le statut actuel de la branche sur laquelle on est, ainsi que des indications sur quoi faire. Par exemple, cette commande renvoie les fichiers modifiés en rouge s'ils n'ont pas été ajouté avec `git add`, et en vert si cette étape a été faite. La commande vous indique aussi combien de commits vous n'avez pas encore envoyés sur GitHub avec `git push`.

Autre commande sympa, c'est `git log`. La commande affiche les derniers commits de la branche avec toutes leurs informations (message, auteur, date, et). Si vous voulez moins d'information, vous pouvez marquer `git log --oneline`, et l'affichage sera plus compact.


Si jamais vous avez une erreur ou un problème (conflit, merge, etc), demandez-moi, ça peut être assez chiant.
