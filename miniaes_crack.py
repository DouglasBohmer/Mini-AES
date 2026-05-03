import string
import itertools
import time
from miniaes_encrypt import matrix_nibble_generator
from miniaes_decrypt import matrix_nibble_decryptor

# [MARCAÇÃO]
def nibbles_to_text(nibble_matrix):
    bit_string = "".join(nibble_matrix)
    chars = []
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return "".join(chars)

# [MARCAÇÃO]
def brute_force_attack(ciphertext_matrix, expected_plaintext, max_key_len=2):
    characters = string.ascii_letters + string.digits
    
    # [MARCAÇÃO]
    for length in range(1, max_key_len + 1):
        for guess_tuple in itertools.product(characters, repeat=length):
            guess_key = "".join(guess_tuple)
            
            # [MARCAÇÃO]
            # Imprime cada tentativa na tela para o efeito visual da apresentacao
            print(f"[*] Tentando chave: {guess_key}")
            time.sleep(0.002) # Pausa de 2 milissegundos para dar efeito de "varredura"
            
            # [MARCAÇÃO]
            decrypted_matrix = matrix_nibble_decryptor(ciphertext_matrix, guess_key)
            decrypted_text = nibbles_to_text(decrypted_matrix)
            
            # [MARCAÇÃO]
            if decrypted_text == expected_plaintext:
                return guess_key
    return None

# [MARCAÇÃO]
if __name__ == '__main__':
    texto_original = "Oi"
    chave_secreta = "X7" 
    
    # [MARCAÇÃO]
    print("Gerando texto cifrado...")
    matriz_cifrada = matrix_nibble_generator(texto_original, chave_secreta)
    print("Matriz Cifrada:", matriz_cifrada)
    
    # [MARCAÇÃO]
    print("\nIniciando ataque de forca bruta...")
    chave_encontrada = brute_force_attack(matriz_cifrada, texto_original, max_key_len=2)
    
    if chave_encontrada:
        print("\nSUCESSO! A chave foi quebrada.")
        print("Chave original utilizada:", chave_encontrada)
    else:
        print("\nFALHA. Chave nao encontrada nos parametros definidos.")