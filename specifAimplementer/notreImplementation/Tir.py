#! /usr/bin/python
# -*- coding: utf-8 -*-
#authors : Thais Aurard, Maxime Soustelle
from Joueur import *
from Bateau import *

#Fonctions
class Tir:
	def __init__(self, coordA, coordB, joueur):
        #			int x int x Joueur --> Tir
		self.joueur = joueur
		try:
			if 0<=coordA and coordA<=20 and 0<=coordB and coordB<=20 :
				self.coordA = coordA
				self.coordB = coordB
			else:
				raise Exception("les coordonnees choisies")
		except Exception as inst:
			print("Erreur dans "+inst.args[0])
			raise#Bloquer l'exécution

	def resultatTir(self):
	#			Tir --> str
		result = ""
		for i in range(0,len(self.joueur.bateaux())): #Itere sur les bateaux du joueur
			for l in range(0,len(self.joueur.bateaux()[i].positionBateau())) : #Itere sur les positions du bateau courant
				if((self.joueur.bateaux()[i].positionBateau()[l][0] == self.coordA and self.joueur.bateaux()[i].positionBateau()[l][1] == self.coordB) and (not self.joueur.bateaux()[i].etatPosition()[l])) : #Si les coordonnées du tir concorde avec la position du bateaux et quelle n'est pas touche
					self.joueur.bateaux()[i].etatPosition()[l] = True
					isDead = True
					cpt = 0
					while (isDead and cpt < len(self.joueur.bateaux()[i].etatPosition())) : #Verifie si le bateau est mort
						if((not self.joueur.bateaux()[i].etatPosition()[cpt])):
							isDead = False
						cpt = cpt + 1
					if(isDead):
						self.joueur.bateaux().pop(i)
						return "coulé"
                        #coule
					else:
						return "touché"
                        #Touche
				elif(self.joueur.bateaux()[i].positionBateau()[l][0] == self.coordA or self.joueur.bateaux()[i].positionBateau()[l][1] == self.coordB) :
					result = "en vue"
                    #En vue
				else :
					if(result != "en vue"):
						result = "à l’eau"
                    #A l'eau
		return result

	def verifierEnVue(self):
	#			Tir --> bool
		for i in range(0,len(self.joueur.bateaux())) : #Itere sur les bateaux du joueur
			for l in range(0,len(self.joueur.bateaux()[i].positionBateau())) : #Itere sur les positions du bateau courant
				if((self.joueur.bateaux()[i].positionBateau()[l][0] == coordA and self.joueur.bateaux()[i].positionBateau()[l][1] != coordB) or (self.joueur.bateaux()[i].positionBateau()[l][1] == coordB and self.joueur.bateaux()[i].positionBateau()[l][0] != coordA)) :
					return True
		return False
