import maya.cmds as cmds
cmds.file(f = True, new = True)

def sunF():




	# -------------------- VARIABLES --------------------- #

	VintensiteEmission = 4
	#Vcouleur1
	#Vcouleur2
	Vpropcouleurs = 0.8
	VintensiteBump = 0.06
	VtypeTexture = 1
	VqtiteTexture = 0.0
	VformeTexture = 2.0

	#Filtre pour séléctionner que les png
	basicFilter = "*.png"
	#on ouvre une image ( car le filemode est à 1 ) , on utilise le filtre basicfilter
	img = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	img2 = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)

	moon = cmds.polyCube(n = "BaseSphere", sx=1,sy=1,sz=1) # pour des raisons de displacement on utilise un cube subdivisé 0 fois
	
	# ------  TOUJOURS A PLACER EN PREMIER  ------ #
	cmds.HypershadeWindow() #permet de manipuler l'hypershade en code

	cmds.createNode('transform', n='transform1', ss = True, p = "BaseSphere" ) #on creer un node de modification qu'on parente à l'objet ( pour l'instant ça ne sert à rien )

	# ------  SHADER SIMPLE AVEC UNE TEXTURE ET UNE NORMALE ------ #

	myShader = cmds.shadingNode('lambert', asShader=True, n="myLambertShader") #on creer son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myLambertShaderSG") # on lui applique son shadergraph
	cmds.connectAttr(myShader+".outColor", "myLambertShaderSG.surfaceShader") #on connecte les deux
	
	
	
	myFile = cmds.shadingNode('file', asTexture=True, n="myLambertFile") #on creer le node de chemin
	my2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture") #on creer le node de texture 2d

	cmds.setAttr( "myLambertFile.fileTextureName",img[0], type="string") #on definit le chemin sur l'image qu'on a cliqué au début 
	cmds.connectAttr(my2DTexture+".coverage", myFile+".coverage") #on relie le node texture 2d au node chemin
	cmds.defaultNavigation(connectToExisting=True, source="myLambertFile", destination="myLambertShader") # vu qu'on a initialisé le shader on peut relier à partir de la connexion existante, dans le bon ordre, le node chemin au shader lambert
	

	myFile2 = cmds.shadingNode('file', asTexture=True, n="myNormalFile") #on creer le node de chemin
	my2DTexture2 = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture2") #on creer le node de texture 2d
	cmds.setAttr( "myNormalFile.fileTextureName",img2[0], type="string") #on definit le chemin sur l'image qu'on a cliqué au début 
	cmds.connectAttr(my2DTexture2+".coverage", myFile2+".coverage") #on relie le node texture 2d au node chemin
	myBump = cmds.shadingNode('bump2d', asTexture=True, n="myBumpShader") # un bump s ajoute au normal
	cmds.connectAttr(myFile2+".outAlpha", myBump+".bumpValue") #on relie le node texture 2d au node chemin
	cmds.setAttr(myBump+".bumpInterp", 1) #le mode de bump est 1 soit Tangent Space Normal
	cmds.connectAttr(myBump+".outNormal", myShader+".normalCamera") #on relie le node texture 2d au node chemin

	# ------  SHADER EMISSION ------ #

	myEmissionShader = cmds.shadingNode('standardSurface', asShader=True, n="myEmissionShader") #on creer son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myEmissionShaderSG") # on lui applique son shadergraph
	cmds.connectAttr(myEmissionShader+".outColor", "myEmissionShaderSG.surfaceShader") #on connecte les deux
	cmds.setAttr(myEmissionShader+".emission", VintensiteEmission) # VARIABLES ----------------------------------------------------------------------------------------------------------------------
	#couleur = cmds.colorEditor(q=True, rgb = True)
	#R = couleur[0]
	#G = couleur[1]
	#B = couleur[2]

	# ------  SHADER MIX ------ #

	myMixShader = cmds.shadingNode('aiMixShader', asShader=True, n="myMixShader") #on creer son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myMixShaderSG") # on lui applique son shadergraph
	cmds.connectAttr(myMixShader+".outColor", "myMixShaderSG.surfaceShader")
	cmds.connectAttr("myLambertShaderSG.surfaceShader", "myMixShader.shader1")
	cmds.connectAttr("myEmissionShaderSG.surfaceShader", "myMixShader.shader2")
	# -------  Mix parameter -------- #

	myAOShader = cmds.shadingNode('aiAmbientOcclusion', asShader=True, n="myAOShader") #on creer son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myAOShaderSG")
	cmds.connectAttr(myAOShader+".outColor", "myAOShaderSG.surfaceShader")
	cmds.connectAttr("myAOShaderSG.surfaceShader","myMixShader.mix")

	cmds.setAttr(myAOShader+".white",0,0,0,type="double3")
	cmds.setAttr(myAOShader+".black",1,1,1,type="double3")

	# ------  DISPLACEMENT ------ #
	myFile3 = cmds.shadingNode('noise', asTexture=True, n="myDispFile") #on creer le node de chemin
	my2DTexture3 = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture3") #on creer le node de texture 2d
	cmds.connectAttr(my2DTexture3+".outUV", myFile3+".uv") #on relie le node texture 2d au node chemin
	cmds.connectAttr(my2DTexture3+".outUvFilterSize", myFile3+".uvFilterSize") #on relie le node texture 2d au node chemin
	cmds.connectAttr(myFile3+".outColor", "myMixShaderSG.displacementShader") #on relie le node dispalcement a son shader graph

	cmds.setAttr("myDispFile.threshold", VqtiteTexture) # quantite de disp  0 max a 1 rien  # VARIABLES ----------------------------------------------------------------------------------------------------------------------
	cmds.setAttr("myDispFile.noiseType", VtypeTexture) # Perlin noise 0 ou Billow 1  # VARIABLES ----------------------------------------------------------------------------------------------------------------------
	cmds.setAttr("myDispFile.frequencyRatio", VformeTexture) # variation de la forme 1.5 a 8 : 2  # VARIABLES ----------------------------------------------------------------------------------------------------------------------

	# ------  2 couleures SHADER EMISSION------ #

	myMixColorShader = cmds.shadingNode('blendColors',asUtility=True,n='myMixColorShader')
	cmds.connectAttr(myMixColorShader+".output", myEmissionShader+".emissionColor")

	#intensite de la premiere valeure

	myMath = cmds.shadingNode('floatMath', asUtility=True,n="myColorRatio")
	cmds.connectAttr(myMath+".outFloat",myMixColorShader+".blender")
	cmds.connectAttr("myDispFile.outAlpha", myMath+".floatA")
	cmds.setAttr(myMath+".floatB", Vpropcouleurs) # ajustement intensite 0.8  # VARIABLES ----------------------------------------------------------------------------------------------------------------------
	cmds.setAttr(myMath+".operation", 2 ) #multiply 

	cmds.setAttr(myMixColorShader+".color1",1,0,0 ,type="double3") # VARIABLES ----------------------------------------------------------------------------------------------------------------------
	cmds.setAttr(myMixColorShader+".color2",1,0.1685,0 ,type="double3") # VARIABLES ----------------------------------------------------------------------------------------------------------------------


	#--------- ARNOLD RENDERER PARAMETER ---------------------#
	
	cmds.setAttr ("BaseSphereShape.aiSubdivType", 1); #catclark
	cmds.setAttr ("BaseSphereShape.aiSubdivIterations", 6); #equivalant du polysmooth
	cmds.setAttr ("BaseSphereShape.aiSubdivAdaptiveMetric", 1); #type d iteration
	cmds.setAttr ("BaseSphereShape.aiSubdivPixelError", 0.230); #valeure d erreur de calcul
	cmds.setAttr ("BaseSphereShape.aiSubdivUvSmoothing", 1); #focalisation du smooth sur les bords 
	cmds.setAttr ("BaseSphereShape.aiSubdivSmoothDerivs", 1); #bolleen pour smooth les tangentes

	cmds.setAttr ("BaseSphereShape.aiDispHeight", VintensiteBump); #0.03 - 0.1 : 0.06#---------------------------------------------------VARIABLES
	cmds.setAttr ("BaseSphereShape.aiDispAutobump", 1); #bolleen pour autobump = surcouche de bump pour les details

	#------------------- LIGHT ---------------------------#
	light = cmds.directionalLight(rotation=(-45, 30, 0))
	cmds.directionalLight( light, e=True, intensity=0.8 )

	# -------------------- APPLICATION SHADER -------------------#

	cmds.select("BaseSphere" ,replace=True) #on select l'objet à appliquer le shader
	cmds.hyperShade(a = myMixShader) #on initialise le shader avec a



	# ------ ANIMATION --------- #

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
	cmds.setKeyframe( "BaseSphere", time = endTime, attribute='rotateY', v=360 ) #cmds.setKeyframe( "BaseSphere", time = endTime - (endTime/3.0), attribute='rotateY', v=360 )
	cmds.selectKey("BaseSphere", time = (startTime, endTime), attribute ='rotateY', keyframe = True)
	cmds.keyTangent ( inTangentType = 'linear', outTangentType = 'linear')

	#cmds.setKeyframe("my2DTexture3", time = startTime, attribute ='rotateUV' , v=0 )
	#cmds.setKeyframe("my2DTexture3", time = endTime, attribute ='rotateUV' , v=-360 )

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

	#cmds.setInfinity( 'BaseSphere', poi='cycle' )
	#cmds.play( forward=True )

	# ------  PENSER A APPUYER SUR L ICONE D AFFICHAGE DE TEXTURE  ------ #
	

