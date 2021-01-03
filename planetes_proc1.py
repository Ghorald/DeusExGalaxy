import maya.cmds as cmds
cmds.file(f = True, new = True)

def planeteF():

	#------------- variables -----------------#

	VsubdX = 20
	VsubdY = 20
	Vradius = 1
	#Vcouleur1
	#Vcouleur2
	VformeCouleur = 4
	VtypeCouleur = 4
	VtypeBlend = 3
	Vqtite0 = 0.3
	Vqtite1 = 0.7
	Vqtite2 = 0.5
	#--------------------- TABLEAU AVEC LES DIFFERENTES TEXTURES POSSIBLE DE CHOISIR EN CHEMIN UNIVERSEL -------------#

	texture1 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_ceres_fictional.jpg"
	texture2 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_earth_clouds.jpg"
	texture3 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_eris_fictional.jpg"
	texture4 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_haumea_fictional.jpg"
	texture5 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_jupiter.jpg"
	texture6 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_makemake_fictional.jpg"
	texture7 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_mars.jpg"
	texture8 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_mercury.jpg"
	texture9 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_neptune.jpg"
	texture10 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_saturn.jpg"
	texture11 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_sun.jpg"
	texture12 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_uranus.jpg"
	texture13 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_venus_atmosphere.jpg"
	texture14 = "D:/ATI/L3/python/projet1/V2/PLANETE2KJPG/2k_venus_surface.jpg"
	

	planete = cmds.polySphere(n = "planete1", sx=VsubdX, sy=VsubdY, r=Vradius)
	
	
	# ------  TOUJOURS A PLACER EN PREMIER  ------ #
	cmds.HypershadeWindow()

	# ------  SHADER SIMPLE AVEC UNE TEXTURE ------ #

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

	#--------------- parametres de la planete 

	cmds.setAttr(myPRampColor+".type", VformeCouleur) # type radial
	cmds.setAttr(myPRampColor+".interpolation", VtypeCouleur) # interpolation des couleurs en smooth
	cmds.setAttr("myPRampColorN.colorEntryList[0].color", 0.2218, 0.0695, 0.0711,  type="double3") # couleur0
	cmds.setAttr("myPRampColorN.colorEntryList[0].position", Vqtite0)
	cmds.setAttr("myPRampColorN.colorEntryList[1].color", 0.0356, 0.0475, 0.1069,  type="double3") # couleur1
	cmds.setAttr("myPRampColorN.colorEntryList[1].position", Vqtite1)
	
	#couleures suplementaires
	cmds.setAttr("myPRampColorN.colorEntryList[2].color", 0.4013, 0.5065, 0.4564, type="double3") # couleur2
	cmds.setAttr("myPRampColorN.colorEntryList[2].position", Vqtite2)
	#type de blend
	cmds.setAttr("myPMixColorN.operation", VtypeBlend) # divide

	#------------------- LIGHT ---------------------------# 
	light = cmds.directionalLight(rotation=(-45, 30, 15))
	cmds.directionalLight( light, e=True, intensity=0.8 )


	# -------------------- APPLICATION SHADER -------------------#

	cmds.select("planete1" ,replace=True)
	cmds.hyperShade(a = myPShader1)
	cmds.select(cl=True)

	# -------------------- REGLAGE DE LA SCENE -------------------#

	cmds.displaySmoothness( du=2, dv=2, pw=16, ps=4 , po=3 )


window = cmds.window(title = "planete", widthHeight=(200, 55))
cmds.columnLayout( adjustableColumn=True )

cmds.button( label='Close', c=('cmds.deleteUI(\"' + window + '\", window=True)') )

cmds.intSliderGrp( field=True, label='Texture parmi tableau', minValue=1, maxValue=14, fieldMinValue=-100, fieldMaxValue=100, value=11 )
cmds.intSliderGrp( field=True, label='Type d interpolation de couleur', minValue=0, maxValue=7, fieldMinValue=-100, fieldMaxValue=100, value=4 )
cmds.intSliderGrp( field=True, label='Forme de la couleur', minValue=0, maxValue=9, fieldMinValue=-100, fieldMaxValue=100, value=4 )
cmds.intSliderGrp( field=True, label='Type de blend entre la texture et la couleur', minValue=0, maxValue=6, fieldMinValue=-100, fieldMaxValue=100, value=3 )

cmds.colorSliderGrp( label='Couleur 1', rgb=(0, 0, 0) )
cmds.colorSliderGrp( label='Couleur 2', rgb=(1, 1, 1) )

cmds.floatSliderGrp( field=True, label='qtite couleur 1', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0.3 )
cmds.floatSliderGrp( field=True, label='qtite couleur 2', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0.7 )

cmds.floatSliderGrp( field=True, label='Radius', minValue=0.001, maxValue=10, fieldMinValue=-100, fieldMaxValue=100, value=1)
cmds.intSliderGrp( field=True, label='Nombre de subdivisions X', minValue=3, maxValue=30, fieldMinValue=-100, fieldMaxValue=100, value=20 )
cmds.intSliderGrp( field=True, label='Nombre de subdivisions Y', minValue=3, maxValue=30, fieldMinValue=-100, fieldMaxValue=100, value=20 )



cmds.button( label='GenererUnePlanete', c= "planeteF()" )

cmds.showWindow(window)








# ------------------------------ A FAIRE -----------------------#

# relier les sliders aux variables
# créer des variables pour les couleurs grâce à la fonction colorSliderGrp
# mettre les textures en chemin universel
# automatiser le programme pour plusieurs planetes cad avoir un shader assigné à chaque nouvelle planete
# retirer la lumiere de ce script quand il sera relier au script du soleil qui posseded déjà une lumière
