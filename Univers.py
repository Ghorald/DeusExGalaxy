# coding: utf-8

import maya.cmds as cmds

class Univers:
	def __init__(self):
		self.nbSysteme = 0
		self.nbPlanete = []

	#Generateur d'Univers
	def creerUnivers():

	    for i in range(cmds.intSliderGrp(nbSysteme, q=True, value=True)):
	        creerSysteme(rd.randint(-500, 500), rd.randint(-500, 500), rd.randint(-500, 500), nbPlanete[i])

	#Génération Système Planétaire
	def creerSysteme(xr, yr, zr, nbPlanete):

	    cmds.polySphere(r = 4, n = "Soleil")
	    cmds.move(xr, yr, zr)

	    for i in range(nbPlanete):
	        cmds.polySphere(r = rd.randint(0, 2),n = "pla" + str(i))
	        cmds.move(5*i + 7 + xr, yr, zr)