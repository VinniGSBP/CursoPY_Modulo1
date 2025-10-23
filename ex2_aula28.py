#Calculadora com WHILE

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')
    
    num_ok = None
    
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        num_ok = True
    except:
        num_ok = None
        
    if num_ok is None:
        print('Um ou ambos os numeros digitados sao invalidos')
        continue
        
    operador_permitido = '+-/*'
    
    if operador not in operador_permitido: 
        print('Operador invalido')    

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print ('Realizando sua conta, confira resultado')
    if operador == '+':
        print(num1_float + num2_float)
        
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
        
    else:
        print('Nunca deveria chegar aqui') 
        
        
        
        
    sair = input('Quer sair? [S]im: ').lower().startswith('s')
    
    if sair is True:
        break