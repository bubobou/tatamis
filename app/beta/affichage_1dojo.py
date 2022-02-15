from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
from pavage_recursif import Dispositions


class Dojo(QWidget):
    '''
    La classe permettant d'afficher une disposition du dojo
    Paramètres
    ----------
        (W,H) : largeur et hauteur du dojo.
    '''
    def __init__(self,W,H):
        super().__init__()

        self.title = "Pavage par tatamis"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.H=H
        self.W=W


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.darkYellow, Qt.SolidPattern))
        marge = 20
        
        disp=Dispositions(self.W,self.H)
        solutions= disp.listeTatamis()
        unitW=(self.width-40)//disp.W
        unitH=(self.height-40)//disp.H
        unit = min(unitW,unitH)
        margeW=(self.width-unit*disp.W)//2
        margeH=(self.height-unit*disp.H)//2

        if disp.count :            
            for tatamis in solutions[0] :
                painter.drawRect(tatamis['x']*unit+margeW, tatamis['y']*unit+margeH, tatamis['largeur']*unit,tatamis['hauteur']*unit)



App = QApplication(sys.argv)
dojo = Dojo(6,13)
sys.exit(App.exec())