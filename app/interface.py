from alpha import *


def non_entier(dim):
    "retourne vrai si l'argument ne peut être convertit en entier"    
    try :
        int(dim)
    except ValueError as e:
        print("Erreur : vous n'avez pas entré un nombre entier")
        return True
    return False

def demande(dimension) :
    "retourne la dimension demandée en argument sous forme d'entier"
    assert type(dimension)==str
    
    dim = input(f"Entrez la {dimension} (entière) de votre dojo : ")
    while non_entier(dim
        dim = input(f"Entrez la {dimension} (entière) de votre dojo : ")
    return int(dim)

nombre_disposition = nombre_de_dispositions(demande("largeur"),demande("longueur"))

if  nombre_disposition  :
    print("Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo")

else:
    print("Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo")

