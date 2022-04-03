import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QGridLayout, QMessageBox
from PyQt5.QtGui import * 
from calcul_nombre_dispositions import *
from dojo import *

class MessageSaisieInvalideDim(QMessageBox):
    "classe qui affiche un message pour avertir que la saisie est invalide"
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Erreur de saisie des dimensions")
        self.setInformativeText("Aucune dimension ne peut avoir une valeur nulle ou vide")
        self.setStandardButtons(QMessageBox.Ok)
        
class MessageSaisieInvalideNbTatamis(QMessageBox):
    "classe qui affiche un message pour avertir que la saisie est invalide"
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Erreur de saisie du nombre de tatamis")
        self.setInformativeText("Le nombre de tatamis ne peut avoir une valeur nulle ou vide")
        self.setStandardButtons(QMessageBox.Ok)

class MessageDemandeImpossible(QMessageBox):
    "classe qui affiche un message pour avertir qu'il n'existe pas de solutions"
    def __init__(self):
        super().__init__()
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle('Super Dojo Calculator')
        self.setText("Demande impossible")
        self.setInformativeText("Il n'existe pas de disposition possible avec des tatamis 2x1 pour ce dojo")
        self.setStandardButtons(QMessageBox.Ok)

class MessageInfo(QMessageBox):
    "classe qui créée un message avec une question et une info passées en paramètres"
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
        
        # creation de la fenetre
        self.resize(600,350)
        self.setWindowTitle('Super Dojo Calculator')
        
        # couleur de la fenetre
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor('#FAC2C1'))
        gradient.setColorAt(1.0, QColor('#87C1AF'))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)
        
        # texte des champs de saisie
        longueur = QLabel('Longueur (entre 1 et 25)')
        largeur = QLabel('Largeur (entre 1 et 25)')
        nbTatamisDispo = QLabel('Nombre de tatamis 2x1 disponibles (entre 1 et 300)')
        
        # determination des polices et tailles
        QFontDatabase.addApplicationFont("NexaBold.otf")
        QFontDatabase.addApplicationFont("NexaLight.otf")

        fontTitre = QFont("Nexa Bold", 16)
        fontTexte = QFont("Nexa Light",12)
        
        # style des textes des champs de saisie
        longueur.setFont(fontTexte)
        largeur.setFont(fontTexte)
        nbTatamisDispo.setFont(fontTexte)
                

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
        grid.setSpacing(20)
        
        #placement des champs de saisie
        grid.addWidget(longueur, 2, 0)
        grid.addWidget(self.longueurEdit, 2, 1)


        grid.addWidget(largeur, 3, 0)
        grid.addWidget(self.largeurEdit, 3, 1)
        
        grid.addWidget(nbTatamisDispo, 8, 0)
        grid.addWidget(self.nbTatamisDispoEdit, 8, 1)

        # mise en place de texte pour faciliter la comprehension
        textDimension = QLabel("Entrez la dimension de votre dojo:\n (en valeur relative de tatamis standards 2x1)", self)
        textDimension.setFont(fontTitre)
        grid.addWidget(textDimension, 1, 0)
        
        textFonctionalite = QLabel('Que cherchez vous?', self)
        textFonctionalite.setFont(fontTitre)
        grid.addWidget(textFonctionalite, 4, 0)
        

        # creation des boutons
        boutonFonctionaliteExiste = QPushButton("Savoir si il existe une disposition pour le dojo")
        boutonFonctionaliteNbDispositions = QPushButton("Connaître le nombre de dispositions possibles")
        boutonFonctionaliteNbTatamis = QPushButton("Connaître le nombre de tatamis 2x1 nécessaires pour la taille du dojo")
        boutonFonctionaliteUneDisposition = QPushButton("Afficher une disposition")
        boutonFonctionaliteToutesDispositions = QPushButton("Afficher toutes les dispositions possibles")
        boutonFonctionaliteSolutionAPartirDim = QPushButton("Obtenir une solution etant donne un nombre de tatamis")

        # couleur et style des boutons
        boutonFonctionaliteExiste.setStyleSheet("border : 2px solid black; border-radius : 20px;")
        boutonFonctionaliteNbDispositions.setStyleSheet("border : 2px solid black; border-radius : 20px;")
        boutonFonctionaliteNbTatamis.setStyleSheet("border : 2px solid black; border-radius : 20px;")
        boutonFonctionaliteUneDisposition.setStyleSheet("border : 2px solid black; border-radius : 20px;")
        boutonFonctionaliteToutesDispositions.setStyleSheet("border : 2px solid black; border-radius : 20px;")
        boutonFonctionaliteSolutionAPartirDim.setStyleSheet("border : 2px solid black; border-radius : 20px;")
        
        
        # placement des boutons
        grid.addWidget(boutonFonctionaliteExiste, 5, 1)
        grid.addWidget(boutonFonctionaliteNbDispositions, 6, 1)
        grid.addWidget(boutonFonctionaliteNbTatamis, 6, 2)
        grid.addWidget(boutonFonctionaliteUneDisposition, 7, 1)
        grid.addWidget(boutonFonctionaliteToutesDispositions, 7, 2)
        grid.addWidget(boutonFonctionaliteSolutionAPartirDim, 9, 1)


        # connecter les boutons
        boutonFonctionaliteExiste.clicked.connect(self.clickExiste)
        boutonFonctionaliteNbDispositions.clicked.connect(self.clickNbDispositions)
        boutonFonctionaliteNbTatamis.clicked.connect(self.clickNbTatamis)
        boutonFonctionaliteUneDisposition.clicked.connect(self.clickUneDisposition)
        boutonFonctionaliteToutesDispositions.clicked.connect(self.clickToutesDispositions)
        boutonFonctionaliteSolutionAPartirDim.clicked.connect(self.clickSolutionAPartirDim)


        # bouton supplementaire pour fermer
        boutonFermer = QPushButton("Fermer", self)
        boutonFermer.setToolTip("Fermer l'application")
        boutonFermer.clicked.connect(self.close)
        boutonFermer.setStyleSheet("background-color:#41b3a3;");
        grid.addWidget(boutonFermer, 10, 4)

        
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

    def clickExiste(self):
        "fonction d'action sur le bouton Existe"
        
        if self.valeur_vide() :
            message = MessageSaisieInvalideDim()          
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
            message = MessageSaisieInvalideDim()          
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
            message = MessageSaisieInvalideDim()            
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
            message = MessageSaisieInvalideDim()            
            message.exec()

        # affichage de la réponse a l'utilisateur
        elif nombre_de_dispositions(self.largeur_dojo, self.longueur_dojo) :
            fenetre = FenetreDojos(self.largeur_dojo,self.longueur_dojo,tous=True)
                       
            fenetre.exec()

        else :
            message = MessageDemandeImpossible()                   
            message.exec()      


    def clickSolutionAPartirDim(self):
        "fonction d'action sur le bouton Nombre de tatamis"
        
        if self.tatamis_vide() :
            message = MessageSaisieInvalideNbTatamis()          
            message.exec()
        
        else :
            info = f"TBD"
            message = MessageInfo("Solution étant donné le nombre de tatamis saisi",info)
            message.exec()

def main():
    app = QApplication(sys.argv)
    interface = Interface()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    main()
