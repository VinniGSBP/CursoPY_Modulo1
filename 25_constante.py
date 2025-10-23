"""
CONSTANTE = Variaveis que nao mudam o valor
Muitas condiçoes no mesmo if (ruim)
 <- Contagem de complexidade (ruim)
"""
velocidade = 58 #velocidade atual do carro em km/h

local_carro = 101 #local onde o carro esta na estrada

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta na estrada
RADAR_RAGE = 1 #raio de alcance do radar

vel_carro_passa_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= LOCAL_1 - RADAR_RAGE and local_carro <= LOCAL_1 + RADAR_RAGE
carro_multado_radar_1 = vel_carro_passa_radar_1 and carro_passou_radar_1

if vel_carro_passa_radar_1:
    print('Velocidade do carro passou do radar 1')
    
    if carro_passou_radar_1:
        print('Carro foi multado no radar 1')
        
    if carro_multado_radar_1:
        print('Carro foi multado no radar 1')