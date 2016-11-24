class Joueur:

    def __init__(self): # creer_joueur : -> Joueur -- Instancie un joueur.

	def aPerdu(self): # aPerdu : Joueur -> boolean -- Renvoie true si le joueur a perdu (si tous ses bateaux sont coulés), false sinon.
	def ajoutBateau(self, posDX, posDY, posFX, posFY): # ajoutBateau : Joueur x Bateau -> boolean -- Ajoute un bateau si les cases du nouveau bateau ne sont pas occupees par un bateau deja existant. Renvoie true si succes, false sinon.
	def viser(self): # tir : Joueur -> INT[2] -- Demande à l'utilisateur de saisir des coordonnées cibles et les renvoie dans un tableau.
	def seFaitTirer(self, x, y): # Joueur x INT x INT -> Int -- Renvoie 0 un bateau est touche, 1 un bateau est en vue, 2 si le tir est a l'eau.
