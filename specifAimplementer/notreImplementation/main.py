#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
from Joueur import *
from Tir import *
from Bateau import *

#Programme principal

def entrerBateau(longueur):
	x = input("entrer coordonnee X de debut ")
	y = input("entrer coordonnee Y de debut ")
	orientation = raw_input("entrer l orientation du bateau: 'verticale' ou 'horizontale' ")
	b = Bateau(longueur, orientation, x, y)
	return b


def main():
	#Placement des bateaux (la fonction creerBateau est appelee a l interieur de entrerBateau avec les informations entrees par l utilisateur)
	print("Joueur 1")
	b11 = entrerBateau(1)
	b12 = entrerBateau(2)
	b13 = entrerBateau(3)
	b14 = entrerBateau(3)
	b15 = entrerBateau(4)
	print("Joueur 2")
	b21 = entrerBateau(1)
	b22 = entrerBateau(2)
	b23 = entrerBateau(3)
	b24 = entrerBateau(3)
	b25 = entrerBateau(4)

	#Creation des joueurs
	batJ1 = [b11,b12,b13,b14,b15]
	batJ2 = [b21,b22,b23,b24,b25]
	j1 = Joueur(batJ1)
	j2 = Joueur(batJ2)

	tour = int(1) #tour du joueur
	x = int(0)
	y = int(0)

	#Boucle de jeu
	while (j1.nbBateauxRestants() != 0) and (j2.nbBateauxRestants() != 0):
		 print("Joueur" + str(tour + 1 ) +" "+ " choisit une position de tir")
		 x = input("Coordonnee x : ")
		 y = input("Coordonnee y : ")
		 if tour == 1:
		 	tir = Tir(x,y,j1)
		 else:
		 	tir = Tir(x,y,j2)
		 print(tir.resultatTir())
# Dans resultatTir on appelle les fonctions verifierEnVue, etatPosition et nbBateauxRestants
		 if tour == 1 :
			tour += 1
		 else:
			tour -= 1

	if(j1.nbBateauxRestants == 0):
		print("Joueur 2 a gagne")
	else:
		print("Joueur 1 a gagne")

main()
