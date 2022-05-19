
from calcul_nombre_dispositions import *
from calcul_coordonnees_tatamis import *

def recherche_disposition_max(r :int, s :int) -> tuple:
    """Retourne un tuple contenant les plus grandes largeur et longueur permettant d'obtenir
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
    """Fonction qui extrait les couples de multiples d'un entier, avec une valeur de multiple minimale 
    
        Paramètres :
            nombre (int) : l'entier dont il faut extraire les multiples

            mini (int) : le multiple minimal

        Return :
            resultat (list) : une liste de couple (tuple) de multiples
    """
    resultat = []
    for w in range(mini, nombre//mini) :
        h = nombre//w
        if w*h == nombre :
            resultat.append((h,w))
        
    return resultat


def multiples_inf(nombre,ratio=3,rendement=0.75) :
    """Fonction qui sélectionne les multiples d'entiers inférieurs à un entier selon un critère de ratio et de rendement
        
        Paramètres :
            nombre (int) : l'entier dont il faut extraire les multiples

            ratio (int) : le ratio maximal entre les multiples

            rendement (float) : la proportion minimale que représente le produit des multiples par rapport à l'entier "nombre"

        Return :
            resultat (list) : une liste de couple (tuple) de multiples
    """
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


def recherche_disposition(nombre: int) -> list:
    aire = nombre*2
    dimensions = multiples_inf(aire)    
    dispositions = []

    #%TODO  refactoring du reste de la fonction
    for h,w in dimensions :
        dispositions.append(recherche_disposition_max(h,w))

    nb_disp = len(dispositions)-1 # élimination des doublons : à extraire dans une fonction

    for i in range(nb_disp,0,-1):
        tab = dispositions[:i]
        if ((dispositions[i][1],dispositions[i][0]) in tab) or (dispositions[i] in tab ) :
            dispositions.pop(i)

    return dispositions


### Symetrie ###

def nombre_dispo_uniques(w,h):
    return Dispositions(w, h, False).count

### Interface ###

def affichage_dimension(dispositions):
    affichage = ""
    for h,w in dispositions :
        affichage += f"{h} x {w} \n"
    return affichage

### Largeur dimension max ###

def dimension_max(W,H):
    if W < H :
        W, H = H, W
    return W,H
            

