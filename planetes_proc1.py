# coding: utf-8

import maya.cmds as cmds
cmds.file(f = True, new = True)

def planeteF(typeCouleur, formeCouleur, typeBlend, couleur1, couleur2, qtite1, qtite2, radius, subdX, subdY):
	#--------------------- TABLEAU AVEC LES DIFFERENTES TEXTURES POSSIBLE DE CHOISIR EN CHEMIN UNIVERSEL -------------#

	texture1 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_ceres_fictional.jpg"
	texture2 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\2k_earth_clouds.jpg"
	texture3 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_eris_fictional.jpg"
	texture4 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_haumea_fictional.jpg"
	texture5 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_jupiter.jpg"
	texture6 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_makemake_fictional.jpg"
	texture7 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_mars.jpg"
	texture8 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_mercury.jpg"
	texture9 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_neptune.jpg"
	texture10 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_saturn.jpg"
	texture11 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_sun.jpg"
	texture12 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_uranus.jpg"
	texture13 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_venus_atmosphere.jpg"
	texture14 = "C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\PLANETE2KJPG\\2k_venus_surface.jpg"
	

	planete = cmds.polySphere(n = "planete1", sx=subdX, sy=subdY, r=radius)
	
	
	# Toujours à placer en premier
	cmds.HypershadeWindow()

	# Shader simple avec une texture

	myPShader1 = cmds.shadingNode('lambert', asShader=True, n="myPLambertShaderN")
	cmds.sets(renderable=True, noSurfaceShader=True,n="myPLambertShaderNSG")

	myPFile = cmds.shadingNode('file', asTexture=True, n="myPLambertFileN")
	myP2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n="myP2DTextureN")
	myPMixColor = cmds.shadingNode('colorMath', asUtility=True, n="myPMixColorN")
	myP2DTexture2 = cmds.shadingNode('place2dTexture', asUtility=True, n="myP2DTexture2N")
	myPRampColor = cmds.shadingNode('ramp', asTexture=True, n="myPRampColorN")

	cmds.connectAttr(myPRampColor+".outColor", myPMixColor+".colorA")
	cmds.connectAttr(myPFile+".outColor", myPMixColor+".colorB")
	cmds.connectAttr(myPMixColor+".outColor", myPShader1+".color" )

	cmds.setAttr( "myPLambertFileN.fileTextureName",texture11, type="string")
	cmds.connectAttr(myP2DTexture+".coverage", myPFile+".coverage")
	cmds.connectAttr(myP2DTexture2+".outUV", myPRampColor+".uvCoord")
	cmds.connectAttr(myPShader1+".outColor", "myPLambertShaderNSG.surfaceShader")

	# Paramètres de la planète 

	cmds.setAttr(myPRampColor+".type", formeCouleur) # type radial
	cmds.setAttr(myPRampColor+".interpolation", typeCouleur) # interpolation des couleurs en smooth
	cmds.setAttr("myPRampColorN.colorEntryList[0].color", couleur1[0], couleur1[1], couleur1[2],  type="double3") # couleur 1
	cmds.setAttr("myPRampColorN.colorEntryList[0].position", qtite1)
	cmds.setAttr("myPRampColorN.colorEntryList[1].color", couleur2[0], couleur2[1], couleur2[2], type="double3") # couleur 2
	cmds.setAttr("myPRampColorN.colorEntryList[1].position", qtite2)
	
	# Type de blend
	cmds.setAttr("myPMixColorN.operation", typeBlend) # divide

	# LIGHT
	light = cmds.directionalLight(rotation=(-45, 30, 15))
	cmds.directionalLight( light, e=True, intensity=0.8 )

	# APPLICATION SHADER
	cmds.select("planete1" ,replace=True)
	cmds.hyperShade(a = myPShader1)
	cmds.select(cl=True)

	# Réglages de la scène
	cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 , po=3 )



# À faire

# relier les sliders aux variables
# creer des variables pour les couleurs grâce à la fonction colorSliderGrp
# mettre les textures en chemin universel
# automatiser le programme pour plusieurs planetes cad avoir un shader assigne à chaque nouvelle planete
# retirer la lumiere de ce script quand il sera relier au script du soleil qui posseded déjà une lumière
