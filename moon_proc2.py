import maya.cmds as cmds
cmds.file(f = True, new = True)

def moonF():

	#Filtre pour séléctionner que les png
	basicFilter = "*.png"
	#on ouvre une image ( car le filemode est à 1 ) , on utilise le filtre basicfilter
	img = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	print(img[0])
	#on cree un cube
	moon = cmds.polyCube(w = 2, h = 2, d = 2, n = "BaseSphere")
	#on le subdivise et smooth
	cmds.polySmooth(moon,dv=6)
	
	# ------  TOUJOURS A PLACER EN PREMIER  ------ #
	cmds.HypershadeWindow() #permet de manipuler l'hypershade en code
	

	cmds.createNode('transform', n='transform1', ss = True, p = "BaseSphere" ) #on creer un node de modification qu'on parente à l'objet ( pour l'instant ça ne sert à rien )
	
	
	
	
	# ------  SHADER SIMPLE AVEC UNE TEXTURE  ------ #

	myShader = cmds.shadingNode('lambert', asShader=True, n="myLambertShader") #on creer son shader
	cmds.select("BaseSphere" ,replace=True) #on select l'objet à appliquer le shader
	cmds.hyperShade(a = myShader) #on initialise le shader avec a
	
	
	myFile = cmds.shadingNode('file', asTexture=True, n="myLambertFile") #on creer le node de chemin
	my2DTexture = cmds.shadingNode('place2dTexture', asUtility=True, n="my2DTexture") #on creer le node de texture 2d

	cmds.setAttr( "myLambertFile.fileTextureName",img[0], type="string") #on definit le chemin sur l'image qu'on a cliqué au début 
	cmds.connectAttr(my2DTexture+".coverage", myFile+".coverage") #on relie le node texture 2d au node chemin

	#cmds.defaultNavigation(connectToExisting=True, source='myLambertFile', destination="my2DTexture") #on peut faire expres de mal connecter pour savoir toutes les proprietes de chaque node
	cmds.defaultNavigation(connectToExisting=True, source="myLambertFile", destination="myLambertShader") # vu qu'on a initialisé le shader on peut relier à partir de la connexion existante, dans le bon ordre, le node chemin au shader lambert
	

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