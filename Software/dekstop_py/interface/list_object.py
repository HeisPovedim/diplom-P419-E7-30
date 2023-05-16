from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

# DATABASE
from database.requests import get_parameters, get_objects


class ListObject(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Список объектов")
        self.resize(1000, 800)
        
        self.page_size = 10  # Количество элементов на странице
        self.current_page = 1  # Текущая страница
        
        self.setupUi()
    
    def setupUi(self):
        """Таблица параметров"""
        
        # Создание таблицы
        self.table = QTableWidget(self)
        self.table.setColumnCount(10)  # Установка количества столбцов
        
        # Кнопки пагинации
        self.prev_button = QPushButton("Предыдущая страница")
        self.next_button = QPushButton("Следующая страница")
        self.prev_button.clicked.connect(self.previous_page)
        self.next_button.clicked.connect(self.next_page)
        
        # Размещение таблицы и кнопок в компоновке
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)
        
        # Создание виджета и установка компоновки
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
        self.load_data()
    
    def load_data(self):
        """Загрузка данных для текущей страницы"""
        
        parameters = get_parameters(None, True)
        total_count = len(parameters)
        
        headers = [
            "ID Параметра",
            "Частота",
            "z_real_path_parameters",
            "z_imaginary_part_parameters",
            "Phi",
            "Gp",
            "Rp",
            "Cp",
            "Дата измерения",
            "ID Объекта"
        ]
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(parameters))
        self.table.setColumnCount(len(headers))
        
        for row, data in enumerate(parameters):
            for col, header in enumerate(headers):
                if header == 'ID Параметра':
                    item = QTableWidgetItem(str(data['idparameters']))
                elif header == 'Частота':
                    item = QTableWidgetItem(str(data['Freq']))
                elif header == 'z_real_path_parameters':
                    item = QTableWidgetItem(str(data['z_real_path_parameters']))
                elif header == 'z_imaginary_part_parameters':
                    item = QTableWidgetItem(str(data['z_imaginary_part_parameters']))
                elif header == 'Phi':
                    item = QTableWidgetItem(str(data['phi_parameters']))
                elif header == 'Gp':
                    item = QTableWidgetItem(str(data['gp_parameters']))
                elif header == 'Rp':
                    item = QTableWidgetItem(str(data['rp_parameters']))
                elif header == 'Cp':
                    item = QTableWidgetItem(str(data['cp_parameters']))
                elif header == 'Дата измерения':
                    item = QTableWidgetItem(str(data['measurement_date']))
                elif header == 'ID Объекта':
                    item = QTableWidgetItem(str(data['objects_idobjects']))
                
                self.table.setItem(row, col, item)
                self.table.setColumnWidth(col, 200)
        
        # Отключение кнопки "Предыдущая страница" при достижении первой страницы
        self.prev_button.setEnabled(self.current_page > 1)
        
        # Отключение кнопки "Следующая страница" при достижении последней страницы
        self.next_button.setEnabled(self.current_page * self.page_size < total_count)
        
        self.setCentralWidget(self.table)
    
    def previous_page(self):
        """Обработчик нажатия кнопки "Предыдущая страница" """
        
        self.current_page -= 1
        self.load_data()
    
    def next_page(self):
        """Обработчик нажатия кнопки "Следующая страница" """
        
        self.current_page += 1
        self.load_data()