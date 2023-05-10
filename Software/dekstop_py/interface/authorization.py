# PyQt6 && LIBS
from PyQt6 import QtCore, QtWidgets

# IMPORT WINDOWS
from interface.personal_account import PersonalAccount

# DATABASE
from database.requests import auth_check

class Authorization(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Настройки окна
        self.setWindowTitle("Авторизация")
        self.resize(266, 98)
        
        self.setupUi()
        
    def setupUi(self):
        """Интерфейс окна"""
        
        # Выравнивание элементов по центру
        central_widget = QtWidgets.QWidget(parent=self)
        central_interface = QtWidgets.QGridLayout(central_widget)
        
        # Создание сетки
        gridLayout = QtWidgets.QGridLayout()
        
        # поле "Логин"
        login = QtWidgets.QLabel(parent=central_widget); login.setText("Логин:")
        gridLayout.addWidget(login, 0, 0, 1, 1)
        
        login_input = QtWidgets.QLineEdit(parent=central_widget)
        gridLayout.addWidget(login_input, 0, 1, 1, 1)
        
        # поле "Пароль"
        password = QtWidgets.QLabel(parent=central_widget); password.setText("Пароль:")
        gridLayout.addWidget(password, 1, 0, 1, 1)
        
        password_input = QtWidgets.QLineEdit(parent=central_widget)
        password_input.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        gridLayout.addWidget(password_input, 1, 1, 1, 1)
        
        # кнопки
        buttons = QtWidgets.QHBoxLayout()
        gridLayout.addLayout(buttons, 2, 0, 1, 2)

        auth_btn = QtWidgets.QPushButton(parent=central_widget)
        auth_btn.setText("Войти")
        auth_btn.clicked.connect(lambda: self.authorization(login_input.text(), password_input.text()))
        buttons.addWidget(auth_btn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        exit_btn = QtWidgets.QPushButton(parent=central_widget)
        exit_btn.setText("Выйти")
        exit_btn.clicked.connect(lambda: self.exit())
        buttons.addWidget(exit_btn, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        
        # Размещение элементов в окне
        central_interface.addLayout(gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(central_widget)
        
    def authorization(self, login, password):
        """Функция авторизации"""
        
        result = auth_check(login, password)
        
        if result:
            self.close()
            self.window = PersonalAccount(self)
            self.window.show()
        else:
           QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")
        
    def exit(self):
        """Выход из приложения"""
        
        self.close()