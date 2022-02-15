from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
from pavage_recursif import Dispositions


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 800


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

        disp=Dispositions(3,4)
        solutions= disp.listeTatamis()
        print(disp.count)
        if disp.count :
            
            for tatamis in solutions[1] :
                painter.drawRect(tatamis['x']*100+5, tatamis['y']*100+5, tatamis['largeur']*100,tatamis['hauteur']*100)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())