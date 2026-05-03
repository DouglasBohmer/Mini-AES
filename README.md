⚠️ Aviso Importante
Este projeto tem fins estritamente educacionais e acadêmicos. Devido ao tamanho reduzido da chave (16 bits), a criptografia gerada por este código é extremamente frágil e vulnerável a ataques de força bruta básicos. NÃO utilize este algoritmo para proteger dados sensíveis, senhas ou informações reais.

\# Mini-AES 

Projeto educacional de criptografia implementando uma versão simplificada do Advanced Encryption Standard (AES). 

Enquanto o AES padrão da indústria utiliza blocos de 128 bits para garantir a segurança dos dados, este Mini-AES foi projetado com blocos de \*\*16 bits\*\* (suportando blocos de 2 caracteres). Essa redução intencional permite que a matemática do algoritmo seja estudada de forma visual e didática, sendo ideal para estudantes de cibersegurança e desenvolvedores que desejam entender as entranhas da criptografia.

\## Funcionalidades

O sistema conta com um menu interativo pelo terminal, oferecendo as seguintes operações:

\*   \*\*🎓 Tutorial Interativo:\*\* Uma explicação passo a passo das operações internas (Nibbles, \*NibbleSub\*, \*ShiftRow\*, \*MixColumn\* e \*KeyAddition\*).
\*   \*\*🔒 Encriptação (Modo ECB):\*\* Converte palavras e frases longas em matrizes de bits cifrados usando uma chave de 2 caracteres.
\*   \*\*🔓 Decriptação:\*\* Reverte a matriz cifrada para o texto legível através das funções matemáticas inversas (ex: \*Inverse ShiftRow\*).
\*   \*\*⚔️ Criptoanálise (Força Bruta):\*\* Um script de ataque que explora o baixo espaço de chaves (16 bits) para testar todas as combinações possíveis e quebrar a criptografia em milissegundos, revelando a senha e a mensagem completa.

\## Como Executar

Certifique-se de ter o Python instalado na sua máquina.

1\. Clone o repositório:
&#x20;  ```bash
&#x20;  git clone \[https://github.com/SEU\_USUARIO/NOME\_DO\_REPOSITORIO.git](https://github.com/SEU\_USUARIO/NOME\_DO\_REPOSITORIO.git)

