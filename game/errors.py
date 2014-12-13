"""
Regroupe l'ensemble des exceptions et erreurs utilisées par la logique du jeu.
"""

__author__ = 'François Gouet, Paul Ecoffet'


class NotEnoughCellsError(Exception):
    """
    Levée quand la cellule cliquée n'a pas assez de cases adjacentes de
    même couleur pour être supprimée.
    """
    pass


class InvalidCellError(Exception):
    """
    Levée quand la case cliquée est invalide (vide ou inexistante)
    """
    pass
