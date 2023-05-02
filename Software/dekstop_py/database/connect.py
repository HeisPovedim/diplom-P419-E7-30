import mysql.connector
from PyQt6.QtWidgets import QApplication, QMessageBox


class DB(object):
    def __init__(self):
        super().__init__()

        self.cursor = None
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='projectnew'
        )
        window = QApplication.activeWindow()

        if self.con is None:
            QMessageBox.warning(window, "Ошибка", "Не удалось подключиться к базе данных!")
        else:
            QMessageBox.information(window, "Ок", " Удалось подключиться к базе данных!")
            self.cursor = self.con.cursor(dictionary=True)

    