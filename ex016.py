# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

# Usando trunc
from math import trunc
nr = float(input('Digite um valor: '))
print('O número digitado foi {} e a sua parte inteira é {}'.format(nr, trunc(nr)))

# Usando a função interna int
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))


