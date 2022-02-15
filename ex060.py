'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5*4*3*2*1 = 120
'''
# Utilizando módulo
'''from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''

# Forma tradicional
num = int(input('Digite um número: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print('{}'.format(f))