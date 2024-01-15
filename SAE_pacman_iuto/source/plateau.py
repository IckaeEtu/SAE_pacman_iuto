"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module plateau.py
        Ce module contient l'implémentation de la structure de données
        qui gère le plateau jeu aussi qu'un certain nombre de fonctions
        permettant d'observer le plateau et d'aider l'IA à prendre des décisions
"""
import const
import case
import random



def get_nb_lignes(plateau):
    """retourne le nombre de lignes du plateau

    Args:
        plateau (dict): le plateau considéré

    Returns:
        int: le nombre de lignes du plateau
    """
    return plateau['nb_lignes']


def get_nb_colonnes(plateau):
    """retourne le nombre de colonnes du plateau

    Args:
        plateau (dict): le plateau considéré

    Returns:
        int: le nombre de colonnes du plateau
    """
    return plateau['nb_colonnes']

def pos_ouest(plateau, pos):
    """retourne la position de la case à l'ouest de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    x = pos[0]
    y = pos[1]
    if y == 0:
        return (x,get_nb_colonnes(plateau)-1)
    return (x,y-1)

def pos_est(plateau, pos):
    """retourne la position de la case à l'est de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    x = pos[0]
    y = pos[1]
    if y == get_nb_colonnes(plateau)-1:
        return (x,0)
    return (x,y+1)

def pos_nord(plateau, pos):
    """retourne la position de la case au nord de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    x = pos[0]
    y = pos[1]
    if x == 0:
        return (get_nb_lignes(plateau)-1,y)
    return (x-1,y)


def pos_sud(plateau, pos):
    """retourne la position de la case au sud de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    x = pos[0]
    y = pos[1]
    if x == get_nb_lignes(plateau)-1:
        return (0,y)
    return (x+1,y)

def pos_arrivee(plateau,pos,direction):
    """ calcule la position d'arrivée si on part de pos et qu'on va dans
    la direction indiquée en tenant compte que le plateau est un tore
    si la direction n'existe pas la fonction retourne None
    Args:
        plateau (dict): Le plateau considéré
        pos (tuple): une paire d'entiers qui donne la position de départ
        direction (str): un des caractère NSEO donnant la direction du déplacement

    Returns:
        None|tuple: None ou une paire d'entiers indiquant la position d'arrivée
    """
    match direction:
        case 'N':
            if pos_nord(plateau,pos)[0] < 0:
                return (get_nb_lignes(plateau)-1,pos[1])
        case 'S':
            if pos_sud(plateau,pos)[0] >= get_nb_lignes(plateau):
                return (0,pos[1])
        case 'E':
            if pos_est(plateau,pos)[1] >= get_nb_colonnes(plateau):
                return (pos[0],0)
        case 'O':
            if pos_ouest(plateau,pos)[1] < 0:
                return (pos[0],get_nb_colonnes(plateau)-1)
        case _:
            return None


def get_case(plateau, pos):
    """retourne la case qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        dict: La case qui se situe à la position pos du plateau
    """
    case_plateau=plateau['le_plateau'][pos[0]][pos[1]]
    mur = case_plateau == "#"
    ens_pac = None
    ens_fantome = None
    if mur:
        for entity in plateau:
            if entity.isalpha() and plateau[entity] == pos:
                if entity in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    if ens_pac is None:
                        ens_pac = set()
                        ens_pac.add(entity)
                    else:
                        ens_pac.add(entity)
                else:
                    if ens_fantome is None:
                        ens_fantome = set()
                        ens_fantome.add(entity)
                    else:
                        ens_fantome.add(entity)
        return case.Case(mur,const.AUCUN,ens_pac,ens_fantome)
    
    else:  
        if case_plateau == ' ':
            obj = const.AUCUN
        else:
            obj = case_plateau
        for entity in plateau:
            if entity.isalpha() and plateau[entity] == pos:
                if entity in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    if ens_pac is None:
                        ens_pac = set()
                        ens_pac.add(entity)
                    else:
                        ens_pac.add(entity)
                else:
                    if ens_fantome is None:
                        ens_fantome = set()
                        ens_fantome.add(entity)
                    else:
                        ens_fantome.add(entity)
        return case.Case(mur,obj,ens_pac,ens_fantome)

                
        

def get_objet(plateau, pos):
    """retourne l'objet qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        str: le caractère symbolisant l'objet
    """
    return case.get_objet(get_case(plateau,pos))

def poser_pacman(plateau, pacman, pos):
    """pose un pacman en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le pacman
        pos (tuple): une paire (lig,col) de deux int
    """
    plateau[pacman] = pos
    set_case(plateau,pos,case.poser_pacman(get_case(plateau,pos),pacman))

def poser_fantome(plateau, fantome, pos):
    """pose un fantome en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int
    """
    plateau[fantome] = pos
    set_case(plateau,pos,case.poser_fantome(get_case(plateau,pos),fantome))

def poser_objet(plateau, objet, pos):
    """Pose un objet en position pos sur le plateau. Si cette case contenait déjà
        un objet ce dernier disparait

    Args:
        plateau (dict): le plateau considéré
        objet (int): un entier représentant l'objet. const.AUCUN indique aucun objet
        pos (tuple): une paire (lig,col) de deux int
    """
    set_case(plateau,pos,case.poser_objet(get_case(plateau,pos),objet))

def plateau_from_str(la_chaine, complet=True):
    """Construit un plateau à partir d'une chaine de caractère contenant les informations
        sur le contenu du plateau (voir sujet)

    Args:
        la_chaine (str): la chaine de caractères décrivant le plateau

    Returns:
        dict: le plateau correspondant à la chaine. None si l'opération a échoué
    """
    pass

def Plateau(plan):
    """Créer un plateau en respectant le plan donné en paramètre.
        Le plan est une chaine de caractères contenant
            '#' (mur)
            ' ' (couloir non peint)
            une lettre majuscule (un couloir peint par le joueur représenté par la lettre)

    Args:
        plan (str): le plan sous la forme d'une chaine de caractères

    Returns:
        dict: Le plateau correspondant au plan
    """
    les_lignes = plan.split("\n")
    [nb_lignes,nb_colonnes]=les_lignes[0].split(";")
    nb_lignes = int(nb_lignes)
    nb_colonnes = int(nb_colonnes)
    plateau_res = {'nb_lignes': nb_lignes, 'nb_colonnes': nb_colonnes, 'le_plateau': [les_lignes[i] for i in range(1,nb_lignes+1)]}

    for ind_ligne in range(nb_lignes+1,len(les_lignes)):
        la_ligne = les_lignes[ind_ligne].split(";")
        if len(la_ligne) > 1:
            plateau_res[la_ligne[0]] = (int(la_ligne[1]),int(la_ligne[2]))
    return plateau_res


def set_case(plateau, pos, une_case):
    """remplace la case qui se trouve en position pos du plateau par une_case

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int
        une_case (dict): la nouvelle case
    """
    x=pos[0]
    y=pos[1]
    plateau[x][y] = une_case




def enlever_pacman(plateau, pacman, pos):
    """enlève un joueur qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le joueur
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    if pacman in plateau and plateau[pacman]==pos:
        del plateau[pacman]
        return True
    return False


