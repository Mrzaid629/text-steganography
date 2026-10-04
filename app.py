import streamlit as st
from cryptography.fernet import Fernet
import base64
import hashlib
import random


# -------------------------------
# Generate encryption key
# -------------------------------

def generate_key(password):
    password_hash = hashlib.sha256(password.encode()).digest()
    key = base64.urlsafe_b64encode(password_hash)
    return key


# -------------------------------
# Encrypt message
# -------------------------------

def encrypt_message(message, password):
    key = generate_key(password)
    cipher = Fernet(key)

    encrypted_message = cipher.encrypt(
        message.encode()
    )

    return encrypted_message.decode()


# -------------------------------
# Generate innocent text
# -------------------------------

sentences = [
    "Today I attended my regular college classes.",
    "The weather was pleasant in the morning.",
    "I completed my assignment before lunch.",
    "Our teacher explained the topic clearly.",
    "I spent some time studying in the library.",
    "The students discussed the project together.",
    "I had lunch with my friends at college.",
    "The computer lab was busy today.",
    "I worked on my Python program in the evening.",
    "The class started at the usual time.",
    "I reviewed my notes after the lecture.",
    "My friends and I discussed our project work.",
    "The college campus was quiet in the afternoon.",
    "I practiced programming for some time.",
    "We submitted our assignment successfully.",
    "I learned something new during today's class.",
    "The project discussion was useful.",
    "I organized my study materials.",
    "The laboratory session was interesting.",
    "I completed my work before going home.",
    "The students were preparing for the examination.",
    "I spent the evening reviewing important topics.",
    "The teacher gave us a new assignment.",
    "I checked my project files carefully.",
    "The day was productive and useful."
]


def generate_text(required_words):

    generated_words = []

    while len(generated_words) < required_words:

        sentence = random.choice(sentences)

        words = sentence.split()

        generated_words.extend(words)

    return " ".join(generated_words)


# -------------------------------
# Convert text to binary
# -------------------------------

def text_to_binary(message):

    binary = ""

    for character in message:
        binary += format(ord(character), "08b")

    return binary


# -------------------------------
# Hide message
# -------------------------------

def encode_message(message, cover_text):

    binary = text_to_binary(message)

    end_marker = "1111111111111110"

    binary += end_marker

    words = cover_text.split()

    encoded_text = ""

    bit_index = 0

    for word in words:

        encoded_text += word

        if bit_index < len(binary):

            if binary[bit_index] == "0":
                encoded_text += " "

            else:
                encoded_text += "  "

            bit_index += 1

        else:
            encoded_text += " "

    return encoded_text


# -------------------------------
# Decode message
# -------------------------------

def extract_message(stego_text):

    binary = ""

    i = 0

    while i < len(stego_text):

        if stego_text[i] == " ":

            if i + 1 < len(stego_text) and stego_text[i + 1] == " ":

                binary += "1"
                i += 2

            else:

                binary += "0"
                i += 1

        else:

            i += 1

    end_marker = "1111111111111110"

    if end_marker not in binary:
        return None

    binary = binary.split(end_marker)[0]

    if len(binary) == 0:
        return None

    message = ""

    for i in range(0, len(binary), 8):

        byte = binary[i:i + 8]

        if len(byte) == 8:

            character = chr(int(byte, 2))

            message += character

    return message


# -------------------------------
# Decrypt message
# -------------------------------

def decrypt_message(encrypted_message, password):

    key = generate_key(password)

    cipher = Fernet(key)

    decrypted_message = cipher.decrypt(
        encrypted_message.encode()
    )

    return decrypted_message.decode()


# -------------------------------
# Streamlit UI
# -------------------------------

st.set_page_config(
    page_title="Text Steganography",
    page_icon="🔐"
)

st.title("🔐 Text Steganography")

st.write(
    "Text Steganography Using Innocuous Text Generation"
)

st.divider()


operation = st.radio(
    "Select Operation",
    ["Encode Message", "Decode Message"]
)


# ==========================================
# ENCODE
# ==========================================

if operation == "Encode Message":

    st.header("🔒 Encode Secret Message")

    message = st.text_area(
        "Enter your secret message:",
        height=150
    )

    password = st.text_input(
        "Enter password:",
        type="password"
    )

    if st.button("Generate Stego Text"):

        if not message:

            st.warning("Please enter a secret message.")

        elif not password:

            st.warning("Please enter a password.")

        else:

            encrypted_message = encrypt_message(
                message,
                password
            )

            required_words = (
                len(encrypted_message) * 8
                + 16
                + 30
            )

            cover_text = generate_text(
                required_words
            )

            stego_text = encode_message(
                encrypted_message,
                cover_text
            )

            st.success(
                "Secret message successfully encrypted and hidden!"
            )

            st.subheader("Generated Innocuous Stego Text")

            st.text_area(
                "Stego Text:",
                stego_text,
                height=350
            )

            st.download_button(
                "Download Stego Text",
                stego_text,
                file_name="stego_text.txt"
            )


# ==========================================
# DECODE
# ==========================================

else:

    st.header("🔓 Decode Secret Message")

    stego_text = st.text_area(
        "Paste the complete stego text:",
        height=350
    )

    password = st.text_input(
        "Enter password:",
        type="password"
    )

    if st.button("Recover Secret Message"):

        if not stego_text:

            st.warning("Please paste the stego text.")

        elif not password:

            st.warning("Please enter the password.")

        else:

            encrypted_message = extract_message(
                stego_text
            )

            if encrypted_message is None:

                st.error(
                    "No hidden message was found."
                )

            else:

                try:

                    recovered_message = decrypt_message(
                        encrypted_message,
                        password
                    )

                    st.success(
                        "Message successfully decrypted!"
                    )

                    st.subheader(
                        "🔓 Recovered Secret Message"
                    )

                    st.write(
                        recovered_message
                    )

                except Exception:

                    st.error(
                        "Incorrect password or corrupted data."
                    )