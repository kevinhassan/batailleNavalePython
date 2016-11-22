#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import abs

class Position:
	"""Constructeur de notre classe Pre-condition : les coordonnées appartiennent a la grille, non occupees."""
	def __init__(self, x, y): # creer_position : INT x INT -> Position -- Instancie une position en stockant son x et son y avec 0 <= x , y <= 20.
	

	def estTouche(self): # estTouche: Position -> boolean -- Renvoie vrai si la position est touche, false sinon.

	def setTouche(self): # setTouche: Position -> -- Marque la position a touche.

	def x(self): # x : Position -> INT -- Renvoie x.

	def y(self): # y : Position -> INT -- Renvoie y.



class Bateau:

   
    def __init__(self, posDX, posDY, posFX, posFY): # creer_bateeau : INT x INT x INT x INT -> Bateau -- Instancie un bateau.
        """Constructeur de notre classe 
        	Données : posDX = position de depart en x, posDY = position de depart en y, posFX = position d'arrivee en x, posFY = position d'arrivee en y, taille = taille du bateau

        	Pre-condition : les coordonnées appartiennent a la grille, non occupees, ne doivent pas representer un bateau en diagonale.
        """


    def estCoule(self): # estCoule : Bateau -> boolean -- Renvoie vrai si il est coule, false sinon.
 	def caseOccupee(self, x, y): # caseOccupee : Bateau x INT x INT -> boolean -- Renvoie vrai si la position definit par x et y en parametre est occupee par le bateau, false sinon.
    def tir(self, x, y): # tir : Bateau x INT x INT -> Int -- Si le tir est sur une position occupee par le bateau et non touche, elle devient touche. Renvoie 0 si le bateau est touche, 1 si il est en vue, 2 si le tir est a l'eau



class Joueur:

    def __init__(self): # creer_joueur : -> Joueur -- Instancie un joueur.


	def aPerdu(self): # aPerdu : Joueur -> boolean -- Renvoie true si le joueur a perdu, false sinon.
	def ajoutBateau(self, posDX, posDY, posFX, posFY): # ajoutBateau : Joueur x Bateau -> boolean -- Ajoute un bateau si les cases du nouveau bateau ne sont pas occupe par un bateau deja existant. Renvoie true si succes, false sinon.
	def tir(self): # tir : Joueur -> INT[2] -- Renvoie un tableau de 2 entier avec 0 <= entier <= 20. 
	def getShot(self, x, y): # Joueur x INT x INT -> Int -- Renvoie 0 un bateau est touche, 1 un bateau est en vue, 2 si le tir est a l'eau.



def main():
	j1 = Joueur()
	j2 = Joueur()
	joueurs = [j1,j2]
	taille = [1,2,3,3,4]
	cpt = 0
	for i in range(0,2):
		while(cpt != 5):
			if(taille[cpt] == 1):
				x1 = -1
				while( x1 < 0  or x1 > 20):
					x1 = input("Entrez un x de depart: ")
				y1 = -1
				while( y1 < 0  or y1 > 20):
					y1 = input("Entrez un y de depart: ")
				x2 = x1
				y2 = y1
			else:
				print("Entrez un bateau de taille : " + taille[cpt])
				valide = False
				while(not(valide)):
					x1 = -1
					while( x1 < 0  or x1 > 20):
						x1 = input("Entrez un x de depart: ")
					y1 = -1
					while( y1 < 0  or y1 > 20):
						y1 = input("Entrez un y de depart: ")
					x2 = -1
					while( x2 < 0  or x2 > 20):
						x2 = input("Entrez un x de fin: ")
					y2 = -1
					while( y2 < 0  or y2 > 20):
						y2 = input("Entrez un y de fin: ")

					if(x1 == x2):
						valide = (abs(y1 - y2) + 1) == taille[cpt]
					else if (y1 == y2):
						valide = (abs(x1 - x2) + 1) == taille[cpt]
			joueurs[i].ajoutBateau(x1,y1,x2,y2)
			cpt = cpt + 1

	fin = False
	courant = 0
	next = 1
	while(not(fin)):
		tir = joueurs[courant].tir()
		retour = joueurs[next].getShot(tir[0], tir[1])

		if(retour == 0):
			print("Touché !")
		if(retour == 1):
			print("En vue !")
		if(retour == 2):
			print("A l'eau ")

		for i in xrange(0,2):
			if(joueurs[i].aPerdu()):
				fin = True

		tmp = courant
		courant = next
		next = tmp

	


