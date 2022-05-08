import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QGridLayout, QMessageBox, QDialog, QVBoxLayout, QDialogButtonBox
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtGui import QBrush, QColor, QPen, QPainter
from calcul_coordonnees_tatamis import Dispositions


COULEUR_FOND = "white"
COULEUR_CONTOUR = "gray"
COULEUR_TATAMI = QColor('#87C1AF')

class Tatami(QGraphicsRectItem):
    "classe permettant d'instancier un tatamis d'après ces propriétés: position,dimensions,couleur"

    _pen = QPen(QColor(COULEUR_CONTOUR))
    _pen.setCosmetic(True)

    def __init__(self,x,y,l,h):
        QGraphicsRectItem.__init__(self,0,0,l,h)
        self.setPos(x,y)
        self.setPen(Tatami._pen)
        self.brush = QBrush(QColor(COULEUR_TATAMI))
        self.setBrush(self.brush)

class Dojos(QGraphicsScene):
    "classe créant un seul ou tous les dojos possibles d'après les dimensions données"
    
    def __init__(self,H,W,tous=0):
        QGraphicsScene.__init__(self)

        self.H = H
        self.W = W
        self.tous = tous
        self.ajoutDojos()

    def ajoutDojos(self):
        "fonction permettant d'ajouter un dojo sur la scène"        
        # placementTatamis = Dispositions(self.W,self.H)
        # if self.tous :
        #     dojos = placementTatamis.coordonnees
        # else :
        #     dojos = [placementTatamis.coordonnees[0]]

        if self.tous == 0 :
            dispositions = Dispositions(self.W, self.H, True)
            dojos = dispositions.coordonnees
        elif self.tous == 1 :
            dojos = [Dispositions(self.W, self.H, True).coordonnees[0]]
        else :
            dispositions = Dispositions(self.W, self.H, False)
            dojos = dispositions.coordonnees
            print(dispositions.grilles)





        decalage = 0
        size = min(750//self.W,550//self.H)
        for dojo in dojos:
            self.ajoutTatamis(dojo,decalage,size)
            decalage += (self.W)*size+50

    def ajoutTatamis(self,dojo,decalage,size):
        "fonction plaçant un tatamis sur la scene d'après ses propriétés"
        for element in dojo:
                tatami = Tatami(element['x']*size,decalage+element['y']*size,element['largeur']*size,element['hauteur']*size)
                self.addItem(tatami)

class VueDojo(QGraphicsView):
    "classe permettant d'instancier la vue contenant les dojos"
    
    def __init__(self,dojo):
        QGraphicsView.__init__(self,dojo)
       

        self.setBackgroundBrush(QColor(COULEUR_FOND))
        #self.resize (800,600)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dojos = Dojos(7,12,True)
#     vueDojo = VueDojo(dojos)
#     vueDojo.show()
#     sys.exit(app.exec_())



class FenetreDojos(QDialog):
    "classe qui crée la fenêtre d'affichage du ou des dojos"
    def __init__(self,H,W,tous):
        super().__init__()
        self.H = H
        self.W = W
        self.tous = tous

        self.setWindowTitle("Dispositions")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        
        dojos = Dojos(self.H,self.W,tous)        
        vueDojo = VueDojo(dojos)

        aire = int(self.H*self.W)
        nombre = int(aire/2)
        info = QLabel(f"Dojo de dimension : {self.H} x {self.W}   |   Surface : {aire} m²   |   {nombre} tatamis")


        self.layout.addWidget(info)
        self.layout.addWidget(vueDojo)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.resize (800,600)