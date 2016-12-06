#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle

class Joueur:
	__Bateaux = []
	def bateaux(self):
		return self.Bateaux
	#			Joueur --> [Bateau](5)

	def nbBateauxRestants(self):
		return len(self.bateaux)
	#			Joueur --> int


	#Remarques : - Créer Joueur est un constructeur ->
	def __init__(tabB):
	#			[Bateau](5) --> Joueur
		self.Bateaux = tabB
