#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle
import Tir
import Joueur
import Bateau

def testsTir():

	b1 = creerBateau(1,"verticale",2,12)
	b2 = creerBateau(1,"verticale",3,12)
	b3 = creerBateau(1,"verticale",4,12)
	b4 = creerBateau(1,"verticale",5,12)
	b5 = creerBateau(1,"verticale",6,12)

	joueur1 = creerJoueur([b1, b2, b3, b4, b5])

	tir = creerTir(1,18,joueur1)

	assert(resultatTir(tir) == "coule" or "touche" or "en vue" or "a l eau"), "erreur_resultatTir"
	assert((resultatTir(tir) == "en vue") and (verifierEnVue(tir) == True)), "erreur_resultatTir"
	assert(creerTir(-2,3,joueur1) == "erreur"), "erreur_resultatTir"
	assert(creerTir(5,21,joueur1) == "erreur"), "erreur_resultatTir"