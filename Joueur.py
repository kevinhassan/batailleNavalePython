# -*- coding: utf-8 -*-
class Joueur:
    """
    	Resultat: Instancie un joueur qui n'a pas de bateau et qui n'a pas encore perdu
    """
    def __init__(self): # creer_joueur : -> Joueur
        return

    """
        Pre: Le joueur a déjà placé tous ses bateaux
    	Resultat: Renvoie True si le joueur a perdu <= si tous ses bateaux sont coulés sinon False
    """
    def aPerdu(self): # aPerdu : Joueur -> boolean
        return

    """
        Pre: Le bateau appartient à la grille et il est soit horizontale soit verticale
        Post: Ajoute un bateau qui n'est pas déjà existant dans la grille du joueur
    	Resultat: Renvoie True si succès sinon False (avec au moins une case occupée par un autre bateau)
    """
    def ajoutBateau(self, bateau): # ajoutBateau : Joueur x Bateau -> boolean
        return

    """
        Resultat: demande la saisie par l'utilisateur de coordonnée tant que les coordonnées saisies ne sont pas dans la grille [0,20]
    """
    def viser(self): # tir : Joueur -> INT[2]
        return

    """
        Données: Int x, Int y
        Pre: x,y appartient à [0,20]
        Resultat: - renvoie 0 si le bateau est touché
                  - renvoie 1 si le bateau est en vue
                  - renvoie 2 si à l'eau
    """
    def seFaitTirer(self, x, y): # Joueur x INT x INT -> Int
        return
