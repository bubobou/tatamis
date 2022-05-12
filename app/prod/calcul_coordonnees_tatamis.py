import sys
import time
import datetime
import numpy as np

class Dispositions:
    "classe qui calcul les coordonnées des tatamis d'après les dimensions du dojo"

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
        "fonction qui créé une matrice de 0 de dimension H*W"
        room = np.zeros((self.H+2, self.W+2))
        room[0,:] = -1
        room[self.H+1,:] = -1
        room[:,0] = -1
        room[:,self.W+1] = -1
        return room


    def init_grille(self):
        grille = np.zeros((self.H, self.W),int)
        return grille

    def setTatami_rowscan(self,h,w,idx):
        '''
        Paramètres
        ----------
        (h,w) : La position courante d'exploration du dojo. h correspond au numéro de la ligne,
        w correspond au numéro de la colonne.
        idx   : le numéro d'identification du Tatami en courant de positionnement.

        Incrémentation: 
            Le nombre total de dispositions possibles (count :int).
            La liste contenant toutes les dispositions  (solutions : list)

        '''        
               
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
        if self.symetrie :
            self.solutions.append(self.room.copy())
            self.count = self.count + 1

        elif self.existe_symetrie(self.grille) :
            self.grilles.append(self.encode(self.grille))
            self.solutions.append(self.room.copy())
            self.count = self.count + 1
            

    def encode(self,grille):
        mot = ""
        for v in grille.flatten():
            mot += str(v)
        return mot

    def symetrie_verticale(self,grille):
        return grille[::-1]


    def symetrie_horizontale(self,grille):
        s = []
        for ligne in grille :
            symetrie = ligne[::-1]
            s.append(symetrie)
        return np.array(s)

    def existe_symetrie(self,grille):               
        grilleSymH = self.symetrie_horizontale(grille)
        motSymH = self.encode(grilleSymH)

        grilleSymV = self.symetrie_verticale(grille)
        motSymV = self.encode(grilleSymV)

        mot = self.encode(grille)

        return mot not in self.grilles and motSymH not in self.grilles and motSymV not in self.grilles  


    
    def listeTatamis(self):
        ''' fonction qui renvoie une liste de tatamis décrits par un dictionnaire contenant leur largeur, hauteur et position'''
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
