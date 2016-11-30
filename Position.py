# -*- coding: utf-8 -*-
class Position:
	"""
		Données: x et y des entiers
		Pre: Les coordonnées x et y entiers appartenant à la grille [0,20] et non occupées
		Resultat: Instancie une position non touchée
	"""
	def __init__(self, x, y): # creer_position : INT x INT -> Position
		return
	"""
		Resultat: Renvoie True si la position est touche sinon False
	"""
	def estTouche(self): # estTouche: Position -> boolean
		return
	"""
		Pre: La position n'a jamais était touchée auparavant
		Resultat: Marquer la position a touchée
	"""
	def setTouche(self): # setTouche: Position -> -- Marque la position a touche
		return
	"""
		Resultat: Renvoie un entier x
	"""
	def x(self): # x : Position -> INT
		return
	"""
		Resultat: Renvoie un entier y
	"""
	def y(self): # y : Position -> INT
		return

"""
--------------------------------PROPRIETES--------------------------------------
    - P1: estTouche(Position(x,y)) == False
    - P2: estTouche(setTouche(Position(x,y))) == True
    - P3: x(Position(x,y)) == x
    - P4: y(Position(x,y)) == y
--------------------------------------------------------------------------------
"""
