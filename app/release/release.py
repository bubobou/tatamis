
from calcul_nombre_dispositions import *

def recherche_disposition_max(r :int, s :int) -> set:
    """Retourne un set contenant les plus grandes largeur et longueur permettant d'obtenir
     au moins un pavage tatamis-parfait"""
    r_max = r
    s_max = s
    while nombre_de_dispositions(r_max,s_max) == 0 :
        if (r_max - 1)*s_max > r_max*(s_max-1):
            r_max -= 1 
        else :
            s_max -= 1
    return (r_max, s_max)


def nombre_tatamis_max(largeur_dojo:int,longueur_dojo:int) -> int:
    """Retourne le nombre de tatamis nécessaires pour réaliser un pavage 
    tatamis-parfait dans un rectangle de dimensions largeur * longueur"""
    largeur,longueur = recherche_disposition_max(largeur_dojo,longueur_dojo)
    return nombre_tatamis(largeur,longueur)
    

def multiples(nombre: int) ->list :
    '''
    Retourne une liste contenant les couples de multiples d'un nombre, avec une valeur minimale de 3 pour un élément
    '''
    res = []
    mini = 2
    for w in range(1, nombre//mini) :
        h = nombre//w
        if w*h == nombre and (w,h) not in res :
            res.append(h,w)
    return res

def multiples_alternatifs(nombre) :
    res = multiples(nombre)
    while len(res)==0 and nombre > 3:
        nombre =-1
    return res

    
### Interface ###


   
def affichage_solution():
    """Propose l'affichage du nombre de solutions et du nombre de tatamis nécessaires"""
    aff_nombre = input("Souhaitez-vous connaître le nombre de dispositions ? O->Oui")
    if aff_nombre.upper() != "O":
        exit()
    else:    
        print(f"Il existe {nombre_disposition} disposition(s) possible(s)")
        print(f"Le nombre de tatamis 2x1 utilisables pour ce dojo est : {nombre_tatamis(largeur_dojo,longueur_dojo)} ")

def affichage_solution_alt():
    """Propose d'afficher une solution alternative de dimensions moindre et le nombre de tatamis correspondant"""
    aff_autre = input("Souhaitez-vous connaître le nombre de dispositions avec des dimensions plus petites? O->Oui")
    if aff_autre.upper() != "O":
        exit()
    else:
        largeur_max,longueur_max=recherche_disposition_max(largeur_dojo,longueur_dojo)
        nombre_disposition = nombre_de_dispositions(largeur_max, longueur_max)
        print(f"Il existe {nombre_disposition} disposition(s) possible(s) avec les dimensions : {largeur_max}x{longueur_max}")
        print(f"Le nombre de tatamis 2x1 utilisables pour ce dojo est :{nombre_tatamis(largeur_max,longueur_max)}" )

