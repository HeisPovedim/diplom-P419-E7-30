# DATABASE
from database.connect import Connect

# HELPERS
from helpers.helpers import hash_generation

# LOCALSTORAGE
from data.localstorage import user

# date
from datetime import datetime

def auth_check(login, password):
    """Проверка пользователя на существование"""
    
    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        
        has_password = hash_generation(password)
        cursor.execute(f"SELECT * FROM users WHERE login = '{login}' AND password = '{has_password}'")
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
    
# сохранение результатов полученных при измерении с последовательной схемой

def add_parameters_parallel(freq,gp,rp,cp,id_object):
    date = datetime.today()
        
    formatted_date = date.strftime('%Y-%m-%d')
    default_value = None

    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        sql = f"""INSERT INTO `diplom`.`parameters`
        (`Freq`,
        `z_real_path_parameters`,
        `z_imaginary_part_parameters`,
        `phi_parameters`, `gp_parameters`,
        `rp_parameters`, `cp_parameters`,
        `measurement_date`,
        `objects_idobjects`)
        VALUES ('{freq}',
        '{default_value}',
        '{default_value}',
        '{default_value}',
        '{gp}',
        '{rp}',
        '{cp}',
        '{formatted_date}',
        '{id_object}');"""
        cursor.execute(sql)
        conn.close()
        return True

# функция для проверки объекта на существования
def check_object(id):
    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        sql = "SELECT `name` FROM `objects` WHERE `idobjects`=%s"
        cursor.execute(sql,(id,))
        response = cursor.fetchone()
        return response
# сохранение результатов полученных при измерении с последовательной схемой

def add_parameters_consistent(freq,real,imaginary,phi,id_object):
    date = datetime.today()
        
    formatted_date = date.strftime('%Y-%m-%d')
    default_value = None

    conn = Connect()
    cursor = conn.cursor
    if conn.cursor:
        sql = f"""INSERT INTO `diplom`.`parameters`
        (`Freq`,
        `z_real_path_parameters`,
        `z_imaginary_part_parameters`,
        `phi_parameters`, `gp_parameters`,
        `rp_parameters`, `cp_parameters`,
        `measurement_date`,
        `objects_idobjects`)
        VALUES ('{freq}',
        '{real}',
        '{imaginary}',
        '{phi}',
        '{default_value}',
        '{default_value}',
        '{default_value}',
        '{formatted_date}',
        '{id_object}');"""
        cursor.execute(sql)
        conn.close()
        return True
    