def enlever_fantome(plateau, fantome, pos):
    """enlève un fantome qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    if fantome in plateau and plateau[fantome]==pos:
        del plateau[fantome]
        return True
    return False

def prendre_objet(plateau, pos):
    """Prend l'objet qui se trouve en position pos du plateau et retourne l'entier
        représentant cet objet. const.AUCUN indique qu'aucun objet se trouve sur case

    Args:
        plateau (dict): Le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        int: l'entier représentant l'objet qui se trouvait sur la case.
        const.AUCUN indique aucun objet
    """
    return case.get_objet(get_case(plateau,pos))

        
def deplacer_pacman(plateau, pacman, pos, direction, passemuraille=False):
    """Déplace dans la direction indiquée un joueur se trouvant en position pos
        sur le plateau si c'est possible

    Args:
        plateau (dict): Le plateau considéré
        pacman (str): La lettre identifiant le pacman à déplacer
        pos (tuple): une paire (lig,col) d'int
        direction (str): une lettre parmie NSEO indiquant la direction du déplacement
        passemuraille (bool): un booléen indiquant si le pacman est passemuraille ou non

    Returns:
        (int,int): une paire (lig,col) indiquant la position d'arrivée du pacman 
                   (None si le pacman n'a pas pu se déplacer)
    """
    new_pos = pos_arrivee(plateau,pos,direction)
    case_arrivee = get_case(plateau,pos_arrivee)
    if (case.est_mur(case_arrivee) and not passemuraille) or  case.get_fantomes != None:
        return None
    else:
        plateau[pacman]=new_pos
        return new_pos

def deplacer_fantome(plateau, fantome, pos, direction):
    """Déplace dans la direction indiquée un fantome se trouvant en position pos
        sur le plateau

    Args:
        plateau (dict): Le plateau considéré
        fantome (str): La lettre identifiant le fantome à déplacer
        pos (tuple): une paire (lig,col) d'int
        direction (str): une lettre parmie NSEO indiquant la direction du déplacement

    Returns:
        (int,int): une paire (lig,col) indiquant la position d'arrivée du fantome
                   None si le joueur n'a pas pu se déplacer
    """
    new_pos = pos_arrivee(plateau,pos,direction)
    case_arrivee = get_case(plateau,pos_arrivee)
    if case.est_mur(case_arrivee):
        return None
    else:
        plateau[fantome] = pos_arrivee
        return pos_arrivee

def case_vide(plateau):
    """choisi aléatoirement sur la plateau une case qui n'est pas un mur et qui
       ne contient ni pacman ni fantome ni objet

    Args:
        plateau (dict): le plateau

    Returns:
        (int,int): la position choisie
    """
    pass


def directions_possibles(plateau,pos,passemuraille=False):
    """ retourne les directions vers où il est possible de se déplacer à partir
        de la position pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): un couple d'entiers (ligne,colonne) indiquant la position de départ
        passemuraille (bool): indique si on s'autorise à passer au travers des murs
    
    Returns:
        str: une chaine de caractères indiquant les directions possibles
              à partir de pos
    """
    direct_possible = ""
    if (case.est_mur(get_case(pos_est(plateau,pos))) and passemuraille) or not case.est_mur(get_case(pos_est(plateau,pos))):
        direct_possible += "E"
    if (case.est_mur(get_case(pos_ouest(plateau,pos))) and passemuraille) or not case.est_mur(get_case(pos_ouest(plateau,pos))):  
        direct_possible += "O"
    if (case.est_mur(get_case(pos_nord(plateau,pos))) and passemuraille) or not case.est_mur(get_case(pos_nord(plateau,pos))):
        direct_possible += "N"
    if (case.est_mur(get_case(pos_sud(plateau,pos))) and passemuraille) or not case.est_mur(get_case(pos_sud(plateau,pos))):
        direct_possible += "S"
        
    return direct_possible
#---------------------------------------------------------#


def analyse_plateau(plateau, pos, direction, distance_max):
    """calcul les distances entre la position pos est les différents objets et
        joueurs du plateau si on commence par partir dans la direction indiquée
        en se limitant à la distance max. Si il n'est pas possible d'aller dans la
        direction indiquée à partir de pos, la fonction doit retourner None

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers indiquant la postion de calcul des distances
        distance_max (int): un entier indiquant la distance limite de la recherche
    Returns:
        dict: un dictionnaire de listes. 
                Les clés du dictionnaire sont 'objets', 'pacmans' et 'fantomes'
                Les valeurs du dictionnaire sont des listes de paires de la forme
                    (dist,ident) où dist est la distance de l'objet, du pacman ou du fantome
                                    et ident est l'identifiant de l'objet, du pacman ou du fantome
            S'il n'est pas possible d'aller dans la direction indiquée à partir de pos
            la fonction retourne None
    """ 
    pass

def prochaine_intersection(plateau,pos,direction):
    """calcule la distance de la prochaine intersection
        si on s'engage dans la direction indiquée

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position de départ
        direction (str): la direction choisie

    Returns:
        int: un entier indiquant la distance à la prochaine intersection
             -1 si la direction mène à un cul de sac.
    """
    
    pass

# A NE PAS DEMANDER
def plateau_2_str(plateau):
        res = str(get_nb_lignes(plateau))+";"+str(get_nb_colonnes(plateau))+"\n"
        pacmans = []
        fantomes = []
        for lig in range(get_nb_lignes(plateau)):
            ligne = ""
            for col in range(get_nb_colonnes(plateau)):
                la_case = get_case(plateau,(lig, col))
                if case.est_mur(la_case):
                    ligne += "#"
                    les_pacmans = case.get_pacmans(la_case)
                    for pac in les_pacmans:
                        pacmans.append((pac, lig, col))
                else:
                    obj = case.get_objet(la_case)
                    les_pacmans = case.get_pacmans(la_case)
                    les_fantomes= case.get_fantomes(la_case)
                    ligne += str(obj)
                    for pac in les_pacmans:
                        pacmans.append((pac, lig, col))
                    for fantome in les_fantomes:
                        fantomes.append((fantome,lig,col))
            res += ligne+"\n"
        res += str(len(pacmans))+'\n'
        for pac, lig, col in pacmans:
            res += str(pac)+";"+str(lig)+";"+str(col)+"\n"
        res += str(len(fantomes))+"\n"
        for fantome, lig, col in fantomes:
            res += str(fantome)+";"+str(lig)+";"+str(col)+"\n"
        return res

