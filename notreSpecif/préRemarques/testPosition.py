#!/usr/bin/python
# -*- coding: utf-8 -*-

from Position import *

"""
SUCCESS : La position a était crée
ERROR : La position est incorrecte
"""
def testCreation(pos1):
    return (pos1.x() == 1 and pos1.y() == 2)
"""
ERROR : La position est touchee
SUCCESS : La position est bien non touchee
"""
def testEstTouche(pos1):
    return not(pos1.estTouche())

"""
SUCCESS : La position est bien touchee
ERROR : La position devrait être touchee
"""
def testSetTouche(pos1):
    return pos1.estTouche()

def testPosition() :
    #Instancier une position
    pos1 = Position(1, 2)
    if(not(testCreation(pos1))):
        print("TEST creation FAIL")
        return False
    if(not(testEstTouche(pos1))):
        print("TEST testEstTouche FAIL")
        return False
    pos1.setTouche()
    if(not(testSetTouche(pos1))):
        print("TEST setTouche FAIL")
        return False
    return True

print(testPosition())
