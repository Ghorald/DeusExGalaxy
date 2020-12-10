# coding: utf-8

import maya.cmds as cmds
import random as rd

class Univers:
	def __init__(self):
		self.nbPlanetesSlider = []
		self.nbEtoiles
	
	def addPlaneteSlider(self, slider):
		self.nbPlanetesSlider.append(slider)
		self.nbEtoiles

	# Générateur d'Univers
	def creerUnivers(self, sysSlider):
		for i in range(cmds.intSliderGrp(sysSlider, q=True, value=True)):
			self.creerSysteme(
				rd.randint(-1000, 1000),
				rd.randint(-1000, 1000),
				rd.randint(-1000, 1000),
				cmds.intSliderGrp(self.nbPlanetesSlider[i],
				q=True,
				value=True
			))
	    
	# Génération Système Planétaire
	def creerSysteme(self, xr, yr, zr, nbPlanete):

	    cmds.polySphere(r = 10, n = "Soleil")
	    cmds.move(xr, yr, zr)

	    for i in range(nbPlanete):
	        cmds.polySphere(r = rd.randint(0, 4), n = "pla" + str(i))
	        cmds.move(5*i + 10 + xr, yr, zr)

	# Génération d'étoiles
	def creerEtoiles(self, nbEtoiles):

		for i in range(nbEtoiles):
			cmds.polyPlatonicSolid()
			cmds.move(rd.randint(-1000, 1000), rd.randint(-1000, 1000), rd.randint(-1000, 1000))