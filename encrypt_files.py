from cryptography.fernet import Fernet

filename = "possíveis_compras.txt"

key = "key.key"

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def load_key():
    return open(key, "rb").read()

key = load_key()

encrypt(filename, key)
