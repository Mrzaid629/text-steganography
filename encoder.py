def text_to_binary(message):
    binary = ""

    for character in message:
        binary += format(ord(character), "08b")

    return binary


def encode_message(message, cover_text):
    binary_message = text_to_binary(message)

    # Add a special ending marker
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


message = input("Enter your secret message: ")

cover_text = input("Enter your cover text: ")

result = encode_message(message, cover_text)

if result is None:
    print("\nCover text is too short!")
else:
    print("\nGenerated Stego Text:")
    print(result)