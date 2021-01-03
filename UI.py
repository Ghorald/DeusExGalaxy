# coding: utf-8

import maya.cmds as cmds
from DeusExGalaxy import Univers
from DeusExGalaxy import planetes_proc1
from DeusExGalaxy import sun_proc_6bis

reload(Univers)
reload(planetes_proc1)
reload(sun_proc_6bis)

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
        cmds.tabLayout("Univers et soleils")
        cmds.columnLayout("Tanina", adjustableColumn=True)
        self.nbSystemeSlider = cmds.intSliderGrp(field=True, label='Nombre de systemes planetaires', minValue=1, maxValue=10, value=5)
        self.nbEtoilesSlider = cmds.intSliderGrp(field=True, label='Nombre d\'etoiles', minValue=100, maxValue=1000, value=500)
        cmds.button(label="OK", c=self.rechargerFenetre)

        cmds.setParent('..')
        cmds.setParent('..')
        cmds.tabLayout("Planetes")
        cmds.columnLayout(adjustableColumn=True)
        self.UIPlanete()

        cmds.setParent('..')
        cmds.setParent('..')
        cmds.tabLayout("Soleil")
        cmds.columnLayout(adjustableColumn=True)
        self.UISoleil()

        #Lancer la fenetre
        cmds.showWindow()
    
    def UIPlanete(self):
        cmds.intSliderGrp(field=True, label='Texture parmi tableau', minValue=1, maxValue=14, fieldMinValue=-100, fieldMaxValue=100, value=11)
        self.typeCouleurPlanete = cmds.intSliderGrp(field=True, label="Type d'interpolation de couleur", minValue=0, maxValue=7, fieldMinValue=-100, fieldMaxValue=100, value=4)
        self.formeCouleurPlanete = cmds.intSliderGrp(field=True, label='Forme de la couleur', minValue=0, maxValue=9, fieldMinValue=-100, fieldMaxValue=100, value=4)
        self.typeBlendPlanete = cmds.intSliderGrp(field=True, label='Type de blend entre la texture et la couleur', minValue=0, maxValue=6, fieldMinValue=-100, fieldMaxValue=100, value=3)

        self.couleur1Planete = cmds.colorSliderGrp(label='Couleur 1', rgb=(1, 1, 1))
        self.couleur2Planete = cmds.colorSliderGrp(label='Couleur 2', rgb=(1, 1, 1))

        self.qtite1Planete = cmds.floatSliderGrp(field=True, label='Quantite couleur 1', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0.3)
        self.qtite2Planete = cmds.floatSliderGrp(field=True, label='Quantite couleur 2', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0.7)

        self.radiusPlanete = cmds.floatSliderGrp(field=True, label='Radius', minValue=0.001, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=1)
        self.subdXPlanete = cmds.intSliderGrp(field=True, label='Nombre de subdivisions en X', minValue=3, maxValue=30, fieldMinValue=-100, fieldMaxValue=100, value=20)
        self.subdYPlanete = cmds.intSliderGrp(field=True, label='Nombre de subdivisions en Y', minValue=3, maxValue=30, fieldMinValue=-100, fieldMaxValue=100, value=20)

        cmds.button(label='Generer une planete', c=self.creerPlanete)

    def UISoleil(self):
        self.intensiteEmissionSun = cmds.intSliderGrp( field=True, label='Intensite emission', minValue=0, maxValue=30, fieldMinValue=-100, fieldMaxValue=100, value=4 )
        self.propCouleursSun = cmds.floatSliderGrp( field=True, label='Couleur 1 / Couleur 2', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0.8 )

        self.intensiteBumpSun = cmds.floatSliderGrp( field=True, label='Intensite du bump', minValue=0.03, maxValue=0.1, fieldMinValue=-100, fieldMaxValue=100, value=0.06 )

        self.typeTextureSun = cmds.intSliderGrp( field=True, label='Type de texture', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=1 )
        self.formeTextureSun = cmds.floatSliderGrp( field=True, label='Variation de la texture', minValue=1.5, maxValue=8, fieldMinValue=-100, fieldMaxValue=100, value=2 )
        self.qtiteTextureSun = cmds.floatSliderGrp( field=True, label='Quantite de texture', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=11 )

        cmds.button( label='Generer son Soleil', c=self.creerSoleil)

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

    def creerPlanete(self, *args):
        typeCouleur = cmds.intSliderGrp(self.typeCouleurPlanete, q=True, value=True)
        formCouleur = cmds.intSliderGrp(self.formeCouleurPlanete, q=True, value=True)
        typeBlend = cmds.intSliderGrp(self.typeBlendPlanete, q=True, value=True)
        qtite1 = cmds.floatSliderGrp(self.qtite1Planete, q=True, value=True)
        qtite2 = cmds.floatSliderGrp(self.qtite2Planete, q=True, value=True)
        radius = cmds.floatSliderGrp(self.radiusPlanete, q=True, value=True)
        subdX = cmds.intSliderGrp(self.subdXPlanete, q=True, value=True)
        subdY = cmds.intSliderGrp(self.subdYPlanete, q=True, value=True)
        couleur1 = cmds.colorSliderGrp(self.couleur1Planete, q=True, rgb=True)
        couleur2 = cmds.colorSliderGrp(self.couleur2Planete, q=True, rgb=True)
        planetes_proc1.planeteF(typeCouleur, formCouleur, typeBlend, couleur1, couleur2, qtite1, qtite2, radius, subdX, subdY)
    
    def creerSoleil(self, *args):
        intensiteEmission = cmds.intSliderGrp(self.intensiteEmissionSun, q=True, value=True)
        propCouleurs = cmds.floatSliderGrp(self.propCouleursSun, q=True, value=True)
        intensiteBump = cmds.floatSliderGrp(self.intensiteBumpSun, q=True, value=True)
        typeTexture = cmds.intSliderGrp(self.typeTextureSun, q=True, value=True)
        formeTexture = cmds.floatSliderGrp(self.formeTextureSun, q=True, value=True)
        qtiteTexture = cmds.floatSliderGrp(self.qtiteTextureSun, q=True, value=True)

        sun_proc_6bis.sunF(intensiteEmission, propCouleurs, intensiteBump, typeTexture, formeTexture, qtiteTexture)