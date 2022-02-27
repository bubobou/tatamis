from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPen, QPainter
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem
from pavage_recursif import Dispositions
import sys

COULEUR_FOND = "white"
COULEUR_CONTOUR = "gray"
COULEUR_TATAMI = "yellow"

class Tatami(QGraphicsRectItem):

    _pen = QPen(QColor(COULEUR_CONTOUR))
    _pen.setCosmetic(True)

    def __init__(self,x,y,l,h):
        QGraphicsRectItem.__init__(self,0,0,l,h)
        self.setPos(x,y)
        self.setPen(Tatami._pen)
        self.brush = QBrush(QColor(COULEUR_TATAMI))
        self.setBrush(self.brush)

class Dojos(QGraphicsScene):
    
    def __init__(self,H,W,tous=False):
        QGraphicsScene.__init__(self)

        self.H = H
        self.W = W
        self.tous = tous
        self.ajoutDojos()

    def ajoutDojos(self):        
        placementTatamis = Dispositions(self.W,self.H)
        if self.tous :
            dojos = placementTatamis.listeTatamis()
        else :
            dojos = [placementTatamis.listeTatamis()[0]]

        decalage = 0
        size = 40
        for dojo in dojos:
            self.ajoutTatamis(dojo,decalage,size)
            decalage += (self.H+2)*size

    def ajoutTatamis(self,dojo,decalage,size):
        for element in dojo:
                tatami = Tatami(element['x']*size,decalage+element['y']*size,element['largeur']*size,element['hauteur']*size)
                self.addItem(tatami)

class VueDojo(QGraphicsView):
    
    def __init__(self,dojo):
        QGraphicsView.__init__(self,dojo)
        self.setBackgroundBrush(QColor(COULEUR_FOND))
        self.resize (800,600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dojos = Dojos(7,12,True)
    vueDojo = VueDojo(dojos)
    vueDojo.show()
    sys.exit(app.exec_())
