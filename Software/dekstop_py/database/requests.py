# DATABASE
from database.connect import Connect

# HELPERS
from helpers.helpers import hash_generation

# LOCALSTORAGE
from data.localstorage import user

def auth_check(login, password):
    """Проверка пользователя на существование"""
    
    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        
        has_password = hash_generation(password)
        cursor.execute(f"SELECT * FROM personals WHERE login = '{login}' AND password = '{has_password}'")
        personal = cursor.fetchone()

        if personal:
            # conn.close()
            user['username'] = login
            return True
        else:
            # conn.close()
            return False
        
def get_parameters(id, type):
    """
        Получение параметров объекта
        id - номер получаемого объекта
        type - обозначает тип получаемых параметров, т.е. TRUE получить все из таблицы,
        а FALSE получить все из таблицы по определенному id
    """

    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        if type:
            cursor.execute("SELECT * FROM parameters")
            conn.close()
            return cursor.fetchall()
        else:
            cursor.execute(f"SELECT * FROM parameters WHERE objects_idobjects = '{id}'")
            conn.close()
            return [list(item.values()) for item in cursor.fetchall()]
        
def get_objects():
    """Получение списка объектов"""
    
    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        cursor.execute("SELECT * FROM objects")
        conn.close()
        return cursor.fetchall()