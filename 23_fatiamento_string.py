"""
Fatiamento de strings
012345678
Olá mundo
-9876543210
Fatiamento [i:f:p] [::]
obs.: a função len() retorna o tamanho da string
"""

variavel = 'Olá mundo'
print(variavel[-4]) # Acessa o quarto caractere a partir do final
print(variavel[4:8]) # Fatiamento da string do índice 4 ao 7

print(len(variavel))  # Imprime o tamanho da string