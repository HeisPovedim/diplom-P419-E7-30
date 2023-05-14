from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

# DATABASE
from database.requests import getting_parameters

class ListObject(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Список объектов")
        self.resize(1000, 800)
        
        self.setupUi()
        
    def setupUi(self):
        """Таблица параметров"""

        # Создание таблицы
        self.table = QTableWidget(self)
        self.table.setColumnCount(10)  # Установка количества столбцов
        # self.table.setHorizontalHeaderLabels(
        #     [
        #         "id Объекта",
        #         "Наименование",
        #         "Материал",
        #         "Номер пакета",
        #         "Дата изготовления",
        #         "Дата получения",
        #         "Кол-во параметров",
        #         "Ширина керамики",
        #         "Толщина керамики",
        #         "id Создателя"
        #     ]
        # )
        # Добавление данных в таблицу
        parameters = getting_parameters(None, True)
        headers = list(dict(parameters[0]).keys())
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(parameters))  # Установка количества строк
        self.table.setColumnCount(len(headers)) #
        
        print(parameters)
        
        for row, data in enumerate(parameters):
            for col, header in enumerate(headers):
                item = QTableWidgetItem(str(data[header]))
                self.table.setItem(row, col, item)
                self.table.setColumnWidth(col,200)

        self.setCentralWidget(self.table)