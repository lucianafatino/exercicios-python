'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1: # essa linha verifica se apenas um valor foi passado
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg\nO menor peso lido foi {}Kg.'.format(maior, menor))





