class Bateau:
    """
        Données: posDx position de départ du bateau en x et posDY position de départ du bateau en y
                 posFx position finale du bateau en x et posFY position finale du bateau en y
        Pre: Les coordonnées ne représentent pas un bateau en diagonale et respectent la taille fixée
        Post: Les positions du bateau sont toutes non touchées
    	Resultat: Instancie un bateau
    """
    def __init__(self, posDX, posDY, posFX, posFY): # creer_bateeau : Int x Int x Int x Int  -> Bateau
        return
    """
    	Resultat: Renvoie True si TOUTES les positions du bateau ont été touchées sinon False
    """
    def estCoule(self):# estCoule : Bateau -> boolean
        return
    """
    	Resultat: Renvoie True si la position definie par x et y en parametre est occupée par le bateau, False sinon.
    """
    def caseOccupee(self, x, y):# caseOccupee : Bateau x Int x Int -> boolean
        return
    """
    	Resultat: - La position visée devient touchée si elle était occupée par un bateau mais jamais touchée auparavant
    	          - Renvoie 0 si le bateau est touche
    	          - Renvoie 1 si il est en vue
    	          - Renvoie 2 si le tir est a l'eau
    """
    def tir(self, x, y):# tir : Bateau x Int x Int -> Int
        return
    
