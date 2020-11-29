import maya.cmds as cmds
import random as rd

cmds.file(f=True, new=True)

nbPlanete = []
slider1 = 0
nbSysteme = 0

afficherFenetre()

#Afficher la fenetre
def afficherFenetre():
    cmds.window(title="Générateur d'Univers © pouetpouet")
    cmds.columnLayout(adjustableColumn=True)

    nbSysteme = cmds.intSliderGrp(field=True, label='Nombre de Systèmes planétaires', minValue=1, maxValue=10, value=5)
    cmds.button(label = "OK", c='rechargerFenetre()')

    #Lancer la fenetre
    cmds.showWindow()

#Recharger la fenetre avec le bon nombre de sliders
def rechargerFenetre():
    for i in range(cmds.intSliderGrp(nbSysteme, q=True, value=True)):
        nbPlanete + cmds.intSliderGrp(field=True, label='Nombre de planètes', minValue=1, maxValue=10, value=5)

    cmds.button(label = "Génerer un Univers", c='creerUnivers()')

#Generateur d'Univers
def creerUnivers():

    for i in range(cmds.intSliderGrp(nbSysteme, q=True, value=True)):
        creerSysteme(rd.randint(-500, 500), rd.randint(-500, 500), rd.randint(-500, 500), nbPlanete[i])

#Génération Système Planétaire
def creerSysteme(xr, yr, zr, nbPlanete):

    cmds.polySphere(r = 4, n = "Soleil")
    cmds.move(xr, yr, zr)

    for i in range(nbPlanete):
        cmds.polySphere(r = rd.randint(0, 2),n = "pla" + str(i))
        cmds.move(5*i + 7 + xr, yr, zr)