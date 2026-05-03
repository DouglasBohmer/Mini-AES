import random
import string

def nibble():
    # [MARCAÇÃO]
    putty = input(
        'Desculpe, nao entendi. Voce gostaria de ouvir sobre ' +
        'nibbles? ' +
        'Digite sim ou nao ')
    if putty == 'sim':
        putty = input(
            'O tamanho de um nibble e de quatro bits. ' +
            'Pode ser pensado como um campo finito. ' +
            'Voce sabe o que e um campo finito? ')
    elif putty == 'nao':
        return
    else:
        nibble()

def start():
    # [MARCAÇÃO]
    putty = input(
        'Para as proximas etapas, por favor digite sim ou nao. ' +
        'Voce gostaria de ouvir sobre os detalhes (nibbles), ' +
        'que sao os componentes do mini-AES? ')
    if putty == 'sim':
        putty = input(
            'O tamanho de um nibble e de quatro bits. ' +
            'Pode ser pensado como um campo finito. ' +
            'Voce sabe o que e um campo finito? ')
        if putty == 'nao':
            print(
                'Um campo finito e uma area de numeros onde as ' +
                'operacoes +, -, * e / sao todas possiveis. ' +
                'Se voce executa-las, permanecera no campo. ' +
                'Pode ser expresso como um polinomio. Por exemplo, ' +
                'o nibble n=1010 seria o polinomio ' +
                'n=1*x^3+0*x^2+1*x^1+0*x^0 ')
            putty = input('Gostaria de ouvir mais sobre campos? ')
            if putty == 'sim':
                print(
                    'Explicar campos para que todos entendam ' +
                    'excede o escopo deste programa. Para mais referencias, ' +
                    'por favor consulte a documentacao original.')
        print('\n')
    elif putty == 'nao':
        pass
    else:
        nibble()

    # [MARCAÇÃO]
    print(
        'No AES, um bloco geralmente consiste em 128 bits de texto que e' +
        ' transformado em 128 bits de texto cifrado e vice-versa. ' +
        'Para o mini-AES, usaremos blocos de 16 bits de tamanho.\n')

    # [MARCAÇÃO]
    putty = input(
        'Voce gostaria de saber como o texto cifrado e ' +
        'gerado a partir do texto original? ')
    if putty == 'sim':
        print('O AES possui os chamados Modos de Operacao, que determinam como ' +
              'o texto cifrado e gerado. ' +
              'O Mini-AES nao os possui. Ele apenas encripta bloco por bloco com a' +
              'chave, sem levar o resultado do bloco anterior em ' +
              'consideracao. Isso e equivalente ao modo inseguro electronic ' +
              'codebook no AES. Ele nao deve ser usado em programas reais.')

    # [MARCAÇÃO]
    print('Agora sabemos um pouco sobre as funcoes internas, ' +
          'que tal comecar a encriptar nossa propria mensagem com o mini-AES?')
    plaintext = input('Digite o texto que voce gostaria de encriptar aqui:\n')
    input('E agora por favor pressione enter para continuar passo a passo. ')
    input(
        '\nOk, entao vamos comecar. Lembra dos nibbles? ' +
        'Seu texto e pego, dividido em Blocos de 16-Bits, e ' +
        'em cada bloco, temos quatro nibbles, cada um consistindo de quatro bits.' +
        'Primeiro, cada nibble e rearranjado em uma matriz. Fica assim: ' +
        '\nb0, b2 \n' +
        'b1, b3 \n' +
        'Onde b e um unico bit no nibble.\n\n')

    # [MARCAÇÃO]
    input('Agora podemos fazer coisas com as matrizes de nibble. ' +
          'Existem quatro operacoes: NibbleSub, que substitui ' +
          '(troca) um nibble por outro.\n')

    # [MARCAÇÃO]
    input(
        'Existe tambem o ShiftRow, que inverte a linha inferior da matriz.' +
        ' Ela entao fica assim:\n' +
        'b0, b2\n' +
        'b3, b1\n' +
        'em vez de:\n' +
        'b0, b2\n' +
        'b1, b3\n')

    # [MARCAÇÃO]
    input('No MixColumn, cada coluna do bloco de entrada e multiplicada ' +
          'por uma matriz constante para obter uma nova coluna. Se voce nao ' +
          'entende multiplicacao de matrizes, voce deve pesquisar sobre isso ' +
          'antes de continuar. \n')

    # [MARCAÇÃO]
    key = input(
        'Para garantir que apenas pessoas autorizadas possam acessar e decifrar os ' +
        'arquivos, uma chave e criada para ser compartilhada com pessoas confiaveis.\n' +
        'Para fins de demonstracao, voce pode agora criar sua propria chave:\n')
    if len(key) == 1:
        key = input(
            'A chave precisa ter pelo menos duas letras. Por favor, insira duas.')
    if len(key) == 1:
        key = input(
            'A chave precisa ser maior. Vou criar uma para voce agora: ')
        for i in range(16):
            key += random.choice(string.ascii_uppercase +
                                 string.ascii_lowercase + string.digits)
            print(str(key) + '\n')
    if not key:
        print('Voce nao inseriu uma chave. Para continuar, eu criei uma: ')
        for i in range(16):
            key += random.choice(string.ascii_uppercase +
                                 string.ascii_lowercase + string.digits)
        print(str(key) + '\n')
        input(
            'Lembre-se, este programa e puramente educacional! O texto cifrado ' +
            'resultante e facil de quebrar e nao deve ser usado ' +
            'para dados sensiveis!')

    # [MARCAÇÃO]
    input('Nós agora vamos usar a chave para a ultima ' +
          'operacao, o KeyAddition. Para isso, o bloco recebe um XOR (' +
          'OU exclusivo) em conjunto com a chave.\n')

    # [MARCAÇÃO]
    input('Agora, existem tres chaves geradas a partir da chave original. ' +
          'Elas serao chamadas de K0, K1 e K2, e sao usadas ' +
          'em cada rodada de encriptacao do texto. Uma rodada e uma passagem '
          'do texto pelo procedimento. O AES usa '
          'de 10 a 14, dependendo do tamanho da chave.\n')

    # [MARCAÇÃO]
    input('Para a primeira rodada, a chave de saida, K0, ' +
          'sera apenas a nossa chave original, ambas com 16 bits. ' +
          'Se a nossa chave for maior, nao importa, pois apenas os primeiros ' +
          '16 bits serao usados. ')
    input('K0 e usada antes da primeira rodada. O texto original e agora passado ' +
          'pelas operacoes que acabamos de conhecer, que ' +
          'sao usadas na seguinte ordem: \n' +
          'NibbleSub, ShiftRow, MixColumn, KeyAddition, onde a ' +
          'chave recebe um XOR com o resultado intermediario, outro NibbleSub ' +
          'e outro ShiftRow, resultando no primeiro bloco cifrado: ')
    print('              ___        ___        _____        ____ \n' +
          '             |   |      |  /|      | ^ ^ |      |\\  /|\n' +
          'Texto Orig-->| S |----->| / |----->| | | |----->| \\/ |\n' +
          '             |___|      |/__|      |_|_|_|      |_/\\_|\n\n' +
          '            NibbleSub  ShiftRow    MixColumn    KeyAddition \n' +
          '                                                   |   \n' +
          '               ____________________________________|   \n' +
          '              |                                        \n' +
          '             \ /\n' +
          '              ___        ___        _____ \n' +
          '             |   |      |  /|      |ccccc|\n' +
          '             | S |----->| / |----->|ccccc|\n' +
          '             |___|      |/__|      |ccccc|\n\n' +
          '            NibbleSub  ShiftRow  Texto Cifrado \n')