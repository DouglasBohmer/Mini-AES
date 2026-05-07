import argparse
import sys
import time
from miniaes_tutorial import start
from miniaes_encrypt import matrix_nibble_generator
from miniaes_decrypt import matrix_nibble_decryptor
from miniaes_crack import brute_force_attack, nibbles_to_text

# [MARCAÇÃO]
def divide_em_blocos(texto):
    if len(texto) % 2 != 0:
        texto += " " 
    return [texto[i:i+2] for i in range(0, len(texto), 2)]

if __name__ == '__main__':
    # [MARCAÇÃO]
    starter = input('Bem-vindo ao Mini AES. Digite \'T=\' para o tutorial ou \'C\' para rodar o programa:\n').strip()
         
    if starter.title() == 'T': 
        print('Vamos comecar o tutorial sobre o miniAES!')
        start()
        
    # [MARCAÇÃO]
    elif starter.title() == 'C' or starter.title() == 'c':
        while True:
            print('\n' + '='*40)
            print("MENU DO SISTEMA MINI-AES")
            print(" [E] - Encriptar frase longa")
            print(" [D] - Decriptar matriz longa")
            print(" [Q] - Quebrar a chave (Forca Bruta)")
            print(" [S] - Sair do programa")
            print('='*40)
            
            opcao = input("Escolha a sua acao: ").strip().upper()
            
            # [MARCAÇÃO]
            if opcao == 'E':
                print('\n--- MODO: ENCRIPTAÇÃO ---')
                texto = input("Digite a palavra ou frase: ")
                chave = input("Digite a chave secreta (max 2 caracteres): ")
                
                blocos_texto = divide_em_blocos(texto)
                matriz_final = []
                
                input("\n---> Pressione ENTER para aplicar o Mini-AES em blocos...")
                
                for bloco in blocos_texto:
                    matriz_cifrada = matrix_nibble_generator(bloco, chave)
                    matriz_final.extend(matriz_cifrada)
                
                print("\n[!] ENCRIPTACAO CONCLUIDA!")
                print("Matriz Cifrada Gerada (Copie toda essa linha):")
                print(" ".join(matriz_final))
                
            # [MARCAÇÃO]
            elif opcao == 'D':
                print('\n--- MODO: DECRIPTAÇÃO ---')
                print("Cole TODOS os nibbles da matriz separados por espaco.")
                matriz_input = input("Matriz Cifrada: ").strip()
                chave_tentativa = input("Digite a chave secreta: ").strip()
                
                matriz_lista = matriz_input.split()
                
                input("\n---> Pressione ENTER para reverter o algoritmo...")
                
                try:
                    texto_recuperado_completo = ""
                    for i in range(0, len(matriz_lista), 4):
                        bloco_matriz = matriz_lista[i:i+4]
                        matriz_decriptada = matrix_nibble_decryptor(bloco_matriz, chave_tentativa)
                        texto_recuperado_completo += nibbles_to_text(matriz_decriptada)
                        
                    print("\n[!] DECRIPTACAO CONCLUIDA!")
                    print(f"A Mensagem Secreta era: '{texto_recuperado_completo}'")
                except Exception as e:
                    print("\n[X] Erro na decriptacao. Verifique se a matriz e a chave estao corretos.")
            
            # [MARCAÇÃO]
            elif opcao == 'Q':
                print('\n--- MODO: ATAQUE DE FORCA BRUTA ---')
                matriz_input = input("Cole a Matriz Cifrada completa: ").strip()
                texto_esperado = input("Texto original esperado (pelo menos as 2 primeiras letras): ").strip()
                
                matriz_lista = matriz_input.split()
                
                primeiro_bloco_matriz = matriz_lista[0:4]
                primeiro_bloco_texto = divide_em_blocos(texto_esperado)[0]
                
                input("\n---> Pressione ENTER para iniciar a varredura das chaves...")
                print('\n' + '-'*30)
                
                chave_quebrada = brute_force_attack(primeiro_bloco_matriz, primeiro_bloco_texto, max_key_len=2)
                
                print('-'*30)
                if chave_quebrada:
                    print(f"\n[$$$] SUCESSO! Criptografia violada!")
                    print(f"[$$$] A chave que trancou toda a mensagem era: '{chave_quebrada}'")
                    
                    # [MARCAÇÃO]
                    texto_recuperado_completo = ""
                    for i in range(0, len(matriz_lista), 4):
                        bloco_matriz = matriz_lista[i:i+4]
                        matriz_decriptada = matrix_nibble_decryptor(bloco_matriz, chave_quebrada)
                        texto_recuperado_completo += nibbles_to_text(matriz_decriptada)
                        
                    print(f"[$$$] Mensagem completa interceptada: '{texto_recuperado_completo}'")
                else:
                    print("\n[X] FALHA. Senha nao encontrada.")
                    
            # [MARCAÇÃO]
            elif opcao == 'S':
                print("Encerrando o sistema...")
                sys.exit()
            else:
                print("Opcao invalida. Tente novamente.")
    else:
        print('Comando nao reconhecido. Rode o programa novamente.')
