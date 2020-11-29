import maya.cmds as cmds
cmds.file(f = True, new = True)



def moonF():
	basicFilter = "*.jpg"
	cmds.fileDialog2(fileMode = 1 , fileFilter=basicFilter, dialogStyle=2)
	#image = cmds.
	moon = cmds.polyCube(w = 2, h = 2, d = 2, n = "BaseSphere")
	#cmds.polyBevel3(moon, fraction = 1.0, segments = 4 , autoFit = True,  depth = 1, mitering = 'uniform' ,  miterAlong = 'center' , chamfer = True  , angleTolerance = 180.0, worldSpace = True ,  subdivideNgons= True, mergeVertices = True, mergeVertexTolerance = 0.0001, smoothingAngle = 30.0, offset = 0.2, forceParallel = False, OffsetasFraction = True )
	cmds.polySmooth(moon,dv=6)

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

	myBlinn = cmds.shadingNode('blinn', asShader=True)
	cmds.hyperShade( myBlinn, assign=True )
	cmds.select( cl=True )
	cmds.hyperShade( objects=myBlinn )
	blinn = cmds.createNode('blinn')
	cmds.select( 'lambert1', blinn )
	cmds.hyperShade( objects='' )
	


window = cmds.window(title = "choisir_image", widthHeight=(200, 55))
cmds.columnLayout( adjustableColumn=True )
cmds.button( label='Close', c=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.button( label='SelectImage', c= "moonF()" )
#cmds.button(Label = "image", c = "moonF()")




#cmds.optionMenu( menuName, label='test menu')
cmds.showWindow(window)