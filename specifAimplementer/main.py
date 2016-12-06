#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle
import Bateau
import Joueur
import Tir

#Programme principal

def entrerBateau(longueur):
	x = input("entrer coordonnee X de debut ")
	y = input("entrer coordonnee Y de debut ")
	orientation = raw_input("entrer l orientation du bateau: 'verticale' ou 'horizontale' ")
	b = creerBateau(longueur, orientation, x, y)
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
	j1 = creerJoueur(batJ1)
	j2 = creerJoueur(batJ2)

	tour = int(1) #tour du joueur
	x = int(0)
	y = int(0)

	#Boucle de jeu
	while (nbBateauxRestants(j1) != 0) and (nbBateauxRestants(j2) != 0):
		 print("Joueur" + tour + "choisit une position de tir")
		 x = input("Coordonnee x : ")
		 y = input("Coordonnee y : ")
		 if tour == 1:
		 	tir = creerTir(x,y,j1)
		 else:
		 	tir = creerTir(x,y,j2)
		 print(resultatTir(tir))
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



