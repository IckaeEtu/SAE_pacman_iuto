
import random
import const
import case
import joueur
import plateau
import affichage


def direction_j_fantome_pacman(le_plateau,lejoueur):
    """renvoie la direction pour aller vers le pacman le plus proche

    Args:
        le_plateau (dict): le plateau de jeu
        lejoueur (dict): le joueur actuel

    Returns:
        str: la direction choisie
    """    
    direction_possible = plateau.directions_possibles(le_plateau,joueur.get_pos_fantome(lejoueur))
    dico_analyse = dict()
    for direction in direction_possible:
        dico_analyse[direction] = plateau.analyse_plateau(le_plateau,joueur.get_pos_fantome(lejoueur),direction,plateau.get_nb_lignes(le_plateau))

    choix = min(dico_analyse,key=lambda direct: dico_analyse[direct]["pacmans"])

    print(choix)
    if choix is None:                   #Pour éviter tout plantage, si il y a un problème ça choisi au hasard
        return random.choice("NESO") 
    else:
        return choix

def test_direction_j_fantome():
    with open("cartes/test1.txt") as fic:
            plateau1=fic.read()
    plateau1 = plateau.Plateau(plateau1)
    E = plateau.analyse_plateau(plateau1,(7,5),"E",plateau.get_nb_lignes(plateau1))
    print(plateau1)
    print('ici',E)
    O = plateau.analyse_plateau(plateau1,(7,5),"O",plateau.get_nb_lignes(plateau1))
    print(O)
    choix = min((E,O),key=lambda dir: dir["pacmans"])
    print(choix)

def direction_j_pacman_fantome(le_plateau, le_joueur):
    """Définit en fonction de la position de mon pacman sur le plateau, quelle direction
    prendre pour s’éloigner du fantôme le plus proche 

    Args:
        le_plateau (dict): Le plateau considéré
        Joueur (dict): Un dictionnaire représentant le joueur

    Returns:
        (str): une chaine de caractères indiquant les directions possible 
    """
    dir_pos = plateau.directions_possibles(le_plateau, joueur.get_pos_pacman(le_joueur))
    dico_analyse = dict()
    for direction in dir_pos:
        dico_analyse[direction] = plateau.analyse_plateau(le_plateau, joueur.get_pos_pacman(le_joueur), direction, plateau.get_nb_lignes(le_plateau))
        
    choix = max(dico_analyse, key = lambda direct : dico_analyse[direct]["fantomes"])

    if choix is None:
         return random.choice("NESO")
    else:
        return choix 
              


def test_direction_j_pacman_fantome():
    with open("cartes/test1.txt") as fic:
            plateau1=fic.read()
    plateau1 = plateau.Plateau(plateau1)
    E = plateau.analyse_plateau(plateau1,(7,5),"E",plateau.get_nb_lignes(plateau1))
    print(plateau1)
    print('ici',E)
    O = plateau.analyse_plateau(plateau1,(7,5),"O",plateau.get_nb_lignes(plateau1))
    print(O)
    choix = max((E,O),key=lambda dir: dir["fantomes"])
    assert(choix == E)
    print(choix)
    
