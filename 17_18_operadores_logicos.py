#Operadores logicos
#and (e) or(ou) not (nao)
#and - todas as condiçoes devem ser verdadeiras
#Se qualquer valor for falso, o resultado é falso
#Sao consedaros falsos: 0, 0.0, ' ', false
#Também eiste o tipo None que é usado para representar a ausência de valor ou nao valor

entrada = input ('[E]ntrar [S]air: ')

senha = input('Digite a senha: ')
senha_permitida = '123456'


if entrada == 'E' or entrada == 'e' and senha == senha_permitida:
    print('Voce entrou no sistema')
elif entrada == 'S' or entrada == 's':
    print('Voce saiu do sistema')
    