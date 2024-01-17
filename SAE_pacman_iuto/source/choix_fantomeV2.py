import plateau
import random
import joueur

dico_val = {'.': 3,'$': 50,'@': 50,'~': 50,'&': 100,'!': 50, 'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'A':20,'B':20,'C':20,'D':20,'E':20}



def somme(analyse):
    """donne une valeur numérique à l'analyse afin de prendre une décision un peu plus 'réfléchie'

        Args:
            analyse (dict): un dictionnaire {'objets','pacmans','fantomes'}, venant d'une analyse du plateau
        
        Returns:
            float: valeur de l'analyse
        """     
    somme = 0
    print(analyse)
    for cat in analyse:
        print(cat)
        if cat == "objets":
            for entity in analyse[cat]:
                print(entity)
                somme += (1/entity[0])*(dico_val[entity[1]]/5)

        for entity in analyse[cat]:
            somme += (1/entity[0])*dico_val[entity[1]]
    return somme   


def direction_j_fantome_pacmanV2(le_plateau,lejoueur):
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
        dico_analyse[direction] = plateau.analyse_plateau(le_plateau,joueur.get_pos_fantome(lejoueur),direction,5)

    choix = max(dico_analyse,key=somme)

    print(choix)
    if choix is None:                   #Pour éviter tout plantage, si il y a un problème ça choisi au hasard
        return random.choice("NESO") 
    else:
        return choix