import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QGridLayout, QMessageBox, QFrame, QSpacerItem
from PyQt5.QtGui import * 
from calcul_nombre_dispositions import *
from dojo import *
from PyQt5 import QtCore
from prod import *


class MessageSaisieInvalide(QMessageBox):
    "classe qui affiche un message pour avertir que la saisie est invalide"
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Erreur de saisie des dimensions")
        self.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
        self.setStandardButtons(QMessageBox.Ok)
        self.setStyleSheet("background-color:#E27D60 ;color: black;padding: 4px;")

class MessageDemandeImpossible(QMessageBox):
    "classe qui affiche un message pour avertir qu'il n'existe pas de solutions"
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Demande impossible")
        self.setInformativeText("Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo")
        self.setStandardButtons(QMessageBox.Ok)
        self.setStyleSheet("background-color:#E8A87C ;color: black;padding: 4px;")

class MessageInfo(QMessageBox):
    "classe qui créée un message avec une question et une info passées en paramètres"
    def __init__(self,question,info):
        super().__init__()
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText(question)
        self.setInformativeText(info)
        self.setStandardButtons(QMessageBox.Ok)
        self.setStyleSheet("background-color:#F48289 ;color: white;padding: 4px;")
        

class Interface(QWidget):
    "Classe qui cree l'interface"
    
    def __init__(self):
        
        super().__init__()

        self.initialisationUI()

    def initialisationUI(self):
        "fonction d'initialisation de l'interface"
        
        # creation de la fenetre
        self.resize(900,150)
        self.setWindowTitle('*** Super Calculateur Dojo ***')
        
        # couleur de la fenetre
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor('#FAC2C1'))
        gradient.setColorAt(1.0, QColor('#87C1AF'))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        
        # texte des champs de saisie
        longueur = QLabel('Longueur (entre 1 et 25) :')
        longueur.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        largeur = QLabel('Largeur (entre 1 et 25) :')
        largeur.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        nbTatamisDispo = QLabel('Nombre de tatamis 2x1 disponibles (entre 3 et 300) :')        
        nbTatamisDispo.setAlignment(Qt.AlignVCenter | Qt.AlignRight)


        # determination des polices et tailles
        QFontDatabase.addApplicationFont("NexaBold.otf")
        QFontDatabase.addApplicationFont("NexaLight.otf")

        fontTitre = QFont("Nexa Bold", 14, QFont.Bold)
        fontTexte = QFont("Nexa Light",11)
        
        # style des textes des champs de saisie
        longueur.setFont(fontTexte)
        largeur.setFont(fontTexte)
        nbTatamisDispo.setFont(fontTexte)
        
        longueur.setStyleSheet("color: #274a3f")
        largeur.setStyleSheet("color: #274a3f")
        nbTatamisDispo.setStyleSheet("color: #274a3f")

        # choix des limites de validation des saisies de dimension et nombre de tatamis
        validatorDim = QIntValidator(1, 25, self)
        validatorNbTatamis = QIntValidator(1, 300, self)

        # saisie des dimensions et nombre de tatamis
        self.longueurEdit = QLineEdit(self)
        self.largeurEdit = QLineEdit(self)
        self.nbTatamisDispoEdit = QLineEdit(self)
        
        # couleur des saisies
        self.longueurEdit.setStyleSheet("color: white;  background-color: black")
        self.largeurEdit.setStyleSheet("color: white;  background-color: black")
        self.nbTatamisDispoEdit.setStyleSheet("color: white;  background-color: black")
        
        # validation des saisies
        self.longueurEdit.setValidator(validatorDim)
        self.largeurEdit.setValidator(validatorDim)
        self.nbTatamisDispoEdit.setValidator(validatorNbTatamis)

        
        # mise en place d'une grille pour faciliter le placements des objets
        grid = QGridLayout()
        grid.setSpacing(15)
        
        #placement des champs de saisie
        grid.addWidget(longueur, 0, 1)
        grid.addWidget(self.longueurEdit, 0, 2)


        grid.addWidget(largeur, 1, 1)
        grid.addWidget(self.largeurEdit, 1, 2)
        
        grid.addWidget(nbTatamisDispo, 10, 1)
        grid.addWidget(self.nbTatamisDispoEdit, 10, 2)

        # mise en place de texte pour faciliter la comprehension
        textDimension = QLabel("Entrez la dimension de votre dojo:\n (en valeur relative de tatamis standards 2x1)", self, alignment=QtCore.Qt.AlignCenter )
        textDimension.setFont(fontTitre)
        textDimension.setStyleSheet("border: 2px solid black;color: black; padding: 4px;")
        grid.addWidget(textDimension, 0, 0,3,1) 
        
        textFonctionaliteComprendre = QLabel('Comprendre', self,alignment=QtCore.Qt.AlignCenter)
        textFonctionaliteComprendre.setFont(fontTitre)
        textFonctionaliteComprendre.setStyleSheet("border: 2px solid black;color: black;padding: 4px;")
        grid.addWidget(textFonctionaliteComprendre, 3, 0,4,1)
        
        textFonctionalitePasDeSolutions = QLabel("En cas d'absence de solutions:", self,alignment=QtCore.Qt.AlignCenter)
        textFonctionalitePasDeSolutions.setFont(fontTexte)
        textFonctionalitePasDeSolutions.setStyleSheet("color: #274a3f")
        grid.addWidget(textFonctionalitePasDeSolutions, 5, 1,1,2)
        
        textFonctionaliteAfficher = QLabel('Afficher les dispositions', self,alignment=QtCore.Qt.AlignCenter)
        textFonctionaliteAfficher.setFont(fontTitre)
        textFonctionaliteAfficher.setStyleSheet("border: 2px solid black;color: black;padding: 4px;")
        grid.addWidget(textFonctionaliteAfficher, 7, 0,1,1)

        textFonctionaliteAfficher = QLabel('Comprendre et afficher en excluant les symétries', self,alignment=QtCore.Qt.AlignCenter)
        textFonctionaliteAfficher.setFont(fontTitre)
        textFonctionaliteAfficher.setStyleSheet("border: 2px solid black;color: black;padding: 4px;")
        grid.addWidget(textFonctionaliteAfficher, 8, 0,1,1)
        
        textFonctionaliteNbTatamis = QLabel("A partir d'un nombre de tatamis", self,alignment=QtCore.Qt.AlignCenter)
        textFonctionaliteNbTatamis.setFont(fontTitre)
        textFonctionaliteNbTatamis.setStyleSheet("border: 2px solid black;color: black;padding: 4px;")
        grid.addWidget(textFonctionaliteNbTatamis, 10, 0,2,1)

        # creation des boutons
        boutonFonctionaliteSurface = QPushButton("Afficher la surface du dojo")
        boutonFonctionaliteExiste = QPushButton("Savoir si il existe une disposition pour le dojo")
        boutonFonctionaliteNbDispositions = QPushButton("Connaître le nombre de dispositions possibles")
        boutonFonctionaliteNbTatamis = QPushButton("Connaître le nombre de tatamis 2x1 nécessaires pour la taille du dojo")
        boutonFonctionaliteUneDisposition = QPushButton("Afficher une disposition")
        boutonFonctionaliteToutesDispositions = QPushButton("Afficher toutes les dispositions possibles")
        boutonFonctionaliteSolutionAPartirDim = QPushButton("Obtenir une solution étant donné un nombre de tatamis")
        boutonFonctionaliteSansSymetrieNbDispo = QPushButton("Connaître le nombre de dispositions possibles sans symétrie")
        boutonFonctionaliteSansSymetrieAffichage = QPushButton("Afficher toutes les dispositions possibles sans symétrie")
        boutonFonctionaliteSolutionMini = QPushButton("Quelle taille maximum de dojo pour avoir une solution ?")
        boutonFonctionaliteSolutionDemi = QPushButton("Existe-t-il une solution avec un/des demi-tatamis ?")

        # couleur, police et style des boutons
        boutonFonctionaliteSurface.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteExiste.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteNbDispositions.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteNbTatamis.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteUneDisposition.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteToutesDispositions.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteSolutionAPartirDim.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteSansSymetrieNbDispo.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")        
        boutonFonctionaliteSansSymetrieAffichage.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFonctionaliteSolutionMini.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px; ")
        boutonFonctionaliteSolutionDemi.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")

        boutonFonctionaliteSurface.setFont(fontTexte)
        boutonFonctionaliteExiste.setFont(fontTexte)
        boutonFonctionaliteNbDispositions.setFont(fontTexte)
        boutonFonctionaliteNbTatamis.setFont(fontTexte)
        boutonFonctionaliteUneDisposition.setFont(fontTexte)
        boutonFonctionaliteToutesDispositions.setFont(fontTexte)
        boutonFonctionaliteSolutionAPartirDim.setFont(fontTexte)
        boutonFonctionaliteSansSymetrieNbDispo.setFont(fontTexte)
        boutonFonctionaliteSansSymetrieAffichage.setFont(fontTexte)
        boutonFonctionaliteSolutionMini.setFont(fontTexte)
        boutonFonctionaliteSolutionDemi.setFont(fontTexte)
        
        # placement des boutons
        grid.addWidget(boutonFonctionaliteSurface, 2, 1,1,2)
        grid.addWidget(boutonFonctionaliteExiste, 3, 1)
        grid.addWidget(boutonFonctionaliteNbDispositions, 3, 2)
        grid.addWidget(boutonFonctionaliteNbTatamis, 4, 1,1,2)
        grid.addWidget(boutonFonctionaliteSolutionMini, 6, 1)
        grid.addWidget(boutonFonctionaliteSolutionDemi, 6, 2)
        grid.addWidget(boutonFonctionaliteUneDisposition, 7, 1)
        grid.addWidget(boutonFonctionaliteToutesDispositions, 7, 2)
        grid.addWidget(boutonFonctionaliteSansSymetrieNbDispo, 8, 1)
        grid.addWidget(boutonFonctionaliteSansSymetrieAffichage, 8, 2)
        grid.addWidget(boutonFonctionaliteSolutionAPartirDim, 11, 1,1,2)

        
        # creation et placement d'espacements
        spacer = QLabel("", self)
        grid.addWidget(spacer, 9,0,1,1)


        # connecter les boutons
        boutonFonctionaliteSurface.clicked.connect(self.clickSurface)
        boutonFonctionaliteExiste.clicked.connect(self.clickExiste)
        boutonFonctionaliteNbDispositions.clicked.connect(self.clickNbDispositions)
        boutonFonctionaliteNbTatamis.clicked.connect(self.clickNbTatamis)
        boutonFonctionaliteUneDisposition.clicked.connect(lambda: self.clickDisposition(1)) # la fonction lambda permet de passer un argument dans clickDisposition
        boutonFonctionaliteToutesDispositions.clicked.connect(lambda: self.clickDisposition(0))
        boutonFonctionaliteSansSymetrieAffichage.clicked.connect(lambda: self.clickDisposition(2))
        boutonFonctionaliteSansSymetrieNbDispo.clicked.connect(self.clickSansSymetrieNbDispo)
        boutonFonctionaliteSolutionAPartirDim.clicked.connect(self.clickSolutionAPartirDim)
        boutonFonctionaliteSolutionMini.clicked.connect(self.clickSolutionMini)
        boutonFonctionaliteSolutionDemi.clicked.connect(self.clickSolutionDemi)


        # commentaires sur les boutons et champs
        boutonFonctionaliteSurface.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteExiste.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteNbDispositions.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteNbTatamis.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteUneDisposition.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteToutesDispositions.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteSolutionAPartirDim.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteSolutionMini.setToolTip("Cliquer pour accéder à cette fonctionalité")
        boutonFonctionaliteSolutionDemi.setToolTip("Cliquer pour accéder à cette fonctionalité")

        self.longueurEdit.setToolTip("Entrer la longeur du dojo (nombre entier entre 1 et 25)")
        self.largeurEdit.setToolTip("Entrer la largeur du dojo (nombre entier entre 1 et 25)")
        self.nbTatamisDispoEdit.setToolTip("Entrer le nombre de tatamis disponibles (nombre entier entre 3 et 300)")


        # bouton supplementaire pour fermer
        boutonFermer = QPushButton("Fermer", self)
        boutonFermer.setToolTip("Fermer l'application")
        boutonFermer.clicked.connect(self.close)
        boutonFermer.setStyleSheet("border-radius : 1px; background-color:#41b3a3; border-bottom: 1px solid;border-right: 1px solid;color: black;padding: 4px;")
        boutonFermer.setFont(fontTexte)
        grid.addWidget(boutonFermer, 12, 3)

        
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

    def set_NbTatamis(self) :
        "fonction qui affecte le nombre de tatamis saisi en retournant 0 si celle-ci est vide"
        if (self.nbTatamisDispoEdit.text()==""):
            self.nb_tatamis = 0
        else:
            self.nb_tatamis = int(self.nbTatamisDispoEdit.text())

    def tatamis_vide(self):
        "fonction qui vérifie si les valeurs saisies sont nulles"
        self.set_NbTatamis()
        return self.nb_tatamis==0 

    def clickSurface(self):
        "fonction d'action sur le bouton Surface"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalide()          
            message.exec()

        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
            message.exec()

        # affichage de la réponse a l'utilisateur
        else:
            surface = self.largeur_dojo * self.longueur_dojo
            info = f"La surface du dojo est {surface}."
                               
            message = MessageInfo("Surface du dojo",info)
            message.exec()

    def clickExiste(self):
        "fonction d'action sur le bouton Existe"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalide()          
            message.exec()

        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
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
        
        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
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
        
        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
            message.exec()

        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo):
            info = f"Le nombre de tatamis 2x1 nécessaires pour ce dojo est : {nombre_tatamis(self.largeur_dojo, self.longueur_dojo)}"
            message = MessageInfo("Connaître le nombre de tatamis 2x1 nécessaires pour la taille du dojo",info)
            message.exec()

        else :
            message = MessageDemandeImpossible()             
            message.exec()       

    def clickDisposition(self,tous):
        "fonction d'action sur le bouton afficher les dispositions"
        if self.valeur_vide() :
            message = MessageSaisieInvalide()            
            message.exec()
        
        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
            message.exec()

        # affichage de la réponse a l'utilisateur
        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
            W,H = dimension_max(self.largeur_dojo, self.longueur_dojo)
            fenetre = FenetreDojos(W,H,tous)
                       
            fenetre.exec()

        else :
            message = MessageDemandeImpossible()                   
            message.exec()

    def clickSansSymetrieNbDispo(self):
        if self.valeur_vide() :
            message = MessageSaisieInvalide()          
            message.exec()
        
        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
            message.exec()

        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo):
            #nombre = nombre_dispo_uniques(self.largeur_dojo, self.longueur_dojo)    
            nombre = Dispositions(self.largeur_dojo, self.longueur_dojo, False).count        
            info = f"Le nombre disposition(s) sans symétrie pour ce dojo est : {nombre}"
            message = MessageInfo("Connaître le nombre de disposition(s) sans symétrie horizontale et/ou verticale pour ce dojo",info)
            message.exec()

        else :
            message = MessageDemandeImpossible()             
            message.exec()


          
    def clickSolutionAPartirDim(self):
        "fonction d'action sur le bouton Solution Étant Donne Nb Tatamis"
        
        if self.tatamis_vide() :
            message = MessageSaisieInvalide() 
            message.setText("Erreur de saisie du nombre de tatamis")
            message.setInformativeText("Le nombre de tatamis ne peut avoir une valeur nulle ou vide")         
            message.exec()
        
        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.nb_tatamis > 300 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Le nombre de tatamis saisi ne peut excéder 300")  
            message.exec()

        elif (self.nb_tatamis<3) :
            message = MessageDemandeImpossible()  
            message.setInformativeText("Il existe au moins une disposition possible avec des tatamis 2x1 pour ce dojo")
            message.setInformativeText("Saisir au minimum 3 tatamis pour utiliser cette fonctionalité.")       
            message.exec() 
        
        else :
            dim = recherche_dimensions(self.nb_tatamis)
            info = affichage_dimension(dim)
            message = MessageInfo("Dimension(s) possible(s) du dojo étant donné le nombre de tatamis saisi \nCes propositions satisfont aux conditions suivantes: \n   - un ratio maximum de 3 entre la longueur et la largeur\n   - une utilisation de minimum 75% des tatamis saisis",info)
            message.exec()
            
            
    def clickSolutionMini(self):
        "fonction d'action sur le bouton Nombre de tatamis"

        if self.valeur_vide() :
            message = MessageSaisieInvalide()            
            message.exec()

        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
            message.exec()

        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
            message = MessageDemandeImpossible()       
            message.setInformativeText("Il existe au moins une disposition possible avec des tatamis 2x1 pour ce dojo")      
            message.exec() 

        elif (self.largeur_dojo==1 and self.longueur_dojo==1) :
            message = MessageDemandeImpossible()     
            message.setInformativeText("Il existe au moins une disposition possible avec des tatamis 2x1 pour ce dojo")
            message.setInformativeText("Il n'existe pas de solution plus petite que 1 x 1.")       
            message.exec() 

        else:
            taille_max = recherche_disposition_max(self.largeur_dojo, self.longueur_dojo)
            info = f"La taille maximale est {taille_max}"
            message = MessageInfo("Taille maximum de dojo pour le remplir de tatamis 2 x 1",info)
            message.exec()
        
    def clickSolutionDemi(self):
        "fonction d'action sur le bouton Solution avec des demis tatamis"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalide()            
            message.exec()

        # Validation supplementaire pour les versions 5.12.2 de PyQt (compte tenu de l evolution de QIntValidator qui ne bloque plus les valeurs saisies de la meme maniere)
        elif self.largeur_dojo > 25 or self.longueur_dojo > 25 :
            message = MessageSaisieInvalide() 
            message.setInformativeText("Ni la longueur ni la largeur ne peuvent excéder 25")  
            message.exec()
            
        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
            message = MessageDemandeImpossible()
            message.setInformativeText("Il existe au moins une disposition possible avec des tatamis 2x1 pour ce dojo")             
            message.exec() 
        else:
            info = "Oui"
            message = MessageInfo("Existe-t-il une solutions avec des demi-tatamis?",info)
            message.exec()

def main():
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()