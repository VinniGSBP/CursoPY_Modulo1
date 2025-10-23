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


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b

lista_d = lista_a.extend(lista_b)
print(lista_c)
print(lista_d)