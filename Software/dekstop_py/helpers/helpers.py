from hashlib import sha256
def hash_generation(value):
    """Функция хеширования"""
    
    result = sha256(str(value).encode('utf-8')).hexdigest()
    return result