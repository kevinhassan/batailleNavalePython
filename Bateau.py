class Bateau:

    def __init__(self, posDX, posDY, posFX, posFY): # creer_bateeau : INT x INT x INT x INT -> Bateau -- Instancie un bateau.
        """Constructeur de notre classe
        	Données : posDX = position de depart en x, posDY = position de depart en y, posFX = position d'arrivee en x, posFY = position d'arrivee en y
        	Pre-condition : les coordonnées appartiennent a la grille, non occupees, ne doivent pas representer un bateau en diagonale.
        """

    def estCoule(self): # estCoule : Bateau -> boolean -- Renvoie true si toute les positions du bateau sont touchees
 	def caseOccupee(self, x, y): # caseOccupee : Bateau x INT x INT -> boolean -- Renvoie true si la position definit par x et y en parametre est occupee par le bateau, false sinon.
    def tir(self, x, y): # tir : Bateau x INT x INT -> Int -- Si le tir est sur une position occupee par le bateau et non touche, elle devient touche. Renvoie 0 si le bateau est touche, 1 si il est en vue, 2 si le tir est a l'eau
    
