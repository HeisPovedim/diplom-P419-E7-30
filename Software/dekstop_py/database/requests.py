# DATABASE
from database.connect import Connect

# HELPERS
from helpers.helpers import hash_generation

# LOCALSTORAGE
from data.localstorage import user

def auth_check(login, password):
    """Проверка пользователя на существование"""
    
    conn = Connect()
    if conn.init_connect():
        
        cursor = conn.cursor
        
        has_password = hash_generation(password)
        cursor.execute(f"SELECT * FROM `personals` WHERE `login` = '{login}' AND `password` = '{has_password}'")

        if cursor.fetchone():
            conn.close()
            user['username'] = login
            return True
        else:
            conn.close()
            return False