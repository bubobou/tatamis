               
def nombre_de_dispositions(r:int,s:int) -> int:
    "Retourne le nombre de pavage tatamis-parfait réalisable(s) dans un rectangle r*s"
    if r>s:
        return nombre_de_dispositions(s,r)
    elif (((r % 2) != 0) and (r>1)):
        return 2*c(r,s)
    else:
        return c(r,s)

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
    
def eq(x:int,y:int) -> int:    
    if x==y:
        return 1
    else:
        return 0

def c(r:int,s:int) -> int:    
    if s<0:
        return 0
    elif r==1:
        return 1-(s % 2)
    elif r==2:
        return combinaison1(2,s) + combinaison2(2,s) + eq(s,0)
    elif (r % 2) == 0: #even
        return combinaison1(r,s) + combinaison2(r,s) + eq(s,0)
    else:
        return c(r,s-r+1) + c(r,s-r-1) + eq(s,0)
           
def combinaison1(r:int,s:int) -> int:    
    if s<=0:
        return 0
    elif r==2:
        return c(2,s-1)
    else:
        return combinaison2(r,s-1) + eq(s,1)
       
def combinaison2(r:int,s:int) -> int:    
    if s<=0:
        return 0
    elif r==2:
        return combinaison1(2,s-2) + eq(s,2)
    else:
        return combinaison1(r,s-r+2) + combinaison1(r,s-r) + eq(s,r-2) + eq(s,r)

def nombre_tatamis(largeur :int,longueur :int) -> int:
    """Retourne le nombre de tatamis nécessaires pour paver un rectangle 
    de dimensions largeur* longueur"""
    return int(largeur*longueur/2)

def nombre_tatamis_max(largeur_dojo:int,longueur_dojo:int) -> int:
    """Retourne le nombre de tatamis nécessaires pour réaliser un pavage 
    tatamis-parfait dans un rectangle de dimensions largeur * longueur"""
    largeur,longueur = recherche_disposition_max(largeur_dojo,longueur_dojo)
    return nombre_tatamis(largeur,longueur)
    
