from alpha import *

   
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


largeur_dojo = int(input('Entrez la largeur (relative) de votre dojo : '))
longueur_dojo = int(input('Entrez la longueur (relative) de votre dojo : '))

nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)

if  nombre_disposition !=0 :
    print("Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo")
    affichage_solution()  
else:
    print("Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo")
    affichage_solution_alt()
