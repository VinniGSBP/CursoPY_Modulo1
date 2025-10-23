# Repeticoes
# While (enquanto)
#Executa uma acao enquanto uma condição for verdadeira
#Loop infinito -> quando um codigo não tem fim

#Exemplo1
#condicao = True
#while condicao:
 #   nome = input('Qual o seu nome: ')
 #   print(f'Seu nome é {nome}')
 #   if nome == 'sair':
 #       break
    
#print('acabou')
"""
 
 contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)
    
    
print('acabou')
"""
#Exemplo usando operadores de atribuição com operadores aritméticos
"""
contador = 0

while contador <= 10:
    contador += 1
    print(contador)
   
    
    if contador == 4:
         break

print('Acabou')
"""

#Exemplo de while + continue

contador = 0

# while contador <= 100:
#     contador += 1
    
#     if contador == 6:
#         print ('Nao vou mostrar o ', contador)
#         continue
    
#     if contador >= 10 and contador <= 27:
#         print ('Nao vou mostrar o ', contador)
#         continue 
    
#     if contador == 40:
#         break
    
# print('Acabou')
        
#WHILE + WHILE

qtd_linhas = 5 
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
     print(f'{linha=} {coluna=}')
     coluna += 1
    linha += 1
    
print('acabou')