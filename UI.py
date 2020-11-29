# coding: utf-8

import maya.cmds as cmds
from DeusExGalaxy.Univers import Univers

class UI:
    def __init__(self):
        """
        Fonction d'initialisation de la classe UI.
        Crée la fenêtre
        """

        self.nbPlanete = []
        self.slider1 = 0
        self.nbSysteme = 0

        self.U = Univers()

        if cmds.window('window1', ex=True):
            # On vérifie si une fenêtre n'est pas déjà ouverte. Si oui, on la ferme
            cmds.deleteUI('window1', window=True)

        #self.fenetre = cmds.window(title="Deux Ex Galaxy", resizeToFitChildren=True)

        #cmds.frameLayout(label="Boutons")
        #cmds.button(label="Générer la galaxie", command=self.generation, align="center")
        # On crée un bouton qui appelle la fonction "self.generation"

        afficherFenetre()

        #print("Windows")
        #cmds.showWindow()

    def generation(self, *args):
        """
        Fonction qui s'occupe de la génération du côté de l'interface graphique.
        On va pouvoir afficher des informations dans la fenêtre ou la console, et appeler une/des fonction.s qui lanceront les modélisations procédurales.
        """
        cmds.file(f=True, new=True) # On enlèvera cette ligne si on veut pouvoir avoir plusieurs galaxies dans la même scène.

        print("On appellera ici une fonction pour lancer la modélisation")

    #Afficher la fenetre
    def afficherFenetre():
        cmds.window(title="Générateur d'Univers © pouetpouet")
        cmds.columnLayout(adjustableColumn=True)

        nbSysteme = cmds.intSliderGrp(field=True, label='Nombre de Systèmes planétaires', minValue=1, maxValue=10, value=5)
        cmds.button(label = "OK", c='rechargerFenetre()')

        #Lancer la fenetre
        cmds.showWindow()

    #Recharger la fenetre avec le bon nombre de sliders
    def rechargerFenetre():

        for i in range(cmds.intSliderGrp(nbSysteme, q=True, value=True)):
            nbPlanete + cmds.intSliderGrp(field=True, label='Nombre de planètes', minValue=1, maxValue=10, value=5)

        cmds.button(label = "Génerer un Univers", c = self.U.creerUnivers)
