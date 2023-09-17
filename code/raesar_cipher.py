import route_cipher as rc
import caesar_cipher as cc


def encrypt(input, blocks, size, route, key):
    route_output = rc.encrypt(input, blocks, size, route)
    caesar_output = cc.encrypt(route_output, key)
    return caesar_output


def decrypt(input, blocks, size, spaces, route, key):
    caesar_output = cc.decrypt(input, key)
    route_output = rc.decrypt(caesar_output, blocks, size, spaces, route)
    return route_output
