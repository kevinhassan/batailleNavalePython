#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle

class Joueur:
	__Bateaux = []
	def bateaux(self):
		return self.__Bateaux
	#			Joueur --> [Bateau](5)

	def nbBateauxRestants(self):
		return len(self.__Bateaux)
	#			Joueur --> int


	#Remarques : - Créer Joueur est un constructeur ->
	def __init__(tabB):
	#			[Bateau](5) --> Joueur
		self.__Bateaux = tabB
