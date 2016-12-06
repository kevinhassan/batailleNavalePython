#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
#implementation : FAIZA Mohamed Iheb

class Bateau:
    
    #Remarque : creerBateau c'est le constructeur de bateaux donc on doit change son nom à __init__
	#			int x str x int x int --> Bateau
    def __init__(self,  longueur, orientation, coordX, coordY):
        if longueur<=5 :
            self.longueur = longueur
        else :
            return "erreur"
        if orientation=="verticale" or orientation=="horizentale" :
            self.orientation = orientation
        else :
            return "erreur"
        if 0<=coordX and coordX<=20 and 0<=coordY and coordY<=20 :
            self.coordX = coordX
            self.coordY = coordY
        else:            
            return "erreur"
        self.positions = []
        if orientation == "verticale" :
            for i in range(0,longueur) :
                self.positions.append([coordX + i,coordY])
        else :
            for i in range(0,longueur) :
                self.positions.append([coordX,coordY + i])
        self.etats = []
        for i in range(0,longueur) :
            self.etats.append(False)

    #           Bateau --> [bool](n)
    def etatPosition(self):
        return self.etats

    #           Bateau --> int
    def longueurBateau(self):
        return self.longueur

    #           Bateau --> [int x int](n)
    def positionBateau(self):
        return self.positions
