import raesar_cipher as rac

PLAIN_TEXT = "We are going to attack tomorrow be ready"
# PLAIN_TEXT = "yaar tumhy bataya tha na k wo log kal raat ko attack karengy"
# PLAIN_TEXT = "you have to get out of there asap you have been compromised they know"
SIZE = 4
CAESAR_KEY = 4

ROUTE = [
    (0, 0), (1, 0), (2, 0), (3, 0),
    (3, 1), (3, 2), (3, 3), (2, 3),
    (2, 2), (2, 1), (1, 1), (1, 2),
    (1, 3), (0, 3), (0, 2), (0, 1)
]

# ROUTE = [
#     (0, 0), (0, 1), (1, 1), (1, 0),
#     (2, 0), (2, 1), (2, 2), (1, 2),
#     (0, 2), (0, 3), (1, 3), (2, 3),
#     (3, 3), (3, 2), (3, 1), (3, 0)
# ]

# ROUTE = [
#     (0, 0), (0, 2), (3, 3), (3, 0),
#     (2, 1), (1, 2), (0, 1), (1, 3),
#     (3, 2), (2, 2), (3, 1), (1, 0),
#     (0, 3), (1, 1), (2, 3), (2, 0)
# ]

PLAIN_TEXT = input("Enter your message: ")

cipher_text, spaces = rac.encrypt(PLAIN_TEXT, SIZE, ROUTE, CAESAR_KEY)

plain_text = rac.decrypt(cipher_text, spaces, SIZE, ROUTE, CAESAR_KEY)

print(f"Plain text: {PLAIN_TEXT}")
print(f"Final ciphered text: {cipher_text}")
print(f"Final deciphered text: {plain_text}")
