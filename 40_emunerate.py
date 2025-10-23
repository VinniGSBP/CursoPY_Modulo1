###

# enumerate - enumera iteráveis(indices)
####

lista = ['Maria', 'Helena', 'Luiz']

lista.append('Joao')

lista_emunerada = enumerate(lista)
#print(next(lista_emunerada))

#lista_emunerada = list(enumerate(lista))
#print(lista_enumerada)
for item in lista_emunerada:
    print(item)