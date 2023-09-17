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


def encrypt(input, blocks, size, route):
    plain_text = input
    cipher_text = ""
    padded_bytes = len(plain_text) % pow(size, 2)
    blocks_cipher = create_blocks(blocks, size)

    # Fill up the blocks with characters
    for block in blocks_cipher:
        for row in range(size):
            for col in range(size):
                if len(plain_text) > 0:
                    block[row][col] = plain_text[0]
                    plain_text = plain_text[1:]
                else:
                    block[row][col] = str(padded_bytes)

    # Flattening the blocks to a single string
    for block in blocks_cipher:
        for i, indices in enumerate(route):
            row = indices[0]
            col = indices[1]
            cipher_text += block[row][col]

    return cipher_text


def decrypt(input, blocks, size, spaces, route):

    # Output of Caesar decipher
    cipher_text = input

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

    # Flatten the 3D blocks list into 1D string
    deciphered_text = ""
    for block in blocks_decipher:
        for row in range(size):
            for col in range(size):
                char = block[row][col]
                if char.isalpha() or char == " ":
                    deciphered_text += block[row][col]

    return deciphered_text
