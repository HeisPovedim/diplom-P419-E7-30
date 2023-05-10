import pymysql
from sshtunnel import SSHTunnelForwarder

with SSHTunnelForwarder(
        ('port2.aquazond.ru', 268),  # хост и порт SSH-сервера
        ssh_username='test1',
        ssh_password='test1',
        remote_bind_address=('127.0.0.1', 3306)) as server:  # хост и порт базы данных
    conn = pymysql.connect(
        host='127.0.0.1',  # локальный хост для соединения с SSH-туннелем
        port=server.local_bind_port,
        user='root',
        password='1234',
        db='diplom')
    # используем соединение для выполнения запросов к базе данных
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personals')
    results = cursor.fetchall()
    print(results)
    conn.close()