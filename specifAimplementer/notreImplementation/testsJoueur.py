#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle
import Joueur
import Bateau

def testsJoueur():
	
	b1 = creerBateau(1,"verticale",2,12)
	b2 = creerBateau(1,"verticale",3,12)
	b3 = creerBateau(1,"verticale",4,12)
	b4 = creerBateau(1,"verticale",5,12)
	b5 = creerBateau(1,"verticale",6,12)
	b6 = creerBateau(1,"verticale",7,12)
	b7 = creerBateau(1,"verticale",8,12)

	assert(nbBateauxRestants(joueur1)>=0), "erreur_nbBateauxRestants"
	assert(nbBateauxRestants(joueur1)<=5), "erreur_nbBateauxRestants"
	assert(creerJoueur([b1,b2]) == "erreur"), "erreur_creerJoueur"
	assert(creerJoueur([b1,b2,b3,b4,b5,b6,b7]) == "erreur"), "erreur_creerJoueur"