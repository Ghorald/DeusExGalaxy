# coding: utf-8

import maya.cmds as cmds
import mtoa.utils as mutils
import random as rd
cmds.file(f = True, new = True)

def sunF(intensiteEmission, propCouleurs, intensiteBump, typeTexture, formeTexture, qtiteTexture, data, name="tuttut"):
	textures = [
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\brown_mud_03_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\brown_mud_03_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\coral_mud_01_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\coral_mud_01_nor_2k.jpg"
		), 
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\leather_red_02_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\leather_red_02_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\medieval_wall_01_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\medieval_wall_01_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\mossy_rock_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\mossy_rock_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rock_04_diff_2k.png",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rock_04_nor_2k.png"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rock_06_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rock_06_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rocks_ground_08_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rocks_ground_08_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rocks_ground_09_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rocks_ground_09_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rough_plaster_broken_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rough_plaster_broken_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rusty_metal_02_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\rusty_metal_02_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\sandstone_cracks_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\sandstone_cracks_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\snow_03_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\snow_03_nor_2k.jpg"
		),
		(
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\white_rough_plaster_diff_2k.jpg",
			"C:\\Users\\lucas\\Documents\\maya\\2020\\scripts\\DeusExGalaxy\\SUN2KJPG\\white_rough_plaster_nor_2k.jpg"
		)
	]
	texture = rd.randint(0, len(textures)-1)

	cmds.polyCube(n=name, sx=1, sy=1, sz=1, h=12, w=12, d=12)
	cmds.displaySmoothness(du=2, dv=2, pw=16, ps=4 , po=3)
	cmds.move(data[0], data[1], data[2])

	# Toujours à placer en premier
	cmds.HypershadeWindow() # Permet de manipuler l'hypershade en code

	cmds.createNode('transform', n='transform1', ss=True, p=name) # On créé un node de modification qu'on parente à l'objet (pour l'instant ça ne sert à rien)

	# Shader simple avec une texture et une normale
	myShader = cmds.shadingNode('lambert', asShader=True, n=name+"myLambertShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n=name+"myLambertShaderSG") # On lui applique son shadergraph
	cmds.connectAttr(myShader+".outColor", name+"myLambertShaderSG.surfaceShader") # On connecte les deux

	myFile = cmds.shadingNode('file', asTexture=True, n=name+"myLambertFile") # On créé le node de chemin
	my2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n=name+"my2DTexture") # On creer le node de texture 2d

	cmds.setAttr(name+"myLambertFile.fileTextureName", textures[texture][0], type="string") # On definit le chemin sur l'image sur laquelle on a cliqué au début 
	cmds.connectAttr(my2DTexture+".coverage", myFile+".coverage") # On relie le node texture 2d au node chemin
	cmds.defaultNavigation(connectToExisting=True, source=name+"myLambertFile", destination=name+"myLambertShader") # Vu qu'on a initialisé le shader on peut relier à partir de la connexion existante, dans le bon ordre, le node chemin au shader lambert
	
	myFile2 = cmds.shadingNode('file', asTexture=True, n=name+"myNormalFile") # On créé le node de chemin
	my2DTexture2 = cmds.shadingNode('place2dTexture', asUtility=True, n=name+"my2DTexture2") # On créé le node de texture 2d
	cmds.setAttr(name+"myNormalFile.fileTextureName", textures[texture][1], type="string") # On définit le chemin sur l'image sur laquelle on a cliqué au début 
	cmds.connectAttr(my2DTexture2+".coverage", myFile2+".coverage") # On relie le node texture 2d au node chemin
	myBump = cmds.shadingNode('bump2d', asTexture=True, n=name+"myBumpShader") # Un bump s'ajoute au normal
	cmds.connectAttr(myFile2+".outAlpha", myBump+".bumpValue") # On relie le node texture 2d au node chemin
	cmds.setAttr(myBump+".bumpInterp", 1) # Le mode de bump est 1 soit Tangent Space Normal
	cmds.connectAttr(myBump+".outNormal", myShader+".normalCamera") # On relie le node texture 2d au node chemin

	# SHADER EMISSION
	myEmissionShader = cmds.shadingNode('standardSurface', asShader=True, n=name+"myEmissionShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True, n=name+"myEmissionShaderSG") # On lui applique son shadergraph
	cmds.connectAttr(myEmissionShader+".outColor", name+"myEmissionShaderSG.surfaceShader") # On connecte les deux
	cmds.setAttr(myEmissionShader+".emission", intensiteEmission)

	# couleur = cmds.colorEditor(q=True, rgb = True)
	# R = couleur[0]
	# G = couleur[1]
	# B = couleur[2]

	# SHADER MIX
	myMixShader = cmds.shadingNode('aiMixShader', asShader=True, n=name+"myMixShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True, n=name+"myMixShaderSG") # On lui applique son shadergraph
	cmds.connectAttr(myMixShader+".outColor", name+"myMixShaderSG.surfaceShader")
	cmds.connectAttr(name+"myLambertShaderSG.surfaceShader", name+"myMixShader.shader1")
	cmds.connectAttr(name+"myEmissionShaderSG.surfaceShader", name+"myMixShader.shader2")

	# MIX PARAMETER
	myAOShader = cmds.shadingNode('aiAmbientOcclusion', asShader=True, n=name+"myAOShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True, n=name+"myAOShaderSG")
	cmds.connectAttr(myAOShader+".outColor", name+"myAOShaderSG.surfaceShader")
	cmds.connectAttr(name+"myAOShaderSG.surfaceShader", name+"myMixShader.mix")

	cmds.setAttr(myAOShader+".white", 0, 0, 0, type="double3")
	cmds.setAttr(myAOShader+".black", 1, 1, 1, type="double3")

	# DISPLACEMENT
	myFile3 = cmds.shadingNode('noise', asTexture=True, n=name+"myDispFile") # On créé le node de chemin
	my2DTexture3 = cmds.shadingNode('place2dTexture', asUtility=True, n=name+"my2DTexture3") # On créé le node de texture 2d
	cmds.connectAttr(my2DTexture3+".outUV", myFile3+".uv") # On relie le node texture 2d au node chemin
	cmds.connectAttr(my2DTexture3+".outUvFilterSize", myFile3+".uvFilterSize") # On relie le node texture 2d au node chemin
	cmds.connectAttr(myFile3+".outColor", name+"myMixShaderSG.displacementShader") # On relie le node dispalcement a son shader graph

	cmds.setAttr(name+"myDispFile.threshold", qtiteTexture) # Quantite de disp 0 max a 1 rien
	cmds.setAttr(name+"myDispFile.noiseType", typeTexture) # Perlin noise 0 ou Billow 1
	cmds.setAttr(name+"myDispFile.frequencyRatio", formeTexture) # Variation de la forme 1.5 a 8 : 2

	# 2 COULEURS SHADER EMISSION
	myMixColorShader = cmds.shadingNode('blendColors',asUtility=True,n=name+'myMixColorShader')
	cmds.connectAttr(myMixColorShader+".output", myEmissionShader+".emissionColor")

	# Intensité de la première valeur
	myMath = cmds.shadingNode('floatMath', asUtility=True,n="myColorRatio")
	cmds.connectAttr(myMath+".outFloat", myMixColorShader+".blender")
	cmds.connectAttr(name+"myDispFile.outAlpha", myMath+".floatA")
	cmds.setAttr(myMath+".floatB", intensiteEmission) # Ajustement intensité 0.8
	cmds.setAttr(myMath+".operation", 2 ) # Multiply 

	cmds.setAttr(myMixColorShader+".color1", 1, 0, 0, type="double3")
	cmds.setAttr(myMixColorShader+".color2", 1, 0.1685, 0, type="double3")

	# ARNOLD RENDERER PARAMETER
	cmds.setAttr (name+"Shape.aiSubdivType", 1); # Catclark
	cmds.setAttr (name+"Shape.aiSubdivIterations", 6); # Equivalant du polysmooth
	cmds.setAttr (name+"Shape.aiSubdivAdaptiveMetric", 1); # Type d'iteration
	cmds.setAttr (name+"Shape.aiSubdivPixelError", 0.230); # Valeur d'erreur de calcul
	cmds.setAttr (name+"Shape.aiSubdivUvSmoothing", 1); # Focalisation du smooth sur les bords 
	cmds.setAttr (name+"Shape.aiSubdivSmoothDerivs", 1); # Bolleen pour smooth les tangentes

	cmds.setAttr (name+"Shape.aiDispHeight", intensiteBump); # 0.03 - 0.1 : 0.06
	cmds.setAttr (name+"Shape.aiDispAutobump", 1); # Bolleen pour autobump = surcouche de bump pour les details

	# LIGHT
	light = cmds.directionalLight(rotation=(-45, 30, 0))
	cmds.directionalLight(light, e=True, intensity=0.8)
	

	# APPLICATION SHADER
	cmds.select(name, replace=True) # On sélectionne l'objet à appliquer le shader
	cmds.hyperShade(a=myMixShader) # On initialise le shader avec a

	# ANIMATION
	startTime = cmds.playbackOptions( q =True , minTime = True)
	endTime = cmds.playbackOptions(q = True , maxTime = True)

	cmds.cutKey(name, time = (startTime, endTime) , attribute ='rotateY')
	cmds.cutKey(name+"my2DTexture3", time = (startTime, endTime) , attribute ='rotateUV')
	cmds.cutKey(name+"myMixColorShader", time = (startTime, endTime) , attribute ='color1.color1R')
	cmds.cutKey(name+"myMixColorShader", time = (startTime, endTime) , attribute ='color1.color1G')
	cmds.cutKey(name+"myMixColorShader", time = (startTime, endTime) , attribute ='color1.color1B')
	cmds.cutKey(name+"myMixColorShader", time = (startTime, endTime) , attribute ='color2.color2R')
	cmds.cutKey(name+"myMixColorShader", time = (startTime, endTime) , attribute ='color2.color2G')
	cmds.cutKey(name+"myMixColorShader", time = (startTime, endTime) , attribute ='color2.color2B')

	cmds.setKeyframe(name, time = startTime, attribute='rotateY', v=0)
	cmds.setKeyframe(name, time = endTime, attribute='rotateY', v=360)
	# cmds.setKeyframe(name, time = endTime - (endTime/3.0), attribute='rotateY', v=360)
	cmds.selectKey(name, time = (startTime, endTime), attribute ='rotateY', keyframe = True)
	cmds.keyTangent(inTangentType='linear', outTangentType='linear')

	# cmds.setKeyframe("my2DTexture3", time = startTime, attribute ='rotateUV' , v=0)
	# cmds.setKeyframe("my2DTexture3", time = endTime, attribute ='rotateUV', v=-360)

	cmds.setKeyframe(name+"myMixColorShader", time = startTime, attribute ='color1.color1R' , v=1)
	cmds.setKeyframe(name+"myMixColorShader", time = startTime, attribute ='color1.color1G' , v=0)
	cmds.setKeyframe(name+"myMixColorShader", time = startTime, attribute ='color1.color1B' , v=0)
	cmds.setKeyframe(name+"myMixColorShader", time = endTime, attribute ='color1.color1R' , v=1)
	cmds.setKeyframe(name+"myMixColorShader", time = endTime, attribute ='color1.color1G' , v=1)
	cmds.setKeyframe(name+"myMixColorShader", time = endTime, attribute ='color1.color1B' , v=1)

	cmds.setKeyframe(name+"myMixColorShader", time = startTime, attribute ='color2.color2R' , v=1)
	cmds.setKeyframe(name+"myMixColorShader", time = startTime, attribute ='color2.color2G' , v=0.1685)
	cmds.setKeyframe(name+"myMixColorShader", time = startTime, attribute ='color2.color2B' , v=0)
	cmds.setKeyframe(name+"myMixColorShader", time = endTime, attribute ='color2.color2R' , v=0.2)
	cmds.setKeyframe(name+"myMixColorShader", time = endTime, attribute ='color2.color2G' , v=0.965)
	cmds.setKeyframe(name+"myMixColorShader", time = endTime, attribute ='color2.color2B' , v=1)

	# cmds.setInfinity('BaseSphere', poi='cycle')
	# cmds.play( forward=True )

# À faire

# Relier les sliders aux variables
# Décomposer les variables couleurs des sliders en trois couleurs RGB pour les affecter aux matériaux d'émission
# Gérer la directionalLight pour qu'on puisse voir les planetes
