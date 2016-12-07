#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle

class Bateau:

    #Remarque : creerBateau c'est le constructeur de bateaux donc on doit changer son nom à __init__
    #           il faut spécifier les préconditions sur les données
	#			int x str x int x int --> Bateau
    def __init__(self,  longueur, orientation, coordX, coordY):
        #verification de Longeur
        if longeur>=1 and longueur<=4 :
            self.longueur = longueur
        else :
            return "erreur"
        #verification de l'orientation
        if orientation=="verticale" or orientation=="horizentale" :
            self.orientation = orientation
        else :
            return "erreur"
        #verification des coordonnées
        if 0<=coordX and coordX<=20 and 0<=coordY and coordY<=20 :
            self.coordX = coordX
            self.coordY = coordY
        else:
            return "erreur"
        #declaration et remplissage de la liste des positions
        self.positions = []
        if orientation == "verticale" :
            for i in range(0,longueur) :
                self.positions.append([coordX + i,coordY])
        else :
            for i in range(0,longueur) :
                self.positions.append([coordX,coordY + i])
        #declaration et remplissage de la liste des etats (False -> postion non touché)
        self.etats = []
        for i in range(0,longueur) :
            self.etats.append(False)

    #pas de remarques sur la spécification du reste des fonctions

    #           Bateau --> [bool](n)
    def etatPosition(self):
        return self.etats

    #           Bateau --> int
    def longueurBateau(self):
        return self.longueur

    #           Bateau --> [int x int](n)
    def positionBateau(self):
        return self.positions
