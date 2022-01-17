#fonction de calcul du nombre de dispositions
def eq(x,y):    
    if x==y:
        return 1
    else:
        return 0

def c(r,s):    
    if s<0:
        return 0
    elif r==1:
        return 1-(s % 2)
    elif r==2:
        return c1(2,s) + c2(2,s) + eq(s,0)
    elif (r % 2) == 0: #even
        return c1(r,s) + c2(r,s) + eq(s,0)
    else:
        return c(r,s-r+1) + c(r,s-r-1) + eq(s,0)
        
        
def c1(r,s):    
    if s<=0:
        return 0
    elif r==2:
        return c(2,s-1)
    else:
        return c2(r,s-1) + eq(s,1)
    
    
def c2(r,s):    
    if s<=0:
        return 0
    elif r==2:
        return c1(2,s-2) + eq(s,2)
    else:
        return c1(r,s-r+2) + c1(r,s-r) + eq(s,r-2) + eq(s,r)
        
        
def nombre_de_dispositions(r,s):
    if r>s:
        return nombre_de_dispositions(s,r)
    elif (((r % 2) != 0) and (r>1)):
        return 2*c(r,s)
    else:
        return c(r,s)

#fonction de calcul du nombre de tatami 2*1 necessaires
def nombre_de_tatamis_necessaires (r,s):
    if nombre_de_dispositions(r, s)>0:
        return (r*s/2)
    else:
        return("Aucune disposition possible de tatamis 2x1 pour ce dojo")

#interaction utilisateur
largeur_dojo = int(input('Entrez la largeur (relative) de votre dojo : '))
longueur_dojo = int(input('Entrez la longueur (relative) de votre dojo : '))
choix_fonctionalite = int(input('Que cherchez vous? Entrez 1 pour savoir si il existe une disposition pour le dojo; 2 pour savoir le nombre de dispositions possibles; 3 pour savoir le nombre de tatamis 2x1 nécéssaire pour la taille du dojo'))

if choix_fonctionalite == 1:
    if nombre_de_dispositions(largeur_dojo, longueur_dojo) == 0:
        print('Il n existe pas de disposition possible avec des tatamis 2x1 pour ce dojo')
    else:
        print('Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo')
elif choix_fonctionalite ==2:
    nombre_dispositions = nombre_de_dispositions(largeur_dojo,longueur_dojo)
    print('Il existe ',nombre_de_dispositions(largeur_dojo,longueur_dojo), 'disposition(s) possibles')    
elif choix_fonctionalite==3:
    print('Le nombre de tatamis 2x1 necessaires pour ce dojo est :', nombre_de_tatamis_necessaires(largeur_dojo,longueur_dojo))  
else:
    print('Erreur - merci d entrer un choix entre 1 et 3')



