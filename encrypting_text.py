from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open ("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

write_key()

key = load_key()

print("Key is " + str(key.decode("utf-8")))

message = "teste".encode()
print("Plaintext is " + str(message.decode("utf-8")))

f = Fernet(key)

encrypted = f.encrypt(message)

print("Ciphertext is " + encrypted.decode("utf-8"))