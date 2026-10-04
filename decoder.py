def binary_to_text(binary):
    message = ""

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            character = chr(int(byte, 2))
            message += character

    return message


def decode_message(stego_text):

    binary = ""

    # Read each character and check spaces
    i = 0

    while i < len(stego_text):

        if stego_text[i] == " ":

            # Check whether there are two spaces
            if i + 1 < len(stego_text) and stego_text[i + 1] == " ":
                binary += "1"
                i += 2

            else:
                binary += "0"
                i += 1

        else:
            i += 1

    # Find the ending marker
    end_marker = "1111111111111110"

    if end_marker in binary:
        binary = binary.split(end_marker)[0]

    if len(binary) == 0:
        return None

    return binary_to_text(binary)


stego_text = input("Enter the stego text: ")

message = decode_message(stego_text)

if message is None:
    print("\nNo hidden message found.")

else:
    print("\nHidden Message:")
    print(message)