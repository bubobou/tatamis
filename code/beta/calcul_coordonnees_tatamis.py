import sys
import time
import datetime
import numpy as np

class Dispositions:
    """La classe Dispositions permet d'obtenir les coordonnées possibles des tatamis d'après les dimensions du dojo
    
    Paramètres
    ----------
    H : int
        Longueur du dojo
    W : int
        Largeur du dojo

    Attributs
    ---------
    H : int
        Longueur du dojo
    W : int
        Largeur du dojo
    count : int
        Nombre de dispositions possibles
    room : list of list of int
        Matrice modélisant l'état de pavage du dojo
    coordonnes : list of dict
        Liste contenant les cacatéristiques des tatamis pour une disposition possible

    Méthodes
    --------
    init_room
    setTatami_rowscan
    listeTatamis   
    
    """

    def __init__(self, H, W):
        if H < W :
            self.H = H
            self.W = W
        else :
            self.H = W
            self.W = H
      
        self.count = 0 
        self.solutions=[]
        self.room=self.init_room()        
                
        self.coordonnees=self.listeTatamis()

    def init_room(self):
        "fonction qui créé une matrice de 0 de dimension H*W"
        room = np.zeros((self.H+2, self.W+2))
        room[0,:] = -1
        room[self.H+1,:] = -1
        room[:,0] = -1
        room[:,self.W+1] = -1
        return room

    def setTatami_rowscan(self,h,w,idx)->int:
        '''
        Fonction parcourant récursivement la matrice représentant le dojo et paçant les tatamis lorsque cela est possible

        Paramètres
        ----------
        (h,w) : La position courante d'exploration du dojo. h correspond au numéro de la ligne,
        w correspond au numéro de la colonne.
        idx   : le numéro d'identification du Tatami en courant de positionnement.

        Incrémente
        ---------- 
        Le nombre total de dispositions possibles (count :int).

        Modifie
        -------
        La liste contenant toutes les dispositions  (solutions : list)

        '''        
               
        if   h == self.H + 1:
            self.count = self.count + 1        
            self.solutions.append(self.room.copy())
            
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
                self.setTatami_rowscan(h, w+1, idx+1)        
                self.room[h,w]   = 0
                self.room[h+1,w] = 0

    
    def listeTatamis(self):
        """ fonction qui renvoie une liste de tatamis décrits par un dictionnaire contenant leur largeur, hauteur et position

        retourne
        --------
        liste de liste de dictionnaire
                Vide si aucune disposition n'est trouvée
            
        """
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
  