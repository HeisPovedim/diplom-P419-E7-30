# PyQt6 && LIBS
from PyQt6 import QtCore, QtGui, QtWidgets

# Script
from scripts.controller_e730 import ControllerE730
from database.requests import check_object

class RunScript(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        
        # Настройки окна
        self.setWindowTitle("Измерение пьезокерамики")
        self.resize(303, 118)
        
        self.parent_window = parent
        
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        validator_number = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[0-9]*"))
        # Выравнивание элементов по центр
        central_widget = QtWidgets.QWidget(parent=self)
        central_interface = QtWidgets.QGridLayout(central_widget)
        
        # Создание сетки
        gridLayout = QtWidgets.QGridLayout()

        # id объекта Label
        label_id_object = QtWidgets.QLabel(parent=central_widget)
        label_id_object.setText("id объекта:")
        gridLayout.addWidget(label_id_object, 0, 0, 1, 1)
        
        # Введите id объекта
        self.id_object = QtWidgets.QLineEdit(parent=central_widget)
        self.id_object.setValidator(validator_number)
        self.id_object.setPlaceholderText(" Введите id объекта")
        gridLayout.addWidget(self.id_object, 0, 1, 1, 1)

        # начальная частота Label
        label_initial_frequency = QtWidgets.QLabel(parent=central_widget)
        label_initial_frequency.setText("Начальная частота:")
        gridLayout.addWidget(label_initial_frequency, 1, 0, 1, 1)
        
        # начальная частота LineEdit
        lineEdit_initial_frequency = QtWidgets.QLineEdit(parent=central_widget)
        lineEdit_initial_frequency.setValidator(validator_number)
        gridLayout.addWidget(lineEdit_initial_frequency, 1, 1, 1, 1)
        
        # конечная частота Label
        label_final_frequency = QtWidgets.QLabel(parent=central_widget)
        label_final_frequency.setText("Конечная частота:")
        gridLayout.addWidget(label_final_frequency, 2, 0, 1, 1)
        
        # конечная частота LineEdit
        lineEdit_final_frequency = QtWidgets.QLineEdit(parent=central_widget)
        lineEdit_final_frequency.setValidator(validator_number)
        gridLayout.addWidget(lineEdit_final_frequency, 2, 1, 1, 1)
        
        # шаг Label
        label_step = QtWidgets.QLabel(parent=central_widget)
        label_step.setText("Шаг:")
        gridLayout.addWidget(label_step, 3, 0, 1, 1)
        
        # шаг LineEdit
        lineEdit_step = QtWidgets.QLineEdit(parent=central_widget)
        lineEdit_step.setValidator(validator_number)
        gridLayout.addWidget(lineEdit_step, 3, 1, 1, 1)
        
        # Z-Only
        checkBox = QtWidgets.QCheckBox(parent=central_widget)
        checkBox.setText("Z-Only")
        gridLayout.addWidget(checkBox, 4, 0, 1, 1)
        
        # кнопки
        buttons = QtWidgets.QHBoxLayout()
        gridLayout.addLayout(buttons, 4, 1, 1, 1)
        
        # кнопка "Старт"
        btn_start = QtWidgets.QPushButton(parent=central_widget)
        btn_start.setText("Старт")
        btn_start.clicked.connect(lambda: self.run_script_controller(
            lineEdit_initial_frequency.text(),
            lineEdit_final_frequency.text(),
            lineEdit_step.text(),
            checkBox.isChecked()
        ))
        buttons.addWidget(btn_start, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # кнопка "Выйти"
        btn_exit = QtWidgets.QPushButton(parent=central_widget)
        btn_exit.setText("Выйти")
        btn_exit.clicked.connect(lambda: self.exit())
        buttons.addWidget(btn_exit, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # Размещение элементов в окне
        central_interface.addLayout(gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(central_widget)
        
    def run_script_controller(self, initial_freq, final_freq, step, z_only):
        """Запуск скрипта контроллера E7-30"""
        id = self.id_object.text()
        
        if id and initial_freq and final_freq and step:
            response = check_object(id)
            if response:
                response = QtWidgets.QMessageBox.question(self,"Найден объект",f"Название объекта: {response['name']}. Начать вычисления?")
                if response == QtWidgets.QMessageBox.StandardButton.Yes:
                    self.controller_e730 = ControllerE730(id,initial_freq,final_freq,step,z_only)

                    # проверка коннекта с прибором
                    response = self.controller_e730.set_default()
                    if response:
                        self.controller_e730.calc_all()

            else:
                QtWidgets.QMessageBox.warning(self,"Ошибка id","Указан неизвестный идентификатор объекта в базе данных")
        else:
            QtWidgets.QMessageBox.warning(self,"Пустые поля","Заполните все поля")
        
    
    def exit(self):
        """Выход и переход к окну авторизации"""
        self.close()
