import raesar_cipher as rac

PLAIN_TEXT = "WE ARE GOING TO ATTACK TOMORROW BE READY"
BLOCKS = 3
SIZE = 4
CAESAR_KEY = 4

SPACE_INDICES = {
    "block_1": [(3, 0), (3, 3), (1, 2), (0, 2)],
    "block_2": [(3, 3), (1, 2)],
    "block_3": [(0, 2)]
}

ROUTE = [
    (0, 0), (1, 0), (2, 0), (3, 0),
    (3, 1), (3, 2), (3, 3), (2, 3),
    (2, 2), (2, 1), (1, 1), (1, 2),
    (1, 3), (0, 3), (0, 2), (0, 1)
]

cipher_text = rac.encrypt(PLAIN_TEXT, BLOCKS, SIZE, ROUTE, CAESAR_KEY)

plain_text = rac.decrypt(cipher_text, BLOCKS, SIZE,
                         SPACE_INDICES, ROUTE, CAESAR_KEY)

print(f"Plain text: {PLAIN_TEXT}")
print(f"Final ciphered text: {cipher_text}")
print(f"Final deciphered text: {plain_text}")
