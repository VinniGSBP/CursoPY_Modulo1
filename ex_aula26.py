#EXERCICIO 1

numero = input('Digite um numero: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'par'
    
    if par_impar:
        par_imar_texto = 'impar'
        
        print(f'O numero {numero_int} é {par_impar_texto}')
        
    else:
        print('Você não digitou um numero inteiro')
        
        
# Exercicio 2
horario = input('Que horas sao ?: ')

horario_int = int(horario)

if horario_int >= 0 and horario_int <= 11:
    print ('Bom dia')
elif horario_int >= 12. and horario_int <= 17:
    print('Boa tarde')
elif horario_int >=18 and horario_int <= 23:
    print('Boa noite')
else:
    print ('Por favor digite um horario valido')
           
#Exercicio 3
nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) > 4 and len(nome) < 7:
    print ('Seu nome é normal')
else:
    print('Seu nome é muito grande')
    
 