# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
numero = int(input('Digite um número inteiro: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é Par'.format(numero))
else:
    print('O número {} é Ímpar'.format(numero))
