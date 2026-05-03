# [MARCAÇÃO]
nibble_size = 4

def string_to_binary(string):
    # [MARCAÇÃO]
    binary_rep = ''.join('{0:08b}'.format(ord(x), 'b') for x in string)
    return binary_rep

def generate_matrix(binary):
    # [MARCAÇÃO]
    matrix = [binary[i:i + nibble_size]
              for i in range(0, len(binary), nibble_size)]
    return matrix

def nibbles_to_bits(nibbles):
    # [MARCAÇÃO]
    binary = []
    for i in range(0, len(nibbles)):
        tmp = str(nibbles[i])
        binary.append(bin(int(tmp, 2)))
    return(binary)

def string_bitwise_xor(s1, s2):
    # [MARCAÇÃO]
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))