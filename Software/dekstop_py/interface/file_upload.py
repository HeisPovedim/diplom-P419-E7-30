import csv

from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt6 import QtCore, QtWidgets
from database.connect import Connect
from interface.graph_widget import GraphWidget

class FileUpload(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle("Главное окно")
        self.setFixedSize(259, 69)
        
        # Инициализация переменных
        self.GraphWidget = None
        
        # Отрисовка окна
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        
        # Выравнивание элементов по центру
        centralWidget = QtWidgets.QWidget(parent=self)
        verticalLayout = QtWidgets.QVBoxLayout(centralWidget)

        # Создание сетки
        gridLayout = QtWidgets.QGridLayout()

        # кнопка загрузки файла
        file_upload = QtWidgets.QPushButton(parent=centralWidget)
        file_upload.setText("Загрузить файл")
        file_upload.clicked.connect(self.load_data)
        gridLayout.addWidget(file_upload, 1, 0, 1, 1)
        
        # заголовок
        title = QtWidgets.QLabel(parent=centralWidget)
        title.setText("Выберите файл в формате csv")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        gridLayout.addWidget(title, 0, 0, 1, 1)
        
        # Размещение элементов в окне
        verticalLayout.addLayout(gridLayout)
        self.setCentralWidget(centralWidget)
        
    def load_data(self):
        """Функция построение графика и его отображение"""
        
        Connect() # connect database
        