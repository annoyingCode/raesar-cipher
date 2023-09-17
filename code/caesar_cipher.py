def encrypt(input, key):
    input = input.replace(" ", "")
    cipher_text = ""

    # Traverse text
    for i in range(len(input)):
        char = input[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            cipher_text += chr((ord(char) + key-65) % 26 + 65)

        else:
            cipher_text += char

    return cipher_text


def decrypt(input, key):
    plain_text = ""
    key = 26 - key

    # traverse text
    for i in range(len(input)):
        char = input[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            plain_text += chr((ord(char) + key-65) % 26 + 65)

        else:
            plain_text += char

    return plain_text
