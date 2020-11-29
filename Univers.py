# coding: utf-8

import maya.cmds as cmds
import random as rd

class Univers:
	def __init__(self):
		self.nbPlanetesSlider = []
	
	def addPlaneteSlider(self, slider):
		self.nbPlanetesSlider.append(slider)

	# Générateur d'Univers
	def creerUnivers(self, sysSlider):
		for i in range(cmds.intSliderGrp(sysSlider, q=True, value=True)):
			self.creerSysteme(
				rd.randint(-500, 500),
				rd.randint(-500, 500),
				rd.randint(-500, 500),
				cmds.intSliderGrp(self.nbPlanetesSlider[i],
				q=True,
				value=True
			))
	    

	# Génération Système Planétaire
	def creerSysteme(self, xr, yr, zr, nbPlanete):

	    cmds.polySphere(r = 4, n = "Soleil")
	    cmds.move(xr, yr, zr)

	    for i in range(nbPlanete):
	        cmds.polySphere(r = rd.randint(0, 2), n = "pla" + str(i))
	        cmds.move(5*i + 7 + xr, yr, zr)