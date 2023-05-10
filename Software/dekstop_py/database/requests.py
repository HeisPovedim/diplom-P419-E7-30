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
    response = conn.cursor
    if response:
        
        has_password = hash_generation(password)
        cursor.execute(f"SELECT * FROM personals WHERE login = '{login}' AND password = '{has_password}'")
        personal = cursor.fetchone()
        print(personal)

        if personal:
            # conn.close()
            user['username'] = login
            return True
        else:
            # conn.close()
            return False