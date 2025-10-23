"""
    Introdução ao try/except
    try -> tentar executar o codigo
    except -> ocorreu algum erro ao tentar executar o codigo
"""
numero_str = input('Digite um número: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_float} é {numero_float * 2}')
except:
    print('Você não digitou um número válido.')  