# PyQt6 && LIBS
import mysql.connector

import pymysql
import pymysql.cursors
from sshtunnel import SSHTunnelForwarder

from PyQt6.QtWidgets import QApplication, QMessageBox

class Connect(object):
    def __init__(self):
        self.conn = None
        self.cursor =None
        
    def init_connect(self):
        with SSHTunnelForwarder(
                ('port2.aquazond.ru', 268),  # хост и порт SSH-сервера
                ssh_username='test1',
                ssh_password='test1',
                remote_bind_address=('127.0.0.1', 3306)) as server:  # хост и порт базы данных
            self.conn = pymysql.connect(
                host='127.0.0.1',  # локальный хост для соединения с SSH-туннелем
                port=server.local_bind_port,
                user='root',
                password='1234',
                db='diplom'
            )
            
            if self.conn is not None:
                self.cursor = self.conn.cursor()
                
                return True
            else:
                print("Ошибка подключения к БД!")
                return False
    
    
    def commit(self):
        """Коммит БД"""
        
        self.conn.commit()
    
    def close(self):
        """Закрытие соединения"""
        
        self.cursor.close()
        self.conn.close()