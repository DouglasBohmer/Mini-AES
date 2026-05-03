from miniaes_functions import *

# [MARCAÇÃO]
nibble_size = 4  
const_column = nibbles_to_bits(['0011','1010','1010','0011']) 

def inverse_mix_column(string_matrix):
    # [MARCAÇÃO]
    res = []
    for i in range(0, len(string_matrix)):
        # [MARCAÇÃO]
        val1 = string_matrix[i]
        val2 = const_column[i % nibble_size].replace('0b', '').zfill(4)
        
        xor_val = ""
        for b1, b2 in zip(val1, val2):
            xor_val += '1' if b1 != b2 else '0'
        res.append(xor_val)
    return res

def inverse_shift_row(substring):
    # [MARCAÇÃO]
    new_string = []
    for i in range(len(substring)):
        tmp_str = ''
        tmp_str += substring[i][0]
        tmp_str += substring[i][3]
        tmp_str += substring[i][2]
        tmp_str += substring[i][1]
        new_string.append(tmp_str)
    return new_string

def inverse_nibble_sub(nibblestr):
    # [MARCAÇÃO]
    substitute = []
    for i in range(len(nibblestr)):
        if nibblestr[i] == '1110':
            substitute.append('0000')
        elif nibblestr[i] == '0100':
            substitute.append('0001')
        elif nibblestr[i] == '1101':
            substitute.append('0010')
        elif nibblestr[i] == '0001':
            substitute.append('0011')
        elif nibblestr[i] == '0010':
            substitute.append('0100')
        elif nibblestr[i] == '1111':
            substitute.append('0101')
        elif nibblestr[i] == '1011':
            substitute.append('0110')
        elif nibblestr[i] == '1000':
            substitute.append('0111')
        elif nibblestr[i] == '0011':
            substitute.append('1000')
        elif nibblestr[i] == '1010':
            substitute.append('1001')
        elif nibblestr[i] == '0110':
            substitute.append('1010')
        elif nibblestr[i] == '1100':
            substitute.append('1011')
        elif nibblestr[i] == '0101':
            substitute.append('1100')
        elif nibblestr[i] == '1001':
            substitute.append('1101')
        elif nibblestr[i] == '0000':
            substitute.append('1110')
        elif nibblestr[i] == '0111':
            substitute.append('1111')
    return substitute

def key_addition(step_data, key_matrix):
    # [MARCAÇÃO]
    result = []
    for i in range(len(step_data)):
        val_step = step_data[i]
        val_key = key_matrix[i % len(key_matrix)].replace('0b', '').zfill(4)
        
        xor_result = ""
        for b1, b2 in zip(val_step, val_key):
            xor_result += '1' if b1 != b2 else '0'
        result.append(xor_result)
    return result

def matrix_nibble_decryptor(ciphertext_matrix, key):
    # [MARCAÇÃO]
    key_bitstring = string_to_binary(key)
    key_matrix = generate_matrix(key_bitstring)
    
    # [MARCAÇÃO]
    step_1 = key_addition(ciphertext_matrix, key_matrix)
    step_2 = inverse_mix_column(step_1)
    step_3 = inverse_shift_row(step_2)
    step_4 = inverse_nibble_sub(step_3)
    
    # [MARCAÇÃO]
    return step_4