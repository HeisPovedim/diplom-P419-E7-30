import mysql.connector
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget


class Connection(object):
    def __init__(self):
        super().__init__()
        
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='mydb'
        )

        print(self.con)
        if self.con is None:
            window = QApplication.activeWindow()
            # QMessageBox.warning(window, "Ошибка", "Не удалось подключиться к базе данных!")
            print("Ошибка")
        else:
            print("Ошибка")
            self.cursor = self.con.cursor(dictionary=True)