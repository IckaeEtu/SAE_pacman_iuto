import random
import joueur
import plateau



def direction_fantome_chasse(le_plateau,le_joueur):
    """renvoie la direction pour aller vers le pacman le plus proche

    Args:
        le_plateau (dict): le plateau de jeu
        le_joueur (dict): le joueur actuel

    Returns:
        str: la direction choisie
    """    
    direction_possible = plateau.directions_possibles(le_plateau,joueur.get_pos_fantome(le_joueur))
    dico_analyse = dict()
    for direction in direction_possible:
        dico_analyse[direction] = plateau.analyse_plateau(le_plateau,joueur.get_pos_fantome(le_joueur),direction,plateau.get_nb_lignes(le_plateau))

    choix = min(dico_analyse,key=lambda direct: dico_analyse[direct]["pacmans"])

    if choix is None:                   #Pour éviter tout plantage, si il y a un problème ça choisi au hasard (peut être retiré)
        return random.choice("NESO") 
    else:
        return choix

    
def direction_pacman_objet(le_plateau,le_joueur):
    """donne la direction pour aller vers l'objet le plus proche

    Args:
        le_plateau (dict): le plateau de jeu actuel
        le_joueur (dict): le joueur actuel

    Returns:
        str: la direction choisie
    """    
    analyse_direction={}
    passemuraille = pacman_passe_muraille(le_joueur)
    direct_possible=plateau.directions_possibles(le_plateau,joueur.get_pos_pacman(le_joueur),passemuraille)
    for dir in direct_possible:
        analyse_direction[dir]=(plateau.analyse_plateau(le_plateau, joueur.get_pos_pacman(le_joueur), dir, plateau.get_nb_lignes(le_plateau),passemuraille))
    choix=min(analyse_direction,key=lambda dir: analyse_direction[dir]['objets'])
    return choix
    
def pacman_passe_muraille(le_joueur):
    """renvoie si le pacman du joueur a passe-muraille ou non

    Args:
        le_joueur (dict): le joueur actuel

    Returns:
        bool: True si le pacman du joueur a passe-muraille, False sinon
    """    
    return '~' in joueur.get_objets(le_joueur)


def pacman_glouton(le_joueur):
    """renvoie si le pacman du joueur a le mode glouton ou non

    Args:
        le_joueur (dict): le joueur actuel

    Returns:
        bool: True si le pacman du joueur a glouton, False sinon
    """    
    return joueur.get_duree(le_joueur,'$') > 2

def direction_pacman_glouton(le_plateau,le_joueur):
    """renvoie la direction pour aller vers le fantome le plus proche, quand le pacman est en mode glouton

    Args:
        le_plateau (dict): le plateau de jeu
        le_joueur (dict): le joueur actuel

    Returns:
        str: la direction choisie
    """    
    direction_possible = plateau.directions_possibles(le_plateau,joueur.get_pos_pacman(le_joueur))
    dico_analyse = dict()
    for direction in direction_possible:
        dico_analyse[direction] = plateau.analyse_plateau(le_plateau,joueur.get_pos_pacman(le_joueur),direction,plateau.get_nb_lignes(le_plateau))

    choix = min(dico_analyse,key=lambda direct: dico_analyse[direct]["fantomes"])

    if choix is None:                   #Pour éviter tout plantage, si il y a un problème ça choisi au hasard (peut être retiré)
        return random.choice(direction_possible) 
    else:
        return choix

def direction_pacman_fugitif(le_plateau, le_joueur):
    """Définit en fonction de la position du pacman du joueur sur le plateau, quelle direction
    prendre pour s’éloigner du fantôme le plus proche 

    Args:
        le_plateau (dict): Le plateau considéré
        le_joueur (dict): Un dictionnaire représentant le joueur

    Returns:
        (str): la direction choisie  
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


def pacman_normal(le_plateau,le_joueur):
    """ Choisi la direction à prendre pour le pacman entre la direction
    pour aller vers le fantome le plus proche ou la direction pour aller vers l'objet le plus proche

    Args:
        le_plateau (dict): le plateau de jeu actuel
        le_joueur (dict): un dictionnaire représentant un joueur

    Returns:
        str: la direction choisie
    """    
    direct=direction_pacman_objet(le_plateau,le_joueur)
    direct_choisi=plateau.analyse_plateau(le_plateau, joueur.get_pos_pacman(le_joueur), direct, plateau.get_nb_lignes(le_plateau),pacman_passe_muraille(le_joueur))
    for dist_fantome in direct_choisi['fantomes']:
        if dist_fantome[0]<=2:
            return direction_pacman_fugitif(le_plateau,le_joueur)
    return direct
            




def IA_pacman(le_plateau,le_joueur):
    """selon les objets, choisit le mode de décision entre glouton ou normal

    Args:
        le_plateau (dict): le plateau actuel
        le_joueur (dict): un dictionnaire représentant un joueur

    Returns:
        _type_: _description_
    """    
    if pacman_glouton(le_plateau,le_joueur):
        return direction_pacman_glouton(le_plateau,le_joueur)
    else:
        
        return pacman_normal(le_joueur)
    
