nome = input('Digite seu nome: ')
idade = (input('Digite sua idade: '))

if idade != '' and nome != '':
   print (f'Seu nome é {nome} e você tem {idade} anos.')
   print(f'Seu nome invertido é {nome[::-1]}')
   print(f'Seu nome tem {len(nome)} letras.')
   print(f'Seu nome contem (ou nao) espaços: {"sim" if " " in nome else "nao"}')
   print(f'A primeira letra do seu nome é: {nome[0]}')
   print(f'A última letra do seu nome é: {nome[-1]}')
   
else:
    print('Desculpa, você deixou campos em branco.') 
