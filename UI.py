# coding: utf-8

import maya.cmds as cmds
import random as rd
from DeusExGalaxy.Univers import Univers

class UI:
    def __init__(self):
        """
        Fonction d'initialisation de la classe UI.
        Crée la fenêtre
        """

        self.nbPlaneteSlider = []
        #self.U = Univers()

        self.U = Univers()

        if cmds.window('window1', ex=True):
            # On vérifie si une fenêtre n'est pas déj�  ouverte. Si oui, on la ferme
            cmds.deleteUI('window1', window=True)

        #self.fenetre = cmds.window(title="Deux Ex Galaxy", resizeToFitChildren=True)

        #cmds.frameLayout(label="Boutons")
        #cmds.button(label="Générer la galaxie", command=self.generation, align="center")
        # On crée un bouton qui appelle la fonction "self.generation"

        self.afficherFenetre()

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
    def afficherFenetre(self, *args):
        cmds.window(title="Générateur d'Univers © pouetpouet")
        cmds.columnLayout(adjustableColumn=True)

        self.nbSystemeSlider = cmds.intSliderGrp(field=True, label='Nombre de Systèmes planétaires', minValue=1, maxValue=10, value=5)
        cmds.button(label = "OK", c = self.rechargerFenetre)

        #Lancer la fenetre
        cmds.showWindow()

    #Recharger la fenetre avec le bon nombre de sliders
    def rechargerFenetre(self, *args):

        nbSys = cmds.intSliderGrp(self.nbSystemeSlider, q=True, value=True)

        for i in range(nbSys):
            self.nbPlaneteSlider.append(cmds.intSliderGrp(field=True, label='Nombre de planètes', minValue=1, maxValue=10, value=5))

        cmds.button(label = "Génerer un Univers", c = self.creerUnivers)




    #PROBLEME TEMPORAIRE NIKMAYA
    def creerUnivers(self, *args):

        for i in range(cmds.intSliderGrp(self.nbSystemeSlider, q=True, value=True)):
            self.creerSysteme(rd.randint(-500, 500), rd.randint(-500, 500), rd.randint(-500, 500), cmds.intSliderGrp(self.nbPlaneteSlider[i], q=True, value=True))

    #Génération Système Planétaire
    def creerSysteme(self, xr, yr, zr, nbPlanete):

        cmds.polySphere(r = 4, n = "Soleil")
        cmds.move(xr, yr, zr)

        for i in range(nbPlanete):
            cmds.polySphere(r = rd.randint(0, 2),n = "pla" + str(i))
            cmds.move(5*i + 7 + xr, yr, zr)
