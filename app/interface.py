from alpha import *

def non_entier(dim : str) -> bool:
    "retourne vrai si l'argument ne peut être convertit en entier"    
    try :
        int(dim)
    except ValueError as e:        
        return True
    return False

def demande(dimension : str) -> int:
    "retourne la dimension demandée en argument sous forme d'entier"
    assert type(dimension)==str    
    dim = input(f"Entrez la {dimension} (entière) de votre dojo : ")
    while non_entier(dim):
        print("Erreur : vous n'avez pas entré un nombre entier")
        dim = input(f"Entrez la {dimension} (entière) de votre dojo : ")
    return int(dim)

def reponse_existe_disposition(nombre_disposition: int) -> str:
    "retourne la réponse à la question de savoir s'il existe au moins une disposition"
    if  nombre_disposition  :
        return "Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo"
    else:
        return "Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"

def reponse_nombre_disposition(nombre_disposition: int) -> str:
    "retourne la réponse à la question de savoir combien il existe de disposition"
    if nombre_disposition in (0,1):
        return f"Il existe {nombre_disposition} disposition possible"
    else :
        return f"Il existe {nombre_disposition} dispositions possibles"

def reponse_nombre_tatamis(largeur_dojo : int, longueur_dojo : int) -> str:
    "retourne la réponse à la question de savoir combien de tatamis sont nécessaires"    
    return f"Le nombre de tatamis 2x1 necessaires pour ce dojo est : {nombre_tatamis(largeur_dojo, longueur_dojo)}"  


def choix_fonctionnalite() -> str:
    "propose 3 fonctionnalité à l'utilisateur et retourne le numéro choisi"
    question = """Que cherchez vous? Entrez : 
    \n1 pour savoir si il existe une disposition pour le dojo; 
    \n2 pour connaître le nombre de dispositions possibles; 
    \n3 pour connaître le nombre de tatamis 2x1 nécéssaires pour la taille du dojo
    \nune autre touche pour sortir du programme
    \n ? """
    choix = input(question)
    return choix


def main() :
    largeur_dojo = demande("largeur")
    longueur_dojo = demande("longueur")
    nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)
    choix = choix_fonctionnalite()
    while choix in ("1","2","3"):
        if choix == "1":
            print(reponse_existe_disposition(nombre_disposition))
            choix = choix_fonctionnalite()
        elif choix == "2":
            print(reponse_nombre_disposition(nombre_disposition))
            choix = choix_fonctionnalite()
        elif choix == "3" and nombre_disposition :
            print(reponse_nombre_tatamis(largeur_dojo, longueur_dojo))
            choix = choix_fonctionnalite()
        else :
            print(reponse_existe_disposition(nombre_disposition))
            return
    return

if __name__ == '__main__':
    main()

