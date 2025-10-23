#Formatação basica de strings
#s - string
#d e i - int
#f - float
#.<numero de digitos>f
#x ou X - hexadecimal (ABCDEF01233456789)
#(caractere) (><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centralizado
# Sinal + ou - 
# EX.: 0>-100,.1f
#Conversion flags - !r, !s, !a

variavel = 'abc'
print (f'{variavel}')  # Imprime a variável como string
print(f'{variavel: >10}')  # Imprime a variável com 10 caracteres à direita
print(f'{variavel: <10}')  # Imprime a variável com 10 caracteres à esquerda
print(f'{variavel: ^10}')  # Imprime a variável centralizada em 10 caracteres
print(f'{variavel:!^10}')  # Imprime a variável centralizada com '!' como preenchimento
print(f'{variavel:!<10}')  # Imprime a variável à esquerda com '!' como preenchimento
print(f'{variavel:!>10}')  # Imprime a variável à direita com '!' como preenchimento


print(f'{1000.43123128391273:+,.1f}')