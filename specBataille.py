#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *
from Joueur import *
from Position import *
from Bateau import *


def Tests():
	# Instantier deux joueurs
	j1 = Joueur()
	# Ajout Bateaux
	if j1.ajoutBateau(0, 0, 0, 5):
		print("SUCCESS : ajoutBateau, j1 a placé un bateau")
	else:
		print("ERROR : ajoutBateau, j1 n'a pas réussi à placer le bateau")
	if j1.ajoutBateau(0, 0, 5, 0):
		print("ERROR : ajoutBateau, j1 a placé deux bateaux avec des cases en commun")
	else:
		print("SUCCESS : ajoutBateau, j1 n'a pas réussi à placer deux bateaux avec des cases en commun")
	# Test aPerdu
	if j1.aPerdu():
		print("ERROR : aPerdu")
	else:
		print("SUCCESS : aPerdu")
	# Test Viser
	valide = [0, 20]
	coord = j1.viser()
	if len(coord) != 2:
		print("ERROR: viser, la fonction renvoie plus ou moins de deux coordonnees")
	elif (coord[0] not in valide) or (coord[1] not in valide):
		print("ERROR: viser, la fonction renvoie des coordonnees non valides")
	else:
		print("SUCCESS : viser, la fonction renvoie des coordonnees valides")
	# Test seFaitTirer
	valide = [0, 1, 2]
	if (j1.seFaitTirer(0, 0) in valide) and (j1.seFaitTirer(1, 0) in valide) and (j1.seFaitTirer(1, 20) in valide):
		if j1.seFaitTirer(0, 0) == 0:
			("SUCCESS: seFaitTirer, bateau touché")
		else:
			("ERROR: seFaitTirer, le bateau est censé etre touché")
		if j1.seFaitTirer(1, 0) == 1:
			("SUCCESS: seFaitTirer, en vue")
		else:
			("ERROR: seFaitTirer, fonction censé retourner en vue ")
		if j1.seFaitTirer(1, 20) == 2:
			("SUCCESS: seFaitTirer, a l'eau")
		else:
			("ERROR: seFaitTirer, fonction censé retourner en vue")
	else:
		print("ERROR: seFaitTirer, la fonction renvoie un valeur incorrecte")

	# Test Position
	pos1 = Position(1, 2)
	pos2 = Position(100, 25)
	if (pos1.x() == 1 and pos1.y() == 2):
		print("SUCCESS : La position a était crée")
	else:
		print("ERROR : La position est incorrecte")
	if ((pos2.x() >= 0 and pos2.x() <= 20) and (pos2.y() >= 0 and pos2.y() <= 20)):
		print("SUCCESS : La position est valide")
	else:
		print("ERROR : La position n'est pas valide")
	if (pos1.estTouche()):
		print("ERROR : La position ne peut pas être touchee")
	else:
		print("SUCCESS : La position est bien non touchee")
	if (estTouche(pos1.setTouche())):
		print("SUCCESS : La position est bien touchee")
	else:
		print("ERROR : La position devrait être touchee")


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


main()
