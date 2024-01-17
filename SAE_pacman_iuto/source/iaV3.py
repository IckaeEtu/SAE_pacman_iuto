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

    if choix is None:                   #Pour éviter tout plantage, si il y a un problème ça choisi au hasard
        return random.choice("NESO") 
    else:
        return choix

    
def deplacement_pacman_objet(le_plateau,Joueur):
    analyse_direction={}
    passemuraille = joueur_passe_muraille(Joueur)
    direct_possible=plateau.directions_possibles(le_plateau,joueur.get_pos_pacman(Joueur),passemuraille)
    for dir in direct_possible:
        analyse_direction[dir]=(plateau.analyse_plateau(le_plateau, joueur.get_pos_pacman(Joueur), dir, plateau.get_nb_lignes(le_plateau),passemuraille))
    choix=min(analyse_direction,key=lambda dir: analyse_direction[dir]['objets'])
    return choix
    
def joueur_passe_muraille(Joueur):
    return '~' in joueur.get_objets(Joueur)


def pacman_glouton(le_plateau,lejoueur):
    return joueur.get_duree(lejoueur,'$') > 2

def direction_pacman_glouton(le_plateau,lejoueur):
    """renvoie la direction pour aller vers le fantome le plus proche, quand le pacman est en mode glouton

    Args:
        le_plateau (dict): le plateau de jeu
        lejoueur (dict): le joueur actuel

    Returns:
        str: la direction choisie
    """    
    direction_possible = plateau.directions_possibles(le_plateau,joueur.get_pos_pacman(lejoueur))
    dico_analyse = dict()
    for direction in direction_possible:
        dico_analyse[direction] = plateau.analyse_plateau(le_plateau,joueur.get_pos_pacman(lejoueur),direction,plateau.get_nb_lignes(le_plateau))

    choix = min(dico_analyse,key=lambda direct: dico_analyse[direct]["fantomes"])

    if choix is None:                   #Pour éviter tout plantage, si il y a un problème ça choisi au hasard
        return random.choice(direction_possible) 
    else:
        return choix

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
        
    choix = min(dico_analyse, key = lambda direct : dico_analyse[direct]["fantomes"])

    if choix is None:
         return random.choice(dir_pos)
    else:
        if choix == "N" and "S" in dir_pos:
            direction = "S"
        elif choix == "S" and "N" in dir_pos:
            direction = "N"
        elif choix == "E" and "O" in dir_pos:
            direction = "O"
        elif choix == "O" and "E" in dir_pos:
            direction = "E"
        else:
            direction = random.choice(dir_pos)
             
    return direction 
    
def danger_pacman(le_plateau,le_joueur):
    

def IA_pacman(le_plateau,le_joueur):
    if pacman_glouton(le_plateau,le_joueur):
        return direction_pacman_glouton(le_plateau,le_joueur)
    else:
        
        return deplacement_pacman_objet(le_plateau,le_joueur)
    
