# coding: utf-8

import maya.cmds as cmds
from DeusExGalaxy.Univers import Univers

class UI:
    def __init__(self):
        """
        Fonction d'initialisation de la classe UI.
        Crée la fenêtre
        """
        self.U = Univers()

        if cmds.window('window1', ex=True):
            # On vérifie si une fenêtre n'est pas déjà  ouverte. Si oui, on la ferme
            cmds.deleteUI('window1', window=True)
        self.afficherFenetre()

    def afficherFenetre(self, *args):
        """
        Affichage de la fenêtre
        """
        cmds.window(title="Generateur d'Univers - pouetpouet")
        cmds.columnLayout(adjustableColumn=True)

        self.nbSystemeSlider = cmds.intSliderGrp(field=True, label='Nombre de Systemes planetaires', minValue=1, maxValue=10, value=5)
        cmds.button(label = "OK", c = self.rechargerFenetre)

        #Lancer la fenetre
        cmds.showWindow()

    # Recharger la fenetre avec le bon nombre de sliders
    def rechargerFenetre(self, *args):
        """
        Rechargement de la fenêtre avec le bon nombre de sliders
        """
        nbSys = cmds.intSliderGrp(self.nbSystemeSlider, q=True, value=True)

        for i in range(nbSys):
            self.U.addPlaneteSlider(cmds.intSliderGrp(field=True, label='Nombre de planetes', minValue=1, maxValue=10, value=5))

        cmds.button(label="Generer un Univers", c=self.creerUnivers)


    def creerUnivers(self, *args):
        self.U.creerUnivers(self.nbSystemeSlider)
