import csv

from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets

from interface.graph_widget import GraphWidget

class FileUpload(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # Настройки окна
        self.setWindowTitle("Главное окно")
        self.setFixedSize(259, 69)
        
        # Инициализация переменных
        self.GraphWidget = None
        
        self.setupUi()
        
    def setupUi(self):
        
        centralWidget = QtWidgets.QWidget(parent=self)

        verticalLayout = QtWidgets.QVBoxLayout(centralWidget)

        gridLayout = QtWidgets.QGridLayout()

        file_upload = QtWidgets.QPushButton(parent=centralWidget)
        file_upload.setText("Загрузить файл")
        file_upload.clicked.connect(self.load_data)

        gridLayout.addWidget(file_upload, 1, 0, 1, 1)
        title = QtWidgets.QLabel(parent=centralWidget)
        title.setText("Выберите файл в формате csv")
        font = QtGui.QFont()
        font.setPointSize(12)
        title.setFont(font)
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)

        gridLayout.addWidget(title, 0, 0, 1, 1)
        verticalLayout.addLayout(gridLayout)
        
        self.setCentralWidget(centralWidget)
        
    def load_data(self):
        
        # Открываем диалоговое окно для выбора файла CSV
        filename, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "CSV Files (*.csv)")

        # Читаем данные из файла CSV
        data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Пропускаем заголовок
            for row in reader:
                x = float(row[0])
                y = float(row[1])
                data.append([x, y])

        # Данные для построения графика
        x_data = [row[0] for row in data]
        y_data = [row[1] for row in data]
        
        # Отрисовка графика
        self.GraphWidget = GraphWidget(x_data, y_data)
        self.GraphWidget.show()