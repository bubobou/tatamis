import sys
import time
import datetime
import numpy as np

class Dispositions:
    """Classe qui modélise un dojo et permet de caractériser les solutions de pavage tatamis-parfait

        Attributs:
            (H : int) : la hauteur du dojo

            (W : int) : la largeur du dojo

            (count : int) : le nombre de dispositions possibles

            (solution : list) : liste contenant les dispositions (room) satisfaisant le pavage tatamis-parfait

            (room : np.array) : matrice modélisant le placement des tatamis avec leur numéro

            (grille : np.array) : grille modélisant le placement des tatamis d'après leur position horizontale ou verticale

            (coordonnees : list) : liste des dictionnaires décrivant les caractéristiques des tatamis de chaque solution
    """

    def __init__(self, H, W, symetrie=True):
        
        self.H = H
        self.W = W
      
        self.count = 0 
        self.solutions=[]
        self.symetrie = symetrie
        self.room=self.init_room() 
        self.grille=self.init_grille()
        self.grilles=[]       
                
        self.coordonnees=self.listeTatamis()

    def init_room(self):
        "Fonction qui créé une matrice de 0 de dimension H*W, bordée par le nombre '-1' à ses extrémités"
        room = np.zeros((self.H+2, self.W+2))
        room[0,:] = -1
        room[self.H+1,:] = -1
        room[:,0] = -1
        room[:,self.W+1] = -1
        return room


    def init_grille(self):
        "Fonction qui créé une matrice de 0 de dimension H*W"
        grille = np.zeros((self.H, self.W),int)
        return grille

    def setTatami_rowscan(self,h:int,w:int,idx:int):
        """Fonction qui parcours la grille modélisant le tatami et qui vérifie si un tatami peut être déposé

            Paramètres:
                (h :int),(w :int) : les coordonnées de la position courante d'exploration de la grille. h correspond au numéro de la ligne,
                w correspond au numéro de la colonne.

                (idx :int)  : le numéro d'identification du Tatami en courant de positionnement.
        """     
               
        if   h == self.H + 1:
            self.add_room()
            # self.count = self.count + 1        
            # self.solutions.append(self.room.copy())
            
        elif w == self.W + 1: 
            # Reach the right boundary, go to explore the next row from the left 
            self.setTatami_rowscan(h+1, 1, idx)
        elif self.room[h,w] > 0: 
            # This grid has been occupied, move to the right one
            self.setTatami_rowscan(h, w+1, idx)
        elif self.room[h-1,w]==self.room[h-1,w-1] or self.room[h,w-1]==self.room[h-1,w-1]:
            # if (the same IDX for up and left-up) or (the same IDX for left and left-up), 
            # Tatami arrangement is allowed.
            if self.room[h,w+1]==0: 
                # Horizontal arrangement is allowed
                self.room[h,w]   = idx
                self.room[h,w+1] = idx
                        
                self.setTatami_rowscan(h, w+2, idx+1)            
                self.room[h,w]   = 0
                self.room[h,w+1] = 0  
            if self.room[h+1,w]==0:
                # Vertical arrangement is allowed
                self.room[h,w]   = idx
                self.room[h+1,w] = idx
                self.grille[h-1,w-1] = 1  
                self.grille[h,w-1] = 1             
                self.setTatami_rowscan(h, w+1, idx+1)        
                self.room[h,w]   = 0
                self.room[h+1,w] = 0
                self.grille[h-1,w-1] = 0 
                self.grille[h,w-1] = 0

    def add_room(self):
        """Fonction qui ajoute une solution de pavage à la liste des solutions """
        if self.symetrie :
            self.solutions.append(self.room.copy())
            self.count = self.count + 1

        elif self.verifie_symetrie(self.grille) :
            self.grilles.append(self.encode(self.grille))
            self.solutions.append(self.room.copy())
            self.count = self.count + 1
            

    def encode(self,grille):
        """Fonction réduisant une matrice n x n en chaîne de caractères

            Paramètre :
                (grille : np.array) : matrice modélisant une solution de pavage

            Return :
                (mot : Str) : chaîne de caractères contenant les valeurs de la matrice 'grille' ordonnées par colonne puis par ligne
        """
        mot = ""
        for value in grille.flatten():
            mot += str(value)
        return mot

    def symetrie_verticale(self,grille):
        """Fonction qui réalise une symétrie verticale de la grille passée en paramètre

            Paramètre :
                (grille : np.array) : matrice modélisant une solution de pavage

            Return :
                (np.array) : matrice modélisant une solution de pavage
        """
        return grille[::-1]


    def symetrie_horizontale(self,grille):
        """Fonction qui réalise une symétrie horizontale de la grille passée en paramètre

            Paramètre:
                (grille : np.array) : matrice modélisant une solution de pavage

            Return :
                (np.array) : matrice modélisant une solution de pavage
        """
        s = []
        for ligne in grille :
            symetrie = ligne[::-1]
            s.append(symetrie)
        return np.array(s)

    def verifie_symetrie(self,grille) -> bool:
        """Fonction qui vérifie si une grille symétrique à la grille passée en paramètre n'a pas déjà été répertoriée parmi les grilles déjà validées

            Paramètre :
                (grille: np.array) : solution de pavage du dojo

            Return :
                (Bool) : True si un symétrique de la grille n'a pas été répertorié, False sinon
        """               
        grilleSymH = self.symetrie_horizontale(grille)
        motSymH = self.encode(grilleSymH)

        grilleSymV = self.symetrie_verticale(grille)
        motSymV = self.encode(grilleSymV)

        mot = self.encode(grille)

        return mot not in self.grilles and motSymH not in self.grilles and motSymV not in self.grilles  


    
    def listeTatamis(self) -> list:
        """Fonction qui renvoie une liste de tatamis décrits par un dictionnaire contenant leur largeur, hauteur et position"""
        self.setTatami_rowscan(1,1,1) 
        dispositions=[]
        for array in self.solutions :
            tatamis = []    
            for i in range(1,self.H+1):
                for j in range(1, self.W+1):
                    if array[i,j]==array[i,j+1]:
                        tatamis.append(dict(id=int(array[i,j]),x=j-1,y=i-1,largeur=2,hauteur=1))
                    elif array[i,j]==array[i+1,j]:
                        tatamis.append(dict(id=int(array[i,j]),x=j-1,y=i-1,largeur=1,hauteur=2))
            dispositions.append(tatamis)
        return dispositions
    
# décommenter les lignes pour tester la classe Disposition

# tStart = time.perf_counter()
# disp=Dispositions(20,19)
# tCost  = time.perf_counter() - tStart
# print('count = {0}, tCost = {1:6.3f}(sec)'.format(disp.count,tCost))
