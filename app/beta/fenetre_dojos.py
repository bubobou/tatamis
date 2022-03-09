import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QLineEdit, QGridLayout, QMessageBox, QDialog, QVBoxLayout, QDialogButtonBox
from scene_dojo import *

class FenetreDojos(QDialog):
    "classe qui crée la fenêtre d'affichage du ou des dojos"
    def __init__(self,H,W,tous):
        super().__init__()
        
        self.H = H
        self.W = W
        self.tous = tous

        self.setWindowTitle("Dispositions")

        QBtn = QDialogButtonBox.Ok 

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        
        dojos = Dojos(self.H,self.W,tous)
        vueDojo = VueDojo(dojos)

        self.layout.addWidget(vueDojo)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.resize (800,600)
