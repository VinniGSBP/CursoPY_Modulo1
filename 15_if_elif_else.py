#if /elif /else
#se / se nao se / se nao

entrada = input ('Voce quer entrar? [S/N] ')

if entrada == 'entrar' or entrada == 'Entrar':
    print('Voce entrou no sistema')
    
elif entrada == 'sair ' or entrada == 'Sair':
    print('Voce saiu do sistema')
    
else:
    print('Opção inválida, tente novamente')
    
    
condicao1 = True
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print ('Codigo para condicao 1')
elif condicao2:
    print ('Codigo para condicao 2')
elif condicao3:
    print ('Codigo para condicao 3')
elif condicao4:
    print ('Codigo para condicao 4')
    
print ('Fim do programa')