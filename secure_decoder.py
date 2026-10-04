from cryptography.fernet import Fernet, InvalidToken
import base64
import hashlib


# ==========================================
# 1. GENERATE ENCRYPTION KEY
# ==========================================

def generate_key(password):

    password_hash = hashlib.sha256(
        password.encode()
    ).digest()

    key = base64.urlsafe_b64encode(
        password_hash
    )

    return key


# ==========================================
# 2. DECRYPT MESSAGE
# ==========================================

def decrypt_message(encrypted_message, password):

    key = generate_key(password)

    cipher = Fernet(key)

    decrypted_message = cipher.decrypt(
        encrypted_message.encode()
    )

    return decrypted_message.decode()


# ==========================================
# 3. BINARY TO TEXT
# ==========================================

def binary_to_text(binary):

    message = ""

    for i in range(0, len(binary), 8):

        byte = binary[i:i + 8]

        if len(byte) == 8:

            character = chr(
                int(byte, 2)
            )

            message += character

    return message


# ==========================================
# 4. EXTRACT HIDDEN DATA
# ==========================================

def extract_message(stego_text):

    binary = ""

    i = 0

    while i < len(stego_text):

        if stego_text[i] == " ":

            # Two spaces = 1
            if (
                i + 1 < len(stego_text)
                and stego_text[i + 1] == " "
            ):

                binary += "1"

                i += 2

            # One space = 0
            else:

                binary += "0"

                i += 1

        else:

            i += 1


    # Ending marker
    end_marker = "1111111111111110"


    if end_marker not in binary:

        return None


    binary = binary.split(
        end_marker
    )[0]


    if len(binary) == 0:

        return None


    return binary_to_text(binary)


# ==========================================
# MAIN PROGRAM
# ==========================================

print("==============================================")
print(" SECURE TEXT STEGANOGRAPHY DECODER")
print("==============================================")


# ------------------------------------------
# Get stego text
# ------------------------------------------

print("\nPaste the complete stego text below.")

stego_text = input("\nStego Text: ")


# ------------------------------------------
# Extract encrypted message
# ------------------------------------------

encrypted_message = extract_message(
    stego_text
)


if encrypted_message is None:

    print(
        "\nNo hidden message was found."
    )

else:

    print(
        "\nHidden encrypted data extracted."
    )


    # --------------------------------------
    # Password
    # --------------------------------------

    password = input(
        "Enter password: "
    )


    try:

        decrypted_message = decrypt_message(
            encrypted_message,
            password
        )


        print(
            "\n=============================================="
        )

        print(
            " RECOVERED SECRET MESSAGE"
        )

        print(
            "=============================================="
        )

        print(
            decrypted_message
        )


        print(
            "\nMessage successfully decrypted!"
        )


    except InvalidToken:

        print(
            "\nIncorrect password or corrupted data."
        )