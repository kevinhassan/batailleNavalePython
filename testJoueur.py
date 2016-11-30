#!/usr/bin/python
# -*- coding: utf-8 -*-

from Joueur import *
from Bateau import *

"""
SUCCESS : Le Joueur a était crée
ERROR : La joueur est incorrecte
"""
def testCreation(j1):
    return not(j1.aPerdu())

"""
SUCCESS : ajoutBateau, j1 a reussie à placer un bateau
ERROR : ajoutBateau, n'a pas reussie à ajouter le bateau
"""
def testAjoutBateau(j1,B1):
    return j1.ajoutBateau(B1)

"""
ERROR : aPerdu
SUCCESS : aPerdu
"""
def testAperdu(j1):
    return j1.aPerdu()

"""
SUCCESS: testTirEstTouche, bateau touché
ERROR: testTirEstTouche, le bateau est censé etre touché
"""
def testSeFaitTirerEstTouche(j1,x,y):
    return j1.seFaitTirer(x, y) == 0
"""
SUCCESS: testSeFaitTirerEnVue, en vue
ERROR: testSeFaitTirerEnVue, fonction censé retourner en vue
"""
def testSeFaitTirerEnVue(j1,x,y):
    return j1.seFaitTirer(x, y) == 1

"""
SUCCESS: testSeFaitTirerAleau, a l'eau
ERROR: testSeFaitTirerAleau, fonction censé retourner en vue
"""
def testSeFaitTirerAleau(j1,x,y) :
    return j1.seFaitTirer(x, y) == 2
"""
SUCCESS: testViser, les coordonnées sont valides (dans la grille)
ERROR: testViser, les coordonnéees sont invalides

"""
def testViser(j1):
    coord = j1.viser()
    return coord[0]>=0 and coord[0]<=20 and (coord[1]>=0 and coord[1]<=20)
def testJoueur() :
    #Instancier un joueur
    j1 = Joueur()
    B1 = Bateau(0, 0, 0, 4)
    B2 = Bateau(0, 0, 0, 4)
    if(not(testCreation(j1))):
        print("TEST creation FAIL")
        return False
    if(not(testAjoutBateau(j1,B1))):
        print("TEST testAjoutBateau FAIL")
        return False
    if(testAjoutBateau(j1,B2)):
        print("TEST testAjoutBateau déjà occupé FAIL")
        return False
    if(not(testSeFaitTirerEstTouche(j1,0,0))):
        print("TEST testSeFaiTirerEstTouche FAIL")
        return False
    if(not(testSeFaitTirerEnVue(j1,0,10))):
        print("TEST testSeFaitTirerEnVue FAIL")
        return False
    if(not(testSeFaitTirerAleau(j1,20,20))):
        print("TEST testSeFaitTirerAleau FAIL")
        return False
    if(not(testViser(j1))):
        print("TEST testViser FAIL")
        return False

    #On coule B1
    j1.seFaitTirer(0,0)
    j1.seFaitTirer(0,1)
    j1.seFaitTirer(0,2)
    j1.seFaitTirer(0,3)
    j1.seFaitTirer(0,4)
    if(not(testAperdu(j1))):
        print("TEST testAperdu FAIL")
        return False
    return True

print(testJoueur())
