import random
from cryptography.fernet import Fernet
import base64
import hashlib


# ==================================================
# 1. ENCRYPTION
# ==================================================

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


# ==================================================
# 2. INNOCUOUS TEXT GENERATOR
# ==================================================

sentences = [

    "The students attended their classes in the morning.",

    "They later visited the library to complete their assignments.",

    "The weather was pleasant throughout the afternoon.",

    "Many students discussed their work with their classmates.",

    "The library remained quiet during the study hours.",

    "Everyone returned home after completing their daily activities.",

    "The students prepared notes for their upcoming examination.",

    "Some students spent time reading useful materials.",

    "The afternoon lecture ended earlier than expected.",

    "The students planned to continue their studies the next morning.",

    "The roads were relatively quiet during the evening.",

    "The college campus was peaceful after the classes ended.",

    "Several students worked together on their academic projects.",

    "The teacher explained the topic during the morning session.",

    "The students completed their laboratory work before lunch.",

    "After the class, some students discussed their assignments.",

    "The students gathered in the classroom before the lecture.",

    "The professor provided useful examples during the lesson.",

    "The students spent the evening preparing their project work.",

    "The library provided a comfortable place for studying.",

    "Several students reviewed their notes before the examination.",

    "The class ended after the students completed their activities.",

    "The students discussed different ideas for their project.",

    "The campus became quieter after the afternoon classes.",

    "The students returned to their homes after completing their work."

]


def generate_text(required_words):

    generated_words = []

    while len(generated_words) < required_words:

        sentence = random.choice(sentences)

        words = sentence.split()

        generated_words.extend(words)

    return " ".join(generated_words)


# ==================================================
# 3. TEXT TO BINARY
# ==================================================

def text_to_binary(message):

    binary = ""

    for character in message:

        binary += format(
            ord(character),
            "08b"
        )

    return binary


# ==================================================
# 4. STEGANOGRAPHY ENCODER
# ==================================================

def encode_message(message, cover_text):

    binary_message = text_to_binary(message)

    # Special ending marker
    binary_message += "1111111111111110"

    words = cover_text.split()

    if len(binary_message) > len(words):

        return None

    stego_words = []

    for i, word in enumerate(words):

        if i < len(binary_message):

            if binary_message[i] == "0":

                stego_words.append(
                    word + " "
                )

            else:

                stego_words.append(
                    word + "  "
                )

        else:

            stego_words.append(
                word + " "
            )

    return "".join(stego_words)


# ==================================================
# MAIN PROGRAM
# ==================================================

print("==============================================")
print(" SECURE TEXT STEGANOGRAPHY SYSTEM")
print("==============================================")


# Get secret message

message = input(
    "\nEnter your secret message: "
)


# Get password

password = input(
    "Enter password: "
)


# ------------------------------------------
# Encrypt the message
# ------------------------------------------

encrypted_message = encrypt_message(
    message,
    password
)


print("\nMessage encrypted successfully.")


# ------------------------------------------
# Calculate required text length
# ------------------------------------------

required_words = (
    len(encrypted_message) * 8
    + 16
    + 30
)


# ------------------------------------------
# Generate innocent text
# ------------------------------------------

print(
    "\nGenerating innocuous text..."
)


cover_text = generate_text(
    required_words
)


# ------------------------------------------
# Hide encrypted message
# ------------------------------------------

stego_text = encode_message(
    encrypted_message,
    cover_text
)


if stego_text is None:

    print(
        "\nError: Message could not be hidden."
    )

else:

    print(
        "\n=============================================="
    )

    print(
        " GENERATED INNOCUOUS COVER TEXT"
    )

    print(
        "=============================================="
    )

    print(cover_text)


    print(
        "\n=============================================="
    )

    print(
        " FINAL STEGO TEXT"
    )

    print(
        "=============================================="
    )

    print(stego_text)


    print(
        "\nSecret message successfully encrypted "
        "and hidden!"
    )