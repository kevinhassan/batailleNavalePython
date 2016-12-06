#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle
import Bateau

def testsBateau():
	
	for i in range(1,5):
		bateau1 = creerBateau(i,"verticale",2,12)
		assert(longueurBateau(bateau1) == i), "erreur_longueurBateau"

	assert(creerBateau(2,"banane",3,4) == "erreur"), "erreur_creerBateau"
	assert(creerBateau(-3,"horizontale",3,4) == "erreur"), "erreur_creerBateau"
	assert(creerBateau(5,"horizontale",3,4) == "erreur"), "erreur_creerBateau"
	assert(creerBateau(2,"horizontale",-6,4) == "erreur"), "erreur_creerBateau"
	assert(creerBateau(2,"horizontale",7,28) == "erreur"), "erreur_creerBateau"