window = cmds.window(title = "choisir_image", widthHeight=(200, 55))
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Close', c=('cmds.deleteUI(\"' + window + '\", window=True)') )

cmds.intSliderGrp( field=True, label='Intensite emission', minValue=0, maxValue=30, fieldMinValue=-100, fieldMaxValue=100, value=4 )
cmds.floatSliderGrp( field=True, label='couleur1', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0 )
cmds.floatSliderGrp( field=True, label='couleur2', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0 )
cmds.floatSliderGrp( field=True, label='proportion couleurs 1 par rapport a 2', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=0.8 )

cmds.floatSliderGrp( field=True, label='Intensite du bump', minValue=0.03, maxValue=0.1, fieldMinValue=-100, fieldMaxValue=100, value=0.06 )

cmds.intSliderGrp( field=True, label='Type de texture', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=1 )
cmds.floatSliderGrp( field=True, label='Variation de la texture', minValue=1.5, maxValue=8, fieldMinValue=-100, fieldMaxValue=100, value=2 )
cmds.floatSliderGrp( field=True, label='Quantite de texture', minValue=0, maxValue=1, fieldMinValue=-100, fieldMaxValue=100, value=11 )


cmds.button( label='Creer son Soleil', c= "sunF()" )

cmds.showWindow(window)

# ------------------------------- A FAIRE ----------------------------- #

# relier les sliders aux variables
# décomposer les variables couleurs des sliders en trois couleurs RGB pour les affecter aux matériaux d emission
# gerer la directionalLight  pour qu on puisse voir les planetes
