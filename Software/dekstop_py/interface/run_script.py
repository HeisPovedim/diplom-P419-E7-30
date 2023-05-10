# PyQt6 && LIBS
from PyQt6 import QtCore, QtGui, QtWidgets

class RunScript(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        
        # Настройки окна
        self.setWindowTitle("Запуск скрипта")
        self.resize(303, 118)
        
        self.parent_window = parent
        
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        
        # Выравнивание элементов по центр
        central_widget = QtWidgets.QWidget(parent=self)
        central_interface = QtWidgets.QGridLayout(central_widget)
        
        # Создание сетки
        gridLayout = QtWidgets.QGridLayout()

        # начальная частота Label
        label_initial_frequency = QtWidgets.QLabel(parent=central_widget)
        label_initial_frequency.setText("Начальная частота:")
        gridLayout.addWidget(label_initial_frequency, 0, 0, 1, 1)
        
        # начальная частота LineEdit
        lineEdit_initial_frequency = QtWidgets.QLineEdit(parent=central_widget)
        gridLayout.addWidget(lineEdit_initial_frequency, 0, 1, 1, 1)
        
        # конечная частота Label
        label_final_frequency = QtWidgets.QLabel(parent=central_widget)
        label_final_frequency.setText("Конечная частота:")
        gridLayout.addWidget(label_final_frequency, 1, 0, 1, 1)
        
        # конечная частота LineEdit
        lineEdit_final_frequency = QtWidgets.QLineEdit(parent=central_widget)
        gridLayout.addWidget(lineEdit_final_frequency, 1, 1, 1, 1)
        
        # шаг Label
        label_step = QtWidgets.QLabel(parent=central_widget)
        label_step.setText("Шаг:")
        gridLayout.addWidget(label_step, 2, 0, 1, 1)
        
        # шаг LineEdit
        lineEdit_step = QtWidgets.QLineEdit(parent=central_widget)
        gridLayout.addWidget(lineEdit_step, 2, 1, 1, 1)
        
        # Z-Only
        checkBox = QtWidgets.QCheckBox(parent=central_widget)
        checkBox.setText("Z-Only")
        gridLayout.addWidget(checkBox, 3, 0, 1, 1)
        
        # кнопки
        buttons = QtWidgets.QHBoxLayout()
        gridLayout.addLayout(buttons, 3, 1, 1, 1)
        
        # кнопка "Старт"
        btn_start = QtWidgets.QPushButton(parent=central_widget)
        btn_start.setText("Старт")
        # btn_start.clicked.connect(lambda: calc_all(
        #     lineEdit_initial_frequency.text(),
        #     lineEdit_final_frequency.text(),
        #     lineEdit_step.text(),
        #     checkBox.isChecked()
        # ))
        buttons.addWidget(btn_start, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # кнопка "Выйти"
        btn_exit = QtWidgets.QPushButton(parent=central_widget)
        btn_exit.setText("Выйти")
        btn_exit.clicked.connect(lambda: self.exit())
        buttons.addWidget(btn_exit, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # Размещение элементов в окне
        central_interface.addLayout(gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(central_widget)
    
    def exit(self):
        """Выход и переход к окну авторизации"""
        
        self.close()
        self.parent_window.show()