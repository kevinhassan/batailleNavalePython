#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
from Tir import *
from Joueur import *
from Bteau import *

def testsTir():

	b1 = Bateau(1,"verticale",2,12)
	b2 = Bateau(1,"verticale",3,12)
	b3 = Bateau(1,"verticale",4,12)
	b4 = Bateau(1,"verticale",5,12)
	b5 = Bateau(1,"verticale",6,12)

	joueur1 = Joueur([b1, b2, b3, b4, b5])

	tir = Tir(1,18,joueur1)

	assert((tir.resultatTir() == "coulé") or (tir.resultatTir() == "touche") or (tir.resultatTir() == "en vue") or (tir.resultatTir() == "à l'eau")), "erreur_resultatTir"
	assert(tir.resultatTir() == "en vue") and (tir.verifierEnVue() == True), "erreur_resultatTir"
	assert(Tir(-2,3,joueur1) == "erreur"), "erreur_resultatTir"
	assert(Tir(5,21,joueur1) == "erreur"), "erreur_resultatTir"


testsTir()