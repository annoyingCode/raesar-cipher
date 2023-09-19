# def create_2D_list(rows, cols):

#     # Create an empty list
#     a_list = []

#     # Create a for loop to append rows
#     for row in range(rows):
#         a_list += [[0] * cols]

#     return a_list


# lst = create_2D_list(3, 4)

# size = 4
# route = {
#     (0, 0): 'H',
#     (1, 0): 'O',
#     (2, 0): 'L',
#     (3, 0): 'W',
#     (3, 1): 'A',
#     (3, 2): 'R',
#     (3, 3): 'E',
#     (2, 3): 'O',
#     (2, 2): 'H',
#     (2, 1): 'D',
#     (1, 1): 'W',
#     (1, 2): 'O',
#     (1, 3): 'R',
#     (0, 3): 'L',
#     (0, 2): 'L',
#     (0, 1): 'E'
# }

# decrypt = create_2D_list(size, size)

# for indices in route:
#     row = indices[0]
#     col = indices[1]
#     decrypt[row][col] = route[indices]

# for i in range(size):
#     for j in range(size):
#         print(decrypt[i][j], end=" ")

import math


def create_blocks(blocks, size):

    # Create an empty list
    block_list = []

    # Create a for loop to append blocks
    for block in range(blocks):
        block_list += [[0] * size]

    # Create a for loop to append columns
    for block in range(blocks):
        for row in range(size):
            block_list[block][row] = [0] * size

    return block_list


def encrypt(input, size, route):
    blocks_space_indices = {}

    plain_text = input.upper()
    cipher_text = ""
    padded_bytes = pow(size, 2) - len(plain_text) % pow(size, 2)

    # Number of blocks
    blocks = math.ceil(len(plain_text) / pow(size, 2))

    # Creating equal size blocks of plain text
    blocks_cipher = create_blocks(blocks, size)

    # Fill up the blocks with characters
    for block_number, block in enumerate(blocks_cipher):

        # Block key to store space indices in dictionary
        block_key = "block_" + str(block_number)

        # List to store space indices (cell positions)
        space_indices = []

        # Fill up a block
        for row in range(size):
            for col in range(size):
                if len(plain_text) > 0:

                    # Space character found and cell position not in space indices list
                    if plain_text[0] == " " and (row, col) not in space_indices:
                        space_indices.insert(0, (row, col))

                    block[row][col] = plain_text[0]
                    plain_text = plain_text[1:]

                # Input text characters are completed. Pad the remaining bytes
                else:
                    block[row][col] = str(padded_bytes)

        blocks_space_indices[block_key] = space_indices

    # Flattening the blocks to a single string
    for block in blocks_cipher:
        for indices in route:
            row, col = indices
            cipher_text += block[row][col]

    return cipher_text, blocks_space_indices


def decrypt(input, spaces, size, route):

    # Output of Caesar decipher
    cipher_text = input
    cipher_text = decimal_to_hex(cipher_text)

    # Number of blocks
    blocks = math.ceil(len(cipher_text) / pow(size, 2))

    # Create blocks
    blocks_decipher = create_blocks(blocks, size)

    # Getting the block number as indicies keys (Dict)
    block_numbers = spaces.keys()

    # Fill the blocks with the characters (Route Decipher)
    for block, block_number in zip(blocks_decipher, block_numbers):
        _indices = spaces[block_number]

        for route_indices in route:
            row, col = route_indices
            if (route_indices) in _indices:
                block[row][col] = " "
            else:
                block[row][col] = cipher_text[0]
                cipher_text = cipher_text[1:]

    # Flattening the 3D blocks list into a single string
    deciphered_text = ""
    for block in blocks_decipher:
        for row in range(size):
            for col in range(size):
                char = block[row][col]
                if (char.isalpha() or char == " ") and (not char.islower()):
                    deciphered_text += block[row][col]

    return deciphered_text


def decimal_to_hex(input):
    i = 0
    while i < len(input):

        if not input[i].isdigit():
            i += 1
            continue

        # For two digit numbers (10 to 15)
        elif (i + 1) < len(input) and input[i] == "1" and (input[i+1] >= "0" and input[i+1] <= "5"):
            number = int(input[i:i+2])

            # Get the hex form of the number (0x)
            hex_string = hex(number)

            # Remove the 0x prefix
            hex_string = hex_string[2:]

            # Replace the hex form of the integer (e.g. 15 to F)
            input = input[:i] + hex_string + input[i+2:]

        # For one digit numbers (1 to 9)
        else:
            number = int(input[i])

            # Get the hex form of the number (0x)
            hex_string = hex(number)

            # Remove the 0x prefix
            hex_string = hex_string[2:]

            # Replace the hex form of the integer (e.g. 1 to 9)
            input = input[:i] + hex_string + input[i+1:]

        i += 1

    return input
