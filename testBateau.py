#!/usr/bin/python
# -*- coding: utf-8 -*-

from Bateau import *

"""
ERROR : estCoule, les deux bateaux ne peuvent pas étre coulé
SUCCESS : estCoule, création de deux bateaux avec réussite
"""
def testCreation(B1):
    return not(B1.estCoule())

"""
ERROR : caseOccupee, la case (0,0) doit etre occupé par B1
SUCCESS : caseOccupee, la case (0,0) est bien occupé par B1
"""
def testCaseOccupee(B1):
    return B1.caseOccupee(0,0)

"""
SUCCESS: tir, bateau touché
ERROR: tir, le bateau est censé etre touché
"""
def testTirEstTouche(B1):
    return B1.tir(0, 0) == 0

"""
SUCCESS: tir, en vue
ERROR: tir, fonction censé retourner en vue
"""
def testTirEnVue(B1):
    return B1.tir(1, 0) == 1

"""
SUCCESS: tir, a l'eau
ERROR: tir, fonction censé retourner en vue
"""
def testTirAleau(B1) :
    return B1.tir(1, 20) == 2

"""
SUCCESS: le bateau est coulé
ERROR: le bateau n'est pas coulé
"""
def testEstCoule(B1):
    return B1.estCoule()

def testBateau() :
    #Instancier un bateaux
    B1 = Bateau(0, 0, 0, 4)
    if(not(testCreation(B1))):
        print("TEST creation FAIL")
        return False
    if(not(testCaseOccupee(B1))):
        print("TEST caseOccupee FAIL")
        return False
    if(not(testTirEstTouche(B1))):
        print("TEST testTirEstTouche FAIL")
        return False
    if(not(testTirEnVue(B1))):
        print("TEST testTirEnVue FAIL")
        return False
    if(not(testTirAleau(B1))):
        print("TEST testTirAleau FAIL")
        return False
    B1.tir(0,0)
    B1.tir(0,1)
    B1.tir(0,2)
    B1.tir(0,3)
    B1.tir(0,4)
    if(not(testTirEstTouche(B1))):
        print("TEST touché FAIL")
        return False
    return True

print(testBateau())
