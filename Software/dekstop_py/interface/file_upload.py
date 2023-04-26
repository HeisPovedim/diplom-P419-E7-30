from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets

class FileUpload(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Главное окно")
        self.setFixedSize(259, 69)
        
        self.setupUi()
        
    def setupUi(self):
        
        self.centralwidget = QtWidgets.QWidget(parent=self)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.gridLayout = QtWidgets.QGridLayout()

        self.file_upload = QtWidgets.QPushButton(parent=self.centralwidget)
        self.file_upload.setText("Загрузить файл")

        self.gridLayout.addWidget(self.file_upload, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setText("Выберите файл в формате csv")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        
        self.setCentralWidget(self.centralwidget)