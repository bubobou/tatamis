from denombrement import nombre_de_dispositions
from interface import *

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
    

def multiples(nombre: int, ratio : int, mini=2) ->list :
    """Fonction qui extrait les couples de multiples d'un entier, avec une valeur de multiple minimale et un ratio à respecter
    
        Paramètres :
            nombre (int) : l'entier dont il faut extraire les multiples

            mini (int) : le multiple minimal

            ratio (int) : le ratio à ne pas excéder entre les deux multiples

        Return :
            resultat (list) : une liste de couple (tuple) de multiples
    """
    resultat = []
    for w in range(mini, nombre//mini) :
        h = nombre//w
        if w*h == nombre and verif_ratio(h,w,ratio):
            resultat.append((h,w))
        
    return resultat

def verif_ratio(h,w, ratio) -> bool:
    """Fonction qui vérifie si le quotient entre deux entier n'excède un ratio donné"""
    return h/w < ratio and w/h < ratio

def recherche_dimensions(nombreTatamis : int, ratio=3, rendement=0.75 ) -> list:
    """Fonction qui recherche les dimensions possibles pour un dojo état donné un nombre de tatamis
    
        Paramètres :
            nombreTatamis (int) : le nombre de tatamis donné

            ratio (int) : la valeur maximale du quotient entre la longueur et largeur

            rendement (float) : le taux d'utilisation minimale de tatamis par rapport au nombre donné

        Return :
            dimensionsPossibles (list) : tableau des couples (longueur, largeur) permettant un pavage du dojo 
            avec le nombre de tatamis donné et les contraintes imposées 
    """
    aire_max = nombreTatamis*2
    aire = aire_max
    dimensionsPossibles = []
    while aire > aire_max*rendement :
        listDimensions = multiples(aire, ratio)
        if len(listDimensions) != 0:
            for longueur, largeur in listDimensions :
                if nombre_de_dispositions(longueur, largeur) and ((largeur, longueur) not in dimensionsPossibles):
                    dimensionsPossibles.append((longueur, largeur))
        aire -=1
    return dimensionsPossibles


### Symetrie ###

def nombre_dispo_uniques(w,h):
    """Fonction qui dénombre les dispositions de tatamis sans symétrique"""
    return Dispositions(w, h, False).count

### Interface ###

def affichage_dimension(dispositions):
    """Fonction qui créée une chaîne de caractère pour affichage dans une fenêtre"""
    affichage = ""
    for h,w in dispositions :
        affichage += f"{h} x {w} \n"
    return affichage

### Largeur dimension max ###

def dimension_max(W,H):
    """Fonction qui retourne deux paramètres de tel sorte que le premier soit toujours supérieur au second """
    if W < H :
        W, H = H, W
    return W,H
            
def main():
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()