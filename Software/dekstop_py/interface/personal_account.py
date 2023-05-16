# PyQt6 && LIBS
from PyQt6 import QtCore, QtGui, QtWidgets

# IMPORT WINDOWS
from interface.graph_widget import GraphWidget
from interface.run_script import RunScript
from interface.list_object import ListObject

# LOCALSTORAGE
from data.localstorage import user

class PersonalAccount(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
    
        # Настройки окна
        self.setWindowTitle("Личный кабинет")
        self.resize(298, 84)
        
        # self.parent_window = parent
        
        self.setupUi()
    
    def setupUi(self):
        """Интерфейс окна"""
        
        # Выравнивание элементов по центру
        central_widget = QtWidgets.QWidget(parent=self)
        central_interface = QtWidgets.QGridLayout(central_widget)
        
        # Создание сетки
        gridLayout = QtWidgets.QGridLayout()
        
        # логин
        login = QtWidgets.QLabel(parent=central_widget)
        login.setText(f"Логин: {user['username']}")
        login.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        login.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading |
            QtCore.Qt.AlignmentFlag.AlignLeft |
            QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        login.setWordWrap(False)
        gridLayout.addWidget(login, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        # кнопка "Выйти"
        exit_btn = QtWidgets.QPushButton(parent=central_widget)
        exit_btn.setText("Выйти")
        exit_btn.clicked.connect(lambda: self.exit())
        gridLayout.addWidget(exit_btn, 0, 1, 1, 1)

        # кнопка "Запустить скрипт"
        run_script_btn = QtWidgets.QPushButton(parent=central_widget)
        run_script_btn.setText("Измерение пьезокерамики")
        run_script_btn.clicked.connect(lambda: self.open_run_script())
        gridLayout.addWidget(run_script_btn, 1, 0, 1, 1)
        
        # копка "Открыть графики"
        open_graph_btn = QtWidgets.QPushButton(parent=central_widget)
        open_graph_btn.setText("Меню графиков")
        open_graph_btn.clicked.connect(lambda: self.open_graph_widget())
        gridLayout.addWidget(open_graph_btn, 1, 1, 1, 1)
        
        # копка "Список объектов"
        open_graph_btn = QtWidgets.QPushButton(parent=central_widget)
        open_graph_btn.setText("Открыть список объектов")
        open_graph_btn.clicked.connect(lambda: self.open_list_object())
        gridLayout.addWidget(open_graph_btn, 2, 0, 1, 1)
        
        # Размещение элементов в окне
        central_interface.addLayout(gridLayout, 0, 0, 1, 1)
        self.setCentralWidget(central_widget)
        
    def open_list_object(self):
        """Открыть список объектов"""
        
        self.window_list_object = ListObject()
        self.window_list_object.show()
        
        
    def open_graph_widget(self):
        """Открытие графиков"""
        
        self.window_graph_widget = GraphWidget()
        self.window_graph_widget.show()
        
    def open_run_script(self):
        """Открытие окна запуска скрипта"""
        
        self.close()
        self.window_run_script = RunScript(self)
        self.window_run_script.show()
        
    def exit(self):
        """Выход и переход к окну авторизации"""
        
        self.close()
        self.parent_window.show()