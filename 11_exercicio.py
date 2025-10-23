#Calcular IMC 

# IMC = peso / (altura * altura)

nome = 'Vinicius Gabriel'
peso = 115.0 #em KG
altura = 1.75 #em metros
imc = peso / (altura * altura) #Calcula o IMC
print('Nome:', nome)  # Imprime o nome
print('Peso:', peso, 'kg')  # Imprime o peso
print('Altura:', altura, 'm')  # Imprime a altura
print('IMC:', imc)  # Imprime o IMC
print('IMC arredondado:', round(imc, 2))  # Imprime o IMC arredondado para 2 casas decimais
print(nome, 'tem', peso, 'kg e', altura, 'm de altura. Seu IMC é', imc)