# coding: utf-8

import maya.cmds as cmds
import random as rd
from DeusExGalaxy import planetes_proc1
from DeusExGalaxy import sun_proc_6bis


class Univers:
    def __init__(self):
        self.nbPlanetesSlider = []

    def addPlaneteSlider(self, slider):
        self.nbPlanetesSlider.append(slider)

    def getPlaneteSlider(self):
        return self.nbPlanetesSlider

    def resPlaneteSlider(self):
        self.nbPlanetesSlider = []

    # Générateur d'Univers
    def creerUnivers(self, nbSys):
        for i in range(nbSys):
            self.creerSysteme(
                rd.randint(-200, 200),
                rd.randint(-200, 200),
                rd.randint(-200, 200),
                cmds.intSliderGrp(self.nbPlanetesSlider[i],
                q=True,
                value=True
            ))

    # Génération Système Planétaire
    def creerSysteme(self, xr, yr, zr, nbPlanete):
        sun_proc_6bis.sunF(rd.randint(0, 30), rd.random(), rd.random()*0.97+0.03, rd.randint(0, 1), rd.random()*6.5+1.5, rd.random(), [xr, yr, zr], name="sun"+str(abs(xr)))

        for i in range(nbPlanete):
            couleur1 = [rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)]
            couleur2 = [rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)]
            planetes_proc1.planeteF(-1, rd.randint(0, 6), rd.randint(0, 8), rd.randint(0, 6), couleur1, couleur2, rd.random(), rd.random(), rd.randint(2, 4), rd.randint(10, 30), rd.randint(10, 30), [xr, yr, zr, i*2], name="pla"+str(i)+str(abs(xr)))

    # Génération d'étoiles
    def creerEtoiles(self, nbEtoilesSlider):
        nbEtoile = cmds.intSliderGrp(nbEtoilesSlider, q=True, value=True)

        for i in range(nbEtoile):
            cmds.polyPlatonicSolid()
            cmds.move(rd.randint(-1000, 1000), rd.randint(-1000, 1000), rd.randint(-1000, 1000))
