#Usando a funcao input para coletar dados do usuario
#input é uma funçao

nome = input ('Qual é o seu nome? ')
print (f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print (f'A Soma dos numeros é: {numero_1 + numero_2}')  # Isso não vai somar os números corretamente, pois input retorna strings
