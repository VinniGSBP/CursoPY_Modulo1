#interpolação basica de strings
#s - string
#d e i - int
#f - float
#x e x - hexadecimal (ABCDEF01233456789)

nome = 'Vinicius'
preco = 10000.139120831
variavel = '%s, o preco total foi R$: %.2f' %(nome, preco)
print (variavel)

print('o hexadecialmal de %d é %x' %(1500, 1500)) #15 em decimal é F em hexadecimal