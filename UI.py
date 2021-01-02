# coding: utf-8

import maya.cmds as cmds
from DeusExGalaxy import Univers

reload(Univers)

class UI:
    def __init__(self):
        """
        Fonction d'initialisation de la classe UI.
        Crée la fenêtre
        """
        self.U = Univers.Univers()

        if cmds.window('window1', ex=True):
            # On vérifie si une fenêtre n'est pas déjà  ouverte. Si oui, on la ferme
            cmds.deleteUI('window1', window=True)
        self.afficherFenetre()

    def afficherFenetre(self, *args):
        """
        Affichage de la fenêtre
        """
        window = cmds.window(title="Generateur d'univers")
        cmds.tabLayout()
        cmds.columnLayout("Tanina", adjustableColumn=True)
        self.nbSystemeSlider = cmds.intSliderGrp(field=True, label='Nombre de systemes planetaires', minValue=1, maxValue=10, value=5)
        self.nbEtoilesSlider = cmds.intSliderGrp(field=True, label='Nombre d\'etoiles', minValue=100, maxValue=1000, value=500)
        cmds.button(label="OK", c=self.rechargerFenetre)

        #Lancer la fenetre
        cmds.showWindow()

    # Recharger la fenetre avec le bon nombre de sliders
    def rechargerFenetre(self, *args):
        """
        Rechargement de la fenêtre avec le bon nombre de sliders
        """
        planSlider = self.U.getPlaneteSlider()
        if planSlider != []:
            for i in planSlider:
                cmds.deleteUI(i, control=True)
            self.U.resPlaneteSlider()
            cmds.deleteUI('createUni', control=True)
            cmds.deleteUI('createStars', control=True)

        nbSys = cmds.intSliderGrp(self.nbSystemeSlider, q=True, value=True)

        for i in range(nbSys):
            self.U.addPlaneteSlider(cmds.intSliderGrp(field=True, label='Nombre de planetes', minValue=1, maxValue=10, value=5))

        cmds.button('createUni', label="Generer un univers", c=self.creerUnivers)
        cmds.button('createStars', label="Generer les etoiles", c=self.creerEtoiles)


    def creerUnivers(self, *args):
        self.U.creerUnivers(self.nbSystemeSlider)

    def creerEtoiles(self, *args):
        self.U.creerEtoiles(self.nbEtoilesSlider)
