import maya.cmds as cmds
cmds.file(f = True, new = True)

def moonF():

	#Filtre pour séléctionner que les png
	basicFilter = "*.png"
	#on ouvre une image ( car le filemode est à 1 ) , on utilise le filtre basicfilter
	img = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	img2 = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	#print(img[0])
	#on cree un cube
	#moon = cmds.polySphere(n = "BaseSphere")
	moon = cmds.polyCube(n = "BaseSphere", sx=1,sy=1,sz=1) # pour des raisons de displacement on utilise un cube subdivisé 0 fois
	#on le subdivise et smooth
	#cmds.polySmooth(moon,dv=1) # on va plutot passer par le rendu arnold
	
	# ------  TOUJOURS A PLACER EN PREMIER  ------ #
	cmds.HypershadeWindow() #permet de manipuler l'hypershade en code
	

	cmds.createNode('transform', n='transform1', ss = True, p = "BaseSphere" ) #on creer un node de modification qu'on parente à l'objet ( pour l'instant ça ne sert à rien )
	
	
	
	
	# ------  SHADER SIMPLE AVEC UNE TEXTURE ET UNE NORMALE ------ #

	myShader = cmds.shadingNode('lambert', asShader=True, n="myLambertShader") #on creer son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myLambertShaderSG")
	cmds.connectAttr(myShader+".outColor", "myLambertShaderSG.surfaceShader")
	
	
	
	myFile = cmds.shadingNode('file', asTexture=True, n="myLambertFile") #on creer le node de chemin
	my2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture") #on creer le node de texture 2d

	cmds.setAttr( "myLambertFile.fileTextureName",img[0], type="string") #on definit le chemin sur l'image qu'on a cliqué au début 
	cmds.connectAttr(my2DTexture+".coverage", myFile+".coverage") #on relie le node texture 2d au node chemin

	#cmds.defaultNavigation(connectToExisting=True, source='myLambertFile', destination="my2DTexture") #on peut faire expres de mal connecter pour savoir toutes les proprietes de chaque node
	cmds.defaultNavigation(connectToExisting=True, source="myLambertFile", destination="myLambertShader") # vu qu'on a initialisé le shader on peut relier à partir de la connexion existante, dans le bon ordre, le node chemin au shader lambert
	

	myFile2 = cmds.shadingNode('file', asTexture=True, n="myNormalFile") #on creer le node de chemin
	my2DTexture2 = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture2") #on creer le node de texture 2d
	cmds.setAttr( "myNormalFile.fileTextureName",img2[0], type="string") #on definit le chemin sur l'image qu'on a cliqué au début 
	cmds.connectAttr(my2DTexture2+".coverage", myFile2+".coverage") #on relie le node texture 2d au node chemin
	myBump = cmds.shadingNode('bump2d', asTexture=True, n="myBumpShader")
	cmds.connectAttr(myFile2+".outAlpha", myBump+".bumpValue") #on relie le node texture 2d au node chemin
	cmds.setAttr(myBump+".bumpInterp", 1) #le mode de bump est 1 soit Tangent Space Normal
	cmds.connectAttr(myBump+".outNormal", myShader+".normalCamera") #on relie le node texture 2d au node chemin

	# ------  SHADER EMISSION ------ #

	myEmissionShader = cmds.shadingNode('standardSurface', asShader=True, n="myEmissionShader")
	cmds.sets(renderable=True, noSurfaceShader=True,n="myEmissionShaderSG")
	#sets -renderable true -noSurfaceShader true -empty -name standardSurface2SG;
	cmds.connectAttr(myEmissionShader+".outColor", "myEmissionShaderSG.surfaceShader")
	cmds.setAttr(myEmissionShader+".emission", 1)
	#couleur = cmds.colorEditor(q=True, rgb = True)
	#R = couleur[0]
	#G = couleur[1]
	#B = couleur[2]
	cmds.setAttr(myEmissionShader+".emissionColor",0.895,0.0800,0, type = "double3") # 0.895,0.0800,0


	# ------  SHADER MIX ------ #

	myMixShader = cmds.shadingNode('aiMixShader', asShader=True, n="myMixShader") #on creer son shader
	cmds.sets(renderable=True, noSurfaceShader=True,n="myMixShaderSG")
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
	cmds.connectAttr(myFile3+".outColor", "myMixShaderSG.displacementShader")

	#--------- ARNOLD RENDERER PARAMETER ---------------------#
	
	cmds.setAttr ("BaseSphereShape.aiSubdivType", 1); #catclark
	cmds.setAttr ("BaseSphereShape.aiSubdivIterations", 6); #equivalant du polysmooth
	cmds.setAttr ("BaseSphereShape.aiSubdivAdaptiveMetric", 1); #type d iteration
	cmds.setAttr ("BaseSphereShape.aiSubdivPixelError", 0.230); #valeure d erreur de calcul
	cmds.setAttr ("BaseSphereShape.aiSubdivUvSmoothing", 1); #focalisation du smooth sur les bords 
	cmds.setAttr ("BaseSphereShape.aiSubdivSmoothDerivs", 1); #bolleen pour smooth les tangentes

	cmds.setAttr ("BaseSphereShape.aiDispHeight", 0.06); #0.03 - 0.1
	cmds.setAttr ("BaseSphereShape.aiDispAutobump", 1); #bolleen pour autobump = surcouche de bump pour les details

	#------------------- LIGHT ---------------------------# a enlever
	light = cmds.directionalLight(rotation=(-45, 30, 15))
	cmds.directionalLight( light, e=True, intensity=0.8 )

	# -------------------- APPLICATION SHADER -------------------#

	cmds.select("BaseSphere" ,replace=True) #on select l'objet à appliquer le shader
	cmds.hyperShade(a = myMixShader) #on initialise le shader avec a

	# ------  PENSER A APPUYER SUR L ICONE D AFFICHAGE DE TEXTURE  ------ #
	# TO DEVELOPP #
	#normal
	#emission
	#mix du shader avec l emission avec un masque
	

	

	######## TEST #########

	#filename = cmds.fileDialog2(fileMode=1,  ft = "image" , caption="Import Image" )
	#############	imgnormal = cmds.fileBrowserDialog( m=0, fc=importImage, ft='image', an='ImportImage', om='Import' )
	#cmds.file( filename[0], i=True );
	#image = cmds.
	#cmds.fileDialog2(fileFilter=basicFilter, fileMode = 0, om = "Import", caption="Import JPG",  dialogStyle=2)
	#cmds.polyBevel3(moon, fraction = 1.0, segments = 4 , autoFit = True,  depth = 1, mitering = 'uniform' ,  miterAlong = 'center' , chamfer = True  , angleTolerance = 180.0, worldSpace = True ,  subdivideNgons= True, mergeVertices = True, mergeVertexTolerance = 0.0001, smoothingAngle = 30.0, offset = 0.2, forceParallel = False, OffsetasFraction = True )


	#cmds.listNodeTypes( 'shader' )
	#myAiStandardSurface = cmds.shadingNode('anisotropic', asShader=True, n = "shaderNode") # je cree un shader node de type anisotropic
	#fileNode = cmds.shadingNode('file', name='fileTexture', asTexture=True) # je cree un texture node de type anisotropic
	#cmds.select("BaseSphere" ,replace=True)
	#cmds.hyperShade( "myAiStandartSurface", assign=True ) # j assigne le shader node dans l hypershade
	#cmds.hyperShade(assign = 'lambert1')
	#shaders = cmds.ls(selection=True)
    #return 0
    #myShader = cmds.shadingNode('blin1', asShader=True)
	#cmds.hyperShade(myShader)

	#myBlinn = cmds.shadingNode('blinn', asShader=True)
	#cmds.hyperShade( myBlinn, assign=True )
	#cmds.select( cl=True )
	#cmds.hyperShade( objects=myBlinn )
	#blinn = cmds.createNode('blinn')
	#cmds.select( 'lambert1', blinn )
	#cmds.hyperShade( objects='' )
	
	#cmds.setAttr(img+'".fileTextureName", "myLambertFile")
	#cmds.connectAttr("myLambertFile.outColor", "myLambertShader.Color") 
	#mds.connectAttr("standardSurface1.outColor", myShader+".surfaceShader")
	#cmds.connectAttr( "BaseSphere"+".outColor", "myShadern"+".surfaceShader", force=True )
	#cmds.connectAttr( myShader+".outColor",myShader+".surfaceShader", force=True )
	#cmds.assign

window = cmds.window(title = "choisir_image", widthHeight=(200, 55))
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Close', c=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.button( label='SelectImage', c= "moonF()" )
#cmds.button(Label = "image", c = "moonF()")
#cmds.optionMenu( menuName, label='test menu')
cmds.showWindow(window)