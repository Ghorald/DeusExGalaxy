import maya.cmds as cmds
cmds.file(f = True, new = True)

###old
def importImage( fileName, fileType):
   cmds.file(fileName, i=True)
   return 1


def moonF():

	# On ne veut rechercher qu'une image jpg
	basicFilter = "*.jpg"
	# On ouvre une image avec le filemode à 0, une image filtré
	img = cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	# On crée un cube
	moon = cmds.polyCube(w = 2, h = 2, d = 2, n = "BaseSphere")
	# On le subdivise et smooth
	cmds.polySmooth(moon,dv=6)
	# On crée un node
	cmds.createNode( 'transform', n='transform1' )
	# On crée un shader lambert
	myShader = cmds.shadingNode('lambert', asShader=True, n="lambert3")
	# On crée une texture2D
	my2Dtexture = cmds.shadingNode('place2dTexture', asUtility=True, n="texturec")
	# On crée un shader surface
	myShader = cmds.shadingNode('surfaceShader', asShader=True, n="myShadern")
	# On choisit la sphere
	cmds.select("BaseSphere" ,replace=True)
	# On initialise le shader et la texture
	cmds.hyperShade(myShader)
	cmds.hyperShade(my2Dtexture)
	cmds.hyperShade(myShader)


	# TO DEVELOPP #
	# On relie les shaders
	# cmds.connectAttr( myShader+".outColor",myShader+".surfaceShader", force=True )

	# On l'applique a l'objet
	# ...
	# cmds.assign

	
	cmds.HypershadeWindow()
	







	######## TEST #########

	# filename = cmds.fileDialog2(fileMode=1,  ft = "image" , caption="Import Image" )
	#############	imgnormal = cmds.fileBrowserDialog( m=0, fc=importImage, ft='image', an='ImportImage', om='Import' )
	# cmds.file( filename[0], i=True );
	# image = cmds.

	# cmds.fileDialog2(fileFilter=basicFilter, fileMode = 0, om = "Import", caption="Import JPG",  dialogStyle=2)

	# cmds.polyBevel3(moon, fraction = 1.0, segments = 4 , autoFit = True,  depth = 1, mitering = 'uniform' ,  miterAlong = 'center' , chamfer = True  , angleTolerance = 180.0, worldSpace = True ,  subdivideNgons= True, mergeVertices = True, mergeVertexTolerance = 0.0001, smoothingAngle = 30.0, offset = 0.2, forceParallel = False, OffsetasFraction = True )


	# cmds.listNodeTypes( 'shader' )
	# myAiStandardSurface = cmds.shadingNode('anisotropic', asShader=True, n = "shaderNode") # je cree un shader node de type anisotropic
	# fileNode = cmds.shadingNode('file', name='fileTexture', asTexture=True) # je cree un texture node de type anisotropic
	# cmds.select("BaseSphere" ,replace=True)
	# cmds.hyperShade( "myAiStandartSurface", assign=True ) # j assigne le shader node dans l hypershade
	# cmds.hyperShade(assign = 'lambert1')
	# shaders = cmds.ls(selection=True)
    # return 0
    # myShader = cmds.shadingNode('blin1', asShader=True)
	# cmds.hyperShade(myShader)

	# myBlinn = cmds.shadingNode('blinn', asShader=True)
	# cmds.hyperShade( myBlinn, assign=True )
	# cmds.select( cl=True )
	# cmds.hyperShade( objects=myBlinn )
	# blinn = cmds.createNode('blinn')
	# cmds.select( 'lambert1', blinn )
	# cmds.hyperShade( objects='' )
	


window = cmds.window(title = "choisir_image", widthHeight=(200, 55))
cmds.columnLayout(adjustableColumn=True)
cmds.button(label='Close', c=('cmds.deleteUI(\"' + window + '\", window=True)'))
cmds.button(label='SelectImage', c= "moonF()")
# cmds.button(Label = "image", c = "moonF()")
# cmds.optionMenu( menuName, label='test menu')
cmds.showWindow(window)