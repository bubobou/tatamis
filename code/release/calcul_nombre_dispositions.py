               
def nombre_de_dispositions(r :int, s : int) -> int:
    "Retourne le nombre de pavage tatamis-parfait réalisable(s) dans un rectangle r*s"
    if r>s:
        return nombre_de_dispositions(s,r)
    elif (((r % 2) != 0) and (r>1)):
        return 2*combinaison(r,s)
    else:
        return combinaison(r,s)

    
def eq(x:int,y:int) -> int:    
    if x==y:
        return 1
    else:
        return 0

def combinaison(r:int,s:int) -> int:    
    if s<0:
        return 0
    elif r==1:
        return 1-(s % 2)
    elif r==2:
        return combinaison1(2,s) + combinaison2(2,s) + eq(s,0)
    elif (r % 2) == 0: #even
        return combinaison1(r,s) + combinaison2(r,s) + eq(s,0)
    else:
        return combinaison(r,s-r+1) + combinaison(r,s-r-1) + eq(s,0)
           
def combinaison1(r:int,s:int) -> int:    
    if s<=0:
        return 0
    elif r==2:
        return combinaison(2,s-1)
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

