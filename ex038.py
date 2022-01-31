'''Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela a mensagem:
    - O primeiro valor é maior
    - O segundo valor é maior
    - Não existe valor maior, os dois são iguais
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro valor - {} - é maior'.format(n1))
elif n1 < n2:
    print('O segundo valor - {} - é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')