import mysql.connector
from PyQt6.QtWidgets import QApplication, QMessageBox


class Connect(object):
    def __init__(self):

        self.cursor = None
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123',
            database='diplom'
        )
        
        window = QApplication.activeWindow()
        if self.con is None:
            QMessageBox.warning(window, "Ошибка", "Не удалось подключиться к базе данных!")
        else:
            self.cursor = self.con.cursor(dictionary=True)
            
    def close(self):
        self.cursor.close()
        self.con.close()