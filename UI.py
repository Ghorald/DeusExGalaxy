import maya.cmds as cmds

class UI:
    def __init__(self):
        """
        Fonction d'initialisation de la classe UI.
        Crée la fenêtre
        """
        if cmds.window('window1', ex=True):
            # On vérifie si une fenêtre n'est pas déjà ouverte. Si oui, on la ferme
            cmds.deleteUI('window1', window=True)

        self.fenetre = cmds.window(title="Deux Ex Galaxy", resizeToFitChildren=True)

        cmds.frameLayout(label="Boutons")
        cmds.button(label="Générer la galaxie", command=self.generation, align="center")
        # On crée un bouton qui appelle la fonction "self.generation"

        cmds.showWindow()

    def generation(self, *args):
        """
        Fonction qui s'occupe de la génération du côté de l'interface graphique.
        On va pouvoir afficher des informations dans la fenêtre ou la console, et appeler une/des fonction.s qui lanceront les modélisations procédurales.
        """
        cmds.file(f=True, new=True) # On commentera cette ligne si on veut pouvoir avoir plusieurs galaxies dans la même scène.

        print("On appellera ici une fonction pour lancer la modélisation")
