#INTRODUÇAO AS F-STRING (FORMATACAO DE STRINGS)

nome = 'Vinicius Gabriel'
peso = 115.0 #em KG
altura = 1.75 #em metros
imc = peso / (altura * altura) #Calcula o IMC

linha_1 = f'{nome} tem {altura:,.2f} de altura e {peso} kg de peso '

print(linha_1)  # Imprime a linha formatada
#print(nome, 'tem', peso, 'kg e', altura, 'm de altura. Seu IMC é', imc)