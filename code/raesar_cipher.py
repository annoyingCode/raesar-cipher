import route_cipher as rc
import caesar_cipher as cc


def encrypt(input, size, route, key):
    route_output, blocks_space_indices = rc.encrypt(input, size, route)
    caesar_output = cc.encrypt(route_output, key)
    return caesar_output, blocks_space_indices


def decrypt(input, spaces, size, route, key):
    caesar_output = cc.decrypt(input, key)
    route_output = rc.decrypt(caesar_output, spaces, size, route)
    return route_output
