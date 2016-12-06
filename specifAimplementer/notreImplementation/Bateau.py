#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
#implementation : FAIZA Mohamed Iheb

class Bateau:
    
    #Remarque : creerBateau c'est le constructeur de bateaux donc on doit change son nom à __init__
	#			int x str x int x int --> Bateau
    def __init__(self,  longueur, orientation, coordX, coordY):
        self.longueur = longueur
        self.orientation = orientation
        self.coordX = coordX
        self.coordY = coordY
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