#!/usr/bin/python

class Position:
   
    def __init__(self, x, y): # creer_position : INT x INT -> Position -- Instancie une position en stockant son x et son y.
        """Constructeur de notre classe 
        	Pre-condition : les coordonnées appartiennent a la grille, non occupees.
        """


    def estTouche(self): # estTouche: Position -> boolean -- Renvoie vrai si la position est touche, false sinon.
    def setTouche(self): # setTouche: Position -> -- Marque la position a touche.
    def x(self): # x : Position -> INT -- Renvoie x.
    def y(self): # y : Position -> INT -- Renvoie y.



class Bateau:

   
    def __init__(self, posDX, posDY, posFX, posFY, taille): # creer_bateeau : INT x INT x INT x INT x INT -> Bateau -- Instancie un bateau.
        """Constructeur de notre classe 
        	Données : posDX = position de depart en x, posDY = position de depart en y, posFX = position d'arrivee en x, posFY = position d'arrivee en y, taille = taille du bateau

        	Pre-condition : les coordonnées appartiennent a la grille, non occupees, ne doivent pas representer un bateau en diagonale.
        					La taille en parametre doit etre conforme a l'espacement entre les coordonnees et superieure a 0.
        """


    def estCoule(self): # estCoule : Bateau -> boolean -- Renvoie vrai si il est coule, false sinon.
    def tir(self, x, y): # tir : Bateau -> Int -- Si le tir est sur une position occupee par le bateau et non touche, elle devient touche. Renvoie 0 si le bateau est touche, 1 si il est en vue, 2 si le tir est a l'eau



class Joueur:

	def aPerdu(self): # aPerdu : Joueur -> boolean -- Renvoie true si le joueur a perdu, false sinon.
	def ajoutBateau(self): # ajoutBateau : Joueur Bateau -> -- Ajoute un bateau au joueur.
	def tir(self): # tir : Joueur
	def getShot(self, x, y): #  



def main():
