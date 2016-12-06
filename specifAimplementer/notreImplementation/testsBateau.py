#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle
from Bateau import *	

def testsBateau():
	
	for i in range(1,5):
		bateau1 = Bateau(i,"verticale",2,12)
		assert(bateau1.longueurBateau() == i), "erreur_longueurBateau"

	assert(Bateau(2,"banane",3,4) == "erreur"), "erreur_creerBateau"
	assert(Bateau(-3,"horizontale",3,4) == "erreur"), "erreur_creerBateau"
	assert(Bateau(5,"horizontale",3,4) == "erreur"), "erreur_creerBateau"
	assert(Bateau(2,"horizontale",-6,4) == "erreur"), "erreur_creerBateau"
	assert(Bateau(2,"horizontale",7,28) == "erreur"), "erreur_creerBateau"


testsBateau()