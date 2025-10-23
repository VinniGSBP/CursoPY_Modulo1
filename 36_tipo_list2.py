## continuação lista em Python
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


lista = [10,22,33,44]
lista[2] = 300
del lista[2] #deletar item da lista
print(lista)
print(lista[2]) 

lista.append(50) #adicionado item a lista
lista.pop() #remove o ultimo item da lista
lista.append(60)
lista.append(70)
print(lista)