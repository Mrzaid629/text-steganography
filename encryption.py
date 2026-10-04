from cryptography.fernet import Fernet
import base64
import hashlib


def generate_key(password):

    password_hash = hashlib.sha256(
        password.encode()
    ).digest()

    key = base64.urlsafe_b64encode(password_hash)

    return key


def encrypt_message(message, password):

    key = generate_key(password)

    cipher = Fernet(key)

    encrypted_message = cipher.encrypt(
        message.encode()
    )

    return encrypted_message.decode()


def decrypt_message(encrypted_message, password):

    key = generate_key(password)

    cipher = Fernet(key)

    decrypted_message = cipher.decrypt(
        encrypted_message.encode()
    )

    return decrypted_message.decode()


if __name__ == "__main__":

    message = input("Enter message: ")

    password = input("Enter password: ")

    encrypted = encrypt_message(
        message,
        password
    )

    print("\nEncrypted Message:")
    print(encrypted)

    decrypted = decrypt_message(
        encrypted,
        password
    )

    print("\nDecrypted Message:")
    print(decrypted)