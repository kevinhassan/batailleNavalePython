#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
from Joueur import *
from Tir import *
from Bateau import *
from GraphicLibrary import *
import time

#Programme principal

def entrerBateau(longueur):
	if longueur == 1 :
		x = int(input("entrer coordonnee X de debut "))
		y = int(input("entrer coordonnee Y de debut "))
		return Bateau(longueur, "verticale", x, y)
	x = int(input("entrer coordonnee X de debut "))
	y = int(input("entrer coordonnee Y de debut "))
	orientation = raw_input("entrer l orientation du bateau: v pour 'verticale' ou h pour'horizontale' ")
	if orientation == "v" :
		return Bateau(longueur, "verticale", x, y)
	else :
		return Bateau(longueur, "horizontale", x, y)

def main():
	#Affichage du menu principal
	nettoyer()
	afficherTitre()
	start = raw_input("Commencer le jeu ? (o/n) ")
	if start != "o" :
		return

	nettoyer()

	#Placement des bateaux (la fonction creerBateau est appelee a l interieur de entrerBateau avec les informations entrees par l utilisateur)
	valider = "n"
	while valider == "n" :
		nettoyer()
		print("Joueur 1")
		S1 = getEmptyGrid()
		afficher(S1)
		b11 = entrerBateau(1)
		ajoutMatrice(b11,S1)
		nettoyer()
		print("Joueur 1")
		afficher(S1)
		b12 = entrerBateau(2)
		ajoutMatrice(b12,S1)
		nettoyer()
		print("Joueur 1")
		afficher(S1)
		b13 = entrerBateau(3)
		ajoutMatrice(b13,S1)
		nettoyer()
		print("Joueur 1")
		afficher(S1)
		b14 = entrerBateau(3)
		ajoutMatrice(b14,S1)
		nettoyer()
		print("Joueur 1")
		afficher(S1)
		b15 = entrerBateau(4)
		ajoutMatrice(b15,S1)
		nettoyer()
		afficher(S1)
		valider = raw_input("valider? (o/n) ")
	valider = "n"

	nettoyer()

	while valider == "n" :
		print("Joueur 2")
		S2 = getEmptyGrid()
		afficher(S2)
		b21 = entrerBateau(1)
		ajoutMatrice(b21,S2)
		nettoyer()
		print("Joueur 2")
		afficher(S2)
		b22 = entrerBateau(2)
		ajoutMatrice(b22,S2)
		nettoyer()
		print("Joueur 2")
		afficher(S2)
		b23 = entrerBateau(3)
		ajoutMatrice(b23,S2)
		nettoyer()
		print("Joueur 2")
		afficher(S2)
		b24 = entrerBateau(3)
		ajoutMatrice(b24,S2)
		nettoyer()
		print("Joueur 2")
		afficher(S2)
		b25 = entrerBateau(4)
		ajoutMatrice(b25,S2)
		nettoyer()
		afficher(S2)
		valider = raw_input("valider? (o/n) ")

	#Creation des joueurs
	batJ1 = [b11,b12,b13,b14,b15]
	batJ2 = [b21,b22,b23,b24,b25]
	j1 = Joueur(batJ1)
	j2 = Joueur(batJ2)

	tour = int(1) #tour du joueur
	x = int(0)
	y = int(0)

	G1 = getEmptyGrid()
	G2 = getEmptyGrid()
	G = [G1,G2]

	#Boucle de jeu
	while (j1.nbBateauxRestants() != 0) and (j2.nbBateauxRestants() != 0):
		 nettoyer()
		 print("Joueur " + str(tour) +" "+ " choisit une position de tir")
		 afficher(G[tour-1])
		 x = input("Coordonnee x : ")
		 y = input("Coordonnee y : ")
		 if tour == 1:
		 	tir = Tir(x,y,j2)
		 else:
		 	tir = Tir(x,y,j1)
		 result = tir.resultatTir()
		 if result == "touché" :
			 G[tour-1][x][y] = 1
		 nettoyer()
		 afficher(G[tour-1])
		 print(result)
		 time.sleep(5)
		 #Dans resultatTir on appelle les fonctions verifierEnVue, etatPosition et nbBateauxRestants
		 if tour == 1 :
			 tour += 1
		 else :
			 tour -= 1

	nettoyer()
	if(j1.nbBateauxRestants == 0):
		felicitation(2)

	else:
		felicitation(2)

main()
