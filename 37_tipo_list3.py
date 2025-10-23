## Listas em Python
## Tipo llist - mutável
## Suporta varios valores de qualquer tipo
## Conhecimentos reutilizáveis - indices e fatiamento
## metodos uteis: 
## append - Adiciona um item ao final 
## insert - Adiciona um item no indice escolhido
## pop - Remove do final ou do indice escolhido
## del - apaga um indice
## clear - limpa a lista
## extend - estende a lista
## + - contatena a lista

##Create Read  Update Delete
## Criar, lear, alterar, apagar = lista[i] (CRUD)


lista = [10, 20, 30, 40]
lista.append('Vinicius')
nome = lista.pop()

lista.append(1234)  #Adiciona item a lista

del lista[-1] # Apaga o ultimo item da lista

lista.insert(0, 'Vinni') #Adiciona um item a lista no indice escolhido
#lista.clear()# Limpa a lista completa
print(lista)
