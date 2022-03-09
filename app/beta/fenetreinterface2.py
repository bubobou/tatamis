
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 23:18:59 2022

@author: benoitanger
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QGridLayout, QMessageBox
from PyQt5.QtGui import QIntValidator
from calcul_nombre_dispositions import *
from fenetre_dojos import *

class MessageSaisieInvalide(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Erreur de saisie des dimensions")
        self.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
        self.setStandardButtons(QMessageBox.Ok)

class MessageDemandeImpossible(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Demande impossible")
        self.setInformativeText("Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo")
        self.setStandardButtons(QMessageBox.Ok)

class MessageInfo(QMessageBox):
    def __init__(self,question,info):
        super().__init__()
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText(question)
        self.setInformativeText(info)
        self.setStandardButtons(QMessageBox.Ok)
        

class Interface(QWidget):
    "Classe qui cree l'interface"
    
    def __init__(self):
        
        super().__init__()

        self.initialisationUI()

    def initialisationUI(self):
        "fonction d'initialisation de l'interface"
        
        self.resize(600,350)
        self.setWindowTitle('Super Dojo Calculator')

        
        # champs de dimensions
        longueur = QLabel('Longueur (en nombre de tatamis entre 1 et 25)')
        largeur = QLabel('Largeur (en nombre de tatamis entre 1 et 25)')

        # choix des limites de validation des saisies de dimension
        validator = QIntValidator(1, 25, self)

        # saisie des dimensions
        self.longueurEdit = QLineEdit(self)
        self.largeurEdit = QLineEdit(self)
        
        # validation des dimensions
        self.longueurEdit.setValidator(validator)
        self.largeurEdit.setValidator(validator)

        
        # mise en place d'une grille pour faciliter le placements des objets
        grid = QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(longueur, 2, 0)
        grid.addWidget(self.longueurEdit, 2, 1)


        grid.addWidget(largeur, 3, 0)
        grid.addWidget(self.largeurEdit, 3, 1)

        # mise en place de texte pour faciliter la comprehension
        textDimension = QLabel('Entrez la dimension de votre dojo:', self)
        grid.addWidget(textDimension, 1, 0)
        
        textFonctionalite = QLabel('Que cherchez vous?', self)
        grid.addWidget(textFonctionalite, 4, 0)

        # creation des boutons
        boutonFonctionaliteExiste = QPushButton("Savoir si il existe une disposition pour le dojo")
        boutonFonctionaliteNbDispositions = QPushButton("Connaître le nombre de dispositions possibles")
        boutonFonctionaliteNbTatamis = QPushButton("Connaître le nombre de tatamis 2x1 nécessaires pour la taille du dojo")
        boutonFonctionaliteUneDisposition = QPushButton("Afficher une disposition")
        boutonFonctionaliteToutesDispositions = QPushButton("Afficher toutes les dispositions possibles")
        
        # placement des boutons
        grid.addWidget(boutonFonctionaliteExiste, 5, 1)
        grid.addWidget(boutonFonctionaliteNbDispositions, 6, 1)
        grid.addWidget(boutonFonctionaliteNbTatamis, 6, 2)
        grid.addWidget(boutonFonctionaliteUneDisposition, 7, 1)
        grid.addWidget(boutonFonctionaliteToutesDispositions, 7, 2)

        # connecter les boutons
        boutonFonctionaliteExiste.clicked.connect(self.clickExiste)
        boutonFonctionaliteNbDispositions.clicked.connect(self.clickNbDispositions)
        boutonFonctionaliteNbTatamis.clicked.connect(self.clickNbTatamis)
        boutonFonctionaliteUneDisposition.clicked.connect(self.clickUneDisposition)
        boutonFonctionaliteToutesDispositions.clicked.connect(self.clickToutesDispositions)

        # bouton supplementaire pour fermer
        boutonFermer = QPushButton("Fermer", self)
        boutonFermer.setToolTip("Fermer l'application")
        boutonFermer.clicked.connect(self.close)
        grid.addWidget(boutonFermer, 8, 4)

        
        self.setLayout(grid)
        self.show()

    def set_longueur(self) :
        "fonction qui affecte la longueur saisie en retournant 0 si celle-ci est vide"
        if (self.longueurEdit.text()==""):
            self.longueur_dojo = 0
        else:
            self.longueur_dojo = int(self.longueurEdit.text())

    def set_largeur(self) :
        "fonction qui affecte la largeur saisie en retournant 0 si celle-ci est vide"
        if (self.largeurEdit.text()==""):
            self.largeur_dojo = 0
        else:
            self.largeur_dojo = int(self.largeurEdit.text())

    def valeur_vide(self):
        "fonction qui vérifie si les valeurs saisies sont nulles"
        self.set_largeur()
        self.set_longueur()
        return self.largeur_dojo==0 or self.longueur_dojo==0    

    def clickExiste(self):
        "fonction d'action sur le bouton Existe"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalide()          
            message.exec()

        # affichage de la réponse a l'utilisateur
        else:
            if nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
                info = "Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo"
            else:
                info = "Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"
                                  
            message = MessageInfo("Existe-t-il une disposition pour le dojo?",info)
            message.exec()

        
    def clickNbDispositions(self):
        "fonction d'action sur le bouton Nombre de dispositions"

        if self.valeur_vide() :
            message = MessageSaisieInvalide()          
            message.exec() 
        # affichage de la réponse a l'utilisateur
        else:
            nombre_disposition = nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo)
            
            if nombre_disposition in (0,1):
                info = f"Il existe {nombre_disposition} disposition possible"
            else :
                info = f"Il existe {nombre_disposition} dispositions possibles"
                         
            message = MessageInfo("Connaître le nombre de dispositions possibles",info)
            message.exec()


    def clickNbTatamis(self):
        "fonction d'action sur le bouton Nombre de tatamis"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalide()          
            message.exec()

        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo):
            info = f"Le nombre de tatamis 2x1 nécessaires pour ce dojo est : {nombre_tatamis(self.largeur_dojo, self.longueur_dojo)}"
            message = MessageInfo("Connaître le nombre de tatamis 2x1 nécessaires pour la taille du dojo",info)
            message.exec()

        else :
            message = MessageDemandeImpossible()             
            message.exec()       
        
        
    def clickUneDisposition(self):
        "fonction d'action sur le bouton afficher une disposition"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalide()            
            message.exec()

        # affichage de la réponse a l'utilisateur

        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
            fenetre = FenetreDojos(self.largeur_dojo,self.longueur_dojo,tous=False)            
            fenetre.exec()
        
        else:
            message = MessageDemandeImpossible()             
            message.exec()            
   
        
    def clickToutesDispositions(self):
        "fonction d'action sur le bouton afficher toutes les dispositions"
        if self.valeur_vide() :
            message = MessageSaisieInvalide()            
            message.exec()

        # affichage de la réponse a l'utilisateur
        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
            fenetre = FenetreDojos(self.largeur_dojo,self.longueur_dojo,tous=True)            
            fenetre.exec()

        else :
            message = MessageDemandeImpossible()                   
            message.exec()      


def main():
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()

