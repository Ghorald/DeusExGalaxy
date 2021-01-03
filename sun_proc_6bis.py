# coding: utf-8

import maya.cmds as cmds
cmds.file(f = True, new = True)

def sunF(intensiteEmission, propCouleurs, intensiteBump, typeTexture, formeTexture, qtiteTexture):
	# Filtre pour sélectionner que les png
	basicFilter = "*.jpg"
	# On ouvre une image (car le filemode est à 1), on utilise le filtre basicfilter
	img = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	img2 = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)

	moon = cmds.polyCube(n = "BaseSphere", sx=1,sy=1,sz=1) # Pour des raisons de displacement, on utilise un cube subdivisé 0 fois

	# Toujours à placer en premier
	cmds.HypershadeWindow() # Permet de manipuler l'hypershade en code

	cmds.createNode('transform', n='transform1', ss = True, p = "BaseSphere" ) # On créé un node de modification qu'on parente à l'objet (pour l'instant ça ne sert à rien)

	# Shader simple avec une texture et une normale
	myShader = cmds.shadingNode('lambert', asShader=True, n="myLambertShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myLambertShaderSG") # On lui applique son shadergraph
	cmds.connectAttr(myShader+".outColor", "myLambertShaderSG.surfaceShader") # On connecte les deux

	myFile = cmds.shadingNode('file', asTexture=True, n="myLambertFile") # On créé le node de chemin
	my2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture") # On creer le node de texture 2d

	cmds.setAttr( "myLambertFile.fileTextureName",img[0], type="string") # On definit le chemin sur l'image sur laquelle on a cliqué au début 
	cmds.connectAttr(my2DTexture+".coverage", myFile+".coverage") # On relie le node texture 2d au node chemin
	cmds.defaultNavigation(connectToExisting=True, source="myLambertFile", destination="myLambertShader") # Vu qu'on a initialisé le shader on peut relier à partir de la connexion existante, dans le bon ordre, le node chemin au shader lambert
	
	myFile2 = cmds.shadingNode('file', asTexture=True, n="myNormalFile") # On créé le node de chemin
	my2DTexture2 = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture2") # On créé le node de texture 2d
	cmds.setAttr( "myNormalFile.fileTextureName",img2[0], type="string") # On définit le chemin sur l'image sur laquelle on a cliqué au début 
	cmds.connectAttr(my2DTexture2+".coverage", myFile2+".coverage") # On relie le node texture 2d au node chemin
	myBump = cmds.shadingNode('bump2d', asTexture=True, n="myBumpShader") # Un bump s'ajoute au normal
	cmds.connectAttr(myFile2+".outAlpha", myBump+".bumpValue") # On relie le node texture 2d au node chemin
	cmds.setAttr(myBump+".bumpInterp", 1) # Le mode de bump est 1 soit Tangent Space Normal
	cmds.connectAttr(myBump+".outNormal", myShader+".normalCamera") # On relie le node texture 2d au node chemin

	# SHADER EMISSION
	myEmissionShader = cmds.shadingNode('standardSurface', asShader=True, n="myEmissionShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myEmissionShaderSG") # On lui applique son shadergraph
	cmds.connectAttr(myEmissionShader+".outColor", "myEmissionShaderSG.surfaceShader") # On connecte les deux
	cmds.setAttr(myEmissionShader+".emission", intensiteEmission)

	# couleur = cmds.colorEditor(q=True, rgb = True)
	# R = couleur[0]
	# G = couleur[1]
	# B = couleur[2]

	# SHADER MIX
	myMixShader = cmds.shadingNode('aiMixShader', asShader=True, n="myMixShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myMixShaderSG") # On lui applique son shadergraph
	cmds.connectAttr(myMixShader+".outColor", "myMixShaderSG.surfaceShader")
	cmds.connectAttr("myLambertShaderSG.surfaceShader", "myMixShader.shader1")
	cmds.connectAttr("myEmissionShaderSG.surfaceShader", "myMixShader.shader2")

	# MIX PARAMETER
	myAOShader = cmds.shadingNode('aiAmbientOcclusion', asShader=True, n="myAOShader") # On créé son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myAOShaderSG")
	cmds.connectAttr(myAOShader+".outColor", "myAOShaderSG.surfaceShader")
	cmds.connectAttr("myAOShaderSG.surfaceShader","myMixShader.mix")

	cmds.setAttr(myAOShader+".white",0,0,0,type="double3")
	cmds.setAttr(myAOShader+".black",1,1,1,type="double3")

	# DISPLACEMENT
	myFile3 = cmds.shadingNode('noise', asTexture=True, n="myDispFile") # On créé le node de chemin
	my2DTexture3 = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture3") # On créé le node de texture 2d
	cmds.connectAttr(my2DTexture3+".outUV", myFile3+".uv") # On relie le node texture 2d au node chemin
	cmds.connectAttr(my2DTexture3+".outUvFilterSize", myFile3+".uvFilterSize") # On relie le node texture 2d au node chemin
	cmds.connectAttr(myFile3+".outColor", "myMixShaderSG.displacementShader") # On relie le node dispalcement a son shader graph

	cmds.setAttr("myDispFile.threshold", qtiteTexture) # Quantite de disp 0 max a 1 rien
	cmds.setAttr("myDispFile.noiseType", typeTexture) # Perlin noise 0 ou Billow 1
	cmds.setAttr("myDispFile.frequencyRatio", formeTexture) # Variation de la forme 1.5 a 8 : 2

	# 2 COULEURS SHADER EMISSION
	myMixColorShader = cmds.shadingNode('blendColors',asUtility=True,n='myMixColorShader')
	cmds.connectAttr(myMixColorShader+".output", myEmissionShader+".emissionColor")

	# Intensité de la première valeur
	myMath = cmds.shadingNode('floatMath', asUtility=True,n="myColorRatio")
	cmds.connectAttr(myMath+".outFloat",myMixColorShader+".blender")
	cmds.connectAttr("myDispFile.outAlpha", myMath+".floatA")
	cmds.setAttr(myMath+".floatB", intensiteEmission) # Ajustement intensité 0.8
	cmds.setAttr(myMath+".operation", 2 ) # Multiply 

	cmds.setAttr(myMixColorShader+".color1",1,0,0 ,type="double3")
	cmds.setAttr(myMixColorShader+".color2",1,0.1685,0 ,type="double3")

	# ARNOLD RENDERER PARAMETER
	cmds.setAttr ("BaseSphereShape.aiSubdivType", 1); # Catclark
	cmds.setAttr ("BaseSphereShape.aiSubdivIterations", 6); # Equivalant du polysmooth
	cmds.setAttr ("BaseSphereShape.aiSubdivAdaptiveMetric", 1); # Type d'iteration
	cmds.setAttr ("BaseSphereShape.aiSubdivPixelError", 0.230); # Valeur d'erreur de calcul
	cmds.setAttr ("BaseSphereShape.aiSubdivUvSmoothing", 1); # Focalisation du smooth sur les bords 
	cmds.setAttr ("BaseSphereShape.aiSubdivSmoothDerivs", 1); # Bolleen pour smooth les tangentes

	cmds.setAttr ("BaseSphereShape.aiDispHeight", intensiteBump); # 0.03 - 0.1 : 0.06
	cmds.setAttr ("BaseSphereShape.aiDispAutobump", 1); # Bolleen pour autobump = surcouche de bump pour les details

	# LIGHT
	light = cmds.directionalLight(rotation=(-45, 30, 0))
	cmds.directionalLight( light, e=True, intensity=0.8 )

	# APPLICATION SHADER
	cmds.select("BaseSphere" ,replace=True) # On sélectionne l'objet à appliquer le shader
	cmds.hyperShade(a = myMixShader) # On initialise le shader avec a

	# ANIMATION
	startTime = cmds.playbackOptions( q =True , minTime = True)
	endTime = cmds.playbackOptions(q = True , maxTime = True)

	cmds.cutKey ( "BaseSphere", time = (startTime, endTime) , attribute ='rotateY' )
	cmds.cutKey ( "my2DTexture3", time = (startTime, endTime) , attribute ='rotateUV' )
	cmds.cutKey ( "myMixColorShader", time = (startTime, endTime) , attribute ='color1.color1R' )
	cmds.cutKey ( "myMixColorShader", time = (startTime, endTime) , attribute ='color1.color1G' )
	cmds.cutKey ( "myMixColorShader", time = (startTime, endTime) , attribute ='color1.color1B' )
	cmds.cutKey ( "myMixColorShader", time = (startTime, endTime) , attribute ='color2.color2R' )
	cmds.cutKey ( "myMixColorShader", time = (startTime, endTime) , attribute ='color2.color2G' )
	cmds.cutKey ( "myMixColorShader", time = (startTime, endTime) , attribute ='color2.color2B' )

	cmds.setKeyframe( "BaseSphere", time = startTime, attribute='rotateY', v=0 )
	cmds.setKeyframe( "BaseSphere", time = endTime, attribute='rotateY', v=360 )
	# cmds.setKeyframe( "BaseSphere", time = endTime - (endTime/3.0), attribute='rotateY', v=360 )
	cmds.selectKey("BaseSphere", time = (startTime, endTime), attribute ='rotateY', keyframe = True)
	cmds.keyTangent ( inTangentType = 'linear', outTangentType = 'linear')

	# cmds.setKeyframe("my2DTexture3", time = startTime, attribute ='rotateUV' , v=0 )
	# cmds.setKeyframe("my2DTexture3", time = endTime, attribute ='rotateUV' , v=-360 )

	cmds.setKeyframe("myMixColorShader", time = startTime, attribute ='color1.color1R' , v=1 )
	cmds.setKeyframe("myMixColorShader", time = startTime, attribute ='color1.color1G' , v=0 )
	cmds.setKeyframe("myMixColorShader", time = startTime, attribute ='color1.color1B' , v=0 )
	cmds.setKeyframe("myMixColorShader", time = endTime, attribute ='color1.color1R' , v=1 )
	cmds.setKeyframe("myMixColorShader", time = endTime, attribute ='color1.color1G' , v=1 )
	cmds.setKeyframe("myMixColorShader", time = endTime, attribute ='color1.color1B' , v=1 )

	cmds.setKeyframe("myMixColorShader", time = startTime, attribute ='color2.color2R' , v=1 )
	cmds.setKeyframe("myMixColorShader", time = startTime, attribute ='color2.color2G' , v=0.1685 )
	cmds.setKeyframe("myMixColorShader", time = startTime, attribute ='color2.color2B' , v=0 )
	cmds.setKeyframe("myMixColorShader", time = endTime, attribute ='color2.color2R' , v=0.2 )
	cmds.setKeyframe("myMixColorShader", time = endTime, attribute ='color2.color2G' , v=0.965 )
	cmds.setKeyframe("myMixColorShader", time = endTime, attribute ='color2.color2B' , v=1 )

	# cmds.setInfinity( 'BaseSphere', poi='cycle' )
	# cmds.play( forward=True )

# À faire

# Relier les sliders aux variables
# Décomposer les variables couleurs des sliders en trois couleurs RGB pour les affecter aux matériaux d'émission
# Gérer la directionalLight pour qu'on puisse voir les planetes
