
from calcul_nombre_dispositions import *

def recherche_disposition_max(r :int, s :int) -> tuple:
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
    

def multiples(nombre: int,mini=2) ->list :
    '''
    Retourne une liste contenant les couples de multiples d'un nombre, avec une valeur de facteur minimale
    '''
    resultat = []
    for w in range(mini, nombre//mini) :
        h = nombre//w
        if w*h == nombre :
            resultat.append((h,w))
        
    return resultat


def multiples_inf(nombre,ratio=3,rendement=0.75) :
    facteurs = []
    nb = nombre    
    while nb > 3 :
        resultat = multiples(nb)
        if len(resultat) != 0:
            for h,w in resultat :
                if h/w < ratio and w/h < ratio and w*h > rendement*nombre:
                    facteurs.append((h,w))
        nb -= 1              
    return facteurs


def recherche_disposition(nombre):
    aire = nombre*2
    dimensions = multiples_inf(aire)    
    dispositions = []
    for h,w in dimensions :
        dispositions.append(recherche_disposition_max(h,w))

    nb_disp = len(dispositions)-1 # élimination des doublons : à extraire dans une fonction

    for i in range(nb_disp,0,-1):
        tab = dispositions[:i]
        if ((dispositions[i][1],dispositions[i][0]) in tab) or (dispositions[i] in tab ) :
            dispositions.pop(i)

    return dispositions

# ### Interface ###

def affichage_dimension(dispositions):
    affichage = ""
    for h,w in dispositions :
        affichage += f"{h} x {w} \n"
    return affichage


   
# def affichage_solution():
#     """Propose l'affichage du nombre de solutions et du nombre de tatamis nécessaires"""
#     aff_nombre = input("Souhaitez-vous connaître le nombre de dispositions ? O->Oui")
#     if aff_nombre.upper() != "O":
#         exit()
#     else:    
#         print(f"Il existe {nombre_disposition} disposition(s) possible(s)")
#         print(f"Le nombre de tatamis 2x1 utilisables pour ce dojo est : {nombre_tatamis(largeur_dojo,longueur_dojo)} ")

# def affichage_solution_alt():
#     """Propose d'afficher une solution alternative de dimensions moindre et le nombre de tatamis correspondant"""
#     aff_autre = input("Souhaitez-vous connaître le nombre de dispositions avec des dimensions plus petites? O->Oui")
#     if aff_autre.upper() != "O":
#         exit()
#     else:
#         largeur_max,longueur_max=recherche_disposition_max(largeur_dojo,longueur_dojo)
#         nombre_disposition = nombre_de_dispositions(largeur_max, longueur_max)
#         print(f"Il existe {nombre_disposition} disposition(s) possible(s) avec les dimensions : {largeur_max}x{longueur_max}")
#         print(f"Le nombre de tatamis 2x1 utilisables pour ce dojo est :{nombre_tatamis(largeur_max,longueur_max)}" )

