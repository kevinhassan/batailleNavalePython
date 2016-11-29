#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *
from Joueur import *
from Position import *
from Bateau import *
from Tests import *

def main():
	j1 = Joueur()
	j2 = Joueur()
	joueurs = [j1, j2]
	tailles = [1, 2, 3, 3, 4]  # On fixe les tailles des bateaux à créer
	k = 0  # Compteur pour le nombre de bateau à créer (ici 5)

	'''
		Saisie des bateaux pour les 2 joueurs
	'''
	x1, y1, x2, y2 = -1, -1, -1, -1
	for i in range(0, 2):  # Alterner du joueur 1 au joueur2
		while (k != 5):
			if (tailles[k] == 1):  # Si la taille est de 1 on saisie une seule coordonnee
				while (x1 < 0 or x1 > 20):
					x1 = int(input("Entrez un x de depart: "))
				while (y1 < 0 or y1 > 20):
					y1 = int(input("Entrez un y de depart: "))
				x2 = x1
				y2 = y1
				b = Bateau(x1,y1,x2,y2)
				valideAjoutBateau = joueurs[i].ajoutBateau(b)
				if(valideAjoutBateau):
					k = k + 1
			else:
				print("Entrez un bateau de taille : " + str(tailles[k]))
				valideAjoutBateau = False
				while (not (valideAjoutBateau)):
					x1, y1, x2, y2 = -1, -1, -1, -1
					while (x1 < 0 or x1 > 20):
						x1 = int(input("Entrez un x de depart: "))
					while (y1 < 0 or y1 > 20):
						y1 = int(input("Entrez un y de depart: "))
					while (x2 < 0 or x2 > 20):
						x2 = int(input("Entrez un x de fin: "))
					while (y2 < 0 or y2 > 20):
						y2 = int(input("Entrez un y de fin: "))

					if (x1 == x2 and (abs(y1 - y2) + 1) == tailles[k]):  # Verifier que les coordonnees rentrees sont coherentes avec la taille souhaite
						b = Bateau(x1,y1,x2,y2)
						valideAjoutBateau = joueurs[i].ajoutBateau(b)  # si la position n'est pas occupée valideAjoutBateau = true
						if (valideAjoutBateau):  # Si l'ajout est reussie on passe au bateau suivant à placer
							k = k + 1
						else:
							print("La case est déjà occupée par un autre bateau")
					elif (y1 == y2 and (abs(x1 - x2) + 1) == tailles[k]):
						b = Bateau(x1,y1,x2,y2)
						valideAjoutBateau = joueurs[i].ajoutBateau(b)  # si la position n'est pas occupée valideAjoutBateau = true
						if (valideAjoutBateau):  # Si l'ajout est reussie on passe au bateau suivant à placer
							k = k + 1
						else:
							print("La case est déjà occupée par un autre bateau")
					else:
						print("Les coordonnées entrées ne correspondent pas à la taille "+str(tailles[k])+" souhaitée !")




	estFini = False
	courant = 0
	suivant = 1
	'''
		Debut de la partie avec alternance des 2 joueurs
	'''
	while (not (estFini)):
		coordonnee = joueurs[courant].viser()
		retour = joueurs[suivant].seFaitTirer(coordonnee[0], coordonnee[1])

		if (retour == 0):
			print("Touché !")
		elif (retour == 1):
			print("En vue !")
		elif (retour == 2):
			print("A l'eau ")

		estFini = joueurs[suivant].aPerdu()  # On vérifie que le joueur adverse sur lequel on a tiré a perdu
		courant, suivant = suivant, courant  # On permute les joueurs
