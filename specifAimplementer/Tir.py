#! /usr/bin/python
#authors : Thais Aurard, Maxime Soustelle
import Joueur

#Fonctions
class Tir:
    def __init__(coordA, coordB, joueur):
        #			int x int x Joueur --> Tir
        self.coordA = coordA
        self.coordB = coordB
        self.joueur = joueur
        
	def resultatTir(self):
	#			Tir --> str
        return
        
        
	def verifierEnVue(self):
	#			Tir --> bool
        for i in range(0,len(self.joueur.bateaux())) :
            for l in range(0,len(self.joueur.bateaux()[i].positionBateau())) :
                if(self.joueur.bateaux()[i].positionBateau()[l][0] == coordA and self.joueur.bateaux()[i].positionBateau()[l][1] == coordB and (not self.joueur.bateaux()[i].etatPosition()[l])) :
                    self.joueur.bateaux()[i].etatPosition()[l] = True
                    isDead = True
                    for a in range(0,len(self.joueur.bateaux()[i].etatPosition())) :
                        if((not self.joueur.bateaux()[i].etatPosition()[a])):
                            isDead = False
                    if(isDead):
                        #coule
                    else:
                        #Touche
                elif(self.joueur.bateaux()[i].positionBateau()[l][0] == coordA or self.joueur.bateaux()[i].positionBateau()[l][1] == coordB) :
                    #En vue
                else :
                    #A l'eau
        return
        
        
	def creerTir(coordA, coordB, joueur):
	#			int x int x Joueur --> Tir
        return
