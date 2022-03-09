
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
        

    def clickExiste(self):
        "fonction d'action sur le bouton Existe"
        
        # etape de validation pour traiter les cas des dimensions nulles ou vides
        if (self.longueurEdit.text()==""):
            longueur_dojo = 0
        else:
            longueur_dojo = int(self.longueurEdit.text())
        
        if (self.largeurEdit.text()==""):
            largeur_dojo = 0
        else:
            largeur_dojo = int(self.largeurEdit.text())
        
        if (longueur_dojo==0) or (largeur_dojo==0):
            messageErreur = QMessageBox()
            messageErreur.setIcon(QMessageBox.Warning)
            messageErreur.setText("Erreur de saisie des dimensions")
            messageErreur.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
            messageErreur.setStandardButtons(QMessageBox.Ok)
            messageErreur.exec()
        
        # affichage de la reponse a l'utilisateur
        else:
            self.nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)
            
            if  self.nombre_disposition  :
                textboxValue = "Il existe au moins une disposition avec des tatamis 2x1 pour ce dojo"
            else:
                textboxValue = "Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"
        
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText("Existe-t-il une disposition pour le dojo?")
            message.setInformativeText(textboxValue)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()

        
    def clickNbDispositions(self):
        "fonction d'action sur le bouton Nombre de dispositions"
        
        # etape de validation pour traiter les cas des dimensions nulles ou vides
        if (self.longueurEdit.text()==""):
            longueur_dojo = 0
        else:
            longueur_dojo = int(self.longueurEdit.text())
        
        if (self.largeurEdit.text()==""):
            largeur_dojo = 0
        else:
            largeur_dojo = int(self.largeurEdit.text())
        
        if (longueur_dojo==0) or (largeur_dojo==0):
            messageErreur = QMessageBox()
            messageErreur.setIcon(QMessageBox.Warning)
            messageErreur.setText("Erreur de saisie des dimensions")
            messageErreur.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
            messageErreur.setStandardButtons(QMessageBox.Ok)
            messageErreur.exec()
         
        # affichage de la reponse a l'utilisateur
        else:
            self.nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)
            
            if self.nombre_disposition in (0,1):
                textboxValue = f"Il existe {self.nombre_disposition} disposition possible"
            else :
                textboxValue = f"Il existe {self.nombre_disposition} dispositions possibles"
                         
            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText("Connaître le nombre de dispositions possibles")
            message.setInformativeText(textboxValue)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()


    def clickNbTatamis(self):
        "fonction d'action sur le bouton Nombre de tatamis"
        
        # etape de validation pour traiter les cas des dimensions nulles ou vides
        if (self.longueurEdit.text()==""):
            longueur_dojo = 0
        else:
            longueur_dojo = int(self.longueurEdit.text())
        
        if (self.largeurEdit.text()==""):
            largeur_dojo = 0
        else:
            largeur_dojo = int(self.largeurEdit.text())
        
        if (longueur_dojo==0) or (largeur_dojo==0):
            messageErreur = QMessageBox()
            messageErreur.setIcon(QMessageBox.Warning)
            messageErreur.setText("Erreur de saisie des dimensions")
            messageErreur.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
            messageErreur.setStandardButtons(QMessageBox.Ok)
            messageErreur.exec()
        
        # affichage de la reponse a l'utilisateur
        else:
            self.nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)
                
            if  (self.nombre_disposition==0):
            
                textboxValue = "Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"
        
                message = QMessageBox()
                message.setIcon(QMessageBox.Warning)
                message.setText("Demande impossible")
                message.setInformativeText(textboxValue)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
            else:
                self.nombre_tatamis = nombre_tatamis(largeur_dojo, longueur_dojo)
                 
                textboxValue = f"Le nombre de tatamis 2x1 nécessaires pour ce dojo est : {self.nombre_tatamis}"
                 
                message = QMessageBox()
                message.setIcon(QMessageBox.Information)
                message.setText("Connaître le nombre de tatamis 2x1 nécessaires pour la taille du dojo")
                message.setInformativeText(textboxValue)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
            
            
    def clickUneDisposition(self):
        "fonction d'action sur le bouton afficher une disposition"
        
        # etape de validation pour traiter les cas des dimensions nulles ou vides
        if (self.longueurEdit.text()==""):
            longueur_dojo = 0
        else:
            longueur_dojo = int(self.longueurEdit.text())
        
        if (self.largeurEdit.text()==""):
            largeur_dojo = 0
        else:
            largeur_dojo = int(self.largeurEdit.text())
        
        if (longueur_dojo==0) or (largeur_dojo==0):
            messageErreur = QMessageBox()
            messageErreur.setIcon(QMessageBox.Warning)
            messageErreur.setText("Erreur de saisie des dimensions")
            messageErreur.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
            messageErreur.setStandardButtons(QMessageBox.Ok)
            messageErreur.exec()
        
        # affichage de la reponse a l'utilisateur
        else:
            self.nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)
                
            if  (self.nombre_disposition==0):
            
                textboxValue = "Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"
        
                message = QMessageBox()
                message.setIcon(QMessageBox.Warning)
                message.setText("Demande impossible")
                message.setInformativeText(textboxValue)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
            else:
                dlg = FenetreDojos(largeur_dojo,longueur_dojo,False)            
                dlg.exec()
   
        
    def clickToutesDispositions(self):
        "fonction d'action sur le bouton afficher toutes les dispositions"
        
        # etape de validation pour traiter les cas des dimensions nulles ou vides
        if (self.longueurEdit.text()==""):
            longueur_dojo = 0
        else:
            longueur_dojo = int(self.longueurEdit.text())
        
        if (self.largeurEdit.text()==""):
            largeur_dojo = 0
        else:
            largeur_dojo = int(self.largeurEdit.text())
        
        if (longueur_dojo==0) or (largeur_dojo==0):
            messageErreur = QMessageBox()
            messageErreur.setIcon(QMessageBox.Warning)
            messageErreur.setText("Erreur de saisie des dimensions")
            messageErreur.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
            messageErreur.setStandardButtons(QMessageBox.Ok)
            messageErreur.exec()
        
        # affichage de la reponse a l'utilisateur
        else:
            self.nombre_disposition = nombre_de_dispositions(largeur_dojo, longueur_dojo)
                
            if  (self.nombre_disposition==0):
            
                textboxValue = "Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo"
        
                message = QMessageBox()
                message.setIcon(QMessageBox.Warning)
                message.setText("Demande impossible")
                message.setInformativeText(textboxValue)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
            else:
                dlg = FenetreDojos(largeur_dojo,longueur_dojo,True)            
                dlg.exec()


def main():
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()

