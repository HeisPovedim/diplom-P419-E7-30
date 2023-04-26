from PyQt6.QtWidgets import QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget


class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("График")
        self.setFixedSize(700, 519)
        
        self.setupUi()
        
    def setupUi(self):

        self.centralwidget = QtWidgets.QWidget(parent=self)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.graphwidget = PlotWidget(parent=self.centralwidget)
        
        

        self.verticalLayout.addWidget(self.graphwidget)
        self.setCentralWidget(self.centralwidget)