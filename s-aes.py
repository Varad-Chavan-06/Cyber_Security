#s-aes program

def xor(a, b):
    output = ""
    for i, j in zip(a, b):
        if i != j:
            output += '1'
        else:
            output += '0'
    return output

def rotate_key(key):
    return key[1:] + key[0]

def g_function(key, rcon=1):
    n1 = key[:4]
    n0 = key[4:]

    n0 = rotate_key(n0)
    n1 = rotate_key(n1)

    print(f"After rotate: \nn0: {n0}\nn1: {n1}")

    s_box = {'0000': '1001',
            '0001': '0100',
            '0010': '1010',
            '0011': '1011',
            '0100': '1101',
            '0101': '0001',
            '0110': '1000',
            '0111': '0101',
            '1000': '0110',
            '1001': '0010',
            '1010': '0000',
            '1011': '0011',
            '1100': '1100',
            '1101': '1110',
            '1110': '1111',
            '1111': '0111'
            }

    n_1 = s_box[n1]
    n_0 = s_box[n0]

    rcon1 = '10000000'
    rcon2 = '00110000'

    if rcon == 1:
        return xor(rcon1, n_0 + n_1)
    if rcon == 2:
        return xor(rcon2, n_0 + n_1)

def key_Generator(binary_key):
    w0 = binary_key[:8]
    w1 = binary_key[8:]

    gw1 = g_function(w1, rcon=1)

    w2 = xor(w0, gw1)
    w3 = xor(w2, w1)

    gw3 = g_function(w3, rcon=2)

    w4 = xor(w2, gw3)
    w5 = xor(w4, w3)

    key0 = w0 + w1
    key1 = w2 + w3
    key2 = w4 + w5

    print(f"\nw0: {w0}\nw1: {w1}\nw2: {w2}\nw3: {w3}\nw4: {w4}\nw5: {w5}")

    return key0, key1, key2

key = input("Enter a 16-bit Binary key: ")
key0, key1, key2 = key_Generator(key)

print(f"\nKey 0: {key0}\nKey 1: {key1}\nKey 2: {key2}")
