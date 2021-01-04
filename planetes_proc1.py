# coding: utf-8

import maya.cmds as cmds
import random as rd
cmds.file(f = True, new = True)

def planeteF(texture, typeCouleur, formeCouleur, typeBlend, couleur1, couleur2, qtite1, qtite2, radius, subdX, subdY, data, name="tuttut"):
	#--------------------- TABLEAU AVEC LES DIFFERENTES TEXTURES POSSIBLE DE CHOISIR EN CHEMIN UNIVERSEL -------------#
	textures = [
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_ceres_fictional.jpg",
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_earth_clouds.jpg",
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_eris_fictional.jpg",
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_haumea_fictional.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_jupiter.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_makemake_fictional.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_mars.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_mercury.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_neptune.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_saturn.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_sun.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_uranus.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_venus_atmosphere.jpg", 
		"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_venus_surface.jpg"
	]
	if texture == -1:
		texture = rd.randint(0, len(textures)-1)

	planete = cmds.polySphere(n=name, sx=subdX, sy=subdY, r=radius)
	cmds.displaySmoothness(du=2, dv=2, pw=16, ps=4 , po=3)
	if(name != "tuttut"):
		cmds.move(5*data[3]+20+data[0], data[1], data[2])

	# Toujours à placer en premier
	cmds.HypershadeWindow()

	# Shader simple avec une texture

	myPShader1 = cmds.shadingNode('lambert', asShader=True, n=name+"myPLambertShaderN")
	cmds.sets(renderable=True, noSurfaceShader=True,n=name+"myPLambertShaderNSG")

	myPFile = cmds.shadingNode('file', asTexture=True, n=name+"myPLambertFileN")
	myP2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n=name+"myP2DTextureN")
	myPMixColor = cmds.shadingNode('colorMath', asUtility=True, n=name+"myPMixColorN")
	myP2DTexture2 = cmds.shadingNode('place2dTexture', asUtility=True, n=name+"myP2DTexture2N")
	myPRampColor = cmds.shadingNode('ramp', asTexture=True, n=name+"myPRampColorN")

	cmds.connectAttr(myPRampColor+".outColor", myPMixColor+".colorA")
	cmds.connectAttr(myPFile+".outColor", myPMixColor+".colorB")
	cmds.connectAttr(myPMixColor+".outColor", myPShader1+".color" )
	cmds.setAttr(name+"myPLambertFileN.fileTextureName", textures[texture], type="string")
	cmds.connectAttr(myP2DTexture+".coverage", myPFile+".coverage")
	cmds.connectAttr(myP2DTexture2+".outUV", myPRampColor+".uvCoord")
	cmds.connectAttr(myPShader1+".outColor", name+"myPLambertShaderNSG.surfaceShader")

	# Paramètres de la planète 
	cmds.setAttr(myPRampColor+".type", formeCouleur) # type radial
	cmds.setAttr(myPRampColor+".interpolation", typeCouleur) # interpolation des couleurs en smooth
	cmds.setAttr(name+"myPRampColorN.colorEntryList[0].color", couleur1[0], couleur1[1], couleur1[2],  type="double3") # couleur 1
	cmds.setAttr(name+"myPRampColorN.colorEntryList[0].position", qtite1)
	cmds.setAttr(name+"myPRampColorN.colorEntryList[1].color", couleur2[0], couleur2[1], couleur2[2], type="double3") # couleur 2
	cmds.setAttr(name+"myPRampColorN.colorEntryList[1].position", qtite2)
	
	# Type de blend
	cmds.setAttr(name+"myPMixColorN.operation", typeBlend) # divide

	# LIGHT
	# light = cmds.directionalLight(rotation=(-45, 30, 15))
	# cmds.directionalLight( light, e=True, intensity=0.8 )

	# APPLICATION SHADER
	cmds.select(name, replace=True)
	cmds.hyperShade(a = myPShader1)
	cmds.select(cl=True)


# À faire

# relier les sliders aux variables
# creer des variables pour les couleurs grâce à la fonction colorSliderGrp
# mettre les textures en chemin universel
# automatiser le programme pour plusieurs planetes cad avoir un shader assigne à chaque nouvelle planete
# retirer la lumiere de ce script quand il sera relier au script du soleil qui posseded déjà une lumière
