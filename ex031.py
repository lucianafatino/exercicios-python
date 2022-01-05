# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km
# e R$ 0,45 para viagens mais longas

# Minha resolução com correção do professor
viagem = float(input('Digite a distância da viagem em KM: '))
print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))
if viagem <= 200:
    valor = viagem * 0.50
else:
    valor = viagem * 0.45
print('O preço da sua passagem é de R${:.2f}.'.format(valor))
print('Boa viagem!')

# Resolução do professor simplificada
# distância = float(input('Qual é a distância da sua viagem? '))
# print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
# preço = distância * 0.50 if distância <= 200 else distância * 0.45
# print('O preço da sua passagem será de R$ {:.2f}'.format(preço))