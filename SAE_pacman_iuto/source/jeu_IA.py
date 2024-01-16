"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module jeu_IA.py
        Ce module contient la définition et l'implémentation de l'IA.
"""


import const
import case
import joueur
import plateau


def deplacement_pacman(plateau, pacman, pos):
    """Définit en fonction de la position de mon pacman sur le plateau, quelle direction
    prendre pour atteindre l’objet le plus proche et, quelle direction prendre pour s’éloigner
    du fantôme le plus proche 

    Args:
        plateau (dict): Le plateau considéré
        pacman (str): La lettre identifiant le pacman à déplacer
        pos (tuple): une paire (lig,col) d'int

    Returns:
        (str): une chaine de caractères indiquant les directions possible 
    """
    

def deplacement_fantome(plateau, fantome, pos):
    """Définit en fonction de la position de mon fantome sur le plateau, quelle direction
    prendre pour s’approcher d’un pacman adverse.

    Args:
        plateau (dict): Le plateau considéré
        fantome (str): La lettre identifiant le fantome à déplacer
        pos (tuple): une paire (lig,col) d'int

    Returns:
        (str): une chaine de caractères indiquant les directions possible 
    """
