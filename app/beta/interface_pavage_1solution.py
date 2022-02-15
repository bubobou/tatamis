from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
from pavage_recursif import Dispositions


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Pavage par tatamis"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.blue, Qt.DiagCrossPattern))
        marge = 20
        
        disp=Dispositions(7,6)
        solutions= disp.listeTatamis()
        unitW=(self.width-40)//disp.W
        unitH=(self.height-40)//disp.H
        unit = min(unitW,unitH)
        margeW=(self.width-unit*disp.W)//2
        margeH=(self.height-unit*disp.H)//2

        if disp.count :            
            for tatamis in solutions[1] :
                painter.drawRect(tatamis['x']*unit+margeW, tatamis['y']*unit+margeH, tatamis['largeur']*unit,tatamis['hauteur']*unit)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())