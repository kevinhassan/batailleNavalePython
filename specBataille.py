#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import abs
import Joueur
import Position
import Bateau

def Tests():
	#Instantier deux joueurs
	j1 = Joueur()
	#Ajout Bateaux
	if j1.ajoutBateau(0,0,0,5) :
		print("SUCCESS : ajoutBateau, j1 a placé un bateau")
	else :
		print("ERROR : ajoutBateau, j1 n'a pas réussi à placer le bateau")
	if j1.ajoutBateau(0,0,5,0) :
		print("ERROR : ajoutBateau, j1 a placé deux bateaux avec des cases en commun")
	else :
		print("SUCCESS : ajoutBateau, j1 n'a pas réussi à placer deux bateaux avec des cases en commun")
	#Test aPerdu
	if j1.aPerdu :
		print("ERROR : aPerdu")
	else :
		print("SUCCESS : aPerdu")
	#Test Viser
	valide = [0,20]
	coord = j1.viser()
	if len(coord) != 2 :
		print("ERROR: viser, la fonction renvoie plus ou moins de deux coordonnees")
	elif (coord[0] not in valide) or (coord[1] not in valide) :
		print("ERROR: viser, la fonction renvoie des coordonnees non valides")
	else :
		print("SUCCESS : viser, la fonction renvoie des coordonnees valides")
	#Test seFaitTirer
	valide = [0,1,2]
	if (j1.seFaitTirer(0,0) in valide) and (j1.seFaitTirer(1,0) in valide) and (j1.seFaitTirer(1,20) in valide)  :
		if j1.seFaitTirer(0,0) == 0 :
			("SUCCESS: seFaitTirer, bateau touché")
		else
			("ERROR: seFaitTirer, le bateau est censé etre touché")
		if j1.seFaitTirer(1,0) == 1 :
			("SUCCESS: seFaitTirer, en vue")
		else
			("ERROR: seFaitTirer, fonction censé retourner en vue ")
		if j1.seFaitTirer(1,20) == 2 :
			("SUCCESS: seFaitTirer, a l'eau")
		else
			("ERROR: seFaitTirer, fonction censé retourner en vue")
	else :
		print ("ERROR: seFaitTirer, la fonction renvoie un valeur incorrecte")

def main():
	j1 = Joueur()
	j2 = Joueur()
	joueurs = [j1,j2]
	taille = [1,2,3,3,4] #On fixe les tailles des bateaux à créer
	cpt = 0 #Compteur pour le nombre de bateau à créer (ici 5)

	'''
		Saisie des bateaux pour les 2 joueurs
	'''
	for i in range(0,2): #Alterner du joueur 1 au joueur2
		while(cpt != 5):
			x1,y1,x2,y2 = -1,-1,-1,-1
			if(taille[cpt] == 1): #Si la taille est de 1 on saisie une seule coordonnee
				while( x1 < 0  or x1 > 20):
					x1 = input("Entrez un x de depart: ")
				while( y1 < 0  or y1 > 20):
					y1 = input("Entrez un y de depart: ")
				x2 = x1
				y2 = y1
			else:
				print("Entrez un bateau de taille : " + taille[cpt])
				valide = False
				while(not(valide)):
					while( x1 < 0  or x1 > 20):
						x1 = input("Entrez un x de depart: ")
					while( y1 < 0  or y1 > 20):
						y1 = input("Entrez un y de depart: ")
					while( x2 < 0  or x2 > 20):
						x2 = input("Entrez un x de fin: ")
					while( y2 < 0  or y2 > 20):
						y2 = input("Entrez un y de fin: ")

					if(x1 == x2):#Verifier que les coordonnees rentrees sont coherentes avec la taille souhaite
						valide = ((abs(y1 - y2) + 1) == taille[cpt])
					else if (y1 == y2):
						valide = (abs(x1 - x2) + 1) == taille[cpt]

					if valide :
						valide = joueurs[i].ajoutBateau(x1,y1,x2,y2) #si la position n'est pas occupée valide = true
			cpt = cpt + 1

	fin = False
	courant = 0
	suivant = 1
	'''
		Debut de la partie avec alternance des 2 joueurs
	'''
	while(not(fin)):
		coordonnee = joueurs[courant].viser()
		retour = joueurs[suivant].seFaitTirer(coordonnee[0], coordonnee[1])

		if(retour == 0):
			print("Touché !")
		else if(retour == 1):
			print("En vue !")
		else if(retour == 2):
			print("A l'eau ")

		fin = joueurs[suivant].aPerdu() #On vérifie que le joueur adverse sur lequel on a tiré a perdu
		courant, suivant = suivant, courant #On permute les joueurs
