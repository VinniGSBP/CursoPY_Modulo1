#Operadores in e not in
#Strings sao iteaveis
#0 1 2 3 4 5 6 7
#v i n i c i u s
#-6 -5 -4 -3 -2 -1

nome = 'Vinicius'

print(nome[0])  # Imprime o primeiro caractere
print(nome[1])  # Imprime o segundo caractere
print(nome[2])  # Imprime o terceiro caractere
print(nome[2])  # Imprime o terceiro caractere
print(nome[5])  # Imprime o sexto caractere

print(10 * '-')
print('vini' not in nome)  # Verifica se 'vini' não está em 'Vinicius'
 
print (10* '-')
 
nome2 = input('Digite seu nome: ')
encontrar = input('O que deseja encontrar? ')

if encontrar in nome2:
    print (f'{encontrar} está em {nome2}')
else:
    print (f'{encontrar} não está em {nome2}') 