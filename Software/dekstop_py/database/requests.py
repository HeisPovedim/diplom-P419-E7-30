from database.connect import Connect
from helpers.helpers import hash_generation

def auth_check(login, password):
    """Проверка пользователя на существование"""
    
    conn = Connect()
    cursor = conn.cursor
    
    has_password = hash_generation(password)
    sql = "SELECT login, password FROM personals WHERE login = %s AND password = %s"
    cursor.execute(sql, (login, has_password))
    print(cursor.fetchone())