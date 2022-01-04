# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/h, mostre um msg dizendo que ele foi multado
# A multa vai custar R$ 7 por cada km acima do limite
vel = float(input('Digite a velocidade do seu carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Ultrapassou a velocidade máxima de 80KM/h! Você foi multado em R$ {:.2f}'.format(multa))
print('Tudo em ordem! Dirija com segurança!')