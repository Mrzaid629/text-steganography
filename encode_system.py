import random


# --------------------------------
# Innocuous Text Generator
# --------------------------------

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


# --------------------------------
# Generate Innocuous Text
# --------------------------------

def generate_text(required_words):

    generated_words = []

    while len(generated_words) < required_words:

        sentence = random.choice(sentences)

        words = sentence.split()

        generated_words.extend(words)

    return " ".join(generated_words)


# --------------------------------
# Convert Message to Binary
# --------------------------------

def text_to_binary(message):

    binary = ""

    for character in message:

        binary += format(ord(character), "08b")

    return binary


# --------------------------------
# Encode Message
# --------------------------------

def encode_message(message, cover_text):

    binary_message = text_to_binary(message)

    # End marker
    binary_message += "1111111111111110"

    words = cover_text.split()

    if len(binary_message) > len(words):

        return None

    stego_words = []

    for i, word in enumerate(words):

        if i < len(binary_message):

            if binary_message[i] == "0":

                stego_words.append(word + " ")

            else:

                stego_words.append(word + "  ")

        else:

            stego_words.append(word + " ")

    return "".join(stego_words)


# --------------------------------
# Main Program
# --------------------------------

print("====================================")
print(" TEXT STEGANOGRAPHY SYSTEM")
print("====================================")


message = input("\nEnter your secret message: ")


# Calculate required number of words
required_words = len(message) * 8 + 16

# Add extra words for safety
required_words = required_words + 20


print("\nGenerating innocuous text...")

cover_text = generate_text(required_words)


print("\nGenerated Innocuous Cover Text:")
print("------------------------------------")
print(cover_text)


result = encode_message(message, cover_text)


if result is None:

    print("\nMessage is too long for the generated text.")

else:

    print("\nGenerated Stego Text:")
    print("------------------------------------")
    print(result)

    print("\nSecret message successfully hidden!")