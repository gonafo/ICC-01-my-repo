from cryptography.fernet import Fernet

filename = "possíveis_compras.txt"

key = "key.key"

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    decrypted_data = f.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def load_key():
    return open(key, "rb").read()

key = load_key()

decrypt(filename, key)