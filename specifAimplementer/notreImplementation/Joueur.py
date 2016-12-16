#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
from Bateau import *


class Joueur:
	def bateaux(self):
		return self.__Bateaux
	#			Joueur --> [Bateau](5)

	def nbBateauxRestants(self):
		return len(self.__Bateaux)
	#			Joueur --> int


	#Remarques : - Créer Joueur est un constructeur ->
	def __init__(self, tabB):
	#			[Bateau](5) --> Joueur
		try:
			if(len(tabB) == 5):
				self.__Bateaux = tabB
			else:
				raise Exception("Le nombre de bateau du joueur est incorrect")
		except Exception as inst:
			print("Erreur "+ inst.args[0])
			raise
